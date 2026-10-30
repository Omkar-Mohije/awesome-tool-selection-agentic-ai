# P05 → Phases II–III: Portable Research Context

**Project:** Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems (survey-to-implementation study).  
**Course:** AI Tools for Research, IIIT Allahabad.  
**Current date/stage:** 2026-10-28; Prompts 01–05 completed as **planning**; no Prompt 06/07 or Phase III execution.  
**Researcher approval:** No explicit sign-off on the new research direction or frozen protocol is recorded.

## Original review and decision history
The review distinguishes invocation necessity, tool discrimination, retrieval, argument grounding and trajectory ordering. Five provisional gaps: dynamic tool sets; similar-tool confusion; selection-vs-downstream attribution; functional-versus-lexical retrieval; agent-as-tool delegation. Prompt 02 initially ranked dynamic tools, confusability, attribution. Prompt 03 proposed MetaTool/ToolE with BM25/dense retrieval on free Colab (Pathway B); Prompt 04 proposed replacing the correct tool with an equivalent one. Subsequent audit identified gold-label invalidation, recommended a matched-distractor alternative, and found extensive prior art overlap. Pre-P05 audit identified richer capability retrieval, multi-valid labels, abstention, clarification and calibration as established neighboring work. Its **unapproved, provisional** focus became distinguishing missing tool capability from missing user specification. Earlier decisions D001–D011 must remain historical, not silently overwritten.

## Prompt 05 working direction
**Working title:** Diagnosing Capability and Specification Uncertainty in Tool Retrieval: An Evidence-Grounded Evaluation.

**Primary RQ:** Does an explicit requirement/capability-evidence diagnostic improve three-way retrieval-stage decision quality versus calibrated retrieval-confidence policies when distinguishing SELECT, NO_VALID_TOOL and NEEDS_CLARIFICATION?

**Secondary RQ:** Across carefully matched counterfactual capability and specification changes, does the diagnostic switch decisions more appropriately than a calibrated threshold baseline?

**Optional RQ:** How do independently verified multiple valid tool IDs affect retrieval correctness and scoring conclusions?

**Status:** All questions and any associated hypotheses are INFERRED/planned. Novelty, data validity, computation and experimental effects are UNKNOWN. The full RQ-to-variable-to-metric and falsification mapping is in `P05_Research_Questions_and_Criteria.md`.

## Operational ontology
SELECT = at least one documented tool meets mandatory user requirements and the request provides enough information to choose it. NO_VALID_TOOL = no available tool meets essential capabilities/constraints after adjudication. NEEDS_CLARIFICATION = missing user specification changes which available valid tool should be chosen. MULTI_VALID = property of SELECT reference set, not fourth action. INSUFFICIENT_EVIDENCE = annotation-unresolved item, withheld from primary test until reconciled.

## Data candidates and precise access boundaries
- MetaTool/ToolE: https://arxiv.org/abs/2310.03128 ; https://github.com/HowieHwong/MetaTool ; README-listed `dataset/data/all_clean_data.csv`, `dataset/data/multi_tool_query_golden.json`, `dataset/plugin_des.json`. Earlier Colab observation: 20,614 rows with columns `Query`, `Tool`; 199 tool descriptions. Official README earlier reported 20,630 single-tool queries; reconciliation UNKNOWN. These facts DO NOT validate 3-way labels, sufficient query states or dataset permissions.
- ToolRet: https://aclanthology.org/2025.findings-acl.1258/ ; https://github.com/mangopy/tool-retrieval-benchmark . Retrieval queries/labels/tool descriptions publicly documented; direct fit to decision-state ontology UNKNOWN.
- Additional comparisons: Tool-REX, MFTR, ToolEX, AgentAbstain, SAGE-Agent / ClarifyBench; access and license compatibility **must be separately checked**; documentation of a download path is not execution.

