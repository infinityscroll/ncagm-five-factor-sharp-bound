# Sharp five-factor lower endpoint: adversarial theorem-bridge audit

19 October 2026. Private analytical and static-source review only. No worker,
scientific arithmetic, import, solver, numerical test, network request or
publication was performed for this audit. The independent arithmetic replay
remains separate.

**Verdict: PASS for the mathematical bridge, conditional on the exact saved
certificate and its original-word/representation-map identities being
independently replayed. No normalization, domain, finite-n boundary, or
attainment mismatch was found.** This is not a claim that this reviewer
regenerated the large arrays. The concrete additional map check in section5
closes a dependency that coefficient-PSD replay alone would leave open.

All paths below are relative to
`/Users/dusk/technical_contribution_scout_20261003/orthogonal-research-20261018`.

## 1. Precise theorem supported if the replay succeeds

For every integer n>=5 and every finite-dimensional real symmetric or complex
Hermitian tuple A_1,...,A_n satisfying

    A_i >= 0,                 sum_i A_i <= n I,

define the self-adjoint ordered distinct-product sum

    D5(A) = sum_(i1,...,i5 pairwise distinct) A_i1 A_i2 A_i3 A_i4 A_i5,
    (n)_5 = n(n-1)(n-2)(n-3)(n-4).

Set

    r = n/(n-1),
    Delta = sqrt(20n^2-60n+49),
    a = n(6n-9+Delta) / [16(n-1)(n-2)],
    c5(n) = a^2 [r(3-r)a - r^2/2],
    C5(n) = (n)_5 c5(n).

The asserted sharp lower inequality is

    D5(A) >= -C5(n) I,

or equivalently D5(A)/(n)_5 >= -c5(n)I. The normalized constant is positive.
It is attained on a nonzero vector by the explicit real n-dimensional tuple
in section4, so no smaller universal lower constant is possible. There is
no claim here of the minimum attaining dimension or of a full equality
classification. This proves a lower endpoint only, not the upper half of a
two-sided norm inequality.

The certificate target is the **raw** polynomial C5(n)I+D5(A). If one uses
X_i=A_i/n instead, the equivalent statement is D5(X)>=-C5(n)I/n^5 on sum X_i<=I.
The raw constant must not be left unchanged under that rescaling. The current
worker and original orbit map use A_i and the slack nI-sum A_i consistently.

At n=5 the raw constant is the separately established endpoint
3125(9033+581sqrt(249))/393216. The family and its recurrence are attributed to
Zhong; optimizing that recurrence is not claimed as a new family discovery.
Any priority statement about the universal sharp bound requires its separate
source audit. Existing claims of generic five-factor restoration for n>=6
must not be relabeled as unclaimed cases.

## 2. Certificate-to-operator bridge and exact normalizations

Let W_n be the word list of lengths0,1,2 in the n self-adjoint letters. For each
i, G_i is the marked Gram matrix obtained by permuting the distinguished
label of G; H is the permutation-invariant slack Gram matrix. The required
free-polynomial identity is

    C5(n)I + D5(A)
      = sum_i sum_(u,v in W_n) (G_i)_(u,v) u(A)^* A_i v(A)
        + sum_(u,v in W_n) H_(u,v) u(A)^* (nI-sum_i A_i) v(A).       (1)

If all scalar Gram matrices are PSD, factorization of each gives a sum of
terms P(A)^* A_i P(A) or Q(A)^*(nI-sum A_i)Q(A). Thus (1) is positive on the
full subunital domain. No substitution sum A_i=nI is used for the universal
bound. The equality-family kernel constraints only restrict the search;
their necessity is not required for validity of an exact positive identity.

I independently reread `coefficient_row` in the primitive and final workers.
For a target word split as prefix, inserted letter, suffix, the left Gram
word is the reversed prefix. The G coefficient is added, the corresponding
H coefficient subtracted, and the uninserted split contributes nH. This is
exactly (1). The marked-letter swap sends the inserted letter to0 without
collapsing equality patterns. In degree5 there is precisely the quadratic /
letter / quadratic split. Its target coefficient is1 for distinct labels,
not1/5!, 1/(n)_5, or n^(-5). The empty-word target is C5(n).

Every word through degree5 uses at most5 labels. Its equality pattern is one
of the76 checked patterns. Label invariance therefore extends these exact
coefficient identities to every integer n>=5, with no dimension restriction
on the input matrices. Matrix self-adjointness reverses products under *,
not individual letters' order by commutation; no commutativity is assumed.

