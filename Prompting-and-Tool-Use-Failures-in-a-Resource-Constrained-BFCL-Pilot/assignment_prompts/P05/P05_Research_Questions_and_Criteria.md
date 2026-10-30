# PROMPT 05 — Research Questions and Success Criteria

**Date:** 2026-10-28  
**Stage:** Prompt 05 planning only; Prompt 06/07, code and experiments NOT executed.  
**Status:** CONDITIONAL GO for label-feasibility work; study not frozen, user approval not recorded.

## Provenance and evidence labels
**VERIFIED** = supported by specified reviewed publication/official repository or recorded prior interaction; this is not a reproduced empirical finding. **INFERRED** = research design/hypothesis. **UNKNOWN** = needed evidence not obtained. This record draws from the prior PRE-P05 audit and the current user-supplied Prompt 05, and does not introduce new publication-verification activity.

## Working title and motivation
**Diagnosing Capability and Specification Uncertainty in Tool Retrieval: An Evidence-Grounded Evaluation.** Existing studies address tool-selection awareness (MetaTool), tool retrieval (ToolRet), capability-rich descriptions (Tool-REX/MFTR), multi-valid tool labels (ToolEX), abstention (AgentAbstain), structured clarification and action calibration (SAGE-Agent / Calibration is the Bottleneck). **VERIFIED as prior source descriptions, not as independently reproduced results.** Consequently the proposed three-action diagnostic is **INFERRED**, with novelty **UNKNOWN**.

## Precise problem statement
Given a user request *q*, an inventory of documented tools *T*, and evidence of tool capabilities and constraints, determine whether (i) some tool can justifiably be selected, (ii) no tool supports the request's stated needs, or (iii) a user requirement is missing and materially prevents choosing between viable alternatives. Assess whether explicit requirement/capability evidence improves these decisions compared with calibrated scores. The unit of evaluation is a **retrieval-stage request–inventory pair**, not full tool execution or an agent trajectory.

## Decision ontology
- **SELECT:** The request specifies enough to justify at least one tool, and available documented capabilities satisfy all mandatory constraints. Multiple accepted tool IDs may be recorded; MULTI_VALID is a label property, not a fourth decision action.
- **NO_VALID_TOOL:** On the specified interpretation and inventory, no tool demonstrably satisfies a required capability/constraint; mere low text similarity is not proof of absence. Uncertain documentation should not be silently assigned this state.
- **NEEDS_CLARIFICATION:** Available alternatives could satisfy plausible completions of the request, but a missing user choice/constraint materially changes the justified choice; asking that question could resolve it.
- **INSUFFICIENT_EVIDENCE:** Annotation holdout/unresolved provenance state, excluded from three-way ground-truth evaluation until adjudicated; not a predicted fourth action.

## Questions, hypotheses, controls and falsification

### RQ1 (primary)
**Hypothesis (INFERRED):** Constraint-evidence signals improve held-out decision quality over calibrated retrieval confidence.

**Input:** Adjudicated paired request/inventory records with tool descriptions/schemas; SELECT, NO_VALID_TOOL, NEEDS_CLARIFICATION.

**Comparator:** Max-score/margin and calibrated threshold policies; forced select as diagnostic floor.

**Independent variables:** Evidence signals/policy; counterfactual state (capability absent vs requirements missing).

**Dependent variables:** Decision correctness, errors by state.

**Metrics:** Macro-F1; false-selection rate; inappropriate clarification; paired agreement.

**Decision rule:** Pre-register paired improvement in macro-F1 with uncertainty interval excluding zero, without unacceptable degradation in critical false-selection; specify acceptable trade-off before test.

**Contradicting observation:** No reliable improvement, or significant increased false selection; indistinguishable label states.

### RQ2
**Hypothesis (INFERRED):** Counterfactual changes expose distinct failure patterns for threshold-only versus evidence-grounded policies.

**Input:** Matched counterfactuals differing in tool capability or missing requirement, with independently confirmed labels.

**Comparator:** Calibrated threshold policy.

**Independent variables:** Change type; policy.

**Dependent variables:** Correct transition in action; consistency.

**Metrics:** Paired decision consistency, transition confusion matrix, category-specific error rates.

**Decision rule:** Pre-registered comparison and confidence interval on correctly changing actions; report all transition classes.

**Contradicting observation:** Evidence policy fails to distinguish state changes or transitions worse than comparator.

### RQ3 (optional)
**Hypothesis (INFERRED):** Multi-positive-aware labels reduce misleading wrong-tool classifications without inflating decision correctness.

**Input:** Cases with multiple independently verified valid tools, separately marked as multi-valid property.

**Comparator:** Original single-positive scoring versus adjudicated multi-positive scoring.

**Independent variables:** Scoring protocol / label completeness.

**Dependent variables:** Retrieval correctness and discrepancies.

**Metrics:** Recall@k, positive-set accuracy, decision macro-F1 where appropriate.

**Decision rule:** Report paired scoring differences, uncertainty and manual audit; no automatic claim of improvement.

**Contradicting observation:** No material discrepancy or audit cannot establish alternative valid tools.

