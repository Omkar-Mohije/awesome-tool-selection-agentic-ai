# Development pilot result — 20261029T122816Z-5e29a2e6

Date: 2026-10-29. **Recovery/execution completed; no observed complete-task improvement.**

## Official outcome

| Condition | Task successes | Reused records | Newly generated |
|---|---:|---:|---:|
| Vanilla | 0/6 | 6 | 0 |
| Generic control | 0/6 | 5 | 1 |
| Schema-evidence checklist | 0/6 | 0 | 6 |

All six records are variants of **two development families**, not six independent families. The 18 rows are paired condition/record executions, not 18 independent examples. This is not a general estimate of model accuracy. No significance, causal-effect or publication-novelty claim is supported.

## Integrity and authentic provenance
- Full original user-uploaded archive: [P06_BFCL_Development_Pilot_Recovery_Outputs.zip](P06_BFCL_Development_Pilot_Recovery_Outputs.zip).
- Archive SHA-256: `4b7178e4208094c16f04cdaf83235f2986a5923f1b910496d92d545c2b1eba40`; size 2912138 bytes.
- All **203** outer manifest file hashes match.
- The unchanged failed source attempt ZIP is included inside the archive. All **62** source-manifest hashes also match.
- All **11** reused result records were compared field-for-field with their original source records, and their source-file hashes match the saved provenance.
- Exactly 18 unique condition/case records are present, with all six selected IDs in each condition. No top-level inference exception is present.
- Source generic-control context-failure record was excluded from seeding and regenerated; the rest were preserved without rerunning to seek passing outcomes.
- Recorded generic-control loop termination was preserved as a legitimate model/harness task failure. It is not hidden or counted as a serving exception.
- These checks were run locally by the assistant on user-supplied outputs. Actual GPU generation and official scoring occurred in the user's Colab session, not in this workspace.

## What actually changed in the prompts
Inspected saved model-facing formatted prompts: vanilla has neither added instruction; all 116 saved generic-control steps contain its instruction, and all 101 checklist steps contain its checklist instruction. The conditions therefore ran with their intended prompt distinction. Different saved step counts are descriptive and do not establish efficiency improvements.

## Failure analysis
The official scorer reports these first-failure types across condition/case rows: `{"multi_turn:execution_response_mismatch": 4, "multi_turn:force_terminated": 1, "multi_turn:instance_state_mismatch": 13}`. These are first reported task failures, not an exhaustive count of all wrong actions.

File-system state errors dominate. The model creates or operates on directories/files in ways that do not match the reference state, including stray/wrong-location directories and incomplete transformations. Some cases also miss expected execution responses. Generic control has one force-terminated record after a tool-use loop, rather than a context exception.

The checklist changes some trajectories/error types but produces **no complete-task success gain on these six records**. This does not establish that it never helps, nor does it establish that partial behavior is equal. The current complete-task outcome has a floor on this tiny sample and cannot isolate missing-capability versus missing-user-specification reasoning from earlier file-operation failures.

See [paired per-case results](paired_case_results.csv) and raw detailed score files inside the archive. Do not invent cause labels from category names or empty tool-call lists.

## Resource outcome
The 24K server started successfully on the T4 using the existing FP16, 85% memory, single-request, eager V0, chunked-prefill-2048, no-CPU-swap/offload profile. Actual server profiler reports weights **7.61 GiB**, activation peak **0.16 GiB**, KV cache **4.57 GiB**, 2078 GPU blocks and zero CPU blocks. Profiling values are not continuous system-wide peak measurements.

Maximum observed input tokens by condition: vanilla 6234, generic control 9161, checklist 6716. The largest plus the preserved 4096-token answer budget is 13257, below cap 24576. No new context/recorded inference exception is present. This verifies resource feasibility for these recovered development records, not all BFCL tasks.

## Comparison limitations
Eleven records came from the original 12K-cap attempt and seven from the recovery's 24K-cap attempt. The recovery adds an explicit full-answer context guard. Raw provenance records that mixture; no single-run timing or uniform-seed-stream claim is made. The records that exceeded the old cap were explicitly retried, not silently excluded. Formal evaluation still needs a single fixed verified serving configuration.

Prompt lengths are not matched; order is fixed; the generic/checklist conditions share an additional tool-introduction explanation absent from vanilla; only one model and two development families are used; no calibrated action/no-call policy is fitted. Family 1 informed prompt design and is not held-out evidence. These limits preclude a final method claim.

## Decision and next step
**NO-GO for scaling the current checklist or claiming improvement from this pilot. CONDITIONAL GO for a focused validity/diagnostic audit. Prompt 07 remains unfrozen.**

Pause additional GPU runs. Before spending more compute, perform a CPU reference-trajectory replay on these same six cases to verify that the pinned evaluator/environment can accept author reference actions; that control must be labeled synthetic reference replay, never model performance. Then separate ordinary action/state failures from uncertainty-intervention behavior, and reassess whether any independently measurable diagnostic contribution survives. A reference control and a revised contribution are not yet executed/established here.

The negative pilot is preserved. Do not tune on these same records and later present them as unseen-test improvement.
