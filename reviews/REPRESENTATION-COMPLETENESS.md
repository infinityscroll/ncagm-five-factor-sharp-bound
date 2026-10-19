# All-n representation semantics review for the five-factor Gram ansatz

19 October 2026. Independent analytical and source-bound review by the skeptical-review agent. No scientific worker, symbolic algebra program, verifier, import, solver, or numerical probe was executed for this review.

**PASS for representation completeness, generic block-generation semantics, and the stated principal-coordinate reductions for every integer n >= 5.** This is independent of candidate feasibility. It does not establish positive semidefiniteness of the four remaining matrix blocks or an all-n sharp five-factor theorem.

During preparation of this review, root reported that the separate proof-only check of the unchanged candidate failed: the fourth leading minor of H0 has an odd interior root. That execution and root classification were not independently audited here. This report neither reverses that closure nor authorizes another fit or execution.

## Frozen inputs and evidentiary scope

Paths in this report are relative to `/Users/dusk/technical_contribution_scout_20261003/orthogonal-research-20261018`.

| Input | SHA256 |
|---|---|
| `overnight-ncagm-m5-primitive-preflight-20261019/exact_gate.py` | `639b40baa43f77cee71ee4421d1dbf4a389cd8cbc6e796321cdc49a478fcaa84` |
| `overnight-ncagm-m5-primitive-preflight-20261019/AFFINE-FAMILY.json` | `7f8c881a0f58aa0d7e20f5e0b002b5c5d5b493299e8cb772d9eadd79f526a639` |
| `overnight-ncagm-m5-primitive-preflight-20261019/REPRESENTATION-BLOCKS.json` | `bab92a3fd0d78fab2a1018490a93cd342d66e2b0e32293c20b87e25890aa58db` |
| `overnight-ncagm-m5-primitive-preflight-20261019/RESULT.json` | `e5ed362cbf58768f37d97fa1698db1bbc449b616761ca9563d55e07430aebbe4` |
| `overnight-ncagm-m5-primitive-preflight-20261019/DENOMINATOR-ROOTS.json` | `947edca5522d434307f9414d64002de57f8de524b916806a72c8c98e00a493d7` |
| `overnight-ncagm-m5-rational-preflight-20261019/exact_gate.py` | `3367a45a103a7abf9fcdb8d713cc6e5c7a239a60218263e248ed50c32d4a57ae` |
| `overnight-ncagm-m5-candidate-audit-20261019/AFFINE-PREFLIGHT-SEMANTIC-REVIEW.md` | `6621460232e2775e4c4f53bc14821c729b6f9584d02e273526138ad94a908ed8` |
| `overnight-ncagm-m4-manuscript-20261019/main.tex` | `e1921a8a3e894c2f876c74a69fff6ecf2ff39186eb25871c20caf5f23867a3bf` |

The older five-factor semantic review treats n=5. The four-factor manuscript supplies an all-n word-representation argument whose representation-theoretic part does not depend on the target polynomial. I reconstruct that argument below and check it against the five-factor source. Its four-factor affine solution and scalar-block identities are not imported into the five-factor problem. The rational and primitive preflight sources have the same orbit, representative, and tied-label block generators; their relevant changes concern elimination and preconditioning.

## 1. Exact representation and its boundary n=5

Let W_n be the real vector space with orthonormal basis all words of lengths 0, 1, and 2 on n letters. Its dimension is 1+n+n^2. The H Gram matrix commutes with S_n. A marked G Gram matrix commutes with the stabilizer of letter 0, namely S_(n-1).

Write q for the number of active, permuted letters: q=n for H and q=n-1 for G. Thus q >= 4 in every case under review. The fixed letter 0 is not active in G.

The trivial vectors, in source order, are:

- H: 1, sum_i x_i, sum_i x_i^2, sum_(i!=j) x_i x_j.
- G: 1, x_0, sum_i x_i, x_0^2, sum_i x_0 x_i, sum_i x_i x_0, sum_i x_i^2, sum_(i!=j) x_i x_j, where every sum uses active letters.

They are nonzero indicators of disjoint word orbits. They are therefore independent and span the entire fixed subspace, of dimensions 4 and 8 respectively.

