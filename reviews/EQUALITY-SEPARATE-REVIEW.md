# Separate adversarial hand review: equality and minimum dimension

19 October 2026. Reviewer: `sharpness_explicit_family`, a separately tasked
AI agent. **PASS for the stated finite-dimensional real/complex theorem**,
conditional on the accepted strict certificate and its complete invariant
word-space interpretation. I found no mathematical gap in the iff vector
conditions, the full-domain dimension lower bound, the dimension n-1
construction, or the optional direct word-value check.

Reviewed source: `KERNEL-EQUALITY-AND-MINIMUM-DIMENSION.md`, SHA256
`903967205ad25bff845a9f27d83cb964b19a5d323591a629c89ef65a32682aad`.
The source was not changed. This review used reading and hand derivation
only: no calculation program, imports, symbolic/numerical execution,
experiments, solver, refitting, network, publication or contact.

The certificate is `f4727ed67e787acb10208ca8fe7ea7a6c787cebfb117faf77df8647022843225`;
the independent replays and operator bridge are recorded in composite
acceptance `c64dd723abacd28724f3a8472dee2df3f7caa725b91ceca04cf3d826d26084ff`.
I also reread the representation review
`361a6fba36ca02c8bf9ee5676dbb4a175a0886e1fd9a2fa581a40d52931026ea`.
I did not rerun those replays or infer strictness from a floating margin.

## 1. Exact full kernels, rather than only known annihilators

At every finite n>=5 the Bernstein parameter is strictly positive. The
normalized reduced block is bounded below by the positive weight of its
last, positive-definite coefficient. Undoing the nonzero diagonal congruence
and positive scalar preserves positive definiteness. Thus the retained
G0/G1 ranks are exactly7 and4; their independently verified full kernels
have dimensions exactly1 and2. H0,H1 and the two symmetric scalar sectors
are strictly positive, while G3,H3 vanish. The excluded n=infinity endpoint
is not used for this rank assertion.

The passage from a contracted kernel to original word coordinates is sound:
if M=V*GV, G>=0 and Mq=0, then G(Vq)=0. The representatives V are not being
treated as an orthonormal basis. Vq, not an inverse-norm-scaled version of q,
is the full-coordinate kernel vector. All standard weight vectors of sum
zero are included. The complete decomposition then exhausts the kernel.
At n=5 the marked active-letter count is4; its standard and skew modules
have equal dimension3 but different characters and are inequivalent. No
missing or merged sector appears at this boundary.

I reconstructed displayed formula(5) from the representative coefficients.
The trivial direction gives constant active linear coefficient beta and
active pair coefficient gamma. The qS copy gives xi_j, a xi_j, L xi_j and
a(xi_i+xi_j) in the respective coordinates. The qK copy gives
+(n-1)zeta_j and -(n-1)zeta_j for marked/active orders and zeta_i-zeta_j
for active pairs. The remaining zero sector is precisely a skew active
pair array with zero row sums. This verifies the formula in original word
coordinates, including its factors n-1 and absence of extra norm factors.

## 2. Equality on the full subunital domain

With R=sum A_i and T=nI-R, equality in the positive localizer identity puts
the arrays A_k^(1/2)w(A)e and T^(1/2)w(A)e in their full kernels. The latter
has zero constant and linear coordinates, so Te=TA_i e=0. These are exactly
Se=e and SX_i e=X_i e after A_i=nX_i.

The marked linear coordinate gives A_k^2e=L A_ke. For the symmetric defect

    E_ij=A_iA_j+A_jA_i-2a(A_i+A_j-rI),

the marked and unmarked cases follow separately from
beta(L-a)=a(L-r) and gamma=a(2beta-r). They prove
A_k^(1/2)E_ij e=0 for every k. The slack array also has zero symmetric
quadratic, linear and constant coordinates, proving T^(1/2)E_ij e=0.
Consequently

    n||E_ij e||^2 = sum_k||A_k^(1/2)E_ij e||^2+||T^(1/2)E_ij e||^2=0.

This closes the potentially serious subunital gap: no invertibility of R,
or replacement of sum A_i<=nI by equality, is assumed. Division by n^2
gives exactly2h(X_i e+X_j e-b e), with b=1/(n-1).

For the converse I checked the sums in(8), not just the symmetric equations.
The quadratic relation gives y_k=Lf and y_kk=L^2f using
ker A_k=ker A_k^(1/2). Saturation gives [A_i,R]e=0. Hence sum xi_j=0 and
sum zeta_j=0. The active skew row sum is

    sum_(j!=k) (y_ij-y_ji)/2 = (n-1)zeta_i.