I read the colleague's all-n representation review rather than duplicating
its entire representation proof. Its complete word-space decomposition is
consistent with the original `reps_values` and `block_counts` sources:

- Marked G blocks have sizes8,6,1,1 under S_(n-1).
- H blocks have sizes4,4,1,1 under S_n.
- The trivial and standard multiplicity forms, symmetric zero-row-sum pair
  module, and skew zero-row-sum pair module exhaust W_n.
- The standard contractions use c=e_a-e_b with squared norm2. The two scalar
  representatives have squared norms8 and6. These are positive factors,
  not inverse factors or sign changes.

The nonorthonormal representative vectors cause invertible congruences and
positive scalar multipliers; contracted-block PSD is equivalent to full
Gram PSD. At n=5 the G action has4 active letters: its symmetric pair module
is nonzero, and its three-dimensional skew module is inequivalent to the
three-dimensional standard module. Thus no exceptional missing block or
incorrect merger occurs at the smallest allowed n.

The full G0 kernel qT and G1 kernels qS,k permit the exact retained principal
blocks7 and4. With ell=n-(n-2)a, beta=(n-2)a/(n-1),
gamma=a[2(n-2)a-n]/(n-1), these are

    qT=(1,ell,beta,ell^2,beta*ell,beta*ell,beta*ell,gamma),
    qS=(1,a,a,ell,a,0),
    k =(0,n-1,-(n-1),0,0,1).

The final worker checks all these annihilations as rational identities.
For qT the deleted coordinate7 is gamma>0. Indeed
Delta^2-(2n+1)^2=16(n-1)(n-3)>0, so 2(n-2)a-n>0. For qS,k the deleted
coordinates4,5 form diag(a,1), which is invertible. A vector can therefore
be shifted by a kernel vector to have zero deleted coordinates, preserving
its quadratic form. Principal PSD implies full-block PSD even if extra
kernels occur at an exceptional parameter. The H blocks are not truncated.

The scalar obligations are retained: G2-H2=16, the individually positive
G2,H2 rational functions, and G3=H3=0. In particular the degree4 identity
G2=H2 was not imported into degree5.

## 3. Parameter, denominators, and Bernstein positivity

Write

    N=32u^2-18u+1, E=16u^2-12u+1,
    n=N/E, a=N/(16u-6),
    u0=(3+sqrt(5))/8, u5=(21+sqrt(249))/48.

On u0<u<=u5, E>0, n'(u)=-2(48u^2-16u+3)/E^2<0, n(u5)=5, and
n tends to infinity at u0. The inverse is

    u(n)=(6n-9+Delta)/[16(n-2)],  a=n*u/(n-1).

Thus every finite integer n>=5 is represented exactly once, on the larger
stationary branch used in TARGET. The infinite-n endpoint is not a finite
tuple specialization. The parameterization identity is

    16(n-1)(n-2)a^2 - 6n(2n-3)a + n^2 = 0.

The ledger's ten denominator factors have no physical zero: the seven
linear roots are0,1,1/16,1/2,1/6,1/8,3/8; the quadratic roots are
(15 +/- sqrt(129))/32, (17 +/- sqrt(145))/32, and (3 +/- sqrt(5))/8.
Here u0>1/2 and u5<37/48. The first two quadratic pairs have small roots
below1/2 and large roots above13/16 and29/32 respectively; the last large
root is exactly the excluded u0. This checks the signs/domain of the listed
factors. Exhaustiveness still requires the exact denominator-divisibility
checks, as performed by the source and to be repeated independently.

For each reduced source block B, the saved polynomial is

    P_B(u) = [d_B(u)^2/E(u)^v_B] D_B(n) B(u) D_B(n),
    D_B(n)=diag(n^(h_i-2)).                               (2)

All D_B entries are positive and nonzero at finite n>=5. The multiplier in
(2) is strictly positive because d_B has no physical zero and E>0. Thus no
sign can be lost when recovering B from P_B. The particular h vectors change
normalization, not the identity (1).

Let x=(u-u0)/(u5-u0). The exact certificate writes P_B as the degree-q
Bernstein sum sum_k binom(q,k)x^k(1-x)^(q-k) C_B,k. The104 stored coefficient
matrices are PSD in the positive Q(sqrt(5),sqrt(249)) embedding; each last
coefficient is PD. Therefore P_B is PD for every0<x<=1: its last term has
strictly positive weight x^q and every other term is PSD. The real-parameter
statement is stronger than the required integer-n statement. The numerical
discovery margin has no role in this proof, nor does its floating sign
certify any exact margin.