For a zero-sum vector c in R^q, define

    L(c) = sum_i c_i x_i,
    Q(c) = sum_i c_i x_i^2,
    P(c) = sum_(i!=j) (c_i+c_j) x_i x_j,
    M(c) = sum_(i!=j) (c_i-c_j) x_i x_j.

These give the four standard copies for H, in the order L,Q,P,M. G has the six copies L, sum_i c_i x_0 x_i, sum_i c_i x_i x_0, Q,P,M. Distinct supports, or symmetry versus skew symmetry, make these copies orthogonal. Their squared norm multipliers relative to ||c||^2 are 1 for L,Q and the marked copies, 2(q-2) for P, and 2q for M. All are positive for q >= 4. The source uses the same c=e_a-e_b in every copy, with ||c||^2=2.

The remaining spaces on unequal ordered pairs are

    U_q = symmetric, zero-diagonal coefficient arrays with zero row sums,
    V_q = skew coefficient arrays with zero row sums.

Their dimensions are q(q-3)/2 and (q-1)(q-2)/2. The symmetric row-sum map onto R^q is surjective for q>=3; the skew row-sum map has image the zero-sum space. These facts give the stated dimensions and their orthogonal complements consisting of the already listed trivial/standard pair copies.

The source's representatives are a symmetric four-label switch, of squared norm 8,

    x_a x_b+x_b x_a+x_c x_d+x_d x_c
    -x_a x_c-x_c x_a-x_b x_d-x_d x_b,

and a skew triangle, of squared norm 6,

    x_a x_b-x_b x_a+x_b x_c-x_c x_b+x_c x_a-x_a x_c.

They belong to U_q,V_q respectively and are nonzero already at q=4.

Here is an all-q irreducibility check, so testing these representatives is not merely testing a few vectors. The standard representation is absolutely irreducible with scalar commutant. The permutation representation on unordered pairs has a three-dimensional commutant: an equivariant matrix entry depends on intersection size 0,1,2. It contains one trivial and one standard summand. Its remaining nonzero summand U_q must consequently have one-dimensional real commutant and be absolutely irreducible. On skew pairs, an equivariant map is determined by the image of e_1 wedge e_2. Invariance under permutations of the remaining letters and antisymmetry under (1 2) leave exactly two possible directions:

    e_1 wedge e_2,
    sum_(j>2) (e_1 wedge e_j - e_2 wedge e_j).

Thus the skew-pair commutant has dimension 2. One summand is standard; its nonzero orthogonal complement V_q also has scalar real commutant and is absolutely irreducible. The types are inequivalent by dimension except for standard and V_4, both dimension 3. Their characters at a transposition are 1 and -1, so they too are inequivalent. This explicitly covers the G boundary q=4 at n=5.

The dimensions now exhaust W_n:

    H: 4 + 4(q-1) + q(q-3)/2 + (q-1)(q-2)/2 = 1+n+n^2, q=n;
    G: 8 + 6(q-1) + q(q-3)/2 + (q-1)(q-2)/2 = 1+n+n^2, q=n-1.

Consequently an invariant real symmetric Gram matrix is PSD if and only if the source's four contracted blocks are PSD. The sizes are G:8/6/1/1 and H:4/4/1/1. On the standard isotypic subspace, each cross-copy equivariant bilinear form is a scalar times the standard inner product. Contraction against the common c multiplies the multiplicity form by the positive factor 2. The nonunit embedding norms amount to invertible positive diagonal scalings. On U_q,V_q the scalar contractions are positive multiples 8 and 6 of the scalar eigenvalues. These normalizations cannot change PSD signs. Complexification gives the same conclusion for the real Gram certificates used with complex Hermitian input matrices.

This also predicts the full invariant symmetric coordinate counts:

    G: 8*9/2 + 6*7/2 + 1 + 1 = 59;
    H: 4*5/2 + 4*5/2 + 1 + 1 = 22.

There is no additional all-n block hidden behind the 81 orbit coordinates.

## 2. The block generator is an exact all-n contraction

The source's `orbit` canonically renames active letters and minimizes over exchange of the two Gram words. For G it keeps 0 marked. This is exactly simultaneous label-permutation invariance plus Gram symmetry. It does not identify a noncommutative word with its reversal. Two words of lengths at most 2 contain at most four active labels, so every such orbit is present at n=5. Enumerating on six letters defines a stable indexing convention, not a conjectured extrapolation from six letters.

