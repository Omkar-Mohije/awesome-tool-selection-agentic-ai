# P06 BFCL troubleshooting branch — running handoff log

Updated: 2026-10-29 (Asia/Kolkata)
Status: INITIAL SMOKE PIPELINE VERIFIED — 3 records generated and officially scored; task successes 0/3; research still CONDITIONAL GO.

## Purpose
Carry troubleshooting findings back to the original research conversation. Append new entries as errors are resolved. Do not treat setup repairs as experimental results.

## Preserved research state
- PRE-P07 remains CONDITIONAL GO; Prompt 07 is not executed or frozen.
- Primary scope: multi-turn tool-call versus no-call behavior using official BFCL.
- No three-class semantic ground truth or publication novelty is established.
- Another human reviewer is not required for mechanically verifiable outcomes.
- No baseline inference or official evaluation success is evidenced in this branch.

## Entry 001 — editable BFCL install failure
### Observed
User traceback shows /usr/lib/python3.13/subprocess.py and /usr/bin/python3.
Checkout printed commit 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8.
Failed command: /usr/bin/python3 -m pip install -e /content/gorilla/berkeley-function-call-leaderboard[oss_eval_vllm].
Exit status 1. Actual pip diagnostic lines were not supplied.

### Source-verified incompatibility
Pinned berkeley-function-call-leaderboard/pyproject.toml requires numpy==1.26.4 and optional vllm==0.8.5.
NumPy's official 1.26.4 release notes support Python 3.9–3.12, excluding the observed Python 3.13 kernel.
This establishes an environment incompatibility, but the first exact pip failure remains unconfirmed without pip output.
Sources:
- https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/pyproject.toml
- https://numpy.org/doc/stable/release/1.26.4-notes.html

### Repair prepared
Updated P06_BFCL_V4_Smoke_Colab.ipynb:
- Install uv and provision isolated Python 3.12 under /content/bfcl-py312.
- Keep pinned official BFCL source and dependencies.
- Install, check dependency consistency, and verify imports with that interpreter.
- Use /content/bfcl-py312/bin/bfcl for generation and evaluation; prepend that environment to child-process PATH.
- Stream subprocess output and save logs in /content/P06_BFCL_Logs.
- Include logs in successful final output bundle.
- Preserve raw install failure log when setup fails; obtain it through Colab Files panel.
- Correct misleading introduction: one indexed family across three category variants (three records).

### Validation performed here
Notebook JSON parsed and all Python code cells syntax-compiled locally.
No Colab GPU runtime, dependency installation, model inference or official evaluation was performed here.
Remaining risks: dependency resolution, GPU architecture/VRAM, model/backend compatibility, and official CLI behavior require real execution.

### Next action
Open updated notebook in Colab and run from the beginning with GPU enabled.
If setup succeeds, continue to inference and evaluation.
If setup fails, return install_bfcl.log (or failing step log), rather than just CalledProcessError.
Record every subsequent failure and resolution here.

## Entry 002 — Qwen-Agent import fails: missing soundfile
### Observed on the user's real Colab rerun
The generation command now uses /content/bfcl-py312/bin/bfcl.
Traceback enters bfcl_eval.__main__, model_config, the Qwen API handler, then qwen_agent.utils.utils.
It stops at `import soundfile as sf` with `ModuleNotFoundError: No module named 'soundfile'`.
Failure log: /content/P06_BFCL_Logs/generate.log.
This confirms an import-time dependency failure in the isolated environment. It does not evidence model loading, inference or evaluation.
The repeated 'Running:' line came from both the notebook and run_logged; it does not establish two inference attempts.

### Repair prepared
- Install `soundfile` using /content/bfcl-py312/bin/python -m pip, not the notebook kernel's pip.
- Retain all existing BFCL and vLLM pins; do not upgrade the model backend to address this import failure.
- Add complete Qwen-Agent and BFCL CLI import checks, plus generate/evaluate --help, before inference.
- Keep pip check and pip freeze for dependency diagnostics and recording actual resolved versions.
- Remove duplicate command prints.
- Current session can run the soundfile install and CLI preflight, then retry the existing generation cell without reinstalling the environment.
- If soundfile imports but a later import fails, preserve that new traceback; do not mark this as a completed baseline.

