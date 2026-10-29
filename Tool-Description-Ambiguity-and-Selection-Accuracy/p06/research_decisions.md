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

## Methodology review after Prompt 04 — 2026-10-28
### D008/D009 status note (preserve prior recommendations)
- **Status:** Historical recommendations in Prompt 03 (D008: controlled comparison of BM25 and dense tool retrieval under churn/confusability) and Prompt 04 (D009: replace the original correct tool with a functionally similar replacement) remain recorded in the conversation; this note does not retroactively change or claim user acceptance of either.
- **Trigger:** In a replacement condition, the original gold identifier becomes invalid; an allegedly equivalent replacement cannot be validated from description similarity alone.
- **Alternative under audit:** Keep the original correct tool and keep candidate count fixed, comparing unrelated vs confusable distractors. This is a proposed revision, not a user-approved decision.

### D010 — Methodological audit and conditional recommendation
- **Date:** 2026-10-28
- **Status:** VERIFIED (the listed sources and repository READMEs were inspected); INFERRED (research design recommendation); UNKNOWN (dataset label adequacy, novelty, Colab execution)
- **Recommendation, not user-approved:** Prefer Design B over replacement-based Design A for a small *controlled replication/comparative robustness analysis* using BM25 and a pretrained dense retriever. Preserve the correct gold tool in both matched inventories. Do **not** claim novelty or treat this as proof of full LLM-agent tool-use reliability.
- **Reason:** Design A changes the target label unless functional equivalence of a replacement is independently established. Design B preserves the original positive but still requires a validity audit of all distractors; keyword/embedding similarity is not an adequate ground-truth oracle. Design B is strongly overlapped by already published distractor studies, including *Too Many Tools, Too Much Confusion?* (Algorithms 2026; Section 4.4 random vs semantically close distractors). Appropriate paper framing is replication/controlled cross-method comparison unless a distinctive contribution is independently verified.
- **Inspected primary evidence:** Huang et al., MetaTool arXiv 2310.03128 (abstract: similar choices, scenario, reliability, multi-tool; eight models in arXiv abstract), official MetaTool GitHub README (21,127 post-check queries; 20,630 single-tool and 497 multi-tool, reported by maintainers; named files; README says nine models); Shi et al., Findings ACL 2025 DOI 10.18653/v1/2025.findings-acl.1258 (ToolRet; retrieval baseline significance); ToolRet official GitHub README (query–label–tool example, e5-small-v2 example, Apache-2.0 repo license); Shen et al., NeurIPS 2024 TaskBench (tool graph, TaskEval); Blankenstein et al., ICLR 2026 BiasBusters (metadata/position effects); Zou et al., ICML 2026 AutoTool (dynamic tool-set training); *Too Many Tools, Too Much Confusion? Navigating Agentic Tool Selection at Scale*, Algorithms 2026 (random versus semantically similar noise already evaluated).
- **Verification limit:** Public README and examples inspected, but underlying full ToolE CSV/JSON not parsed and no Colab/model inference executed. Repository licenses do not independently establish every constituent dataset's redistribution rights. Detailed overlap and citation-forward search remain incomplete.
- **Candidate primary question (proposed):** On single-tool queries with a validated unique positive, how does swapping matched unrelated versus hard-negative distractors (at fixed tool-count) change top-1 correctness of BM25 compared with a small pretrained dense retriever?
- **Controls:** Same queries, gold tool, candidate counts, shared tool text fields, fixed retrieval configuration, matched negative-pool exclusions, seeded candidate sampling and consistent treatment of multi-valid cases; manual adjudication of a sample of hard negatives. Prefer fixed candidate-count 10 as a pilot, only if labels support it.
- **Next actions (prerequisites):** (1) Inspect actual ToolE dataset rows and tool-ID mapping; (2) assess whether confusable candidates are indeed invalid and quantify usable matched pairs; (3) confirm data and model license/weights access; (4) analyze the exact 2026 distractor study protocol and overlapping works; (5) verify environment on free Colab; (6) obtain user confirmation before changing design and before Prompt 05. Do not run experiment or declare contribution until these are satisfied.

