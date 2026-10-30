# P08 environment verification

## Observed in genuine Colab execution

Python 3.12 virtual environment `/content/bfcl-py312`; source `/content/gorilla/berkeley-function-call-leaderboard`. Verified versions: numpy 1.26.4, torch 2.6.0, vLLM 0.8.5, transformers 4.51.3, tokenizers 0.21.4, huggingface_hub 0.36.2, qwen-agent 0.0.34, soundfile 0.14.0. Full observed freeze is `requirements-colab-observed.txt` and original run logs. The notebook kernel can differ from the subprocess interpreter; all BFCL/vLLM calls use the venv explicitly.

Observed hardware: Tesla T4, 15360 MiB total GPU memory, approximately 12.67 GiB host RAM. Successful recovery cap 24576, memory fraction 0.85, one sequence/thread, FP16, eager V0, chunked prefill 2048, no swap/offload. Profiler: weights 7.61 GiB, activations 0.16 GiB, KV cache 4.57 GiB. Disk free space varies and is measured at runtime rather than assumed.

## New notebook verification boundary

`ATR_P07_Frozen_Evaluation_Colab.ipynb` derives its logger, archive, server lifecycle and scoring flow from the previously executed pilot. It pins source/core dependencies and model revision, verifies input/reference hashes, and runs CPU reference preflight before starting model weights. Warm path reuses the existing interpreter without upgrades. Cold path replays all observed pins and installs BFCL editable at the pinned local checkout; **this exact cold path is TEST REQUIRED**, not a new successful environment claim.

All new notebook cells and four embedded subprocess programs compile locally. Embedded runner equals the versioned runner. Historical subprocess/timeout/archive and mocked lifecycle checks pass; all six newly selected author references pass locally. New GPU generation remains TEST REQUIRED until genuine Colab output is supplied. The fresh code is reproducible in configuration and provenance; byte-identical stochastic output is not guaranteed.

Stop conditions: missing/wrong core dependency, `pip check` failure, no CUDA, mismatched inputs, over-budget initial prompt, failed reference execution, unexpected model endpoint, missing/duplicate results, saved inference exception, failed scoring. Preserve the output ZIP and logs; do not silently alter the environment or discard failed cases.
