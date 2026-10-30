# Prompting and Tool-Use Failures in a Resource-Constrained BFCL Pilot

**Course-study scope approved by the user on 29 October 2026.** Publication novelty is no longer a completion requirement. This is an output-based empirical pilot and attributed metric reproduction. Negative and inconclusive outcomes are retained.

## Research question

What differences are observed in complete-task success, tool-use decisions, and execution failures when a small tool-calling model uses its original prompt, a general review instruction, or a schema-evidence checklist on selected BFCL multi-turn tasks?

This question supports descriptive comparison on the recorded cases. It does not imply that the pilot estimates a causal prompt effect, population accuracy, or a new state-of-the-art method. The earlier retrieval-stage three-class question is historical background; the present experiment concerns executable multi-turn tool calling.

## Method and completed work

The model registry is `Qwen/Qwen3-4B-Instruct-2507-FC`, served through the pinned official Qwen handler and vLLM. The Gorilla source commit is `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`. An initial family-1 smoke run verified generation, output preservation, and official scoring. Its three tasks all failed, and its traces informed prompt design. It is development evidence, not an unseen evaluation.

The comparative development pilot used indexed families 2 and 3 in three variants: base, missing function, and missing parameter. Each condition therefore has six task records, giving 18 condition/task records. These records share two underlying families and are not 18 independent samples.

The conditions are:

1. **Vanilla:** the original formatter and prompt.
2. **General review:** a task-review instruction, including an explanation that tools introduced later become available.
3. **Schema evidence:** a checklist covering requested operation, documented capabilities, required arguments, conversation state, unsupported substitutions, and evidence for completion; it shares the later-tool explanation.

The exact policy text is preserved in [the runner](../development_pilot/p06_policy_runner.py). Policies do not receive references or future turns. Instructions were checked in saved model-facing prompts. Conditions have unmatched prompt lengths and fixed execution order; the extra tool-introduction explanation is absent from vanilla. These are explicit comparison limitations.

## Resource use and recovery

Generation ran in the user's Colab environment on a 15 GiB Tesla T4 with approximately 12.7 GiB host RAM. A Python 3.12 virtual environment resolved dependency compatibility. The working serving profile used FP16, 85% GPU memory utilization, one request at a time, eager execution, 2048-token chunked prefill, and no CPU swap/offload.

The initial 12,288-token context cap failed on a request requiring 8,302 input tokens plus a 4,096-token output allowance. Recovery used a 24,576-token cap and an explicit guard that preserves the answer allowance and rejects oversize requests without truncating history. Eleven valid original records were reused unchanged; seven records were generated during recovery. This mixed provenance prevents treating the pilot as a uniform-run latency or seed-stream experiment.

The successful recovery server profiler reported 7.61 GiB model weights, 0.16 GiB activation peak, and 4.57 GiB KV cache. These are profiler allocations, not continuous system-wide peak measurements. The largest observed input was 9,161 tokens, within the recovered cap with the output allowance.

## Results

| Prompt condition | Official complete-task successes | Complete-task accuracy |
|---|---:|---:|
| Vanilla | 0/6 | 0% |
| General review | 0/6 | 0% |
| Schema evidence | 0/6 | 0% |

The pilot shows no complete-task gain from either added instruction on these six tasks. It does not establish that such prompting never helps. The first reported failures across the 18 records were 13 state mismatches, four execution-response mismatches, and one force termination. The force-terminated general-review record remains a task failure; it is not silently removed as a serving error.

Concrete failures include navigating to `document` when the configured directory is `documents`, failing to create a requested file, and attempting copies from the wrong working directory. These ordinary action/state errors coexist with intervention-turn behavior and limit interpretation of task-level zeros as evidence about uncertainty handling alone.

All 203 recovery-manifest and 62 nested source-manifest hashes matched. All 11 reused records matched their original records field-for-field. The complete records, scores, logs, and provenance are preserved in the [recovery run](../runs/20261029T122816Z-5e29a2e6/README.md).

## Why the metric definition matters

Three measures answer different questions:

| Measure | What it asks | Observed result |
|---|---|---|
| Official complete-task success | Did the recorded trajectory satisfy pinned execution/state/response checks? | 0/6 per condition |
| Strict no-call compliance | Were there no decoded calls on an empty-reference turn? | 0/11 available intervention records; one record lacks decoded evidence |
| Published act/hold score | Was a state-changing call attempted when information was complete, and withheld when incomplete? | Descriptive results below |