### AI-assistance log — methodology audit
- **Date:** 2026-10-28
- **AI tool:** ChatGPT (web search, manual repository/publication inspection, local Markdown file editing).
- **User request:** Audit two candidate designs, verify foundations and dataset feasibility, recommend direction and update research record *without executing Prompt 05, writing implementation code, or fabricating results*.
- **Inputs:** User's detailed audit request, prior Prompt 03/04 responses in the conversation, existing research_decisions.md, primary publications and public repository READMEs.
- **Actual checks:** Publisher/arXiv bibliographic pages for MetaTool, ToolRet, TaskBench, BiasBusters and AutoTool; public GitHub README for MetaTool and ToolRet; searchable publisher excerpt of 2026 distractor-composition study.
- **Corrections:** Distinguish review claim from independently checked abstract; MetaTool arXiv abstract says eight evaluated models whereas official repository README says nine (unresolved version difference). Distinguish Zou et al. ICML 2026 AutoTool from Jia & Li AAAI 2026 AutoTool. Earlier presumption that matching candidate sizes alone establishes label validity is not justified.
- **No execution performed:** No benchmark run, trained model, measured outcomes, or human approval of new decision established.

## Pre-Prompt-05 publication-foundation audit — 2026-10-28
### D011 — Uncertainty-aware direction evaluated but NOT approved
- **Status:** VERIFIED (original publication records and publicly documented repository pages inspected); INFERRED (proposed direction/ranking); UNKNOWN (independent novelty, annotation reliability, experimental feasibility).
- **Historical record:** Retain D001–D010. The user introduced uncertainty-aware retrieval as a candidate, not a final decision. D009 replacement-based design and D010 matched-distractor recommendation remain historical proposals, not silently overwritten.
- **Key prior-art challenge:** Tool-REX (ICLR 2026) and MFTR (EMNLP 2026) already use richer/multi-field tool descriptions; ToolEX (arXiv 2026) explicitly expands labels for functionally equivalent tools; AgentAbstain (arXiv 2026), SAGE-Agent (Findings ACL 2026) and Zhao et al. (Findings EMNLP 2026) investigate abstention, clarification and action-class calibration. See `/mnt/data/PreP05_Research_Foundation_Audit.md` for exact public links and verification limits.
- **Recommendation only:** Explore *distinguishing absent tool capability from underspecified user requirements* in selective tool retrieval. This is a potentially useful question, **not established as new** and not user-approved. Defer an all-in-one algorithm; focus first on label feasibility and comparison with full closest methods.
- **Alternative rankings (qualitative):** 1 evidence-grounded select/abstain/ask under two uncertainty causes, conditional on reliable labels; 2 independent constrained multi-valid annotation/evaluation (ToolEX overlap risk); 3 honest replication of controlled distractor robustness; defer generic capability-aware retrieval and joint architecture.
- **Data caution:** User's prior Colab observation (20,614 rows, `Query`/`Tool`, 199 descriptions) differs from MetaTool README's reported 20,630 single-tool queries. Do not infer contradiction without checking revision, filtering and dataset definitions; this audit did not rerun Colab or recount records.
- **Decision status:** CONDITIONAL GO for verification and annotation pilot planning only. No Prompt 05 execution, code/model run, new experimental metric, human approval or research paper result is claimed.
- **Next:** Read full related methods; inspect actual data/version and licensing; produce human-reviewed rubric and feasibility sample; obtain explicit approval before freezing the direction.

### AI-assistance record — 2026-10-28 PRE-P05
- **AI tool:** ChatGPT (scholarly web search, inspection of official paper pages and repository READMEs, analysis of supplied earlier decision log, local Markdown editing).
- **Inputs:** User's PRE-P05 request, existing Prompt 01–04 and methodology-audit conversation, `research_decisions.md`, official scholarly pages and repositories.
- **Verified checks this interaction:** ICLR Tool-REX publication abstract, EMNLP MFTR entry and repo README, arXiv ToolEX content, AgentAbstain arXiv/README, Findings ACL SAGE-Agent entry, Findings EMNLP calibration paper entry, EMNLP MACRO, ToolRet/MetaTool public metadata, risk-aware retrieval preprint/repository.
- **Not verified:** Complete publisher full texts for every study, each experimental figure/table, human annotation, license inheritance of all benchmark components, executable dataset access, package compatibility, Colab model run, and independent novelty.
- **Human sign-off:** Not given; no approval inferred.


