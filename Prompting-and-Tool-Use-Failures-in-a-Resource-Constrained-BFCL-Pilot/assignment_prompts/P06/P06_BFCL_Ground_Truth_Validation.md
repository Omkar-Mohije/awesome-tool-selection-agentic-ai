# PRE-P07 — BFCL V4 ground-truth validation (2026-10-29)

**Status:** VERIFIED structural and official evaluator behavior; **UNKNOWN** three-way semantic labels. Source commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, repository `ShishirPatil/gorilla`. This is an inspection record, **not** a model result.

## Source files and Git blob SHA
All paths relative to `berkeley-function-call-leaderboard/bfcl_eval/`.

| Source | Blob SHA | Parsed entries |
|---|---|---:|
| `data/BFCL_v4_multi_turn_base.json` | `656fbd5e56969373353cd58b880234a6cc4edc99` | 200 |
| `data/BFCL_v4_multi_turn_miss_func.json` | `28e7987841719aec4e4f3f3f4b6c2f1915c831f3` | 200 |
| `data/BFCL_v4_multi_turn_miss_param.json` | `2e87caf87fb48f7807a18610311bdfa1138d0599` | 200 |
| `data/possible_answer/BFCL_v4_multi_turn_base.json` | `3ee85fcd5e8cccca24e2347e464b58fd1b9f02a1` | 200 |
| `data/possible_answer/BFCL_v4_multi_turn_miss_func.json` | `ec10a3566a613ddce8e05438425d40f6ec15fbfc` | 200 |
| `data/possible_answer/BFCL_v4_multi_turn_miss_param.json` | `94edb50ede0de76f35e937d4b96128857357d95b` | 200 |
| `eval_checker/multi_turn_eval/multi_turn_checker.py` | `34b36715cdfaa4464ba1be137af4d30e85da8efb` | Python source |
| `eval_checker/eval_runner.py` | `2d5c41aac41cd2f1caedf741fb01dfdfd57b1990` | Python source |
| `data/README.md` | `460ddf62835f5cc5c2ec86e254749ce86414e2c3` | Repository documentation |

## Actual JSONL-derived counts
| Category | Families | Question turn slots | Empty reference-call turns | Length mismatch between questions and reference trajectories |
|---|---:|---:|---:|---:|
| base | 200 | 734 | 3 | 0 |
| miss_func | 200 | 934 | 203 | 0 |
| miss_param | 200 | 934 | 203 | 0 |

Every source record is a multi-turn *family*, not one class label. Identical numeric suffixes across categories provide pairing identifiers. The 190 equal-initial-config families may be structurally comparable but still require state/turn alignment to justify a causal one-factor comparison. See pairing audit for the ten exceptions.

## Ground-truth semantics verified in implementation
Official possible-answer files contain `ground_truth: list[list[str]]`, one list of expected calls per turn. In `multi_turn_checker`, nonempty expected call lists must not receive an empty model call list; model and reference calls are executed from `initial_config`, compared through instance state and response checks. Empty expected lists skip the ordinary state/response comparison; `multi_turn_irrelevance_checker` rejects function calls for reference-empty turns. `eval_runner.py` decodes call outputs, and non-call/chat content is not scored for clarity or correctness of a clarifying question. The official score is therefore about tool-call execution/no-call behavior, **not** semantic correctness of the text reply.

At index 0, missing-function variant inserts a zero-message turn and carries `missed_function`; missing-parameter variant splits an underspecified final request into a follow-up. In the latter variant the reference has an empty-call turn followed by executable calls. **Inference:** some source situations are compatible with a clarification interpretation, but this is not an independently verified, per-turn `NEEDS_CLARIFICATION` label.

## Defensible labels
- **VERIFIED:** `REFERENCE_CALL` vs `REFERENCE_NO_CALL` directly from official `ground_truth` turn list; category membership; original execution reference.
- **INFERRED:** candidate *cause* of non-call from category and perturbation, only after checking available functions/parameters and previous turn context.
- **UNKNOWN:** a faithful three-way SELECT / NO_VALID_TOOL / NEEDS_CLARIFICATION label for every turn; equivalence of alternate valid trajectories; whether the model asks a useful question.
- **Not permitted:** label every missing-function turn NO_VALID_TOOL or every missing-parameter turn NEEDS_CLARIFICATION; count absence of calls as successful clarification.

## Important anomalies
The base reference has **3** empty-call turns at families 167 turn 4, 180 turn 3, and 180 turn 4 (0-indexed). Both missing categories have 203 empty-call turns; not all empty turns are necessarily caused by the intervention. This is why category-based wholesale relabeling is invalid.

## Data rights
`data/README.md` declares `license: apache-2.0`. Data origin, upstream dependencies, use rights of generated case extensions, and any model/checkpoint licenses require separate review before redistribution. Official scorer has **not** been executed on model output. No human or full semantic annotation is claimed.

**Verdict:** BFCL is a defensible anchor for tool-calling action/no-action evaluation. A richer three-class cause label is NOT yet a verified official outcome.
