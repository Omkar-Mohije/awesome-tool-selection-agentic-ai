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

## 2026-10-29 execution update — supersedes earlier pending-run status

The first real GPU smoke run completed generation and official partial scoring on a Tesla T4. All three selected records are present without recorded inference exceptions. Official task successes: **0/3**. This confirms execution feasibility for one family, not task correctness or representative performance.

See [complete evidence and diagnosis](runs/20261029T113521Z-d72a657e/README.md). The original archive is preserved unchanged with all 36 manifest hashes verified.

Use the current notebook's 12K single-request resource profile, zero CPU swap/offload and 2048-token chunked prefill; the earlier 8192-token cap caused late-turn context errors. Record actual versions from the successful run's pip freeze before expanding experiments. No need to rerun this same case merely to obtain passing scores.

A second comparator, proposed intervention, family-separated evaluation and cause-label validity checks remain outstanding. PRE-P07 remains CONDITIONAL GO; Prompt 07 is unfrozen.

## 2026-10-29 CPU control completed

[Executed CPU reference control and trace audit](development_pilot/reference_control/README.md): six reference cases pass both decoded layouts (12 positive checks), all six empty-action and four no-call-violation negative controls are rejected; no reference execution exceptions. This ran locally, not in Colab, and tests direct official execution/irrelevance checkers, not model decoding or server behavior. Hash-locked automated reproduction is included.

Post-hoc pilot audit: 0/11 available decoded intervention records satisfy the reference no-call requirement; one force-terminated record has no usable decoded output. The overall three 0/6 task scores remain unchanged. No fresh GPU run was used. Prompt 07 remains unfrozen pending contribution/measurement review.