## 4. Explicit attainment in dimension n

This independently reconstructs the known-family attainment bridge. In R^n,
let e be the normalized all-ones vector, P=I-ee^T, and

    v_i=e_i-(1/n)1, z_i=sqrt(r)v_i,
    d=n-1-(n-2)a,
    A_i=a(P-z_i z_i^T)+(e+sqrt(d)z_i)(e+sqrt(d)z_i)^T.       (3)

The z_i are unit vectors perpendicular to e, sum_i z_i=0, and
sum_i z_i z_i^T=rP. The selected a is strictly between0 and(n-1)/(n-2),
so d>0; both summands in(3) are PSD. Summation gives

    sum_i A_i = n ee^T + [na+r(d-a)]P = nI.

For completeness, put s=2-r and b=3-r. The chosen a is the larger root
r[3b+sqrt(9b^2-16s)]/(16s). Since1<r<=5/4, b<=2, and
sqrt(9b^2-16s)<5, one has0<a<55/(64s)<1/s. This proves the feasibility
used above without relying on a numerical parameter check.

Expanding(3), with rho=rd and h=n(1-a), gives

    A_i=ee^T+sqrt(rho)(e v_i^T+v_i e^T)+aP+h v_i v_i^T.

After j distinct labels, write the current vector as
alpha_j e+sqrt(rho) sum_l eta_l v_(i_l), and put H_j=sum_l eta_l.
A new label has inner product -1/n with every preceding v_(i_l), giving

    alpha_(j+1)=alpha_j-(rho/n)H_j,
    H_(j+1)=alpha_j+(2a-1)H_j.

The transfer matrix has trace2a and determinant ar, hence

    alpha_0=alpha_1=1,
    alpha_(j+2)=2a alpha_(j+1)-ar alpha_j,
    alpha_5=t5(a)=8(2-r)a^4-4r(3-r)a^3+r^2a^2.

Permutation symmetry makes e the one-dimensional invariant subspace of
D5(A), and each distinct word has the same e-to-e coefficient alpha_5.
Consequently D5(A)e=(n)_5 t5(a)e. Using the stationary quadratic,

    t5(a)=a^2[r^2/2-r(3-r)a]=-c5(n).

The larger root exceeds r/[2(3-r)] (the stationary quadratic is negative
there), so c5(n)>0. This proves attainment of exactly the raw constant in
section1. The tuple has real entries, finite dimension n, and each A_i has
rank n-1. No full-rank assumption was used in the universal argument. The
same real tuple also witnesses sharpness over complex Hermitian inputs.

## 5. Concrete source-array gap and its exact closure obligation

The final source independently rechecks the original word identities from
the81 orbit functions. Its block entries, however, are obtained from the
saved `INPUT-BLOCKS.json` affine array. The primitive source constructs that
array correctly by contraction, and the colleague reviewed its semantics.
Nevertheless, a replay that merely trusts this same array and checks its
104 PSD coefficients does not independently close the orbit-to-Gram-map
link. I found no inconsistency in that link; it is a precisely identifiable
dependency, not evidence of a defect.

There are81 independent contracted entries to check: the upper triangles of
G0,G1,H0,H1 have36,21,10,10 entries, plus four scalar blocks. For each such
entry define the contraction coefficient L_(B,ij,c)(n) multiplying orbit
coordinate c. The direct formula is

    L_(B,ij,c)(n)
      = sum_(w,v in W_n : orbit(w,v)=c) R_B,i(w) R_B,j(v).   (4)

For G the orbit is marked, and the appropriate orbit offset is0; for H it is
unmarked with offset59. **Do not reverse the left word in(4):** the Gram
matrix is indexed by the word basis itself. Prefix reversal belongs only
to extracting the operator coefficient in(1).

The complete explicit representative definitions, in source order, are:

- H0: 1, sum x_i, sum x_i^2, sum_(i!=j) x_i x_j.
- G0: 1,x_0,sum_(i!=0)x_i,x_0^2,sum_(i!=0)x_0x_i,
  sum_(i!=0)x_ix_0,sum_(i!=0)x_i^2,sum_(i!=j;i,j!=0)x_ix_j.
