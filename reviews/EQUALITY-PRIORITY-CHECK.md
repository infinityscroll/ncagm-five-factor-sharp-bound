# Bounded priority check: five-factor equality and minimum dimension

19 October 2026, approximately 04:05–04:10 UTC. Private source review by a separately tasked AI agent. No scientific execution, fitting, proof replay, external message, purchase, or publication. This is a bounded literature comparison, not a novelty certificate or an additional mathematical correctness review.

**Finding: no matching five-factor equality theorem or minimum attaining dimension n−1 was identified in the inspected primary texts. The result appears distinct from their stated claims. Priority remains unresolved.** A recent two-factor rigidity paper is a direct conceptual antecedent and should be acknowledged when presenting the equality/dimension extension.

## Exact claim being compared

The reviewed extension concerns every integer n≥5 and every finite-dimensional real symmetric or complex Hermitian tuple A_i≥0 with ∑A_i≤nI. At the sharp five-factor lower endpoint, write X_i=A_i/n, S=∑X_i, and use the selected a=a_+(n), ℓ=1−(n−2)a/n, h=a/n, b=1/(n−1). It characterizes an attaining unit vector e by

    Se=e,   SX_i e=X_i e,
    X_i²e=ℓ X_i e,
    (X_iX_j+X_jX_i)e=2h(X_i e+X_j e−b e)  (i≠j).

It proves dim ker(I−S)≥n−1 and supplies a real construction in dimension n−1. Thus the minimum dimension for **attaining this exact lower endpoint** is n−1 over both fields. It does not classify all tuples up to a common reducing canonical block, prove stability, or determine the smallest dimension in which the ordinary five-factor Recht–Ré inequality can fail. Those are different claims.

The proof being compared is `KERNEL-EQUALITY-AND-MINIMUM-DIMENSION.md`, SHA256 `903967205ad25bff845a9f27d83cb964b19a5d323591a629c89ef65a32682aad`. The separate hand audit is `SEPARATE-REVIEW.md`, SHA256 `e1d5972958ff768e698261331a7d09430fe3484d991a2619350eb39bde35b30b`. Its necessary strict-kernel facts come from the separately accepted all-n certificate; a witness annihilator alone does not establish the iff statement.

## Primary-source comparisons

