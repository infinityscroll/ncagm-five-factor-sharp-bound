# Independent exact replay — prepared only

One solver-free verifier checks the frozen final-margin certificate
`f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225`.
No worker execution is authorized by this plan. Root must first review the
source and manifest and separately authorize one launch.

The target is the raw lower polynomial C(n)I+D5(A) on A_i>=0,
sum_i A_i<=nI, integer n>=5. The certificate's polynomial matrices are checked
on u in ((3+sqrt(5))/8,(21+sqrt(249))/48]. No discovery, fitting, numerical
solver, rounding, root sampling or change to the candidate is allowed.

## Independent checks

1. Newly written arithmetic in Q(sqrt(5),sqrt(249)) uses four rational
   coordinates and multiplication by squarefree-radical index convolution.
   Signs use two successive quadratic norm comparisons. For opposite-sign
   A and B, sign(A+B sqrt(d))=sign(A) sign(A^2-d B^2); equal signs and zero
   components are handled directly. This is applied first over Q with d=5,
   then over Q(sqrt(5)) with d=249. Both radicals are positive. No discovery
   field class or LDL evaluator is imported or copied.
2. Treat the 104 stored matrices and their LDL factors as proposed proof
   data. Check dimensions, exact symmetry, unit lower triangular L, signs
   of every D, and every entry of L D L^T=M. Require strict positivity of
   all final-coefficient pivots. This independently verifies the supplied
   factorization; it does not rerun the discovery elimination routine.
3. Reconstruct each Bernstein polynomial in the ordinary t power basis
   by direct expansion of binomial(q,k)t^k(1-t)^(q-k). Independently form
   the normalized rational block as a polynomial in u and substitute
   u=u0+(u5-u0)t using Horner polynomial multiplication. Compare all
   coefficients exactly, rather than trusting saved transformation flags.
4. Reconstruct the 81 orbit functions from the frozen affine raw inputs
   and exact slopes; compare the resulting rational functions to the
   certificate. Rebuild every word coefficient by expanding concrete
   degree<=2 word-pair localizers over five labels and retaining the 76
   canonical word representatives. This independently generates the
   localizer coefficient equations, without importing discovery helpers.
5. Verify all full G0/G1 equality-kernel rows, the extra G1 kernel, exact
   n5 specialization, four scalar blocks, the polynomial normalization
   identities, and the stated reduced principal-coordinate deletions.
6. Check all actual rational denominators and clearing factors by exact
   division by explicitly proved zero-free factors. Linear factors have
   roots outside the interval. The two convex scalar quadratics are
   negative at both endpoints, hence negative throughout; E/16 vanishes
   only at the excluded lower endpoint. Scalar G2/H2 numerators are
   concave and positive at both endpoints, so positive throughout.
   These proofs do not trust a root-ledger classification.

## Reused dependency and limits

SymPy 1.14.0 is used only as a rational polynomial/field arithmetic engine
over Q(u), not for algebraic field signs, PSD, solver work or root sampling.
The existing CPython3.12 environment is reused without installation or probes.
The invariant representation contraction map in INPUT-BLOCKS.json is reused
as raw data. This verifier does NOT independently prove that those contracted
blocks equal the full permutation-invariant Grams; a separate exact map
reconstruction/representation-completeness audit must discharge that bridge.
The script reports that dependency explicitly even on a successful run.
It checks the kernel-based reductions themselves, not the representation
theorem. No human review, novelty claim, equality-witness replay or publication.

## Resource and stop protocol

One run under the existing reviewed supervisor: 30 worker CPU seconds,
45 wall seconds and 1 GiB sampled/final worker RSS. The supervisor retains
exclusive one-use receipts, input hashes, post-reap CPU/RSS checks, and
requires a complete exact PASS. Any failure/cap/incompleteness is NO_RESULT,
not permission to loosen checks or rerun. No candidate alteration is possible.
This is an additive verification cost. The discovery worker and all earlier
failed gates remain untouched.
