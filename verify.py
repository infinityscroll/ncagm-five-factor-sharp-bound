#!/usr/bin/env python3
"""Offline portable launcher; mathematical workers remain frozen proof checkers."""
import sys
import hashlib
import importlib.metadata
import json
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
CERTIFICATE = "f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225"
ORIGINAL_PSD = "f849d249b5e0350fce864836c9204224250f8c0a2246ac791edf05b3a324498d"
PORTABLE_PSD = "66c9dc0e8b555957d3dcaff9bd2d818c383dcb97c381bff4e1ce46c5848480cd"
ORIGINAL_MAP = "079e2761d4aa0d4f1be35f338d67a0d8c1929b7eb5cac25f4acf4e9ea0f96d21"
WATCHDOG = "cbb7d0485cc19e11993c2d78b9a7f7df9a03baf88185767296782f8dbf1fc1fb"
REMOVE_LINES = (
    'VENV = ROOT.parent / "overnight-ncagm-sharp-root-20261018/.venv"\n',
    'assert Path(sys.prefix).resolve() == VENV.resolve()\n',
    'assert Path(sympy.__file__).resolve().is_relative_to((VENV/"lib/python3.12/site-packages").resolve())\n',
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_path(base, relative):
    path = PurePosixPath(relative)
    require(not path.is_absolute() and ".." not in path.parts, "unsafe manifest path")
    result = base.joinpath(*path.parts)
    require(result.resolve().is_relative_to(base.resolve()), "manifest path escapes package")
    require(result.is_file() and not result.is_symlink(), "missing file or symlink in frozen inputs: "+relative)
    return result


def read_json(path):
    return json.loads(path.read_text())


def validate_hashes(base, hashes):
    for relative, expected in hashes.items():
        require(sha(checked_path(base,relative)) == expected, "hash mismatch: "+relative)


def prepare_stage(name, temp_root):
    original = ROOT/"stages"/name
    manifest_path = original/"FROZEN-MANIFEST.json"
    manifest = read_json(manifest_path)
    validate_hashes(original,manifest["sha256"])
    destination = temp_root/name
    destination.mkdir()
    for relative in manifest["sha256"]:
        source = checked_path(original,relative)
        output = destination/relative
        output.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,output)
    worker = destination/"exact_gate.py"
    original_hash = sha(worker)
    require(sha(destination/"watchdog.py") == WATCHDOG,"unexpected supervisor")
    if name == "psd_words":
        require(original_hash == ORIGINAL_PSD,"unexpected PSD worker")
        source = worker.read_text()
        for line in REMOVE_LINES:
            require(source.count(line) == 1,"runtime guard removal is not unique")
            source = source.replace(line,"",1)
        worker.write_text(source)
        require(sha(worker) == PORTABLE_PSD,"portable source differs beyond the three guards")
        require(worker.read_bytes() == (ROOT/"adaptation/psd_words.effective.py").read_bytes(),
                "portable source differs from frozen effective preview")
        manifest["sha256"]["exact_gate.py"] = PORTABLE_PSD
    else:
        require(name == "block_map" and original_hash == ORIGINAL_MAP,"unexpected map worker")
    manifest["portable_adaptation"] = {
        "original_manifest_sha256":sha(manifest_path),
        "original_worker_sha256":original_hash,
        "effective_worker_sha256":sha(worker),
        "removed_local_runtime_guard_lines":3 if name == "psd_words" else 0,
        "mathematical_core_changes":0,
        "environment":"Isolated CPython3.12 with installed SymPy1.14.0",
    }
    (destination/"FROZEN-MANIFEST.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    return destination,manifest["portable_adaptation"]


def run_stage(name, temp_root):
    directory,adaptation = prepare_stage(name,temp_root)
    completed = subprocess.run(
        [sys.executable,"-I",str(directory/"watchdog.py"),"--authorized-run"],
        cwd=directory,capture_output=True,text=True,
    )
    # The reviewed supervisor owns the 30 CPU / 45 wall / sampled1GiB limits.
    watchdog = read_json(directory/"WATCHDOG-RESULT.json") if (directory/"WATCHDOG-RESULT.json").is_file() else None
    result = read_json(directory/"RESULT.json") if (directory/"RESULT.json").is_file() else None
    failure = read_json(directory/"WORKER-FAILURE.json") if (directory/"WORKER-FAILURE.json").is_file() else None
    stage = {"name":name,"portable_adaptation":adaptation,
             "supervisor_exit_code":completed.returncode,"resource_receipt":watchdog,
             "exact_result":result,"failure_receipt":failure}
    passed = (completed.returncode == 0 and watchdog is not None and result is not None
              and watchdog.get("status") == "COMPLETED_EXACT_GATE"
              and watchdog.get("worker_exit_code") == 0
              and result.get("status") == "COMPLETED_EXACT_GATE"
              and result.get("all_checks") == "PASS"
              and result.get("certificate_sha256") == CERTIFICATE)
    if passed:
        passed = (watchdog.get("worker_total_cpu_seconds") is not None
                  and watchdog["worker_total_cpu_seconds"] <= 30
                  and watchdog.get("elapsed_wall_seconds") is not None
                  and watchdog["elapsed_wall_seconds"] <= 45
                  and watchdog.get("worker_peak_rss_bytes") is not None
                  and watchdog["worker_peak_rss_bytes"] <= 1024**3)
    if not passed:
        stage["supervisor_stdout"] = completed.stdout[-4000:]
        stage["supervisor_stderr"] = completed.stderr[-4000:]
        return False,stage
    if name == "block_map":
        require(result["upper_triangle_identities"] == 81 and result["scalar_polynomial_maps"] == 3965,
                "incomplete representation-map replay")
    else:
        expected = {"matrices_checked":104,"orbit_functions_checked":81,
                    "concrete_word_patterns_checked":76,"kernel_rows_checked":20,
                    "scalar_blocks_checked":4,"zero_free_factor_checks":82}
        require(all(result.get(k) == v for k,v in expected.items()),"incomplete PSD/word replay")
    return True,stage


def main():
    require(sys.argv[1:] == [],"Usage: python3.12 -I verify.py")
    require(sys.flags.isolated == 1 and sys.flags.optimize == 0,
            "Use isolated, non-optimized mode: python3.12 -I verify.py")
    require(sys.implementation.name == "cpython" and sys.version_info[:2] == (3,12),
            "CPython3.12 is required by this frozen portable protocol")
    require(sys.platform == "darwin" or sys.platform.startswith("linux"),
            "The resource supervisor supports macOS and Linux")
    require(importlib.metadata.version("sympy") == "1.14.0","Installed SymPy1.14.0 required; no installation is attempted")
    manifest_path = ROOT/"PACKAGE-MANIFEST.json"
    manifest = read_json(manifest_path)
    validate_hashes(ROOT,manifest["sha256"])
    output = {"status":"INCOMPLETE_NO_RESULT","certificate_sha256":CERTIFICATE,
              "package_manifest_sha256":sha(manifest_path),"stages":[],
              "network_calls":0,"solver_calls":0,"new_roundings":0,
              "mathematical_core_changes":0,"outputs_are_temporary":True,
              "scope":"Exact computational proof checks; analytical representation and attainment arguments remain in reviews",
              "independent_human_review_or_priority_claim":False}
    with tempfile.TemporaryDirectory(prefix="ncagm-m5-verify-") as temporary:
        for name in ("block_map","psd_words"):
            passed,stage = run_stage(name,Path(temporary))
            output["stages"].append(stage)
            if not passed:
                print(json.dumps(output,indent=2,sort_keys=True))
                return 1
    output["status"] = "PASS_BOTH_EXACT_REPLAYS"
    print(json.dumps(output,indent=2,sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(json.dumps({"status":"INCOMPLETE_NO_RESULT","error":type(error).__name__+": "+str(error),
                          "no_automatic_retry":True},sort_keys=True))
        sys.exit(1)
