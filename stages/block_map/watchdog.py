#!/usr/bin/env python3
"""Single-use bounded supervisor. PREPARED ONLY; requires later run authorization."""

import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time


BASE = Path(__file__).resolve().parent
CPU_SECONDS = 30
WALL_SECONDS = 45
RSS_LIMIT_BYTES = 1024 ** 3


def limits_before_exec():
    for name, limit in (("RLIMIT_CPU", CPU_SECONDS),):
        if not hasattr(resource, name):
            raise RuntimeError("unsupported resource: " + name)
        kind = getattr(resource, name)
        resource.setrlimit(kind, (limit, limit))
        if resource.getrlimit(kind) != (limit, limit):
            raise RuntimeError("failed resource enforcement: " + name)


def exclusive_json(filename, payload):
    with (BASE / filename).open("x") as stream:
        json.dump(payload, stream, indent=2, sort_keys=True)
        stream.write("\n")


def rss_bytes(usage):
    if sys.platform == "darwin":
        return int(usage.ru_maxrss)
    if sys.platform.startswith("linux"):
        return int(usage.ru_maxrss) * 1024
    raise RuntimeError("unsupported platform for ru_maxrss units")


def reap_worker(process, blocking=False):
    pid, status, usage = os.wait4(process.pid, 0 if blocking else os.WNOHANG)
    if pid == 0:
        return None
    exit_code = os.waitstatus_to_exitcode(status)
    process.returncode = exit_code
    return exit_code, usage