### Source inspection
BFCL's pinned pyproject lists qwen-agent but does not list soundfile directly.
Current upstream Qwen-Agent utils.py imports soundfile unconditionally. The user's installed traceback independently confirms the same import path; its installed package version has not been supplied.
- https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/pyproject.toml
- https://github.com/QwenLM/Qwen-Agent/blob/main/qwen_agent/utils/utils.py
Also checked pinned BFCL CLI generation/evaluation options and run-ID loader: the existing --run-ids flag, dictionary-shaped selection file and comma-separated evaluation categories match the source. BFCL_PROJECT_ROOT determines the selection-file location, and the notebook sets it to work before generation.

### Validation and limits
Updated notebook JSON parsed and every code cell syntax-compiled locally.
No Colab dependency repair, full CLI preflight, GPU model execution or official scoring was executed by this assistant.
The minimal patch must be confirmed in the user's current runtime. Model/GPU/backend compatibility remains unverified.

## Entry 003 — vLLM 0.8.5 tokenizer API mismatch
### Evidence from uploaded Colab output
Source: Pasted markdown.md uploaded in this troubleshooting branch.
- Qwen-Agent import no longer blocks execution; BFCL selects the intended model and run-ID mode.
- vLLM 0.8.5 starts, detects CUDA, and attempts tokenizer initialization.
- Failure: `AttributeError: Qwen2Tokenizer has no attribute all_special_tokens_extended` from vllm/transformers_utils/tokenizer.py, get_cached_tokenizer.
- Model server exits with code 1; generation.log records the failed generation command.
- Installed Transformers version was not printed; do not assert a specific installed version from this traceback alone.
- Log reports compute capability below 8.0, server dtype bfloat16 and native context length 262144. Exact GPU model/VRAM were not supplied in this attachment.
- The Hugging Face unauthenticated-download warning is not the fatal error.

### Diagnosis and source checks
Pinned vLLM 0.8.5's tokenizer wrapper directly reads all_special_tokens_extended.
Transformers 4.51.3 retains that tokenizer property and meets vLLM 0.8.5's declared minimum of 4.51.1. Qwen's official model card requires at least 4.51.0 for Qwen3.
Thus 4.51.3 is the selected compatibility pin, pending runtime confirmation. Do not upgrade the pinned backend or patch tokenizer semantics to suppress the exception.
BFCL's pinned OSS handler defaults to bfloat16 and does not expose max-model-len in its auto-launch command. The official --skip-server-setup option allows a separately configured local server while retaining official prompts, decoding and scoring.
Sources inspected:
- https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/transformers_utils/tokenizer.py
- https://github.com/vllm-project/vllm/blob/v0.8.5/requirements/common.txt
- https://github.com/huggingface/transformers/blob/v4.51.3/src/transformers/tokenization_utils_base.py
- https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507
- https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/model_handler/local_inference/base_oss_handler.py
- https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/model_handler/local_inference/qwen_fc.py

### Repairs prepared in notebook
- Apply transformers==4.51.3 as a pip resolution constraint when installing BFCL.
- Keep the soundfile repair and full CLI preflight.
- Load the authentic Qwen tokenizer and model config, verify the missing property, and call vLLM's get_cached_tokenizer before GPU server startup. Record version and resolved config commit hash.
- Start a separate local vLLM server and use BFCL's official --skip-server-setup option. No tracked BFCL source changes.
- Choose half (FP16) on GPU architectures below 8.0; use bfloat16 otherwise.
- Smoke-test profile: 8192 context tokens, one server sequence, one BFCL request thread, eager execution, V0 engine, server seed 0, GPU memory utilization 0.85.
- Save vllm_server.log and runtime_profile.json alongside generation/evaluation logs.
- Use a free local port, check server readiness with bounded waiting, and clean up only the process group launched by the cell.
- Keep the original model checkpoint and official QwenFCHandler; no vLLM tool-call parser is required because this handler formats prompts and parses tool-call text itself.