The `reps_values` entries are precisely the eight/four trivial vectors, six/four standard vectors, switch and triangle described above. In particular its standard weights are +1,-1 on two fixed active labels; its P and M coefficients have the correct sum and difference signs.

For each block, `block_counts` fixes all anchor labels required by the representatives (and the marked label for G). Its anchor counts are respectively 1/3/5/4 for G and 0/2/4/3 for H. It supplies four formal fresh labels, sufficient for any pair of degree-two words. Among fresh-label patterns it keeps exactly the pattern in which distinct fresh labels first appear in their prescribed order. A pattern involving k distinct fresh labels has exactly

    (n - number_of_anchors)_k

injective assignments to actual nonanchor labels. The generator multiplies its signed representative coefficient product by this falling factorial and adds it to the appropriate orbit column. This is an exact combinatorial derivation of every entry R_i^T G R_j or R_i^T H R_j, for every integer n>=5. It also proves the pre-substitution degree bound 4 in n. Patterns impossible at a boundary receive the exact falling-factorial value zero; no separate n=5 continuation assumption is needed.

After constructing the 81-by-19 affine orbit matrix Z, the source pads these contraction rows into the appropriate G/H columns and multiplies by Z. Thus `affine_entry_rows` stores the complete contracted affine blocks in the same conventions as the representation proof. Their symmetry follows from contraction of the symmetric orbit matrix. The direct n5 map check in the source is a useful control but is not the basis of the all-n conclusion here.

## 3. Full-domain coefficient identity and normalization

For a word split as u i v, `coefficient_row` reverses the prefix u, takes i as the localizer label, and relabels i to the fixed G mark 0. It adds that G coefficient and subtracts the corresponding H coefficient. The term without an inserted letter contributes nH. These are exactly the coefficients of the Gram-localizer expression with localizers A_i and nI-sum_i A_i.

Every length-at-most-five equality pattern is realized on five letters. The 76 restricted-growth patterns therefore suffice for all n>=5. The source checks all 76 rows as rational identities after affine substitution, not only the pivot rows. Its target is C times the identity plus the **ordered distinct-word sum** D5: coefficient C on the empty word, 1 on each degree-five word with five distinct labels, and 0 otherwise. Accordingly the corresponding average has lower bound -C/(n)_5. There is no extra n, n!, or slack-color factor.

If the resulting full G and H are PSD, factoring them gives sums P* A_i P and Q*(nI-sum A_i)Q. This proves the target on arbitrary finite-dimensional Hermitian PSD inputs with sum A_i<=nI. No scalar-sum assumption is needed. An equality tuple may motivate kernel restrictions in the ansatz, but kernel necessity is not required for validity of a successfully checked localizer identity.

## 4. Physical parameter interval and specialization

Put

    N=32u^2-18u+1, E=16u^2-12u+1,
    n=N/E, a=N/(16u-6),
    u0=(3+sqrt(5))/8, u5=(21+sqrt(249))/48.

The physical interval is (u0,u5]. Its inverse branch for n>=5 is

    Delta=sqrt(20n^2-60n+49),
    u(n)=(6n-9+Delta)/(16(n-2)),
    a=n*u/(n-1).

Indeed n'(u)=-2(48u^2-16u+3)/E^2<0, E>0 on the interval, n tends to infinity at u0, and n(u5)=5. The quadratic in the derivative is positive because its discriminant is negative. Every finite integer n>=5 is therefore represented once. In particular a>0; the infinite-n endpoint is excluded from the representation claim.

The saved denominator ledger lists ten factors: u, u-1, u-1/16, u-1/2, u-1/6, u-1/8, u-3/8, and

    u^2-15u/16+3/32,
    u^2-17u/16+9/64,
    u^2-3u/4+1/16.

Their lack of physical zeros is also apparent without a numerical test. One has u0>1/2 and u5<37/48. The first two quadratic pairs of roots are (15 +/- sqrt(129))/32 and (17 +/- sqrt(145))/32; the smaller roots are below 1/2 and the larger roots exceed 13/16 and 29/32 respectively. The final pair is (3 +/- sqrt(5))/8, whose larger root is exactly the excluded lower endpoint. All listed linear roots are outside. This hand check verifies the classifications of the listed factors. The claim that this list exhausts every denominator still depends on the reviewed generating source and saved output, not an independent factorization replay.

