# ATR-P07-v1 archive analysis

**Run:** `20261117T100033Z-29245346`  
**Archive:** `ATR_Frozen_Evaluation_Outputs.zip`  
**Archive SHA-256:** `745e904d2ed702795ec979f68614aac6c012efea0b0dc3eb4b31e49855108eab`

## Validation performed

- Ran the repository's `scripts/analyze_run.py` against the uploaded archive with plotting disabled.
- All **202** manifest-listed file hashes matched.
- The three conditions contain the six protocol-selected case IDs each: 18 condition/task records total, with no duplicate, unexpected, or missing IDs.
- Generation and evaluation statuses passed for all three conditions. The result-integrity logs list no inference-error IDs.
- Selected families 73 and 89 and their base, missing-function, and missing-parameter variants match `configs/protocol.json`.
- The archived BFCL partial-run score files and the repository analyzer agree on complete-task counts.
- The ZIP's `verify_frozen_inputs.log` says frozen input/reference hashes match. The six reference preflight entries all pass.

## Primary result

| Condition | Successes / tasks | Accuracy | Failures |
|---|---:|---:|---:|
| Vanilla | 0/6 | 0% | 6 |
| Generic control | 1/6 | 16.7% | 5 |
| Schema evidence | 0/6 | 0% | 6 |

The one success is `multi_turn_miss_func_73` under generic control. The prespecified primary contrast, schema evidence minus generic control, is **−1/6 (−16.7 percentage points)**. This is a descriptive difference on two selected vehicle-control families, not an estimate of a population effect.

The 17 failed condition/task records all have first error type `multi_turn:instance_state_mismatch`. The official failure file identifies the first reported failure; it does not enumerate every incorrect action in a trajectory.

## Prespecified secondary measures

The pinned repository scorer ran using the exact source files whose SHA-256 hashes match `configs/published_scorer_lock.json`. It identifies four eligible pairs in the selected archive per condition. Every one of the 12 miss-side anchor turns is available in the raw outputs.

| Condition | Eligible pairs | Act | Strict hold | Hold credited* | Decision mean | Pair correct |
|---|---:|---:|---:|---:|---:|---:|
| Vanilla | 4 | 100% | 25% | 50% | 62.5% | 25% |
| Generic control | 4 | 100% | 25% | 50% | 62.5% | 25% |
| Schema evidence | 4 | 100% | 25% | 50% | 62.5% | 25% |

\*The credited hold measure allows the scorer's certified independent actions on one compound pair. These are attempted-action scores, not task success or evidence that clarification was useful.

A separate strict no-call count from the scorer's raw parsed anchor turns is **1/4 for each condition**; the same missing-parameter family-89 anchor has no parsed calls in all three conditions. The other three miss anchors contain calls. This is distinct from the published scorer's strict hold measure, which concerns state-changing attempts.

## Interpretation cautions and current status

- The per-category JSON score headers are the suitable source for this selected-case result. The adjacent `data_overall.csv` and `data_multi_turn.csv` files explicitly describe a **partial run** and include aggregate percentages that should not be substituted for the frozen 6-task denominator.
- `configs/protocol.json` still says `"inference_status": "NOT RUN"` because it is the immutable freeze-time protocol snapshot. Completed inference and evaluation are established separately by the uploaded run archive, its manifest, status files, and integrity checks; do not edit the snapshot to imply it was written after inference.
- The raw ZIP passed archive validation. All 202 manifest-listed file hashes match; all 18 condition/task records have successful generation/evaluation statuses and no inference-error IDs. The six selected reference preflight entries pass.
- The analyzer export was generated with plotting disabled because Matplotlib was unavailable. Separate prospective figures were generated afterward from the validated case-level outputs; the ZIP was not modified.
- The secondary scorer uses its published parser and inherited eligibility labels. This analysis did not independently establish semantic gold labels or prove parsed calls were useful clarification.
- The prospective result remains descriptive: two correlated vehicle-control families do not support a general population or causal prompt-effect claim.

## Reproduction

From the repository root, with the archive at the indicated path:

```bash
python scripts/analyze_run.py --archive "/path/to/ATR_Frozen_Evaluation_Outputs.zip" --output results/prospective/ATR-P07-v1-20261117
python scripts/score_decisions.py --archive "/path/to/ATR_Frozen_Evaluation_Outputs.zip" --output results/prospective/ATR-P07-v1-20261117/decision --cache results/prospective/ATR-P07-v1-20261117/scorer_cache
```

The initial analyzer run used `--no-plots` because Matplotlib is not installed in the current workspace. The later standalone figure generator produces new labeled prospective PDF/PNG files without changing the analyzer outputs.