## Related primary-source records (previous audits, not reverified in Prompt 05)
- Huang et al., MetaTool, ICLR 2024: https://arxiv.org/abs/2310.03128 ; https://github.com/HowieHwong/MetaTool
- Shi et al., ToolRet, Findings ACL 2025: https://aclanthology.org/2025.findings-acl.1258/
- Lu et al., Tool-REX, ICLR 2026: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e54a9889f1048526365ed8fb56c8c8cd-Abstract-Conference.html
- Tang et al., Multi-Field Tool Retrieval, EMNLP 2026: https://aclanthology.org/2026.emnlp-main.2212/
- Zhu et al., ToolEX, 2026 preprint: https://arxiv.org/abs/2609.08327
- AgentAbstain, 2026 preprint: https://arxiv.org/abs/2607.10059
- Suri et al., Structured Uncertainty guided Clarification, Findings ACL 2026: https://aclanthology.org/2026.findings-acl.2028/
- Zhao et al., Calibration is the Bottleneck, Findings EMNLP 2026: https://aclanthology.org/2026.findings-emnlp.305/
- Too Many Tools, Too Much Confusion?, Algorithms 2026: https://www.mdpi.com/1999-4893/19/6/447

## Baselines and conditions
**Essential:** same base retriever where possible; forced-top-one selector as diagnostic; max-score/margin thresholds; development-calibrated decision baseline; minimal transparent evidence-grounded decision rule. **Desirable:** stronger compatible published comparator; alternative retriever/reproducibility variation; no invented baseline reproduction. Inputs are request/inventory pairs with independently evidenced tool capacities and missing specifications, plus paired counterfactual variants. Hold positive-set completeness distinct from three action labels.

**Variables:** evidence policy; missing capability vs underspecification vs justified select; matched counterfactual type. Outcomes: decision macro-F1, false-selection under NO_VALID_TOOL, unnecessary clarification, correct transition on pairs, multi-positive-aware Recall@k, optional risk–coverage and latency. Success: predeclared, uncertainty-bounded paired differences with explicit safety/cost guardrails; no arbitrary numeric target. Failure: calibrated baseline equal/better or category annotations cannot be made reliably.

## Scientific risks and annotation requirements
Risk list: underdocumented tools, uncertain negatives, multi-valid alternatives, fabricated counterfactuals, annotations dependent on model outputs, annotator disagreement, data leakage between original/pairs, test-set calibration, benchmark contamination and strong overlap with published clarification and uncertainty studies. Require rubric for positive/negative/clarify/unresolved decisions, capability/parameter evidence for every label, independent annotation, agreement/disagreement accounting and adjudication, held-out test by group/family, and explicit redistribution terms. If labels are invalid, do not force the research direction.

## Phase II / Prompt 06 (NOT executed): required checks
1. Materialize genuine benchmark versions; inspect fields, IDs, descriptions, schemas, original splits and exact labels.
2. Confirm code/data/model weights licensing and whether redistribution is permissible.
3. Independently annotate a pilot of actual request/inventory pairs to test three classes and gold-tool completeness; measure annotator reliability.
4. Select baselines aligned to the decision space; check source code, checkpoint weights and comparable parameters.
5. Estimate actual free-Colab resource needs from legitimate diagnostics (no presumed GPU); choose minimal valid primary dataset and fallback.
6. Re-evaluate novelty against full closest methods, not just abstracts.

## Prompt 07 (NOT executed): freezing requirements
Only after Prompt 06 data and comparator go/no-go: lock problem, action ontology, annotation protocol and adjudication; preregister primary score, paired confidence-interval procedure, sampling seeds, power/precision rationale, dev/test splits, guardrail metrics, ablations, source versions and reporting artifacts. Change protocols only through dated decision entries.

## Phase III Prompts 08–10 (NOT executed): evidence standard
Test environment with console output, dependency versions, hardware diagnostics; establish a runnable baseline and compare behavior to verified reference protocol; inspect predictions, no-tool and clarification cases; record exact code/data/weights hashes, seeds, config, model outputs and failures. Only then perform modifications and controlled evaluations. No prior baseline/model execution is claimed by this P05 handoff.

## Decisions and approval status
See `research_decisions.md`: D001–D011 historical; **D012** appended as Prompt 05 working-question formulation, not final user-approved design. Preserve underlying history. Future approvals must be explicit. Current status: CONDITIONAL GO for data/annotation feasibility, not for implementation.

## Not completed
No validated three-way labels; no independent annotation panel or agreement; no resolved dataset version/licensing; no reimplemented baselines; no verified Colab environment this stage; no model training, experimental outputs, publication novelty proof or accepted manuscript.