### Methodological effect
FP16 and an 8192-token context cap define a resource-limited smoke profile, not a full-context leaderboard reproduction. If a request plus generation budget exceeds that cap, preserve it as an infrastructure/context limitation; do not silently truncate, relabel or count it as evidence about uncertainty decisions. Confirm prompt lengths and serving feasibility before any full protocol is frozen.
The pinned BFCL handler still knows the native model context; server-side overflow checks may reject long requests. This limitation is explicit and requires runtime inspection.

### Verification status
Notebook JSON and Python code-cell syntax checked locally. Server lifecycle logic checked using mocked subprocess/HTTP behavior, including successful readiness, early exit and generation-failure cleanup; this does not test actual GPU inference.
Real dependency resolution, Qwen tokenizer check, server memory fit, inference and official evaluation remain pending in the user's Colab environment.

## Entry 004 — pre-run audit requested before another Colab attempt
### Confirmed defects and missing safeguards
- Found a bug in Entry 003's prepared notebook: the constraints file writer contained an escaped backslash+n rather than an actual newline. Syntax compilation did not detect it. Corrected the string and verified its generated file using pip's actual requirement-file parser.
- Existing result files could be silently reused on retry, including recorded inference exceptions. Generation now uses --allow-overwrite within an isolated run directory.
- BFCL may catch inference exceptions, write them into result records and exit with status zero. Added result-integrity checking before evaluation; zero process exit alone is no longer treated as success.
- Shared result/score directories and export staging could mix stale files into an output archive. Every setup creates a new timestamp/UUID run root; generation, scoring and exports use only that run.
- Previous export depended on completing generation and did not preserve stage status. Export is now defined before dependency installation; logged failures create a diagnostic ZIP with status and hashes. The final export cell may be run after a logged failure.
- Streaming child processes had no deadline or cancellation cleanup. Added a one-hour logged-command deadline and process-group cleanup; server readiness retains its separate 30-minute limit.

### Additional preflights and source checks
- Validate all three selected IDs through the official dataset loader and verify corresponding reference trajectory turn counts before starting the model server.
- Re-fetched the actual official index-1 inputs and references: base has 4 turns, missing function and missing parameter each have 5. This is a structural check, not an action-label or semantic correctness claim.
- Check initial prompt token counts using the official QwenFCHandler prompt formatter and tokenizer, reserving the handler's 4096-token generation budget against the 8192-token smoke cap.
- Later conversation growth can still exceed the context cap; recorded inference failures remain blocked from being presented as a successful smoke run.
- Rechecked generation/evaluation flags, --allow-overwrite support, run-ID loading, result JSONL format, model registry directory naming, environment-root handling, partial evaluation and official score output paths against the pinned source.
- BFCL_PROJECT_ROOT now points to the isolated run root, avoiding stale source-tree .env overrides. Package datasets still load from the pinned source package.
- Add notebook cell IDs for current notebook-format compatibility.

### Checks actually executed here
Ten local check groups passed:
1. All notebook Python cells and nested child-preflight program strings syntax-compile.
2. Pip's actual parser reads the generated constraints file as exactly transformers==4.51.3.
3. Real subprocess success and nonzero exit are logged correctly.
4. A real subprocess timeout is terminated and reported.
5. Failure archive includes result bytes, stage status and verified SHA-256 manifest hashes.
6. Mocked ready-server generation runs with official skip-server setup and overwrite flags.
7. Mocked early server exit saves diagnostics and cleans up the launched process group.
8. Mocked generation command failure saves diagnostics and cleans up.
9. Mocked CLI success with an embedded inference exception is rejected before evaluation.
10. Mocked CLI success with a missing result record is rejected before evaluation.
Mocked server tests are software-control-flow checks, not model/server performance evidence.

