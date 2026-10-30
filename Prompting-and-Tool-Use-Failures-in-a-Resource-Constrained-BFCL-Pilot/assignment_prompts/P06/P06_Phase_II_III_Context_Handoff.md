# P06 → Prompt 07 / Phase III Context Handoff
**Status (2026-10-28):** Prompt 06 source-level audit completed with **CONDITIONAL GO** for data-validation and annotation feasibility; experiment still NOT frozen. Prompts 07–18 NOT executed.

## Research continuity
Original literature review: *Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems: A Survey of Metrics, Benchmarks, and Open Challenges*. Earlier Prompt 02 gaps: dynamic tool sets; similar-tool confusion; selection-error attribution; functional retrieval; delegation. Historical Prompt 03/04 work studied MetaTool + BM25/dense retrieval and tool replacement; an audit rejected label-invalidating replacement as a default. Pre-P05 audit questioned novelty and prioritized capability-vs-specification uncertainty. Prompt 05 formulated the current working study: **Diagnosing Capability and Specification Uncertainty in Tool Retrieval: An Evidence-Grounded Evaluation.** Human final approval is not recorded.

## Primary question and hypothesis
Does explicit requirement/capability evidence improve three-class SELECT/NO_VALID_TOOL/NEEDS_CLARIFICATION decision quality over dev-calibrated retrieval-confidence policies? Hypothesis: improved risk–coverage or decision quality under independently adjudicated ambiguity; falsification: calibrated control equal/better, label ontology not consistently annotatable or mechanism adds no value. A secondary paired question asks whether decision transitions are more appropriate after capability/specification perturbations. Multi-valid reference tool sets are tracked separately. No results exist.

## Operational classes
SELECT: at least one supported, sufficiently specified available tool; NO_VALID_TOOL: documented lack of any fitting available tool; NEEDS_CLARIFICATION: essential missing user information changes selection. MULTI_VALID: SELECT property; INSUFFICIENT_EVIDENCE: excluded unresolved source support. No-tool does not mean a merely undocumented tool is incapable.

## P06 actual verifications
GitHub connector parsed MetaTool `dataset/plugin_des.json` (199 entries; blob `0c086d1a5e7b1586e8d5cafdf044871fa07aa8b8`), `dataset/data/multi_tool_query_golden.json` (497 entries; blob `193d1f6ef9ab52d6bc7e51100c69c0d9ab2de259`), `dataset/plugin_info.json` (390 entries; blob `20cbad749a67a3c2ecbdc6a9e2f6342a92e055a0`). Single-tool `all_clean_data.csv` is repository-listed, SHA `ae09901a3522df5ed0f83655f57267a4d6775e16`, but content retrieval yielded empty response and it was not parsed. Prior reported Colab 20,614 rows versus README 20,630 unresolved. In parsed multi-tool sample first actual query mentions Tesla news and has `[FinanceTool, NewsTool]`; these are original label names, not proven functionally exhaustive. ToolRet README publicly documents JSON relevance+parameter sample, but actual downloaded evaluation records were not parsed. Direct container network git access unavailable.

## Source links and licenses
MetaTool https://github.com/HowieHwong/MetaTool (repository marked MIT; dataset-specific rights UNKNOWN); ToolRet https://github.com/mangopy/tool-retrieval-benchmark (repo marked Apache-2.0; dataset-specific terms UNKNOWN), https://aclanthology.org/2025.findings-acl.1258/ . ToolEX https://arxiv.org/abs/2609.08327 (preprint; release and labels not parsed). AgentAbstain https://arxiv.org/abs/2607.10059 (preprint; repo not inspected). Structured Uncertainty / ClarifyBench https://aclanthology.org/2026.findings-acl.2028/ (published; dataset not inspected). MetaTool paper https://arxiv.org/abs/2310.03128 . Verify exact checkpoint license and free-Colab runtime later; no weights downloaded.

## Dataset decision
**Conditional source for an independently annotated extension: MetaTool/ToolE; NOT an accepted three-class benchmark.** Supplement tool metadata from plugin_info if stable mappings verified. ToolRet is an alternative for parameter-rich retrieval examples; ClarifyBench and AgentAbstain are better aligned to particular clarification/abstention behaviors but require compatibility checks. Neither a primary dataset nor an annotation panel is yet validated. No forced retrospective three-class labels.

## Comparators and splits
Mandatory fair controls: (1) calibrated three-way policy from score/margin/inventory features, development-only tuning; (2) simple threshold/score-margin selective rule with transparent action mapping. Forced-top1 BM25/dense is diagnostic, not an apples-to-apples three-class control. Proposed method: capability/requirement evidence. Strong published comparator only when action/task compatibility is verified. Report decision macro-F1, false selection for NO_VALID_TOOL, inappropriate clarification, paired transition correctness, multi-positive Recall@k, optionally risk–coverage and latency. Group original/counterfactual/paraphrase families in one partition. No leakage through templates, tools or tuning. Fixed thresholds and exclusions before test. No arbitrary split proportions frozen.

## Exact prerequisites to Prompt 07
1. Obtain complete CSV and metadata at pinned repository commit; parse columns/row counts, missing values, duplicates, identifier joins and original evaluation split.
2. Resolve the 20,614 vs 20,630 discrepancy.
3. Check data provenance and redistribution rights, plus model license/weights and runnable Colab footprint.
4. Independently review ~30–50 actual family cases; demonstrate all three classes can be justified from tool evidence; record agreement, unresolved cases and valid-tool sets.
5. Demonstrate that calibrated three-class controls are meaningfully defined and executable; inspect stronger comparators for exact action alignment.
6. Audit novelty against SAGE-Agent, AgentAbstain, ToolEX, MFTR, Tool-REX and calibrated action-selection work.
Only then freeze sampling, primary metric, paired uncertainty intervals, controls, seeds, data split, ablations and artifact names under Prompt 07. Changes require dated decision log entries.

## Phase III evidence standard
Preserve actual environment diagnostics, versions and checksums, original repo commits, runnable baseline traces, reference score verification (if comparable), authentic predictions, errors and logs. No current model run or effectiveness metric, trained model or new empirical outcome is claimed.

## Decision history
`research_decisions.md` retains D001–D012. P06 appends D013 as a conditional dataset and baseline recommendation rather than approval of frozen protocol.