The pinned official multi-turn runner does not invoke its imported standalone irrelevance checker. The strict no-call audit is therefore a separate measurement, not an explanation of how the official task zeros were assigned. Read-only exploration can fail strict no-call compliance while satisfying an act/hold definition that allows exploration. None of these measures assesses the usefulness of clarification prose.

For an attributed secondary analysis, we executed the original decision scorer released by Liu and Han in *Asking Earns Nothing* (2026), repository commit `7f20cf1bdc37fc8d3954ef8488b80ef8bf8c9c02`. Only two missing-parameter pairs from this pilot qualify under its default eligibility definition.

| Condition | Eligible pairs | Act on complete | Hold on incomplete | Decision mean |
|---|---:|---:|---:|---:|
| Vanilla | 2 | 50% | 50% | 50% |
| General review | 2 | 50% | 0% | 25% |
| Schema evidence | 2 | 100% | 50% | 75% |

The decision mean averages the complete-side act rate and incomplete-side hold rate. These are post-hoc observations on two inspected pairs. The numerical checklist advantage is not an established improvement. The published metric counts attempted actions, including failed attempts, rather than successful execution. Eligibility, reference alignment, parser checks, and the missing decoded cross-check for the force-terminated record are documented in the [diagnostic review](../development_pilot/diagnostic_review/README.md).

## Evaluator controls

CPU controls supplied author reference actions deliberately; they were not model predictions. All six cases passed original state/response execution checks under both decoded step layouts, with no reference execution exceptions. Six empty-action negative controls and four injected-call controls were rejected by the relevant separately invoked checkers.

A further control isolated the original evaluation dispatch function using an identity decoder and real execution checker. It accepted six references and also accepted four trajectories containing an added read-only `pwd()` on empty-reference turns. The standalone irrelevance checker rejected those four additions. This confirms the integration distinction for the pinned code. It does not validate production decoding or full CLI execution locally.

## Interpretation and limits

The defensible finding is that the three prompting conditions did not complete any of the selected six tasks, while different decision metrics expose different behavior within those failures. Additional instructions were applied, but basic filesystem-state reasoning and inappropriate intervention-turn actions persisted.

The study has one model, two comparative development families, no held-out evaluation, fixed condition order, unequal prompt lengths, mixed recovery provenance, and a post-hoc secondary metric. There is no trained/calibrated abstention comparator or independently validated three-way semantic oracle. No statistical significance, generalization, or novelty claim follows from these data. Reference controls establish specific software behavior, not the correctness of every benchmark item or every part of the generation pipeline.

## Future experiments

The research question remains open for extension. Preserve families 1–3 as inspected development data. Select and record fresh family groups before any new generation, verify eligibility and state/reference alignment, use one fixed serving profile, and report complete-task and decision metrics separately. Compare matched instructions, distinguish exploratory from state-changing calls, and retain failures and incomplete trajectories. A later experiment can test whether a revised prompt or decision policy improves held-out behavior; this pilot must not be relabeled as held-out evidence after tuning.

More models, repeated runs, broader domains, and useful-clarification assessment can be added when resources permit. Each extension should address a specific limitation rather than merely enlarge the same pilot. Publication is optional and would require a separate assessment of contribution and evidence.

## Attribution and artifact map

- BFCL: Patil et al. (ICML 2025), https://proceedings.mlr.press/v267/patil25a.html ; official code/data: https://github.com/ShishirPatil/gorilla .
- When2Call: Ross et al. (NAACL 2025), https://aclanthology.org/2025.naacl-long.174/ . Call/clarify/unavailable-tool decisions are existing research topics.
- Published decision metric: Liu and Han (2026), https://github.com/YangzeLiu/asking-earns-nothing ; https://arxiv.org/abs/2610.04429 . Its code, labels, and certification are attributed, not claimed as original work here.
- [Authentic smoke outputs](../runs/20261029T113521Z-d72a657e/README.md), [comparative recovery outputs](../runs/20261029T122816Z-5e29a2e6/README.md), [reference-control automation](../development_pilot/reference_control/README.md), and [diagnostic replay automation](../development_pilot/diagnostic_review/README.md).

AI assistance supported source inspection, code preparation, debugging, trace analysis, and drafting. Model inference ran in user-operated Colab; CPU controls and offline analysis ran in the assistant workspace. Human annotation, new model training, and additional GPU experiments are not claimed.