### Current log/output locations
New runs print /content/P06_BFCL_Runs/<run-id>.
Logs are in that run's logs directory; the ZIP is P06_BFCL_Smoke_Outputs.zip inside the same run.
The older shared /content/P06_BFCL_Logs path applies only to previous notebook versions.

### Remaining runtime checks
Full dependency resolution/install, real Qwen tokenizer preflight, CUDA/VRAM fit, server startup, model predictions and official evaluation still need the user's Colab GPU execution. No GPU is available in this assistant workspace; direct PyPI connectivity also timed out, so no full install was claimed. Local tests do not establish a complete end-to-end pass.

## Entry 005 — real inference succeeds, late-turn context budget exceeded
### Observed evidence
Attachment: Pasted markdown(1).md.
Server started successfully in FP16 at context limit 8192 on the user's existing GPU runtime.
Actual model inference ran across the three records for approximately 98 seconds. The base record reached completion; its correctness is not established until official scoring.
Two variants hit HTTP 400 at turn 4, step 0:
- multi_turn_miss_func_1: prompt 4164 + completion allowance 4096 = 8260, exceeding 8192 by 68.
- multi_turn_miss_param_1: prompt 4123 + completion allowance 4096 = 8219, exceeding 8192 by 27.
The official handler reports native context 262144, while the server enforces the smaller resource cap. It therefore continued asking for its 4096-token maximum answer allowance on growing conversation histories.
These are request/context configuration errors, not observed CUDA OOMs or evidence of an incorrect uncertainty decision. BFCL continued to 3/3 and returned zero; our result-integrity check correctly rejected the two recorded inference exceptions before scoring.
Messages saying 'Empty response from the model. Proceed to next turn.' refer to the official loop's empty decoded tool-call response and do not alone establish an error or an empty natural-language answer.

### User resource constraints
Reported GPU: approximately 15 GB VRAM.
Reported system RAM: 12.7 GB.
Reported available disk: approximately 40 GB, with previous data present.
Treat these as user-reported capacities; the notebook now records runtime measurements in GiB rather than assuming exact free resources.

### Resource-aware repair
- Increase the context cap to 12288 (12K); retain the official 4096-token answer budget and existing model/checkpoint.
- Retain GPU memory utilization 0.85, one sequence, one request thread, eager execution and FP16 on pre-Ampere GPUs.
- Disable CPU KV swap (--swap-space 0) and CPU weight offload (--cpu-offload-gb 0) to avoid consuming the limited host RAM for these caches/weights.
- Enable chunked prefill with max_num_batched_tokens 2048 to bound prefill activation work. This is a serving-profile change and is recorded for reproducibility; it is not a proven throughput improvement on this GPU.
- vLLM's GPU cache pool is governed by its memory budget and profiling. Increasing the maximum allowed sequence length does not itself double model weights or automatically imply allocation of a second model.
- Record RAM/disk before setup and server use, GPU total/free memory, and RAM after server cleanup. Preserve the actual server memory-profile log.
- Reuse the existing isolated environment and default Hugging Face model cache. Do not reset the runtime or delete old caches/data merely for this repair.
- Use pip --no-cache-dir for future installs to avoid adding new wheel caches; existing caches are preserved.
- Keep official source, prompts, decoding and scoring unchanged. Keep overwrite-on-retry, isolated run output, inference-error checks and failure archives.

### Verification and limits
Checked the pinned vLLM scheduler validation: max_num_batched_tokens below max_model_len is supported when chunked prefill is enabled; the paired flags are both supplied.
Checked pinned worker memory profiling and CPU-cache block allocation from swap_space_bytes.
Official documentation: https://docs.vllm.ai/en/v0.8.5/performance/optimization.html
Sources:
- https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/config.py
- https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/worker/worker.py
Updated code/child-program syntax, pip constraint parsing, subprocess/archive tests and mocked generation control-flow checks pass with the revised resource flags.
No local GPU execution was performed. Exact 12K KV-cache fit and end-to-end official evaluation remain to be verified on the user's GPU. Context growth beyond 12K remains possible in other cases; do not extrapolate this pilot configuration to all BFCL records.

