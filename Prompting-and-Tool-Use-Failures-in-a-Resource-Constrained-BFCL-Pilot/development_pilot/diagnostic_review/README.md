# Diagnostic scope and novelty decision — 29 October 2026

## Decision reached at the planned gate
**NO-GO for claiming a novel BFCL call/no-call diagnostic or a demonstrated checklist improvement.** A course reproduction with a transparent negative pilot is feasible; that is a different contribution classification and is proposed for user review, not silently substituted for the original publication-oriented goal. Prompt 07 remains unfrozen. No additional GPU inference was run.

The current evidence is valuable implementation and measurement work, but the sample comprises two inspected development families, fixed condition order, unmatched prompt lengths, and mixed-attempt provenance. It cannot establish model population performance or an intervention effect.

## Primary literature checked
1. Patil et al. (ICML 2025), *The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models*: https://proceedings.mlr.press/v267/patil25a.html . Publisher abstract and official multi-turn documentation inspected. BFCL already addresses abstention and stateful multi-step interaction. Official documentation: https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html . Missing functions/parameters and error analysis are existing benchmark elements.
2. Ross et al. (NAACL 2025), *When2Call: When (not) to Call Tools*: https://aclanthology.org/2025.naacl-long.174/ . Author/publisher abstract inspected. Calling, asking follow-up questions, and acknowledging unavailable tools are existing evaluated decisions; a three-action framing alone is not novel.
3. Liu and Han (October 2026 preprint), *Asking Earns Nothing: Scoring the Decision to Act in BFCL Multi-Turn*: https://arxiv.org/abs/2610.04429 . Abstract obtained via scholarly search; full arXiv page/PDF access failed. **Author repository and scorer/data inspected directly**, pinned at `7f20cf1bdc37fc8d3954ef8488b80ef8bf8c9c02`: https://github.com/YangzeLiu/asking-earns-nothing . It releases paired decision scoring and distinguishes state-changing attempts from read-only exploration. This directly overlaps the proposed paired diagnostic; it is prior work to reproduce/extend, not our new method.
4. *RealControlBench* (October 2026 preprint), https://arxiv.org/abs/2610.27295 : abstract retrieved via scholarly search, full text unavailable in this session. It describes fine-grained agent tool-use control and capability preservation. No detailed experimental comparison is claimed from the abstract alone.

Searches included BFCL multi-turn missing-function/parameter evaluation, decision-to-act scoring, abstention/clarification benchmarks, and the exact discovered paper titles. This is a focused overlap check, not an exhaustive systematic literature review or proof that no future contribution exists.

## Correction: a checker exists but the runner does not invoke it
Our pinned official `eval_runner.py` imports `multi_turn_irrelevance_checker`, but `_evaluate_single_multi_turn_entry` only invokes `multi_turn_checker` and returns after that result. The execution checker skips state/response scoring on empty-reference turns. Therefore the mere existence and standalone success of the irrelevance checker **does not establish that the official multi-turn task score enforces no-call**.

This corrects any broader interpretation of the previous CPU control. Its results remain valid as separately invoked direct-checker tests. Existing 0/6 task scores are unchanged; they were caused by the recorded state/response/force-termination checks, not demonstrated enforcement of no-call turns.

### Executed dispatch control
`dispatch_control.json` records six author-reference trajectories accepted by the actual pinned evaluation function. In all four intervention cases, adding read-only `pwd()` at an empty-reference turn also passed that function, while the separately invoked irrelevance checker rejected it.

`dispatch_no_call_control.py` extracts the unchanged official evaluation function using AST, provides real original execution/state/response checks and a deliberate identity decoder for synthetic call lists. This isolates dispatch behavior without loading model dependencies. It is not a real production decoder or full-CLI test. Its source hash is locked in `source_lock.json`.

## Three distinct measurements
| Measurement | Rule | Current evidence |
|---|---|---|
| Official complete-task success | Pinned runner state/response/termination checks | 0/6 per condition |
| Strict no-call compliance | No decoded calls at an empty-reference turn | 0/11 available intervention records; one unavailable decoded record |
| Published decision score | State-changing attempt on complete anchor; no such attempt on incomplete twin; allows read-only exploration | Applied post hoc to 2 eligible pairs per condition |

