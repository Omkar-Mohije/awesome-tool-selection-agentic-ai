# P06 BFCL troubleshooting branch — running handoff log

Updated: 2026-10-29 (Asia/Kolkata)
Status: OPEN — soundfile blocker cleared on user rerun; vLLM tokenizer API mismatch observed; compatibility and serving-profile repairs prepared.

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

## Return-to-original-chat summary
Python 3.12 and soundfile repairs progressed to actual vLLM startup. The next observed failure is a tokenizer API mismatch: vLLM 0.8.5 reads all_special_tokens_extended, absent from the installed tokenizer.
Notebook now constrains Transformers to 4.51.3 and tests the real tokenizer through vLLM before generation. It also uses official external-server support to choose an older-GPU-compatible dtype and cap context/concurrency for the smoke test.
Run the updated notebook in the existing GPU runtime; packages already installed/downloaded may be reused. No fresh full runtime is required solely for these child-process dependency changes.
No successful baseline or official evaluation is evidenced. PRE-P07 remains CONDITIONAL GO; Prompt 07 has not been executed.