## Baseline ladder (proposed; none executed)
1. **Forced selection:** top-ranked tool without abstention; diagnostic reference, not a fair complete three-action baseline.
2. **Maximum score / margin policies:** use normalized retrieval scores or ranking gap with development-set tuned thresholds; may abstain but cannot necessarily distinguish clarification from no-tool.
3. **Calibrated baseline (essential):** train or fit decision calibration on development data only; never use held-out test labels to tune thresholds or select policies.
4. **Evidence-grounded diagnostic (proposed):** minimal explicit feature record for required capability, tool-schema compatibility and unresolved user constraint; map observed evidence to SELECT, NO_VALID_TOOL or NEEDS_CLARIFICATION by a fully documented decision rule.
5. **Stronger published comparator (desirable):** only when its official code/data, task mapping and decision space are verified as compatible; otherwise report incommensurability instead of fabricating an implementation.
Use a fixed underlying retriever across policies for the primary ablation; compare additional retrievers only as a secondary sensitivity experiment. Do not claim success merely against BM25.

## Necessary design and measurements
- Source request texts, tool IDs and descriptions/schemas; document capability/parameter restrictions and alternatives.
- Independently adjudicated tool-level validity and requirements: direct evidence with annotator provenance; distinguish unknown validity from negatives.
- Paired counterfactuals: change one element at a time (tool availability/capability vs specified user constraint); explicitly check which action should flip.
- Multiple valid tools: record complete set of supported positives where feasible; do not penalize admissible alternatives under one-gold scoring.
- Define an annotation guide, double-blind independent checks where available, agreement/confusion reporting and disagreement adjudication; split by underlying request/tool family before counterfactual augmentation to prevent leakage.
- Train/dev/test: freeze held-out test before threshold tuning or error-driven method changes. Repeat across predeclared random seeds when sampling inventories; archive all sample IDs.
- Metrics: decision macro-F1, NO_VALID_TOOL false-selection rate, clarification error by state, paired decision consistency and multi-positive Recall@k; optional risk–coverage and latency with specified coverage definition.
- Success is a **pre-registered relative decision rule**, not a fabricated numerical threshold: confidence intervals for paired differences plus cost/safety guardrails chosen before held-out tests. Negative or inconclusive comparisons are valid outcomes.

## Feasibility and validity gates
- **UNKNOWN:** MetaTool/ToolE and ToolRet do not yet establish the three-way labels or adequate real counterfactual pairs. Earlier Colab observation of 20,614 `Query`/`Tool` rows and 199 descriptions is a recorded observation, not proof of annotation validity; MetaTool README listed 20,630 single-tool records. Resolve filtering/version mismatch.
- **UNKNOWN:** the proportion of annotatable capability-deficient vs under-specified cases; sampling representativeness, independent agreement, permitted redistribution, published checkpoint compatibility, free-Colab resources.
- **Threats:** fabricated no-tool cases, artificially clear clarification templates, ambiguous functional equivalence, non-exhaustive tool docs, model-induced gold labels, correlated counterfactual leakage, calibration on test data, benchmark contamination, selection bias and external-validity limits.
- **Out-of-scope:** verified tool execution, multi-agent outcomes, trained new architecture, SOTA claims, publication acceptance, actual results.

## Contribution classification
**Already published / VERIFIED as source descriptions:** retrieval benchmarks and tool awareness; expanded tool descriptions; multi-valid relevance; abstention and clarification/calibration systems. **Proposed / INFERRED:** paired evidence-based separation of missing capability vs missing requirements and test of incremental decision value over calibrated confidence. **UNKNOWN:** novelty, annotation reliability, feasibility and measured improvement. A positive finding would not establish a new general-purpose agent architecture.

## Next-stage handoff (not executed)
Prompt 06 must verify accessible dataset versions/files, license, class feasibility, annotation evidence, comparator access and a trustworthy evaluation partition. Only after these checks may a protocol be frozen under Prompt 07.

## References already reviewed in prior research audit
- Huang et al., MetaTool, ICLR 2024: https://arxiv.org/abs/2310.03128 ; https://github.com/HowieHwong/MetaTool
- Shi et al., ToolRet, Findings ACL 2025: https://aclanthology.org/2025.findings-acl.1258/
- Lu et al., Tool-REX, ICLR 2026: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e54a9889f1048526365ed8fb56c8c8cd-Abstract-Conference.html
- Tang et al., Multi-Field Tool Retrieval, EMNLP 2026: https://aclanthology.org/2026.emnlp-main.2212/
- Zhu et al., ToolEX, 2026 preprint: https://arxiv.org/abs/2609.08327
- AgentAbstain, 2026 preprint: https://arxiv.org/abs/2607.10059
- Suri et al., Structured Uncertainty guided Clarification, Findings ACL 2026: https://aclanthology.org/2026.findings-acl.2028/
- Zhao et al., Calibration is the Bottleneck, Findings EMNLP 2026: https://aclanthology.org/2026.findings-emnlp.305/
- Too Many Tools, Too Much Confusion?, Algorithms 2026: https://www.mdpi.com/1999-4893/19/6/447