## Return-to-original-chat summary
Real Qwen model inference is now evidenced. The base smoke record completed generation, while two variants failed because growing histories plus the official 4096-token answer budget exceeded our old 8192-token serving cap by 68 and 27 tokens. The result guard correctly blocked scoring these infrastructure failures.
The notebook now targets the user's 15 GB GPU / 12.7 GB host RAM with a 12288 context cap, 85% GPU budget, single request, eager FP16 on older GPUs, zero CPU swap/offload, and chunked prefill batches of 2048. It reuses environment/model caches and preserves previous files. Resource measurements are recorded.
Rerun the updated notebook using the same runtime; do not claim a complete benchmark or official score until all three records and the evaluator finish successfully.
PRE-P07 remains CONDITIONAL GO. Prompt 07 has not been executed; no publication result is claimed.

## Entry 006 — uploaded successful execution bundle verified

### Verified milestone

Supersedes earlier statements that all model execution and scoring are pending; those statements describe the historical audit stage.

Evidence: [run 20261029T113521Z-d72a657e](runs/20261029T113521Z-d72a657e/README.md), including the complete original output archive, hashes, raw traces/scores and environment/resource logs.

All three selected records generated without inference exceptions and the official BFCL partial evaluator completed. Official task successes: **0/3** (base and missing-parameter state mismatch; missing-function empty decoded-call turn). Thus execution feasibility is established for this one family; task correctness is not. No broader accuracy or three-class cause-label claim follows.

Verified hardware/profile: Tesla T4 15 GiB, host RAM 12.67 GiB; FP16, context 12288, GPU budget 0.85, one sequence/request, chunked prefill 2048, zero CPU swap/offload. Actual profiler: weights 7.61 GiB, activation peak 0.16 GiB, KV cache 4.57 GiB.

Second calibrated comparator, proposed intervention, held-out family-separated evaluation, valid cause-specific oracle and publication differentiation remain open. PRE-P07 stays CONDITIONAL GO; Prompt 07 remains unfrozen. Do not recruit a second reviewer for strictly mechanically verified outcomes. Continue analysis here; use the GitHub evidence and running log as the handoff to any other chat.

Integrity: all 36 manifest file hashes match; archive SHA-256 `400db99fea9069d9acc87f85981aa1afdb70b54c67a3dcb69e3df28b00dc18fc`. Original archive is preserved unchanged on GitHub with readable key extracts. This assistant inspected outputs locally; the actual GPU execution was performed in the user’s Colab runtime.

## Entry 007 — post-smoke tool-exposure audit and development pilot

## 2026-10-29 post-smoke audit and next development pilot

See [development audit and executable pilot](development_pilot/README.md). The offline auditor checked 14 observed turn slots. `cp` was exposed despite excluded_function metadata; missing `mv` was introduced through a later user message without expansion of the tool block; tail.lines is optional/default 10. These observations rule out a simple required-parameter validator as unrestricted cause ground truth.

Prepared an unexecuted development comparison on families 2 and 3 (six records per condition): vanilla, generic instruction control and schema-evidence checklist. One server is reused across all three conditions; official scoring and raw traces are preserved. Both instruction policies are prompt variants, not native official leaderboard baselines; neither is calibrated. Prompt length/order effects and semantic intent remain limitations.

Local tests passed for wrapper preservation, 14-turn audit findings, real subprocess/archive handling and mocked three-condition control flow. Actual 18-record GPU pilot remains pending. Keep family 1 and the new development families out of future unseen-test claims. PRE-P07 stays CONDITIONAL GO; Prompt 07 is not frozen.

## Entry 008 — development generic-control context overflow and resume repair

## Context recovery update — 2026-10-29

The first development attempt (`20261029T115448Z-6d9a8339`) completed vanilla and then failed during generic-control postflight. `multi_turn_miss_param_2` requested 8302 prompt + 4096 answer = 12398 tokens, 110 over the server cap of 12288. Source: `incident_20261029_context_overflow.md`. This is another serving-budget failure, not a CUDA OOM or model task-accuracy result. Schema-evidence had not started in the supplied log.

