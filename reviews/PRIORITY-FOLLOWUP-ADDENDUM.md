# Focused priority follow-up: partial closure, Liu full-text gap remains

19 October 2026. This is a bounded primary-source applicability audit, supplementary to `ASSESSMENT.md` (SHA256 `5ec74c93c4c728bf5d2c5d7641717f43bcec44e2f6143d1ba5ef38d71e52c121`). It does not verify the new five-factor certificate or certify priority. No scientific code, solver, verifier, fit, experiment, purchase, authentication sharing, access-control bypass, author contact, or publication occurred.

**Verdict: PARTIAL_CLOSURE / LIU_FULLTEXT_GAP_REMAINS.** The primary papers read below do not state the proposed sharp five-factor lower envelope on the unrestricted domain `A_i >= 0, sum A_i <= nI`, for every integer `n >= 5` and every finite dimension. Liu's exact theorem remains unread, so his paper cannot yet be excluded on its title or abstract. The original assessment's conditional selection of the sharp all-n five-factor result is unchanged; “first” or comprehensive novelty wording is still unsupported.

## 1. Liu: what was actually retrieved

Target: Xingtu Liu, **A Note on Arithmetic–Geometric Mean Inequality for Well-Conditioned Matrices**, CISS 2025, DOI [10.1109/CISS64860.2025.10944733](https://doi.org/10.1109/CISS64860.2025.10944733).

The author's current [papers-by-topic page](https://rltheory.com/papers-by-topic/) lists the paper and links it directly to [IEEE document 10944733](https://ieeexplore.ieee.org/document/10944733). The saved author-page HTML, line 431, contains that link; it supplies no manuscript link for this entry. The author home page leads to the same publication list. The IEEE route returned a robot-verification/JavaScript interstitial in this environment. The DOI route did not yield full text. Exact DOI/title/author manuscript searches found publication records and the author list, but no readable author manuscript. A ResearchGate listing reported that full text was unavailable; no request was sent.

The earlier Semantic Scholar metadata describes a weak AM–GM result for matrices with small condition numbers. That is secondary abstract metadata, not an inspected theorem. **No exact condition-number hypothesis, multiplicative/additive constant, normalization, product-length range, or sharpness claim from Liu has been verified.** Peng's distinct theorem below must not be substituted for Liu's. There is no Liu-paper full-text hash in this audit; the author-page hash is only a discovery receipt.

This ends the bounded access attempt. A lawful readable manuscript or authorized publisher access is the precise missing input; no inference that the paper has no overlap is made.

## 2. Targeted primary citation and related-source checks

The earlier saved `s2-citing.json` was used only to select relevant leads among its 25 Lai–Lim citing records. It is a cached discovery index, not a fresh or exhaustive citation census. Each mathematical statement below comes from an inspected primary text.

### Zhao: a sharp endpoint, but only at length two

[Jinze Zhao, arXiv:2610.00155v1](https://arxiv.org/html/2610.00155v1), *Sharpness and Rigidity of the Two-Factor Recht–Ré Lower Bound*, §2, Theorem 2.2, gives

    sum_(i != j) B_i B_j >= -(n-1)/(4n) I

for PSD `B_i` with `sum B_i <= I`. Its sharpness and rigidity analysis concerns this quadratic quantity. The introduction explicitly says, “Higher product lengths and algorithmic convergence rates require separate analyses.” Thus it is relevant prior work for exact lower endpoints and equality structure, but does not supply the proposed five-factor constant. The live abstract page listed only v1 when checked. This was a statement/scope read, not an independent correctness audit of Zhao's proof.

### Peng: an explicit conditioning restriction, not the unrestricted lower envelope

[Binghui Peng, arXiv:2607.22620v1](https://arxiv.org/html/2607.22620v1), *A Resolution of the SS–RS–GD Inequalities*, §1, Theorem 3, states for `n >= 2`, `K >= 1`, `d >= 1`, and real symmetric matrices

    (1 - 1/(4n^2+1)) I <= A_i <= I

that `||W_RS|| <= ||W_GD||`, where `R = (1/n!) sum_sigma A_sigma(1)...A_sigma(n)`, `G = (1/n) sum A_i`, `W_RS = R^K`, and `W_GD = G^(nK)`. Section 4, Lemma 7, proves `0 <= R_tilde <= I` when `C_i = I+X_i >= 0`, their mean is at most `I`, and `max ||X_i|| <= 1/(4n^2)`.

These are explicit near-identity hypotheses. They exclude arbitrary singular PSD tuples and do not state a sharp negative five-factor endpoint. Positivity after a large scalar shift would not itself imply positivity of a chosen coefficient in that shift. The live abstract page listed only v1. Liu's unread constants remain separate.

### A related primary lead: AlphaEvolve's AM–GM problem is different

[Georgiev, Gómez-Serrano, Tao and Wagner, arXiv:2511.02864v3](https://arxiv.org/html/2511.02864v3#S6.SS28), *Mathematical exploration and discovery at scale*, §6.28, Problem 6.47, studies Duchi's ratio with a unitarily invariant norm **inside each summand**:

    [n^(-m) sum_all |||A_i1 ... A_im|||]
    / [(1/(n)_m) sum_distinct |||A_i1 ... A_im|||].

The section reports finite searches including length five without finding a counterexample to ratio at least one. This is not a signed Loewner lower bound for the matrix sum. Consequently the proposed sharp five-factor theorem would not resolve Problem 6.47. Only this relevant section and its version metadata were read, not the entire long paper. This was a related discovery lead, not a verified direct citation to Lai–Lim.

### Zhong: family attribution remains mandatory; forward coverage is incomplete

[Zhong, arXiv:2610.04874v1](https://arxiv.org/html/2610.04874v1), §1.1 and Appendix A, remains the primary source for the attaining covariance family and scalar recurrence. Section 1.2 gives a universal sufficient threshold, rather than the claimed all-n sharp five-factor lower envelope. The live [version page](https://arxiv.org/abs/2610.04874) had only v1 in the preceding assessment's same-day check. Targeted exact-ID/title follow-up searches did not expose a new overlapping primary theorem. One direct citation-API retrieval failed, so **no fresh complete Zhong forward-citation inventory was obtained**. This is not evidence of zero citations.

## 3. What this changes—and what it leaves open

The read sources support maintaining the distinction between a sharp unrestricted five-factor lower bound and prior quadratic endpoint results, conditioned AM–GM inequalities, ordinary low-length validity, and norm-inside-average problems. The clean research description remains the five-factor specialization of Lai–Lim's published §6 question, “What is the correct lower bound?” [PMLR 119 primary paper](https://proceedings.mlr.press/v119/lai20a/lai20a.pdf).

Acceptance still requires the independent replay and theorem bridge identified in `ASSESSMENT.md`. Priority still requires inspection of Liu's full theorem and adequate coverage of later/unindexed work. This bounded negative search cannot establish an absence of prior results. No new computation, refit, or publication is recommended or authorized by this note.

## Frozen source receipts

Fresh source HTML is saved in `priority-followup-sources/`. Hashes bind the retrieved bytes, not endorsement of their mathematics. Version metadata was read from the corresponding arXiv abstract pages; only versioned HTML bodies are archived here.

| Saved file | SHA256 |
|---|---|
| `priority-followup-sources/liu-author-papers.html` | `65214311221b90f7512ab075e1ae7b52a1c3311daf8d907dc7526803b3b62201` |
| `priority-followup-sources/zhao-2610.00155v1.html` | `9b9f5281539e524a16de8cc53cf918db08179a95b977b77b3e0cefeed8519ccc` |
| `priority-followup-sources/peng-2607.22620v1.html` | `61623d911c42ff1ee191210fe34e34bd45f94598a0b7457e4fb82c7c848584e9` |
| `priority-followup-sources/georgiev-et-al-2511.02864v3.html` | `cc1d96fa4a5dd4c9c9efda80205e25a483782bdd7373df4e8814b61f7958dbf9` |
| `../overnight-ncagm-significance-forward-20261019/zhong-2026.html` (existing primary cache) | `d6b871b7bdc2c462a7e88fbb74e07a356f8868f04ae7645bef91d25bfee7f49b` |
| `../overnight-ncagm-significance-forward-20261019/liu-metadata.json` (secondary, not theorem evidence) | `c96c7386ecc4934d6dee905d0e7840180074fba6ce0be6b9aa827178ba5bf21b` |
| `../overnight-ncagm-significance-forward-20261019/s2-citing.json` (cached discovery index) | `78a63b4512733f4e99537c9187c799eb11501e1d26af486bb030410cca6c4275` |

Primary locations in saved HTML: Liu publication link line 431; Zhao §1 scope and §2 Theorem 2.2 (`S2.Thmtheorem2`); Peng Theorem 3 (`Thmtheorem3`, lines 330 onward) and Lemma 7 (`Thmtheorem7`, lines 721 onward); Georgiev et al. §6.28 (`S6.SS28`, lines 3250–3315), specifically `S6.Thmtheorem47`. Source archive and report are private artifacts; no external communication occurred.
