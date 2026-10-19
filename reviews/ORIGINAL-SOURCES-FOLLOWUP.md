# Original-source follow-up: Lai dissertation and De Sa construction

19 October 2026, 04:08–04:12 UTC. Private bounded primary-source check. The two requested access gaps are closed: both original PDFs and De Sa's supplement were obtained from the institutions publishing them. No scientific computation, solver, source-code experiment, contact, purchase or publication occurred. Only retrieval, text extraction, page rendering and file hashing were used. This note does not certify novelty.

**Result:** the inspected original sources do not state the new all-n sharp five-factor equality characterization or minimum exact-attainment dimension n−1. They confirm prior ownership of the numerical n=5 endpoint, the noncommutative SOS approach, and the explicit permutation-covariant counterexample mechanism. This supports the distinction made in `EQUALITY-PRIORITY-CHECK.md`, but does not establish priority outside these sources.

## 1. Lai's dissertation: relevant chapter obtained and read

The citation was followed from Zhao's bibliography to the [University of Chicago record](https://knowledge.uchicago.edu/records/4b7ac-e4976): Zehua Lai, *Algebraic and Differential Geometry in Modern Optimization*, June 2023, DOI 10.6082/uchicago.6409. The [original PDF](https://knowledge.uchicago.edu/records/4b7ac-e4976/files/Lai_uchicago_0330D_16797.pdf?download=1) downloaded successfully despite the web reader's octet-stream rejection.

Chapter 2 occupies printed pages 5–28 (PDF pages 14–37). Its relevant statements are:

- Table 2.1, printed p.19: numerical raw-sum value 144.6488 for m=n=5.
- Printed p.20: the SDP argument does not explicitly produce the five matrices, and the smallest dimension for a counterexample is left unknown.
- Theorem 2.5.1 and discussion, printed pp.25–26: the improved two-factor bound and its all-n sharpness conjecture.
- Section 2.6, printed pp.27–28: the correct lower-bound question remains open; there is no sharp five-factor formula or extremizer-dimension theorem here.

The acknowledgments identify Chapter 2 with the joint Lai–Lim published work. Thus this is a later source preserving those questions, not an overlooked solution of the equality/dimension problem. Its uncertainty about any counterexample's smallest dimension should not be confused with minimum dimension for attaining the exact sharp endpoint. The unrelated thesis chapters were not reviewed.

## 2. De Sa: original paper and derivation obtained

The pinned candidate bibliography supplied the exact citation and URL: Christopher M. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 2020. The [publisher landing page](https://proceedings.neurips.cc/paper/2020/hash/42299f06ee419aa5d9d07798b56779e2-Abstract.html) links the [paper](https://proceedings.neurips.cc/paper_files/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf) and [supplement](https://proceedings.neurips.cc/paper_files/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Supplemental.pdf).

Section 2.1, printed pp.3–4, constructs n matrices in dimension n, A_i=I+1 y_i^T+y_i 1^T, with mean I. Statement 1 gives the exact product eigenvalue; at n=k=5 it is −19/16, with other eigenvalue 29/64. Appendix C, supplement pp.13–15, derives this using the simplex inner products and binomial expansion. These inspected statements supply neither the optimized five-factor sharp constant nor equality/minimum-dimension conditions.

The paragraph following Statement 1 explains enlargement to numbers of matrices and dimensions at least five by identity padding. It is an existence construction, not a proof that dimension below five is impossible. It also concerns the full-epoch comparison; it is not a sharp fixed-five-factor all-n theorem. Section 2.3's tight-frame/direct-sum example addresses a different norm placement and cannot be substituted for the current ordered-average lower endpoint.

## 3. Consequence for attribution and the remaining boundary

Retain De Sa as the explicit construction antecedent, Lai–Lim and Lai's thesis for the numerical endpoint and lower-bound question, and Zhong for the modified family/recurrence used to optimize the endpoint. The present equality theorem depends on the strict full-domain sharp certificate; it cannot be claimed merely from one attaining example.

The two specifically named coverage gaps in the preceding note are now closed at the relevant primary-section level. No matching claim was identified in those sections. Other coverage gaps remain: Xingtu Liu's CISS2025 primary full text, unindexed or unpublished work, and possible equivalent constructions under different terminology. No exhaustive priority or citation search was performed, and no claim of being the first equality result for Recht–Ré inequalities is justified. The two-factor Zhao antecedent recorded in the preceding note remains relevant.

## 4. Archived evidence and scope

All files below are in this directory. Whole primary PDFs are preserved; only the NCAGM chapter and relevant De Sa construction/derivation sections were extracted and examined. Printed Lai p.20 and De Sa p.4 were also rendered and visually inspected to confirm the dimension paragraphs and normalization.

| File | SHA256 |
|---|---|
| `SOURCE-LAI-DISSERTATION.pdf` | `64f1a185d4e86e43fb282ec01ffd50648537b67066cc858fcb8ff62777d7db7b` |
| `SOURCE-LAI-NCAGM-CHAPTER.txt` | `4798501be1b64ad27622f1110243d96f3db95ea3fdfd414a4e3677280baebb14` |
| `SOURCE-DESA-PAPER.pdf` | `30fd8f9e772d51d6d38905e10bd890b2d7e5b15e39b3961847f9bfdd692df550` |
| `SOURCE-DESA-SUPPLEMENT.pdf` | `6677bd0d8d59c6ce8541c48c114510673cc2016bc9b154e7cfbc9f3459fdc3d7` |
| `SOURCE-DESA-CONSTRUCTION.txt` | `762c4d137ea45b32b7a4545e17e2cf0abb251c9ec12148b96fe11e36444f341e` |
| `SOURCE-DESA-APPENDIX-C.txt` | `4b27eb4b0dfd407b401e42a1672170477e8c6d2e4b8220a23b44b74b7d13c99d` |

The existing extension proof, earlier priority note, package and campaign ledgers were not altered. This is an additive source receipt, not a new proof, mathematical replay, or human review.