## Prompt 05 — Question formulation (2026-10-28)
### D012 — Provisional capability-versus-specification diagnostic; protocol NOT frozen
- **Date:** 2026-10-28
- **Status:** INFERRED (working question / design); VERIFIED only as previously documented prior-art descriptions; UNKNOWN (novelty, three-way labels, runtime, results).
- **Decision recorded:** Formulate Prompt 05 around the previously proposed separation of missing tool capability and missing user specification. This is a *planning selection*, **not a researcher-approved change, executable protocol or demonstrated contribution**.
- **Reason:** D009's replacement approach jeopardized original gold labels; D010's matched-distractor approach had major published overlap. PRE-P05 D011 identified a potentially meaningful decision boundary, while documenting overlap with established abstention, clarification, capability retrieval and calibration research.
- **Evidence:** Previous project audit `PreP05_Research_Foundation_Audit.md`; relevant original papers: MetaTool, ToolRet, Tool-REX, MFTR, ToolEX, AgentAbstain, SAGE-Agent and Zhao et al. (links in `P05_Research_Questions_and_Criteria.md`). This P05 step performs **no new primary-source or dataset verification**.
- **Question:** Whether explicit requirement/capability evidence improves SELECT vs NO_VALID_TOOL vs NEEDS_CLARIFICATION decisions relative to development-calibrated retrieval confidence, using adjudicated counterfactual pairs.
- **Alternatives:** Historical D008 BM25/dense, D009 replacement, D010 matched distractors; multi-valid benchmarking retained as optional analysis. None retrospectively deleted.
- **Critical unknowns:** Dataset access and license inheritance, existence/reliability of 3-way gold labels and valid counterfactual pairs, full closest-work overlap, calibrated baseline compatibility, Colab execution and publication novelty.
- **Approval:** Researcher's approval of final topic, label protocol and success criteria **not recorded**.
- **Next:** Prompt 06 resource/dataset/annotation verification. Do not freeze a protocol or implement code before go/no-go checks.

### AI-assistance log — Prompt 05 (2026-10-28)
- **AI tool:** ChatGPT for question formulation, editorial synthesis and local file generation; no fresh scholarly web verification or research execution.
- **User instruction:** User supplied a detailed Prompt 05 specifying provisional context, sources, evidence rules, four files and stopping before Prompt 06.
- **Materials reviewed:** Current provided Prompt 05, local `research_decisions.md`, `PreP05_Research_Foundation_Audit.md`, and prior project/planning history available in conversation.
- **Outputs:** `P05_Research_Problem_Brief.pdf`, `P05_Research_Questions_and_Criteria.md`, `P05_Phase_II_III_Context_Handoff.md`, updated `research_decisions.md`.
- **Verification:** Consistency audit of provenance labels, source links retained from prior audit, PDF generated and rendered for readability; no new empirical verification, human labeling, model execution or computed performance.
- **Human sign-off:** Not recorded.