There are n-1 active indices, so subtracting zeta_i-zeta_j produces a skew
array with exactly zero row sums. This supplies every coordinate in(5).
For the slack array, constant, linear and diagonal coordinates vanish;
the defect equation kills its symmetric pair part; and
sum_j z_ij=T^(1/2)A_i R e=nT^(1/2)A_i e=0. Thus the converse places the
whole slack array in ker H. Positivity of the main polynomial converts its
zero quadratic form to the asserted vector eigenvalue equality. No fourth-
degree identity or commutativity of products is used.

## 3. Branch sign and the complex Gram argument

For F_n(x)=16(n-1)(n-2)x^2-6n(2n-3)x+n^2, the stated a is its larger positive
root. The vertex lies below1 since10n^2-39n+32>0 for n>=5. Moreover
F_n(1)=5(n-3)^2-13>=7. The discriminant is positive, and1 lies to the right
of the vertex with positive value; hence0<a<1. In particular
ell-2h=1-a>0 and h,b>0. This is essential, not a removable convenience.

Let v_i=X_i e and p_i=<e,X_i e>. The symmetric defect initially gives only
the real part of <v_i,v_j>. Testing it against v_i gives the stronger identity

    (ell-2h)<v_i,v_j> = 2h(ell-b)p_i-<v_i,X_jv_i>.

The right side is real for Hermitian X_j, so every Gram entry is real. This
handles complex ambient spaces rather than silently replacing their Gram
matrix by its real part. Its exact formula is

    M=diag((1-a)p_i+hb)+h(p1^T+1p^T-b11^T).

On the complex or real hyperplane sum z_i=0 the second term vanishes and
z*Mz=sum_i((1-a)p_i+hb)|z_i|^2>0. Thus rank M>=n-1 over the corresponding
field. Since every v_i belongs to ker(I-S), the stronger conclusion
dim ker(I-S)>=n-1 follows. At ambient dimension n-1 this forces S=I.

## 4. The smaller attaining family

The proposed m=n-1 simplex fits in e-perp of dimension m-1. With
alpha=1/m, d=ell-alpha and q=(1-ell)/m, one has d,q,h>0: indeed
ell>2/n>1/(n-1). Both terms in each active X_j and X_n=2hP are PSD.
I independently summed their P coefficients:

    [m(m-2)q+md]/(m-1)=1-2h,

while the ee* coefficient is1 and the cross terms cancel. Thus sum X_i=I.
The active v_j=alpha e+sqrt(alpha d)z_j lies in the rank-one block with
eigenvalue alpha+d=ell; X_n e=0. The two identities

    alpha-d/(m-1)=h,            mq/(m-1)=h

give exactly the claimed active anticommutator. The final-label relation is
2hP v_j=2h(v_j-b e). All iff conditions therefore hold. This establishes
attainment in dimension n-1, and with the preceding lower bound proves
the exact minimum over both R and C. It does not classify every equality
tuple or establish a quantitative stability statement.

## 5. Optional transfer/count check

I independently checked this optional argument. For a state written as an
e component plus coefficients on used active simplex vectors, the two
tracked coordinates are the e coefficient and the sum of those coefficients.
A fresh active matrix has transfer

    [[r,-g/(n-2)],[g,2a-r]],   g^2=r(n-2)(r-a),

with trace2a and determinant ra. The initial values1,r give
alpha5=8ra^4-8r^2a^3+r^3a^2. The final matrix2aP acts as diag(0,2a).
The two endpoint insertions vanish. The three remaining insertions sum to
-4ra^2(6a-r)(r-a), by the two- and three-power off-diagonal identities.

The counts are(m)_5 for words avoiding the final label and(m)_4 for each
fixed included position. The denominator is(n)_5=n(m)_4. Expanding the
result gives coefficients8r(n-2)/n, -4r^2(2n-3)/n and r^3(n-1)/n on
a^4,a^3,a^2, respectively. They equal8(2-r), -4r(3-r), r^2. At n=5 the
avoiding term has zero count; no fifth active label is implicitly required.
The active simplex representation has a unique invariant vector e, so
this coefficient is an eigenvalue of the permutation-invariant D5.
The branch stationary equation then gives t5(a)=-kappa5(n), with the same
raw/average normalization as the main theorem.

## Scope of the verdict

The extension is logically separate from the main lower-bound theorem and
uses its accepted strict certificate. The result concerns finite integer
n>=5 and equality on a nonzero vector. The known n-dimensional Zhong family
and recurrence remain prior work; this review does not certify priority for
the smaller family or equality theorem. No new literature search, human
specialist review, publication approval or computational experiment is
implied by this PASS.