The official handler used native context 262144 when computing its 4096-token answer allowance. Initial prompt preflight could not prevent later conversation growth. The fix now sets the handler's effective context to the same server cap and rejects a request if prompt + 4096 + 2 safety tokens cannot fit. It preserves full answer allowance and history: no silent reduction, truncation, retry-until-success, or relabeling.

Current main/recovery cap is **24576**, with the same 85% GPU budget, eager execution, one sequence/request, chunked prefill 2048 and CPU swap/offload zero. The earlier T4 profiler reported 2078 GPU blocks (block size 16), about 33248 cache tokens; this supports trying 24K without changing weights or increasing the budget. It is an estimate from the earlier run, not a guarantee about new memory availability. New startup profiles and validates fit.

### Recover existing work
Use `P06_BFCL_Development_Pilot_Recovery_Colab.ipynb` in the **same existing runtime**. Its source run defaults to the exact failed path above. No dependency reinstall or cache deletion is performed.

The recovery creates a new run, validates the original policy script hash, copies only non-exception model records, and uses BFCL's normal skip-existing behavior (no --allow-overwrite). This should avoid redoing completed vanilla and valid generic records. Actual counts come from files; do not infer them solely from console progress. Genuine model task failures with valid outputs remain reusable. The original run and diagnostic ZIP remain intact; a copy of the original ZIP is included in the new export.

Record provenance names the source files and hashes for reused results. Mixed-attempt outputs and changed capacity are development evidence, not a single uniform-run/latency comparison. If memory/prompt/history exceeds the new cap, preserve a labeled infrastructure failure. Formal held-out comparisons still require one fixed verified serving policy.

Local validation: previous ten pilot check groups pass; added tests verify the 24K full-answer context guard, oversize rejection, and a synthetic recovery retaining 11 valid records while excluding one exception without modifying original files. Those counts are fixture checks, not measurements of the user's files. GPU recovery and comparison scores remain pending.

## Entry 009 — Colab session-limit popup when opening recovery tab
User screenshot shows 'Too many sessions' in the newly opened recovery notebook. Do not terminate the original runtime containing the interrupted run solely to open a new notebook session. Recovery code can execute inside the original active notebook kernel via a code cell that downloads the pinned recovery notebook at fd63f01516a6f5bd2884059bc70497ef313f9fd8 and executes its code cells sequentially. This changes neither the recovery logic nor the original source-run path. The pinned notebook was re-fetched and verified to have seven cells. The launcher is a user-executed option; no live Colab session operation has been performed by the assistant. If the source runtime/files are gone, stop and restore from the diagnostic ZIP rather than rerunning missing-data assumptions.

## Entry 010 — recovery pilot completed; negative task outcome

## 2026-10-29 development recovery results — 20261029T122816Z-5e29a2e6

[Verified result and full archive](runs/20261029T122816Z-5e29a2e6/README.md): generation and official scoring completed for all three conditions, six records each. Task successes: vanilla **0/6**, generic control **0/6**, checklist **0/6**. Two indexed families only; no complete-task improvement is demonstrated.

All 203 outer and 62 nested source-manifest hashes match. All 11 reused records match original records field-for-field; seven new records completed. Intended prompt instructions were checked in saved model-facing inputs. The 24K resource profile worked without new recorded inference exceptions. One generic-control tool-loop force termination is a model/harness outcome and remains in the results.

Do not treat this mixed-attempt development pilot as uniform-run latency/held-out performance. State/execution failures dominate and confound attribution to uncertainty causes. Pause further GPU runs; next recommendation is synthetic CPU reference-trajectory replay, followed by a narrower failure/measurement audit. That control remains unexecuted. NO-GO for scaling/claiming the present checklist as an improvement; CONDITIONAL GO for diagnostic validity work. Prompt 07 is unfrozen.