---
## D013 — Prompt 06 source-level dataset and baseline audit (28 October 2026)
**Decision/recommendation:** CONDITIONAL GO to a MetaTool-derived independent *annotation feasibility* pilot; NO current dataset qualifies as verified three-way ground truth. Prefer a dev-calibrated three-class policy and a transparent score/margin threshold policy as the two fair controls; forced BM25/dense top-one is diagnostic only.
**Reason:** GitHub-file inspection confirms tool descriptions and original tool-use labels but not negative capability, missing specification or complete valid-tool sets. Single-tool CSV inspection blocked; available descriptions may not establish negative claims.
**Evidence actually inspected:** MetaTool repository README, `plugin_des.json` (199 entries, SHA `0c086d1a5e7b1586e8d5cafdf044871fa07aa8b8`), `multi_tool_query_golden.json` (497, SHA `193d1f6ef9ab52d6bc7e51100c69c0d9ab2de259`), `plugin_info.json` (390, SHA `20cbad749a67a3c2ecbdc6a9e2f6342a92e055a0`); ToolRet repository README with a relevance/parameter example; original ToolRet/ClarifyBench/AgentAbstain publication pages; ToolEX metadata/abstract. Single-tool CSV returned empty connector content; container git attempted and failed DNS.
**Statuses:** Source existence/sampled content VERIFIED; three-way label feasibility, data rights, primary test split, weights, Colab execution and publication differentiation UNKNOWN. Resource effort INFERRED. Previous D001–D012 preserved as history.
**Next actions:** Obtain/parse full single-tool CSV, reconcile row counts, audit mappings/permissions, independently annotate 30–50 families, check baseline runtime and compatible published controls, then decide whether to freeze Prompt 07 or revise the question.
**Approval:** Proposed technical recommendation; no explicit user approval or frozen protocol asserted.

### AI-assistance log — Prompt 06 (28 October 2026)
Tool: ChatGPT GPT-6, web original-source lookup, connected GitHub file fetch, local Python/ReportLab document creation. Activities: reviewed P05 handoff + exact P06 submission; fetched repository files and calculated reported JSON-key counts inside connector response; inspected scholarly pages; drafted dataset feasibility / annotation / comparators / leakage plan; created P06 deliverables. Not performed: full CSV download and parsing, human annotation, Colab model execution, license legal clearance, metric calculation or benchmark reproduction.

## PRE-P07 BFCL ground truth and schema validation — 2026-10-29

