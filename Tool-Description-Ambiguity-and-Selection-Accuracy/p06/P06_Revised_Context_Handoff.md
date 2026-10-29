# BFCL PRE-P07 — portable revised context (2026-10-29)

## Origin and decision progression
Original review: *Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems: A Survey of Metrics, Benchmarks, and Open Challenges*. P01–P04 considered evolving inventories, confusable distractors and BM25/dense retrieval. Gold-label and novelty issues led to P05 provisional three-way SELECT/NO_VALID_TOOL/NEEDS_CLARIFICATION diagnostic. P06 initially considered MetaTool-derived labels/human annotations; on 29 Oct the user approved investigating a **benchmark-grounded BFCL approach without two independent human annotators**. This is NOT approval of a frozen protocol.

## Current scientifically correct scope
**BFCL V4 is a multi-turn tool-calling benchmark.** Original possible-answer files describe expected tool calls or no calls on each turn, but do not supply evaluated three-way *reasons* for no-call. The official checker executes calls, compares states/results and checks empty turns for absence of calls. Our candidate diagnostic is cause-of-noncall under explicitly available function/argument evidence. Retrieval-only evaluation can be a separate optional secondary stage; do not silently use top-1 retrieval metrics for BFCL primary outcomes.

## Actual source inspection
Official repository: https://github.com/ShishirPatil/gorilla pinned commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`. Dataset path `berkeley-function-call-leaderboard/bfcl_eval/data/`; `possible_answer/` for reference trajectories; checker `eval_checker/multi_turn_eval/multi_turn_checker.py`, runner `eval_checker/eval_runner.py`. Dataset: 200 each base/miss_func/miss_param, same suffix indexing; 190 matching initial_config; 10 mismatches ID 0,38,76,139,145,154,176,188,189,193. Official reference per-turn empty-call counts: base 3/734, miss_func 203/934, miss_param 203/934. Each input's turn count matches reference trajectory. Blob SHAs and mismatch descriptions: see accompanying ground truth and pairing audit files.

## Evaluation ontology
Primary verified: `REFERENCE_CALL` vs `REFERENCE_NO_CALL` as a reference-call structural fact. Proposed causes `CAPABILITY_UNAVAILABLE`, `SPECIFICATION_MISSING`, `UNRESOLVED`, only when evidence and context justify. An empty call list does not mean a proper clarification, and a source record's category is not per-turn three-class gold. Not all empty turns occur at intervention; baseline itself has 3 empty turns.

## Evidence & tests
Python structural oracle helper executed locally with synthetic fixtures: five checks passed; it never executed BFCL official scoring, model predictions or natural-language reasoning. Companion source file `bfcl_oracle_checks.py` and `P06_Evaluation_Oracle_Specification.md`. All source comparisons were conducted through GitHub connector; container direct GitHub network resolution failed. Report types accurately.

## Baselines and unresolved checks
Comparator A: BFCL-compatible tool-calling model under official harness (not run). B: same model calibrated for no-call/action decision using development groups (not run). Proposed: minimal schema-evidence rule with no reference leakage (not implemented). BM25/dense are supplementary retrieval-only diagnostics, not comparable BFCL agent baselines. Official BFCL data README advertises Apache-2.0 but checkpoint/data-derivative rights and acceptable redistribution need checking. Compute/weights/Colab remain UNKNOWN.

## Novelty and go/no-go
BFCL itself tests missing functions and parameters; SAGE-Agent, AgentAbstain, calibrated tool-action decisions, Tool-REX and MFTR limit broader novelty. Possible contribution: correctly evaluated, provenance-verified attribution of no-call causes under controlled state-matched perturbations and task-compatible calibrated baselines. **Novelty UNKNOWN; no results.** CONDITIONAL GO to verify cause oracle and runnable baseline. **Do not freeze Prompt 07** until per-turn cases/contexts, strict pairings, evaluator tests and two actual compatible baselines have evidence. User must decide whether to accept a narrower action-selection paper, arrange appropriate model access and authorize any manual review for nonmechanical cases.

## Next gate
1. Verify official active-function exposure and state at each intervention turn.
2. Derive an eligible source-grounded cause-label subset; mark unresolved honestly.
3. Verify two compatible models/policies and run genuine baseline traces with environment logs.
4. Assess novel difference vs BFCL and clarification/calibration papers.
5. Then and only then consider Prompt 07.

## 2026-10-29 update — first verified GPU smoke execution

Supersedes earlier statements that all model execution and scoring are pending; those statements describe the historical audit stage.

Evidence: [run 20261029T113521Z-d72a657e](runs/20261029T113521Z-d72a657e/README.md), including the complete original output archive, hashes, raw traces/scores and environment/resource logs.

All three selected records generated without inference exceptions and the official BFCL partial evaluator completed. Official task successes: **0/3** (base and missing-parameter state mismatch; missing-function empty decoded-call turn). Thus execution feasibility is established for this one family; task correctness is not. No broader accuracy or three-class cause-label claim follows.

Verified hardware/profile: Tesla T4 15 GiB, host RAM 12.67 GiB; FP16, context 12288, GPU budget 0.85, one sequence/request, chunked prefill 2048, zero CPU swap/offload. Actual profiler: weights 7.61 GiB, activation peak 0.16 GiB, KV cache 4.57 GiB.

Second calibrated comparator, proposed intervention, held-out family-separated evaluation, valid cause-specific oracle and publication differentiation remain open. PRE-P07 stays CONDITIONAL GO; Prompt 07 remains unfrozen. Do not recruit a second reviewer for strictly mechanically verified outcomes. Continue analysis here; use the GitHub evidence and running log as the handoff to any other chat.