- Put c=e_0-e_1 for H and c=e_1-e_2 on the active nonzero labels for G.
  H1: sum c_i x_i; sum c_i x_i^2; sum_(i!=j)(c_i+c_j)x_ix_j;
  sum_(i!=j)(c_i-c_j)x_ix_j.
- G1: sum c_i x_i; sum c_i x_0x_i; sum c_i x_ix_0;
  sum c_i x_i^2; sum_(i!=j)(c_i+c_j)x_ix_j;
  sum_(i!=j)(c_i-c_j)x_ix_j. Every G sum here is over active nonzero labels.
- Scalar symmetric switch on labels(i,j,k,l):
  ij+ji+kl+lk-ik-ki-jl-lj. Use(0,1,2,3) for H and(1,2,3,4) for G.
- Scalar skew triangle: ij+jk+ki-ji-kj-ik, with the first three labels of
  the corresponding switch.

Each pair of degree-at-most-two words contains at most4 labels not fixed
as representative anchors. Grouping injective assignments to k fresh labels
gives exactly(n-number_of_anchors)_k, k<=4. Hence every coefficient in(4)
is a polynomial in n of degree at most4. This is an analytical degree bound,
not an inference from samples. All needed anchors exist already at n=5.

Therefore root's proposed independent construction at n=5,6,7,8,9, followed
by exact degree4 Lagrange interpolation of these **integer count maps**, is
a valid proof of the complete all-n contraction map. One must interpolate
the count coefficients before substituting rational candidate functions;
the candidate block entries themselves are not degree4 polynomials in n.
The stable orbit indexing must be reconstructed canonically (six labels
suffice) rather than inherited by position without a code check.

After substituting n=N/E and the final81 orbit functions z_c(u), verify the
81 rational identities

    sum_c L_(B,ij,c)(N/E) z_c(u) = saved final B_(ij)(u).    (5)

This checks all full blocks, including deleted rows and scalar sectors, and
therefore validates the subsequent kernel reductions from the same actual
Gram matrices. Full symmetry supplies the remaining lower-triangular
entries. It does not require a new solver, candidate or sampled PSD test.
Root owns preparation/execution of this separate gate; this reviewer has
not prepared or run duplicate code.

The remaining acceptance package should thus independently establish:

1. The final81 orbit functions, all76 word coefficients, original/extra
   kernels, and exact scalar/denominator statements.
2. The direct all-n contraction-map identities(5), or an equally independent
   symbolic falling-factorial derivation of the same maps.
3. All104 exact Bernstein coefficient symmetries and PSD/factor identities,
   the four PD anchor matrices, exact reverse polynomial transforms, and(2).

If these pass, this audit identifies no further mathematical bridge gap.
An arithmetic failure must be classified at its exact identity; a failed
implementation is not automatically a counterexample to the theorem.
The old failed candidate and all failed attempts remain unchanged.

## Bound source records

| Record | SHA256 |
|---|---|
| `overnight-ncagm-m5-interior-margin-gate-20261019/CERTIFICATE.json` | `f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225` |
| Same directory `exact_gate.py` | `947fc9130c778891e37952fa8f7eab459f6341ae13b3631860cf1ba21bdd72b5` |
| Same directory `FROZEN-MANIFEST.json` | `f5d69dfc98c611ced4038f6e581461e693735f75bce2ca7b9bd23f95431ea5b1` |
| `overnight-ncagm-m5-uniform-semantics-review-20261019/REVIEW.md` | `361a6fba36ca02c8bf9ee5676dbb4a175a0886e1fd9a2fa581a40d52931026ea` |
| `overnight-ncagm-m5-general-candidate-20261019/GENERAL-FIVE-FACTOR-CANDIDATE.md` | `3584530ddca2fc965a1f3781a427c9e03353900af0c1d7ef5b87a14f49e1f128` |
| `overnight-ncagm-m5-primitive-preflight-20261019/AFFINE-FAMILY.json` | `7f8c881a0f58aa0d7e20f5e0b002b5c5d5b493299e8cb772d9eadd79f526a639` |
| Same directory `REPRESENTATION-BLOCKS.json` | `bab92a3fd0d78fab2a1018490a93cd342d66e2b0e32293c20b87e25890aa58db` |
| Same directory `DENOMINATOR-ROOTS.json` | `947edca5522d434307f9414d64002de57f8de524b916806a72c8c98e00a493d7` |

The first record is the newly successful candidate. This report does not
transfer acceptance to the earlier rejected coefficient functions.