## 5. G0 and G1 principal deletions are valid for every physical n

The original fourteen imposed kernel equations are retained in the final rational check `KD*Z=0`. They assert

    G0 qT=0, qT=(1,L,beta,L^2,beta*L,beta*L,beta*L,gamma),
    G1 qS=0, qS=(1,a,a,L,a,0),

where L=n-(n-2)a, beta=(n-2)a/(n-1), gamma=a[2(n-2)a-n]/(n-1).

On the specified branch,

    2(n-2)a-n = n[Delta-2n-1]/[8(n-1)],
    Delta^2-(2n+1)^2 = 16(n-1)(n-3)>0.

Thus gamma>0 for every n>=5. The projection of qT onto coordinate 7 is gamma, so deleting coordinate 7 from G0 is safe. This conclusion does not require inferring anything from the n5 kernel or preserving the exact generic kernel dimension.

The saved additional common G1 kernel is

    k=(0,n-1,-(n-1),0,0,1).

The first saved normalized kernel is qS/a and the second is k: the displayed rational strings use n-1=(16u^2-6u)/E and L/a=(10u-5)/E. The source obtains common kernels by stacking every coefficient matrix, including the affine constant, and checks each returned vector by exact multiplication against that stacked matrix over Q(u). The extra vector was not imported from a four-factor scalar identity.

For the two columns qS,k, their projection onto coordinates 4,5 is diag(a,1), which is invertible. Equivalently the saved normalized columns project to the identity. Deleting coordinates 4,5 from G1 is therefore valid uniformly over the physical interval.

The precise linear algebra is useful: if a Hermitian M annihilates columns K and their rows at a deleted coordinate set D form an invertible square matrix K_D, then every vector x differs from a retained-coordinate vector y=x-K K_D^{-1}x_D by a kernel vector. Consequently x*Mx=y*My. Thus M is PSD if and only if its retained principal block is PSD. This needs neither a prior PSD assumption nor equality of the kernel dimension with the generic one. Extra kernels at isolated n are harmless.

The generic output records G0 kernel dimension 1, G1 dimension 2, zero G3,H3, and no common kernels for H0,H1,G2,H2. Those dimensions describe the whole affine family over Q(u); they do not assert that each chosen matrix has exactly that rank at every n. The valid remaining matrix tests are G0 reduced to 7, G1 reduced to 4, and H0,H1 each of size 4. G2 and H2 remain separate scalar obligations. The five-factor identities G3=H3=0 must come from the five-factor computed entries, not merely from G3=H3 or from the old four-factor result. The saved entries report both identically zero; the source constructs all eight blocks before declaring this.

## 6. What is and is not independently established

The complete all-n representation decomposition, its PSD equivalence, the signed falling-factorial contraction formula, the full-domain localizer coefficient interpretation, the physical-branch signs, and the two deletion lemmas are established analytically above. No all-n statement here relies on testing finitely many numerical n.

The following dependencies remain source-bound rather than independently replayed in this review:

1. The 81-by-19 saved affine matrix and all eight large block-entry arrays agree byte-for-byte with a fresh exact derivation. I reviewed the construction and final identity checks, and bound this report to the actual source/output hashes, but did not regenerate those arrays.
2. The completed exact run's claims about all 76 coefficient rows, all 14 kernel rows, the extra stacked common kernel, and exhaustive denominator collection are accepted as outputs of the reviewed code, not as new computations performed by this reviewer. A standalone acceptance replay would be a separate task.
3. No claim of PSD for the four remaining matrix blocks follows from this review. The n5 anchor, family extremizer, affine rank, common kernels, or representation completeness cannot supply that missing positivity. The reported failed candidate remains closed.
4. This is neither an external human-referee report nor a priority or novelty determination. It does not certify that this Gram ansatz contains every possible proof, and it makes no universal extremizer claim.

There is no unresolved representation-theoretic assumption needed to pass from these eight correctly constructed blocks to full Gram positivity at an arbitrary integer n>=5. The unresolved acceptance obligation is the actual positivity of a source-bound candidate, which this report intentionally does not assert.
