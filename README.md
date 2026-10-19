# Sharp five-factor lower bound — paper and exact verifier

AI-assisted research materials prepared for Jitendra Prajapati.

[Read the 14-page paper](paper/sharp-five-factor-bound.pdf).
**Unrefereed; publication priority remains unconfirmed.**
**Portable validation passed both exact replays** on 19 October 2026.
The saved receipt and tested package manifest are in `validation/`. Both
original independent exact replays also passed; their historical receipts
are included separately.

For every integer n>=5 and every finite-dimensional real symmetric or
complex Hermitian tuple A_i>=0 with sum A_i<=nI, define

    D5(A) = sum of A_i1 A_i2 A_i3 A_i4 A_i5 over ordered distinct indices,
    r = n/(n-1),
    a = n(6n-9+sqrt(20n^2-60n+49))/(16(n-1)(n-2)),
    kappa5(n) = a^2 [r(3-r)a-r^2/2].

The internally accepted claim is the sharp lower Loewner inequality

    D5(A)/(n)_5 >= -kappa5(n) I.

Zhong's known real n-dimensional family attains equality. This package
checks the universal certificate; the analytical proof of attainment and
the representation-completeness argument are in `reviews/`. A separate
analytical extension characterizes equality on a vector and proves that
the minimum attaining dimension is exactly n-1 over both fields; its proof
and two AI-agent reviews are also included. These are not formal proof-assistant
certificates. The upper half, an arbitrary-length solution, established
priority, and independent human review are not claimed.

## Paper and optional figure

`paper/sharp-five-factor-bound.pdf` is the 14-page integrated proof, with
editable standalone `paper/main.tex`, source manifest and review receipts.
The source uses ordinary LaTeX packages including xurl. The PDF was compiled
and every page visually checked. `figure/` contains an optional endpoint
plot, CSV and editable source; it illustrates the formula and is not proof
evidence. Plotting requires matplotlib, which the exact verifier does not use.

## One offline command

Use **CPython3.12** on macOS or Linux with **SymPy1.14.0 already installed**
and the ordinary `ps` command available. No solver, NumPy, CVXPY, Clarabel,
network connection, package installation, credentials or source workspace
is required. The dependency pin is in `requirements.txt`.

From this directory:

```sh
python3.12 -I verify.py
```

The command prints a JSON receipt and exits0 only after both exact replays
pass. To retain that receipt, redirect stdout to a file outside the package.
All worker files and outputs are copied into a temporary directory, which
is removed on completion. The package is not edited by verification.

Each sequential stage has a30-worker-CPU-second,45-wall-second and1GiB
sampled/final-RSS limit. The maximum combined worker allocation is60CPU/90wall;
file copying and supervisor overhead are outside worker CPU accounting.
RSS sampling is not a hard allocation ceiling. A cap, missing dependency,
failed identity or incomplete receipt returns a nonzero exit status and
no proof acceptance. There is no automatic retry or fallback.

## What gets checked

1. `block_map` independently builds explicit word-space representative
   contractions and proves81 upper/lower block identities using3965 exact
   count polynomials of degree at most4. Counts at n=5,...,9 reconstruct
   these polynomials by a proved degree bound; this is not sampled PSD.
2. `psd_words` independently checks81 orbit functions,76 original word
   coefficient equations,20 kernel rows,4 scalar sectors,82 zero-free
   denominator checks and104 Bernstein coefficient matrix factorizations.
   Algebraic signs are exact in Q(sqrt(5),sqrt(249)), with both radicals
   positive. Forward differences of the Bernstein coefficients are compared
   to an independent Horner substitution of each normalized block.

Both stages bind the same final certificate:

    f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225

The scripts use different implementations for the relevant independent
checks. They share SymPy's rational polynomial arithmetic engine and the
fixed certificate/input data. The two computational replays must be read
with the analytical representation, degree-bound and operator/attainment
arguments in `reviews/`; this is not a proof-assistant formalization.

## Preservation and portability

`stages/` contains byte-identical copies of the previously checked scripts,
data and original manifests. The wrapper copies them into temporary storage.
It removes exactly three local absolute-environment guard lines from the
PSD worker, retaining its Python3.12 check. The wrapper independently requires
isolated Python mode and the pinned installed SymPy version. No mathematical
line changes. The exact three-line diff and effective source preview are in
`adaptation/`. The map worker and both resource supervisors are unchanged.
Only the temporary manifest is updated to hash the adapted runtime source.

`PACKAGE-MANIFEST.json` binds every supplied package file except itself.
`historical-receipts/` records the accepted original runs, not a portable run.
Original proof artifacts and earlier failed candidates remain outside this
package unchanged. No discovery solver or failed candidate is needed to
replay the final proof data.

## Credits and scope of review

Lai and Lim posed the correct-lower-bound question and already disproved the
original conjecture at product length5; their numerical table includes the
n=5 endpoint. Zhong supplied the permutation-covariant attaining family and
its recurrence. The public `ipitchford/exact-low-length-recht-re-inequalities`
project supplied relevant word-orbit/representation and certificate
architecture, and already claims ordinary m5 upper bounds for n>=5 and
ordinary lower restoration for n>=6. Those claims are not presented as new.
Zhao's earlier two-factor equality classification and minimum-dimension
theorem are related antecedents. Our dimension claim concerns attaining
the exact five-factor endpoint, not the smallest dimension permitting any
violation of the original conjecture.

The present candidate contributions are the matching exact sharp lower
constant for every n>=5 on the full sum A_i<=nI domain, its equality-vector
conditions, and minimum attaining dimension n-1. Formula optimization,
the known family, generic m5 restoration and the original disproof remain
prior work. Codex performed derivation, implementation and preparation;
separately tasked AI agents and the root agent reviewed the proof and
independently checked arithmetic. No independent human specialist review
has occurred. Bounded source searches do not establish priority; the
unread Liu2025 primary paper remains a specific literature gap.

This repository publishes the approved paper and reproducibility package.
Publication does not establish correctness by independent human review,
priority, external adoption or a hiring outcome. The paper and mathematical
verifiers are byte-identical to the approved sealed package. Only this
README, the inventory and publication provenance were updated for release.
Earlier private-status labels in historical receipts describe their original
recording time. The approved inventory is preserved in `publication/`.

Primary references and exact source boundaries are in `SOURCES.md`.
