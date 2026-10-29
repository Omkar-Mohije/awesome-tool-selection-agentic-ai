# P06 — Researcher-delegated decisions and deeper BFCL paired audit
**Date:** 2026-10-29
**Status:** user requested that routine human involvement be minimized/delegated; choices below are **assistant recommendations under this request**, not independent human judgments, signed approvals, or completed experiments.

## Decisions for next stage
- **Working scope:** BFCL V4 **multi-turn tool-call vs no-call reliability** as primary verifiable study. Treat no-call *reason* (capability unavailable vs information missing) as exploratory **only where rule-verified from the benchmark's input/intervention**, not as a universal official gold label. This supersedes retrieval-only framing *provisionally*, with earlier P05 retained.
- **Data:** pinned BFCL V4 base/miss_func/miss_param; preserve official benchmark outcomes and official evaluator, avoid inventing clarification correctness.
- **Comparison:** a single BFCL-compatible model with frozen settings as untreated control; a schema-evidence abstention policy on the *same* model outputs if technically supportable; simple existing no-call calibration decision tuned on development families. A second open model desirable for generalization. **None executed yet**.
- **Resources:** default open-weight model on free Colab if possible, no paid API or purchased hardware. If memory/compatibility prevents execution, report it and supply a reproducible alternative; do not claim run success.
- **Annotation:** NO fabricated independent human reviewers. No second annotator required for reference call/no-call or controlled oracle-backed subset. Natural-language clarification quality excluded from claims unless validated independently.
- **Scientific novelty:** unproven; BFCL and related clarification/abstention studies are directly relevant. Do not freeze publication claim or Prompt 07 until baseline and scope evidence meet requirements.
- **Administrative:** preserve historical decisions, use GitHub as the research log, prefer independent run hashes/logs, avoid asking for routine file movement or research formatting.

## Additional *executed* source-only comparison
Source: `ShishirPatil/gorilla` commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, `bfcl_eval/data/possible_answer/BFCL_v4_multi_turn_{base,miss_func,miss_param}.json` and corresponding inputs.
All 600 records parsed from three JSONL input/reference pairs using the authenticated GitHub connector.
- Base: 734 turn slots, 3 empty-call references.
- Missing function: 934 turn slots, 203 empty-call references.
- Missing parameter: 934 turn slots, 203 empty-call references.
- For **every one of 200 indexed families**: `empty_count(miss_func) - empty_count(base) == 1` and `empty_count(miss_param) - empty_count(base) == 1`. This is a **new verified structural fact**, and does *not* establish an index-level aligned, one-variable causal intervention or semantic three-way action correctness.
- 190/200 identical initial-config triplets as earlier recorded; ten require separate handling.
- Reference per-turn no-call is an *outcome shape*; it is **not evidence the model asked for clarification** or explained function absence.
- No baseline model, scorer, controlled policy intervention, significance test or human annotation executed.

## Explicit technical blockers and division of work
1. **Baseline running environment:** No Colab runtime controls available in this chat. Can prepare version-pinned scripts/notebooks and GitHub files; cannot truthfully execute on user's Colab without a connected runtime.
2. **Model choice:** select a publicly accessible, BFCL-compatible lightweight model only after verifying actual inference format, checkpoint license and resource needs. Defaults are research design choices, not claims of user-owned compute.
3. **Novelty:** validate against BFCL original intervention/scoring and 2026 prior art; publication remains contingent on a differentiated result and strong empirical evidence.
4. **Human involvement:** Only truly non-delegable actions such as opening the user's Colab, granting credentials or committing to academic claims require the user; do not create fictitious user sign-off or independent annotations.

**Gate:** CONDITIONAL GO to baseline-environment setup. NO-GO to freeze Prompt 07.
