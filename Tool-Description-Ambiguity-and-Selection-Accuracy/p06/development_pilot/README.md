# P06 — post-smoke audit and development comparison

Date: 2026-10-29. Status: prepared and locally checked; **GPU comparison not executed**. PRE-P07 remains CONDITIONAL GO.

## Findings established from the saved run
The audit script processed all 14 observed user-turn slots from the original smoke archive, using each turn's saved step-0 formatted prompt. It does not replay the model or invent labels. See `smoke_tool_exposure.csv` and `audit_smoke_trace.py`.

1. `cp` is actually in the tool block throughout all three records, despite the dataset's `excluded_function: [cp]` metadata. Do not call the observed copy operation an invocation of an unavailable tool. Its problem is that copying does not satisfy moving the source file.
2. The missing-function record's tool block has 17 functions, excluding `mv`, through all five turns. At zero-based turn 2, the official prompting path introduces `mv` through a user message containing its specification. The tool-list block does not expand to 18. The restored specification is still visible to the model: unchanged block does **not** mean the model never receives the tool. A validator must account for tool-introduction messages and conversation history, not just the initial block.
3. Base and missing-parameter records contain 18 tools including `mv`. The earlier move was announced without an actual move call; these failures precede the later missing-parameter intervention.
4. `tail.lines` is optional with default 10; only `file_name` is required. The user later clarifies a desired line count. A required-field validator cannot establish that user-intent clarification is necessary merely by inspecting this signature. Dataset category membership is not a mechanically proven three-class label.

Pinned official implementation inspected:
- [base_handler.py](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/model_handler/base_handler.py): prompting path introduces held-out specifications in a message; the native FC path recompiles its tools. These paths must not be conflated.
- [utils.py](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/utils.py): initial function-document population and missed-function removal.
- [qwen_fc.py](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/model_handler/local_inference/qwen_fc.py): official text prompt formatter and tool-call parser.

## Pilot question and limits
Can a capability/state checklist produce useful development evidence beyond the official vanilla policy and a generic instruction reminder, under the same model, tool interface and official task scorer?

This is a small feasibility comparison, not a new benchmark, validated uncertainty-cause oracle, calibrated comparator or established research contribution. Both instructed policies modify the prompt; their results must be distinguished from unmodified official baseline results. No tuned threshold is being described as calibrated.

## Records and conditions
Use indexed families 2 and 3, with base, missing-function and missing-parameter variants: six records per condition, 18 executions total. Their initial configurations were compared across the three official input variants and match within each family. This does not prove intervention-state alignment; actual tool trajectories can diverge.

Family 1 has already been inspected and helped design these prompts. It is development evidence and cannot subsequently be claimed as an unseen held-out test. Families 2 and 3 are also development data; do not infer independence between their three category variants or generalize from two families.

| Condition | Input change | Role |
|---|---|---|
| vanilla | None | Official task-compatible baseline |
| generic_control | General task-review instruction; states how later tool introductions work | Second executable comparator type, uncalibrated |
| schema_evidence | Capability/argument/state checklist; same later-tool introduction rule | Proposed development intervention, unvalidated |

Exact instructions and injection code are in `p06_policy_runner.py` and embedded identically in the notebook. No reference trajectories, `missed_function` indices, category labels or future user messages are fed to the instruction. No runtime tool whitelist is constructed from future tool names. The official model-facing tools/history and decoding remain otherwise unchanged.

The two prompts are not token-length matched. Generic control and checklist share the same explicit later-tool-introduction instruction, but vanilla does not receive that extra explanation. Those differences limit attribution; this pilot cannot establish that any gain is due solely to schema reasoning. Formal comparisons need stronger matched controls, calibrated policies and family-separated held-out outcomes.

## Execution and resources
Open `P06_BFCL_Development_Pilot_Colab.ipynb` using the existing GPU runtime and run from the beginning. Existing Python environment and Hugging Face model cache are reused; nothing is deleted.

The same server remains loaded across the conditions, which execute sequentially in vanilla, generic_control, schema_evidence order. Evaluation occurs after server shutdown to release GPU/server RAM. Settings retain the observed working T4 profile: context 12288, FP16 on pre-Ampere, GPU budget 0.85, single sequence/request, eager V0, chunked prefill 2048, CPU swap/offload zero. Fixed order and cache warm-up mean latency must not be used as a fair policy-comparison result.

Initial prompt/context budgets are checked for all three instructions before model startup. Later history growth or other resource failures can still occur; they are saved and block scoring. Failures are not silently dropped, rerouted or converted into model successes. The final export ZIP includes condition-separated raw results/scores, full logs, status, script and hashes. Upload that ZIP here after execution.

## Outcomes and next gate
Primary development outcome: official BFCL per-record task success, reported by condition and family. Retain full traces and error types; compare the same six records across conditions. Do not infer semantic clarification correctness from an empty decoded-call list. With two families, statistical generalization is inappropriate.

Proceed toward Prompt 07 only after real pilot outputs establish comparable execution, useful failure diagnoses and a supportable outcome definition. A development-calibrated action/no-call policy, independently justified cause labels, intervention-state alignment and publication differentiation remain unresolved. The pilot can be uninformative or negative; preserve that outcome.

## Local validation actually performed
- All notebook cells, embedded child programs and the runner compile.
- The vanilla wrapper preserves the original formatter input/output behavior in fixtures; other wrappers inject only a copied system instruction and leave original history/tool objects unchanged.
- Auditor assertions confirm 14 turn rows, missing-function `mv` introduction at turn 2, unchanged tool block, `cp` exposure and optional `tail.lines` default 10.
- Real subprocess success, nonzero exit, timeout termination and archive hash/status checks pass.
- Mocked three-condition server lifecycle checks pass for readiness, server failure, generation failure, saved inference exceptions and missing records.

These checks do not constitute a BFCL GPU comparison. No pilot outcome or publication claim is reported.
