# Research Decisions Log

**Project:** Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems  
**Created:** 2026-10-21  
**Purpose:** Portable, evidence-linked record of research decisions, reasons, uncertainties, and next actions.

## Evidence-status convention
- **VERIFIED:** Directly supported by an inspected document, primary source, artifact, or actual execution. Specify which evidence was examined; a claim appearing in a review is verified *as a review claim*, not independently established as fact.
- **INFERRED:** Plausible interpretation, design option, or tentative recommendation not yet empirically established.
- **UNKNOWN:** Evidence absent or insufficient; do not treat as a fact.

## Sources inventory
| ID | Source | Status | Notes |
| --- | --- | --- | --- |
| S01 | `Evaluating_Tool_Selection_Accuracy_in_Multi_Tool_Agentic_AI_Systems.pdf` | VERIFIED (file inspected) | 10-page existing survey/review; title, taxonomy, metrics, benchmarks and research-gap sections inspected. |
| S02 | Primary papers referenced in S01 | UNKNOWN (independent verification pending) | Verify bibliographic metadata, claims, experiment settings, and code/dataset availability before design decisions. |
| S03 | Local experiment code and run outputs | UNKNOWN | No experiment or baseline execution has been established. |

## Decision records
### D001 — Research scope is implementation-oriented, grounded in existing review
- **Date:** 2026-10-21
- **Status:** VERIFIED (user objective)
- **Decision:** Develop a defensible implementation-based research paper from the existing survey.
- **Reason:** User-defined research goal.
- **Evidence:** User request and S01.
- **Next:** Extract claim-to-source map and verify priority references.

### D002 — Maintain evidence-status labels and distinguish review claims from validated findings
- **Date:** 2026-10-21
- **Status:** VERIFIED (workflow decision)
- **Decision:** Annotate consequential research claims as VERIFIED, INFERRED, or UNKNOWN and retain source provenance.
- **Reason:** Avoid inventing references, datasets, experimental metrics, or novelty.
- **Evidence:** User request.
- **Next:** Build a literature evidence matrix with citations, exact passages, limitations and accessible artifacts.

### D003 — Candidate research gaps remain unconfirmed
- **Date:** 2026-10-21
- **Status:** VERIFIED (as claims in S01); UNKNOWN (as externally verified gaps)
- **Decision:** Keep the review's proposals provisional; do not freeze the research question yet.
- **Reason:** Review Section 6 discusses cross-benchmark standards, dynamic tool sets, functional retrieval, error disentanglement, agent-as-tool selection, and selection-aware rewards, but recent overlapping work must be checked.
- **Evidence:** S01, Section 6, pp. 8–9.
- **Next:** Search and validate primary research, especially newer work, for each shortlisted direction.

### D004 — Preliminary feasibility hypothesis
- **Date:** 2026-10-21
- **Status:** INFERRED
- **Decision:** Consider controlled tool-selection experiments with candidate-set size, near-duplicate tools, or evolving descriptions as potentially tractable directions, without committing to one.
- **Reason:** They may allow controlled evaluation of selection errors without live external tool side effects.
- **Evidence:** S01 Sections 3, 5, and 6; feasibility not yet tested.
- **Next:** Establish hardware, budget, model access, timeline, and baseline availability.

## Open questions
| ID | Question | Status | Next evidence |
| --- | --- | --- | --- |
| Q01 | Is S01 the final authoritative version of the review? | UNKNOWN | User confirmation or updated manuscript/source |
| Q02 | Which claimed gap remains novel after primary-source and current-literature checks? | UNKNOWN | Verified claim-to-literature matrix |
| Q03 | Which benchmark and baseline can actually be installed and reproduced? | UNKNOWN | Repository/dataset access, environment test, run logs |
| Q04 | What hardware, API budget, and deadline constrain experiments? | UNKNOWN | User constraints |
| Q05 | What paper venue or required manuscript format applies? | UNKNOWN | User/supervisor constraints |

## Next-action checklist
- [ ] Confirm review version and obtain editable source/BibTeX if available.
- [ ] Extract a claim–citation–evidence matrix from S01.
- [ ] Verify core primary papers, benchmarks, datasets, code licenses, and maintenance state.
- [ ] Shortlist 2–3 distinct, testable gaps and assess overlap with prior research.
- [ ] Establish experimental constraints and choose a scoped research question.
- [ ] Reproduce a verified baseline before implementing modifications.
- [ ] Predefine metrics, train/test separation, seeds, and reporting protocol.
- [ ] Record every experiment's code revision, environment, data snapshot, settings, logs, and outputs.

## Template for subsequent decisions
### DXXX — Short title
- **Date:** YYYY-MM-DD
- **Status:** VERIFIED / INFERRED / UNKNOWN
- **Decision:** ...
- **Reason:** ...
- **Evidence:** File/URL, section/page, executable log, or explicit 'none'.
- **Alternatives considered:** ...
- **Next action:** ...


## Stage 1 evidence audit — 2026-10-21
### D005 — Review evidence and latex source located
- **Status:** VERIFIED (local files inspected)
- **Decision:** Use ten-page review PDF as the citation anchor; treat the LaTeX archive as an editable manuscript source, not an independently verified evidence source.
- **Evidence:** Review Sections 2–6, Table 1 pp.4, 6–9; zip inventory includes `main.tex`, `references.bib`, and two figures.
- **Reason:** Source provenance must be distinguished from reported primary findings.
- **Next:** Inspect bib metadata against publisher records; check source-mapping and corrected metadata.

### D006 — Five provisional testable experiments
- **Status:** INFERRED (research gap / novelty unverified)
- **Candidates:** (1) Tool churn and deprecation robustness (review p9 Sec6; Gorilla). (2) Confusable tools and candidate-set composition (review pp6–8; MetaTool and TRAJECT). (3) Causal error attribution separating selection, argument, order, and execution (review pp8–9; TaskBench/TRAJECT/BFCL). (4) Functional retrieval vs lexical similarity under controlled paraphrases (review pp7–9; Shi et al ToolRet). (5) Delegation and agent-as-tool selection (review pp8–9; Tool-RoCo).
- **Reason:** Each supports labeled inputs, independent variable, and measurable outputs.
- **Next:** Validate originality and executable artifact availability; choose research question only after a pilot.

### D007 — Preliminary prioritization
- **Status:** INFERRED
- **Ranking:** 1 dynamic tool churn, 2 confusability/candidate composition, 3 diagnostic error attribution. Ranking balances topic significance, accessible synthetic/benchmark subsets, and manageable engineering requirements. Not novelty ranking.
- **Evidence:** Review pp6–9; selected independent checks include official MetaTool repository, Shi et al. ACL 2025 ToolRet + official code, TRAJECT-Bench arXiv abstract, Tool-RoCo arXiv abstract.
- **Next:** Obtain hardware/API budget/deadline; check existing benchmark licences, exact splits, APIs, and original-author limitations; reproduce baseline and keep leakage-free perturbations.

## Verification warnings
- Table 1 limitations are survey-author assessments unless confirmed in original paper limitations sections.
- Review reports MetaTool evaluation of 8 models in Table 1, but project repo says 9; resolve version/method discrepancy.
- Claims of 88.19% MLLM-Tool accuracy, candidate-size monotonic decline, and BFCL results require original-paper experiments or official evaluation code before stating as independently verified.
- The review already includes TRAJECT-Bench and Tool-RoCo; neither basic trajectory diagnostics nor agent-as-tool framing alone is novel.
- The formatted ACM Comput. Surv. footer is not proof of journal publication.
