# P06 baseline smoke test — execution runbook (2026-10-29)

## Status
**Notebook CREATED, NOT EXECUTED.** No inference results, GPU compatibility, or official score claimed. Proposed model is an **explicitly supported** FC model in pinned official BFCL `SUPPORTED_MODELS.md`: `Qwen/Qwen3-4B-Instruct-2507-FC` (Hugging Face checkpoint model name without BFCL suffix: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507). Source and license should be checked when running; Qwen model card uses Apache 2.0.

## What was delivered
`P06_BFCL_V4_Smoke_Colab.ipynb` clones official https://github.com/ShishirPatil/gorilla and checks out `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, installs `.[oss_eval_vllm]`, selects **one family** from each of `multi_turn_base`, `multi_turn_miss_func`, `multi_turn_miss_param`, runs official `bfcl generate --run-ids`, then `bfcl evaluate --partial-eval`, exports results/score logs in a zip. Official CLI commands taken from the pinned `berkeley-function-call-leaderboard/README.md`; model is taken from pinned `SUPPORTED_MODELS.md`.

## Why a smoke test first
BFCL's multi-turn runner launches a local tool-calling server and executes code-backed trajectories. 4B model may require quantization or a stronger GPU than free Colab. The installed package and runtime dependencies may conflict on changing Colab images. Stop on an actual failure and save error logs; do not silently substitute a different model/parsing mode and call it comparable.

## Source-verifiable finding already obtained
In every one of 200 indexed families, each miss_func and miss_param variant adds **exactly one** official reference no-call turn relative to base. This is a paired *count*, not a correct cause-classification label. The main evaluation must score official tool execution, not just category predictions.

## After smoke test
- Preserve exact GPU details, model checkpoint version, package versions and actual score files. Do not commit confidential environment logs or Hugging Face tokens.
- Only if successful: expand a **dev partition by family**, implement paired prediction error analysis and a development-calibrated no-call decision; hold out whole families for test. Reject any approach that uses official answers or withheld functions at inference time.
- A no-call threshold requires real accessible scores from model output; if scores do not exist, do not invent calibrated confidence.
- Don't claim the alternative policy has been benchmarked before the same model's native call outputs and a comparable validation run exist.
- Research question remains tentative and novelty unproven.

## Human involvement
Only enabling a Colab GPU, executing the notebook and sharing run logs are beyond this GitHub connector's compute capabilities. File updates and downstream analysis can be handled here after results exist.
