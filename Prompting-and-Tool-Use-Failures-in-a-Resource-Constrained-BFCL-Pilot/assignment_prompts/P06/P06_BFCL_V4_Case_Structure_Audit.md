# P06 continuation: BFCL V4 source-data audit

**Date:** 2026-10-29  
**Status:** Source-level validation completed; per-turn evaluation/labels, oracle, model execution, and publication novelty NOT validated.

## Official source inspected
- GitHub: https://github.com/ShishirPatil/gorilla
- Folder: `berkeley-function-call-leaderboard/bfcl_eval/data/`
- Official leaderboard: https://gorilla.cs.berkeley.edu/leaderboard

| JSONL source | Parsed records | Git blob SHA | Key attributes |
|---|---:|---|---|
| `BFCL_v4_multi_turn_base.json` | 200 | `656fbd5e56969373353cd58b880234a6cc4edc99` | id, question, initial_config, path, involved_classes, excluded_function |
| `BFCL_v4_multi_turn_miss_func.json` | 200 | `28e7987841719aec4e4f3f3f4b6c2f1915c831f3` | above plus missed_function |
| `BFCL_v4_multi_turn_miss_param.json` | 200 | `2e87caf87fb48f7807a18610311bdfa1138d0599` | id, question, initial_config, path, involved_classes, excluded_function |

All three files were fetched through GitHub's authenticated connector, parsed as one JSON object per line and counted. **No Colab run, BFCL model inference or official scorer execution was performed.**

## Pairing feasibility checks
- All 200 same-index case IDs exist across the base, missing-function and missing-parameter sets. **This suggests intended pair structure but does NOT establish 200 valid one-factor counterfactual triplets.**
- `initial_config` serializes identically across all three variants for 190/200 indices; **10/200 differ** and must be analyzed before pair-based causal claims.
- All 200 missing-function cases contain a `missed_function` entry.
- Example indexed family 0: base has four user turns; missing-function variant inserts an empty-user-message stage before the same final request and records missing `sort` in the `missed_function` mapping; missing-parameter variant replaces a specific file name with "one of the file" and supplies the file name at the next turn. This demonstrates **multi-turn, time-indexed intervention logic**, not a static query-only classification problem.
- Empty inner turn in the example is part of the JSON structure; its exact runtime/scoring semantics require checking the official harness.

## Research implications
1. **Major scope decision:** BFCL examines tool-calling agent decisions. It cannot be reported as retrieval-only Top-1 performance. P05's "retrieval-stage" problem statement needs a dated amendment if BFCL becomes the primary benchmark.
2. **Labels:** Missing-function and missing-parameter *scenario categories* are known from source files and documentation. This does not mean every turn is labelled NO_VALID_TOOL or NEEDS_CLARIFICATION. Need official per-turn expected actions and state-dependent handling.
3. **Novelty:** BFCL already provides missing-function/missing-parameter distinctions. A paper simply reclassifying these examples or adding a rule-based validator has insufficient independent contribution.
4. **Ground truth:** A structural/schema checker can verify declared parameter requirements, but detecting underspecification in unrestricted natural language requires ground-truth data and/or justified controlled templates. Do not claim entirely deterministic real-user intent.
5. **Method comparison:** Evaluate actual task-compatible baselines. Calibrated scores and a schema-aware decision rule must have identical information access; comparable metrics and calibration splits are required. Avoid test-set leakage when using public benchmark.
6. **Validation split:** keep whole indexed multi-turn family together. Exclude or separately study 10 families with non-identical initial configurations until causal comparability is verified.
7. **Data governance:** validate exact upstream license and use redistributable artifacts. Prefer source pointers and SHA rather than duplicating full BFCL inputs into public repo without review.

## Required next actions
- Pin upstream commit and inspect BFCL V4 per-category ground truth and scoring functions, including multi-turn missing-function and missing-parameter handling.
- Inspect all ten configuration mismatches and verify exact pairing.
- Establish per-turn rather than per-record decision labels.
- Design a no-human-review, **benchmark-grounded** evaluation with transparent evaluator unit tests (not circular AI labels).
- Implement and run at least two task-compatible policies with saved traces. Reassess novelty against BFCL and 2026 clarification/calibration research.

**GO/NO-GO:** CONDITIONAL GO to inspect scoring/labels; **NO-GO to freeze Prompt 07 now**.