**Lai–Lim, ICML/PMLR 2020.** Section 3, published PDF page 6, Table 1 reports the numerical raw endpoint 144.6488 at m=n=5. The following discussion says their argument does not explicitly produce the five matrices and leaves the smallest dimension for a counterexample unknown. Therefore this text does not supply the proposed explicit four-dimensional n=5 attaining tuple, a general n−1 attainment construction, or an equality characterization. Their question concerns any violation, which is broader than exact-endpoint attainment; the present dimension theorem does not settle that separate minimum-violation question. Their SDP/SOS formulation remains a methodological antecedent. [Primary published PDF, §3](https://proceedings.mlr.press/v119/lai20a/lai20a.pdf).

**Zhong, arXiv:2610.04874v1.** Section 1.1, equations (2)–(5), explicitly constructs n matrices in R^{n×n}, using n simplex vertices in the orthogonal complement of one distinguished vector u. Appendix A gives the recurrence from which the campaign obtains the optimized five-factor family value. These are prior ingredients and must retain attribution. The inspected construction and theorem statements do not give an n−1-dimensional endpoint family or classify equality in the universal sharp five-factor bound. [Versioned primary text, §1.1 and Appendix A](https://arxiv.org/html/2610.04874v1).

There is also a limited algebraic reason the smaller construction is not merely deletion of an unused direction from Zhong's displayed family. In his notation A_i u=u+βz_i. On our chosen branch α=a_+(n)∈(0,1), β²=n−1−(n−2)α>0. The z_i span u-perp, and ∑A_i u=nu. Consequently the vectors A_i u span R^n. A common invariant subspace containing the endpoint vector u must therefore have dimension n. This rules out the obvious common-restriction shortcut only; it does not prove that the new construction could not be inferred by a different modification of known examples.

**ipitchford, exact-low-length repository, pinned candidate df3cb842014210eba99d1971be48aa079367feac.** The manuscript's lower m5 result is the ordinary unit bound for n≥6 and a counterexample for n=5. Its explicit n=5 example is De Sa's five-dimensional rational tuple, with normalized negative eigenvalue −19/16. Its “sharpness” language refers to the threshold n=6. Its equality-kernel discussion concerns the upper certificate and its representation blocks; it does not state the present sharp lower-endpoint vector identities or minimum attaining dimension. The public candidate supplies important certificate architecture, not a matching dimension theorem. [Pinned manuscript](https://github.com/ipitchford/exact-low-length-recht-re-inequalities/blob/df3cb842014210eba99d1971be48aa079367feac/paper/exact_low_length_recht_re.tex), [live project scope](https://github.com/ipitchford/exact-low-length-recht-re-inequalities).

**Zhao, “Sharpness and Rigidity of the Two-Factor Recht–Ré Lower Bound,” arXiv:2610.00155v1.** Theorem 5.1 classifies the real two-factor equality cases through a common reducing canonical n-dimensional block and proves that n is the minimum attaining dimension. Appendix A expresses the example using a regular simplex. This is closely related extremal geometry and must not be overlooked in claims about equality or dimension being a new type of question. The introduction and conclusion explicitly restrict the result to two factors and leave higher product lengths to separate analysis. It neither states the five-factor n−1 result nor implies it by replacing the product length: the endpoint, slack behavior and resulting dimension are different. The present extension is also weaker in classification scope than Zhao's common-block theorem. [Primary version, Theorem 5.1 and §8](https://arxiv.org/html/2610.00155v1#S5).

## What this check supports

A defensible description is: “For the sharp five-factor endpoint, the strict certificate yields necessary and sufficient vector conditions and proves that the minimum attaining dimension is n−1, with a real construction of that size. Zhong's known dimension-n family and the earlier two-factor equality/minimum-dimension theorem are related antecedents.”

Do not describe this as the first equality-rigidity result for Recht–Ré inequalities, the first use of simplex geometry, or a complete tuple classification. No “first-ever,” “priority established,” or “smallest counterexample dimension” claim is supported by this check. Extraction of equality from a strict SOS certificate and Gram-rank dimension arguments are standard proof ingredients; their use alone is not a new general method.

## Search scope, evidence and remaining gaps

I read the existing outcome-significance assessment and source ledger, searched the cached Zhong and pinned candidate manuscript for the relevant statements, inspected the primary Lai–Lim PDF, and read Zhao's actual two-factor theorem and scope. Live Zhong and repository pages were also inspected. Three narrow discovery queries were saved alongside this note:

1. `PRIORITY-SEARCH-1.json`: “Recht Re five factor equality minimum dimension attaining matrices Zhong”. It returned the relevant Zhao primary paper plus unrelated items.
2. `PRIORITY-SEARCH-2.json`: “noncommutative arithmetic geometric mean sharp equality rigidity minimum dimension five factors”. Results were predominantly unrelated and provide almost no negative evidence.
3. `PRIORITY-SEARCH-3.json`: quoted Recht/five/dimension/equality terms. Results were unrelated; this query is not evidence excluding prior art.

The saved search results are discovery receipts, not source substitutes. No exhaustive citation search was undertaken. The inherited audit's unread Xingtu Liu CISS2025 primary text (DOI 10.1109/CISS64860.2025.10944733), Lai's dissertation, alternate terminology, unpublished work, and unindexed sources remain coverage gaps. De Sa's construction was compared through the exact pinned primary manuscript that displays and attributes it; his entire original paper was not freshly reviewed here. The repository's entire current tree was not re-pinned in this check. A specialist may recognize a previously known equivalent construction even when the exact theorem is not stated in these sources.

Cached primary bytes actually inspected:

| Source | SHA256 |
|---|---|
| `overnight-ncagm-significance-forward-20261019/zhong-2026.txt` | `eb910a19cadc513386d4a8b2121445b69d419193322d07b6991cc8022e9cae95` |
| `overnight-ncagm-status-20261018/candidate/paper/exact_low_length_recht_re.tex` | `abd479bd75ccc8a79c34f8b5d74fb2eaab94a1f6555c3b9d3c61dbdec0286f99` |

The primary web reads are identified by exact versioned URLs above; this note does not claim a byte-level archive of those newly read pages. The inherited assessment's old pending-acceptance status was not used as the present correctness status. This check is limited to priority and attribution and leaves all frozen proof, package and ledger files unchanged.