def kill_worker_group(process):
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def main():
    if sys.argv[1:] != ["--authorized-run"]:
        print("Prepared only. Do not run without subsequent explicit authorization.", file=sys.stderr)
        return 2
    manifest_path = BASE / "FROZEN-MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("preparation_status") != "PREPARED_NOT_RUN":
        raise RuntimeError("unexpected manifest status")
    if not hasattr(os, "wait4") or not hasattr(os, "waitstatus_to_exitcode"):
        raise RuntimeError("worker-specific resource accounting is unavailable")
    children_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    rss_bytes(children_before)
    for relative, expected in manifest["sha256"].items():
        if hashlib.sha256((BASE / relative).read_bytes()).hexdigest() != expected:
            raise RuntimeError("hash mismatch: " + relative)
    outputs = ("RUN-ATTEMPT.json", "WATCHDOG-RESULT.json", "RESULT.json", "WORKER-FAILURE.json",
               "case-progress.jsonl", "worker.stdout.log", "worker.stderr.log")
    if any((BASE / name).exists() for name in outputs):
        raise RuntimeError("single-use gate: an output or attempt file already exists; no automatic retry")
    exclusive_json("RUN-ATTEMPT.json", {
        "status": "AUTHORIZED_COMMAND_INVOKED", "retry_permitted": False,
        "cpu_seconds": CPU_SECONDS, "wall_seconds": WALL_SECONDS,
        "worker_rss_threshold_bytes": RSS_LIMIT_BYTES,
        "rss_enforcement": "sampled by ps at approximately 50 ms intervals; not a hard allocation ceiling",
        "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "python_executable": sys.executable,
    })
    started = time.monotonic()
    process = None
    status = "INCOMPLETE"
    exit_code = None
    detail = None
    maximum_observed_rss = 0
    wait_record = None
    worker_usage = None
    try:
        with (BASE / "worker.stdout.log").open("x") as stdout, (BASE / "worker.stderr.log").open("x") as stderr:
            process = subprocess.Popen(
                [sys.executable, "-I", "-B", str(BASE / "exact_gate.py"), "--authorized-worker"],
                cwd=str(BASE), stdout=stdout, stderr=stderr,
                start_new_session=True, preexec_fn=limits_before_exec,
            )
            deadline = started + WALL_SECONDS
            while wait_record is None:
                wait_record = reap_worker(process)
                if wait_record is not None:
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    status = "WALL_CAP_EXCEEDED"
                    kill_worker_group(process)
                    break
                try:
                    reading = subprocess.run(
                        ["ps", "-o", "rss=", "-p", str(process.pid)],
                        capture_output=True, text=True, timeout=min(0.5, remaining),
                    )
                except subprocess.TimeoutExpired:
                    status = "WALL_CAP_EXCEEDED" if time.monotonic() >= deadline else "RSS_MONITOR_FAILURE"
                    kill_worker_group(process)
                    break
                raw_rss = reading.stdout.strip()
                if reading.returncode != 0 or not raw_rss:
                    wait_record = reap_worker(process)
                    if wait_record is not None:
                        break
                    status = "RSS_MONITOR_FAILURE"
                    detail = "ps did not return worker RSS while the worker was live"
                    kill_worker_group(process)
                    break
                rss = int(raw_rss) * 1024
                if rss < 0:
                    raise RuntimeError("ps returned a negative RSS")
                maximum_observed_rss = max(maximum_observed_rss, rss)
                if rss > RSS_LIMIT_BYTES:
                    status = "RSS_CAP_EXCEEDED"
                    kill_worker_group(process)
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    status = "WALL_CAP_EXCEEDED"
                    kill_worker_group(process)
                    break
                time.sleep(min(0.05, remaining))
            if wait_record is None:
                wait_record = reap_worker(process, blocking=True)
            exit_code, worker_usage = wait_record
            if status == "INCOMPLETE" and time.monotonic() > deadline:
                status = "WALL_CAP_EXCEEDED"
            if rss_bytes(worker_usage) > RSS_LIMIT_BYTES:
                status = "RSS_CAP_EXCEEDED"
            if worker_usage.ru_utime + worker_usage.ru_stime > CPU_SECONDS:
                status = "CPU_CAP_EXCEEDED"
            if status == "INCOMPLETE":
                if exit_code == 0 and (BASE / "RESULT.json").is_file():
                    result = json.loads((BASE / "RESULT.json").read_text())
                    if result.get("status") == "COMPLETED_EXACT_GATE" and result.get("all_checks") == "PASS":
                        status = "COMPLETED_EXACT_GATE"
                    else:
                        detail = "worker returned an invalid completion record"
                elif exit_code is not None and exit_code < 0:
                    status = "RESOURCE_CAP_OR_SIGNAL"
                else:
                    detail = "worker did not complete all exact checks"
    except Exception as error:
        detail = type(error).__name__ + ": " + str(error)
        if process is not None and process.returncode is None:
            kill_worker_group(process)
            exit_code, worker_usage = reap_worker(process, blocking=True)
    elapsed = time.monotonic() - started
    children_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    children_user_cpu = children_after.ru_utime - children_before.ru_utime
    children_system_cpu = children_after.ru_stime - children_before.ru_stime
    exclusive_json("WATCHDOG-RESULT.json", {
        "status": status, "worker_exit_code": exit_code, "elapsed_wall_seconds": elapsed,
        "maximum_observed_worker_rss_bytes": maximum_observed_rss,
        "worker_peak_rss_bytes": rss_bytes(worker_usage) if worker_usage is not None else None,
        "worker_user_cpu_seconds": worker_usage.ru_utime if worker_usage is not None else None,
        "worker_system_cpu_seconds": worker_usage.ru_stime if worker_usage is not None else None,
        "worker_total_cpu_seconds": (worker_usage.ru_utime + worker_usage.ru_stime) if worker_usage is not None else None,
        "all_children_user_cpu_seconds_delta": children_user_cpu,
        "all_children_system_cpu_seconds_delta": children_system_cpu,
        "all_children_total_cpu_seconds_delta": children_user_cpu + children_system_cpu,
        "all_children_peak_rss_bytes": rss_bytes(children_after),
        "all_children_peak_rss_baseline_bytes": rss_bytes(children_before),
        "resource_accounting_note": "wait4 is worker-specific; RUSAGE_CHILDREN CPU deltas include ps probes. "
                                    "ru_maxrss is a maximum, not an additive counter: its baseline is recorded, not subtracted. "
                                    "macOS ru_maxrss is bytes; Linux ru_maxrss is KiB and is multiplied by 1024.",
        "detail": detail, "partial_results_are_not_a_scientific_pass": True,
        "retry_permitted": False,
    })
    print(json.dumps({"status": status, "worker_exit_code": exit_code}, sort_keys=True))
    return 0 if status == "COMPLETED_EXACT_GATE" else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print("INCOMPLETE / NO_RESULT: " + type(error).__name__ + ": " + str(error), file=sys.stderr)
        sys.exit(2)