None measures whether clarification prose is useful. None establishes SELECT/NO_VALID_TOOL/NEEDS_CLARIFICATION semantic labels for these trajectories. Read-only `cd`, `pwd`, `ls`, or `find` calls can fail the strict no-call measure while satisfying the published hold decision. Inherited mutator labels, including `cd` as read/navigation, belong to the published operational definition.

## Executed published-scorer application
The original published `score_pairs.py`, `pairs.json`, and `mutator_map.json` were downloaded and executed unchanged, with Apache-2.0 LICENSE and NOTICE fetched alongside them. No published code is represented as our own. Our reproduction wrapper downloads their pinned files, verifies SHA256, verifies the preserved pilot archive hash, and runs the original scorer separately for each prompting condition.

Only missing-parameter families 2 and 3 from the pilot belong to the scorer's default eligible population. Missing-function family 3 has a read-only reference anchor and is excluded by that definition; family 2 is absent from its verified pair manifest. Absence is not assigned an invented reason. The scorer's full 223-pair published population is not evaluated by our short pilot.

| Condition | Eligible pairs | Act on complete | Hold on incomplete | Decision mean | Both twins correct |
|---|---:|---:|---:|---:|---:|
| Vanilla | 2 | 50% | 50% | 50% | 0% |
| General review | 2 | 50% | 0% | 25% | 0% |
| Schema checklist | 2 | 100% | 50% | 75% | 50% |

**Do not describe 75% versus 50% as established improvement.** It is a post-hoc descriptive score on two previously inspected pairs, with all existing design confounds. No hypothesis test, confidence interval, broad benchmark claim or held-out result is justified.

The wrapper verified that both anchor turns exist in raw outputs and that deleting the missing twin's empty reference turn restores the complete reference trajectory. It also checked published parser function-name sequences against saved official decoded sequences wherever available. Generic-control family 3 is force-terminated with no saved official decoded sequence, but its raw anchor exists; this missing cross-check is reported. Argument-level parser equivalence is not established. The decision score counts attempts, including failed calls, rather than successful world changes.

## Automation and reproduction
Run from a repository checkout (replace ARCHIVE with the preserved recovery ZIP):

```bash
python Prompting-and-Tool-Use-Failures-in-a-Resource-Constrained-BFCL-Pilot/development_pilot/run_published_diagnostic.py --archive ARCHIVE --output published_diagnostic_results
```

No GPU, API key, or model call is used. The current run used verified locally fetched sources; cold-cache network downloading is implemented but not executed here. The output includes original scorer logs, per-pair CSVs, compatibility evidence, and a structured report.

The synthetic dispatch control can be rerun with the hash-locked BFCL source subset from the preceding CPU control and the pinned official `bfcl_eval/eval_checker/eval_runner.py`:

```bash
python Prompting-and-Tool-Use-Failures-in-a-Resource-Constrained-BFCL-Pilot/development_pilot/dispatch_no_call_control.py --source-root BFCL_SOURCE_ROOT --runner-source EVAL_RUNNER_PY --output dispatch_control.json
```

## Proposed next scope; not a frozen protocol
**Recommended for course delivery:** an explicitly attributed reproduction and resource-constrained negative prompt-intervention study, with the measurement distinction and reproducible controls as engineering evidence. Candidate title: *Reproducing Tool-Use Decision Metrics on a Resource-Constrained BFCL Pilot*. All experiments already completed can be reported honestly. A new independent evaluation, if desired, must use preselected uninspected families, the published eligibility/label definitions, a single fixed serving configuration, family-level accounting, and a bounded sample declared before generation. It would test a local intervention hypothesis, not establish a new benchmark or method.

**If original publication novelty remains essential:** do not freeze Prompt 07 or spend GPU time expanding this checklist. A distinct research question and compatible measurement must be established first; it cannot be guaranteed tonight. Changing model size or using a T4 alone is not sufficient novelty.

The user should choose the contribution goal before we change the project scope. This gate follows the existing plan's novelty check; it is not a deadline-driven shortcut.
