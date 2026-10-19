# Private package provenance

Prepared 19 October 2026. The subsequent portable validation passed both
exact replays; see `validation/PORTABLE-RESULT.json` and its tested manifest.
The final package adds documentation only; executable and proof-data hashes
remain identical to the tested package.
All sources below are campaign-owned frozen artifacts. No original proof,
certificate, source or receipt was modified by this packaging task.

| Component | Original SHA256 |
|---|---|
| Final exact certificate, both packaged copies | `f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225` |
| Independent PSD/word worker | `f849d249b5e0350fce864836c9204224250f8c0a2246ac791edf05b3a324498d` |
| Independent map worker | `079e2761d4aa0d4f1be35f338d67a0d8c1929b7eb5cac25f4acf4e9ea0f96d21` |
| Both30CPU/45wall supervisors | `cbb7d0485cc19e11993c2d78b9a7f7df9a03baf88185767296782f8dbf1fc1fb` |
| Original PSD/word manifest | `6aa2e4cb2270d22389a943ad9d856dd6a78c76892b6519b8f036721480818c31` |
| Original map manifest | `dde7927e95eccaa1808d650bf417c899d2f8231d796c6411f3fec68f0e39ed5b` |
| Internal composite acceptance | `c64dd723abacd28724f3a8472dee2df3f7caa725b91ceca04cf3d826d26084ff` |
| Portable PSD effective preview | `66c9dc0e8b555957d3dcaff9bd2d818c383dcb97c381bff4e1ce46c5848480cd` |

Source directories, relative to the original campaign base:

- `overnight-ncagm-m5-all-n-independent-replay-20261019`: copied into
  `stages/psd_words/`, with its mathematical source byte-identical.
- `overnight-ncagm-m5-independent-block-map-20261019`: copied into
  `stages/block_map/`, with its source byte-identical.
- `overnight-ncagm-m5-all-n-acceptance-20261019`: composite internal acceptance.
- `overnight-ncagm-m5-uniform-semantics-review-20261019`: representation proof.
- `overnight-ncagm-m5-theorem-bridge-audit-20261019`: operator and attainment proof.
- `overnight-ncagm-outcome-significance-audit-20261019` and
  `overnight-ncagm-m5-target-priority-refresh-20261019`: bounded attribution
  and source-status records, copied without rewriting their chronology.

The original successful worker times were3.832851CPU/3.843169wall seconds
for PSD/words and2.347474CPU/2.392411wall seconds for map reconstruction.
These historical, machine-specific timings are not performance guarantees.
The later portable replay used 6.184914 total worker CPU seconds and
6.275738 total worker wall seconds; its independent receipt is included.

The new wrapper does file integrity/environment checks and temporary-copy
orchestration only. Its runtime adaptation removes exactly the local VENV
declaration and two absolute-environment assertions from the copied PSD
worker. All mathematical lines are unchanged; the Python3.12 check remains.
The wrapper additionally requires isolated CPython mode and the exact installed
SymPy version. It does not install or fetch anything. The complete mechanical
diff and effective source are included and hashed.

The temp-only manifest change records original and effective source hashes.
This changes the runtime source identity honestly; it does not pretend that
the adapted whole-file hash equals the original. Source/data originals stay
immutable in the package and prior campaign directories. Package files are
bound by PACKAGE-MANIFEST.json; that manifest cannot contain its own hash.

Codex performed the derivation, implementation and packaging. Separate AI
agents and the root agent performed distinct mathematical/static reviews
and independently implemented exact checks. Human specialist review and
priority certification remain absent. Public sources and known ingredients
are credited in SOURCES.md and the copied reviews. This private package
carries no publication or external-contact authorization.