### D014 — Replace unverified three-way BFCL labels with source-grounded no-call analysis
- **Status:** VERIFIED (official BFCL V4 JSONL, possible-answer files and evaluator inspected); INFERRED (proposed research scope); UNKNOWN (novelty and full three-way cause labels).
- **Decision:** Retain the approved *exploration* of benchmark-supported, no-second-human-annotator validation. **Do not** treat BFCL category names or every empty reference call as gold SELECT/NO_VALID_TOOL/NEEDS_CLARIFICATION action labels. The currently supportable benchmark-facing outcome is call/no-call and execution-state success. A cause-aware diagnostic is a proposed secondary extension.
- **Reason:** Official `multi_turn_checker` evaluates executable calls against state/responses; `multi_turn_irrelevance_checker` tests absence of function calls on empty-reference turns and does not score clarification text.
- **Evidence:** upstream `ShishirPatil/gorilla` commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`; six JSONL and answer blobs with hashes in `P06_BFCL_Ground_Truth_Validation.md`; checker SHA `34b36715cdfaa4464ba1be137af4d30e85da8efb`. Observed 200 families/category, 734/934/934 turn slots, 3/203/203 empty-reference turns.
- **Alternatives:** preserve old retrieval-only question as historical; prefer tool-calling action reliability if BFCL becomes primary; a separated two-stage retrieval/call study is an optional extension, NOT a finalized design.
- **Next:** inspect exact per-turn active function availability and state; derive explicitly evidenced cause labels only for eligible subset; test model comparators before freezing protocol.

### D015 — Exclude ten structurally unequal initial states from strict matched-pair estimates pending resolution
- **Status:** VERIFIED (decoded initial configs recursively compared); INFERRED (strict-pair handling).
- **Decision:** Preserve all source cases, but hold out families 0, 38, 76, 139, 145, 154, 176, 188, 189, 193 from a same-initial-state causal estimate until their state differences are accounted for.
- **Reason:** Differences include additional files/directories, changed tweet content, watchlist entry, transaction timestamp, booking key and card expiry. Even the remaining 190 require intervention-turn state alignment.
- **Evidence:** `P06_BFCL_Pairing_and_Schema_Audit.md` with path-level comparisons and pinned upstream blobs.
- **Next:** check actual runtime states and reference trajectories; publish eligible IDs/exclusion reasons when established.

### D016 — Structural oracle tests and baseline execution boundaries
- **Status:** VERIFIED (five local structural assertions passed); UNKNOWN (semantic oracle, BFCL scorer reproduction and baseline performance).
- **Decision:** Save `bfcl_oracle_checks.py` and the proposed oracle specification, but prohibit describing this as a completed three-way oracle or as a model evaluation.
- **Evidence:** local command `python bfcl_oracle_checks.py` printed `5 structural oracle checks passed; no BFCL model execution or semantic label validation`.
- **Next:** validate official exposed function signatures, compare local checker against genuine reference data, run compatible BFCL model baseline and development-calibrated no-call policy with separate held-out groups.

### Authentic AI assistance log — PRE-P07
- **Date:** 2026-10-29.
- **Tool use actually performed:** GitHub connector fetched user repository artifacts and pinned official upstream BFCL JSONL, possible-answer and evaluator source; JavaScript decoded/count-tested 600 input and 600 answer records and compared ten mismatched configs; Python locally executed five **synthetic structural tests**; GitHub connector committed audit Markdown files and oracle test script.
- **Not done:** no official BFCL scoring run on model predictions; no model weights downloaded; no inference, calibrated policy fitting or Colab run; no independent human annotation or verified natural-language-to-schema oracle; no proof of novel publication contribution.
- **User approval:** approved investigating benchmark-supported, no-two-human-reviewer path; **NOT** approval of a frozen Prompt 07 protocol.
- **Recommendation:** CONDITIONAL GO for additional evidence collection; NO-GO for freezing Prompt 07 at present.

### D017 — First verified BFCL model smoke execution (2026-10-29)
- **Status:** VERIFIED for execution and official partial scoring on one indexed family; not a completed comparative experiment.
- **Evidence:** [run 20261029T113521Z-d72a657e](runs/20261029T113521Z-d72a657e/README.md), unchanged full archive, 36 matching file hashes, raw model traces, official per-case scores, dependency freeze and resource profile.
- **Outcome:** three records generated without recorded inference exceptions; official successes 0/3. Preserve failures rather than altering examples or reporting pipeline success as task success.
- **Compute:** Tesla T4 15 GiB / host RAM 12.67 GiB. Working serving profile: FP16, 12288 context, GPU utilization 0.85, single request, eager V0, 2048-token chunked prefill, zero CPU swap/offload.
- **Decision:** retain this as the verified software feasibility check and development evidence. Do not rerun solely to obtain passing examples; do not treat inspected cases as unseen held-out data.
- **Next:** audit error traces and exposed tools; then define a family-separated development pilot and fairly matched comparator/intervention.
- **Boundary:** no validated three-way semantic oracle, second calibrated comparator, frozen Prompt 07 or publication novelty is claimed. PRE-P07 remains CONDITIONAL GO.

### D018 — Audit actual tool exposure; prepare a development-only policy comparison
- **Date:** 2026-10-29.
- **Verified:** 14 saved turn slots audited. In the Qwen prompting path, restored mv is disclosed in a user message, cp remains model-visible, and tail.lines is optional/default 10. Block-only inventory checks and required-field-only semantic labels are insufficient.
- **Decision:** prepare families 2/3 as development data for vanilla, generic instruction control and schema-evidence checklist, using one persistent T4 server and official per-task scoring. Family 1 remains inspected development evidence.
- **Evidence:** [audit, exact prompts, notebook and limitations](development_pilot/README.md); observed turn CSV and reproducible offline auditor. Initial configurations of both candidate families match across variants; dynamic intervention-state equality is not established.
- **Validation:** local wrapper/audit/subprocess/archive checks and mocked three-condition flow pass. Real GPU comparison is unexecuted.
- **Boundary:** generic control is not a calibrated comparator; the checklist is a development intervention, not a proven contribution. Prompt length, fixed condition order, model-history divergence, semantic labels and final held-out design remain unresolved. No reference answer or future-turn leakage into policy prompts is authorized.
- **Next:** run the 18-record development notebook on the existing Colab runtime and inspect authentic outputs before protocol freeze. Prompt 07 remains unfrozen.

### D019 — Resume development after context failure without discarding valid work
- **Date:** 2026-10-29.
- **Observed:** vanilla completed; generic control reached a 12398-token request against cap 12288. Supplied console log is preserved under development_pilot/incident_20261029_context_overflow.md. No CUDA OOM is shown; no pilot task scores are established.
- **Decision:** synchronize effective handler/server context, try cap 24576 under the same T4 memory controls, preserve the full 4096-token answer allowance and all history, and reject oversize explicitly.
- **Recovery:** create a new run seeded only with non-exception original records, verify the source policy script hash, preserve original data/ZIP and record reused-result provenance. Do not overwrite or regenerate valid results merely to obtain successes.
- **Validation:** local context guard and synthetic seed/copy tests pass along with prior pilot checks. GPU recovery remains unexecuted by the assistant.
- **Boundary:** mixed-attempt development evidence is not a uniform-run timing/held-out comparison. Prior runtime profiles motivate 24K but do not guarantee new fit. PRE-P07 stays CONDITIONAL GO.

### D020 — Preserve negative completed pilot; pause expansion
- **Date:** 2026-10-29.
- **Verified:** [run 20261029T122816Z-5e29a2e6](runs/20261029T122816Z-5e29a2e6/README.md); 203 outer and 62 nested hashes verified, 11 reused records verified unchanged, seven new records, all 18 condition/case records officially scored. Intended instructions present in saved inputs.
- **Outcome:** each of vanilla, generic control and schema checklist scored 0/6. This is two development families, not evidence of population accuracy or a significant method effect. One generic-control loop force termination is preserved as a task failure.
- **Compute:** 24K cap worked on the T4 with the fixed 85%/single-request/chunked-2048 profile. No new recorded inference exceptions are present.
- **Decision:** do not scale or claim improvement for this checklist on the basis of this pilot. Pause further GPU use and first validate an explicitly synthetic CPU reference-replay control, then reassess cause-specific measurement and research differentiation. That control is not yet executed.
- **Boundary:** mixed-attempt provenance, prompt length/order confounds, earlier state failures and unvalidated semantic labels remain explicit. Prompt 07 stays unfrozen; CONDITIONAL GO for validity/diagnostic work, NO-GO for a checklist improvement claim.

### D021 — CPU reference sanity check completed; preserve secondary no-call audit
- **Date:** 2026-10-29.
- **Evidence:** [reference control](development_pilot/reference_control/README.md), six cases pass both decoded layouts with zero reference execution exceptions; six empty-answer and four no-call-violation controls correctly fail. Original official checker/tool code is hash-locked and unchanged.
- **Scope:** local CPU direct-checker control; not a Colab environment reproduction, model prediction, decoding test, or publication contribution.
- **Pilot audit:** 0/11 available decoded intervention records obey reference no-call turns; one force-terminated record has missing decoded evidence. This post-hoc descriptive result uses the existing development data and is not a held-out metric. Ordinary execution failures also remain.
- **Decision:** the planned direct evaluator validity check is complete; do not repeat/scale the same prompt conditions. Next research decision concerns independently measurable diagnostic value and novelty. Prompt 07 remains unfrozen; no improvement claim or extra GPU run follows automatically.

### D022 — Diagnostic novelty collision and corrected scoring boundary
- **Date:** 2026-10-29.
- **Verified:** original pinned evaluator imports but does not call the standalone multi-turn irrelevance checker. Unchanged AST-extracted evaluation function with real checker/identity decoder accepts 6 reference controls and 4 extra-read controls; standalone irrelevance rejects the 4 extra-read controls. Prior direct-checker results remain valid but do not validate production no-call enforcement.
- **Prior work:** BFCL already studies abstention; When2Call evaluates call/clarify/unavailable-tool decisions. Liu and Han (2026), *Asking Earns Nothing*, author repository `7f20cf1bdc37fc8d3954ef8488b80ef8bf8c9c02`, directly covers paired BFCL act/hold metrics. Full arXiv access failed; author repository and released scorer/data were inspected and the original scorer executed.
- **Descriptive replay:** two eligible missing-parameter pairs/condition; original published decision scorer yields vanilla 50%, generic 25%, checklist 75%; no inference test or held-out improvement claim. Strict-any-call and state-changing-attempt metrics differ.
- **Decision:** NO-GO for asserting novelty or checklist improvement from this evidence. Recommend course reproduction/negative-result scope for user review; do not silently substitute it for the original research goal. Prompt 07 remains unfrozen. No additional GPU generation.
- **Evidence:** [scope report, source locks, executed controls and original scorer logs](development_pilot/diagnostic_review/README.md).

### D023 — User approves output-based study; publication no longer required
- **Date:** 2026-10-29.
- **Explicit instruction:** proceed with an output-based study and drop publication as a required goal; retain the ability to experiment on the research question in future.
- **Active scope:** descriptive empirical pilot and attributed metric reproduction; report completed model outputs, negative task outcomes, software controls and limitations. No novelty or statistically established intervention benefit is needed or claimed.
- **Deliverable prepared:** [output-based study draft](output_study/README.md), based on preserved evidence. No new GPU run.
- **Protocol boundary:** this is retrospective analysis of already inspected development cases. Do not call it preregistered, frozen before execution, held-out, or an exact completed numbered Prompt 07 without checking the original assignment wording.
- **Future work:** keep families 1–3 as development evidence; preselect fresh family groups and fixed metrics/configuration before revised-policy experiments. Publication can be reconsidered later as a separate goal.

### D024 — Verify original assignment; distinguish study draft from submission completeness
- **Date:** 2026-10-29.
- **Sources actually read:** full original 11-page instruction sheet (18 prompts) and 28 October Classroom announcement requiring Phase III by 30 October, full phases/paper before end-sem exams.
- **Finding:** original P07 explicitly requires blueprint freeze before viewing results. No completed freeze is established for the inspected pilot. Existing outputs remain development evidence; do not backdate a protocol. A prospective protocol followed by fresh evaluation is the clearest compliance route.
- **Status correction:** the study Markdown draft is not the complete assignment or final LaTeX/PDF package. P08–P11 have substantial genuine technical evidence but still need consolidated reports, code understanding and authentic prompt-to-code records.
- **Next:** requirements-aligned Phase II/III packaging, prospective P07, then bounded fresh evaluation where resources permit; keep all prior outputs. Publication novelty remains unnecessary.
- **Evidence:** [requirement-by-requirement audit](output_study/assignment_status.md).

### D025 — Freeze prospective P07 and prepare instruction-aligned submission artifacts
- **Date:** 2026-10-29.
- **Authorization:** user requested completion of the ATR assignment under the approved output-based scope, all expected deliverables and reproducibility in the observed Colab environment.
- **Freeze:** commit `2d72394d1e725f7a80236661f600d995dd705b39`, ATR-P07-v1, fresh families 89/73 chosen deterministically before their model results. Six selected author references pass locally. New model execution is pending user-run Colab; the pinned one-cell launcher was supplied.
- **Code:** new notebook reuses warm Python 3.12/core pins; optional exact observed cold replay is TEST REQUIRED. Source and server/tokenizer/config model revision pinned; 24K/85%/one sequence/FP16/zero offload profile, no silent truncation or overwrite. Current notebook/child programs compile, nine current lifecycle/subprocess test groups pass; incomplete archives are rejected by analysis. None of these local checks is a GPU execution claim.
- **Prepared artifacts:** current research brief; P06–P18 validation, understanding, debugging, interpretation, internal review, reproducibility and authentic AI-use reports; six-page IEEE-style paper compiled from LaTeX/BibTeX with actual development figures; demo guide and portable handoff. Original negative results and their provenance remain intact.
- **Remaining:** actual frozen-run output ZIP, student-owned personal reflection/code review, final demonstration and Classroom submission. Paper labels prospective results pending. No fabricated outcomes, external peer review or personal understanding is asserted.
- **Evidence:** [submission entry point and status](submission/README.md).
