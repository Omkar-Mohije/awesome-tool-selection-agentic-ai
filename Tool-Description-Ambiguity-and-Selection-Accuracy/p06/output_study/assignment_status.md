# Assignment requirements audit — 29 October 2026

## Sources checked

The original 11-page *AI Tools for Research post mid sem assignment* instruction sheet was read in full. It specifies 18 prompts, six phases, minimum evidence, and final deliverables A–E. The 28 October Classroom announcement was also read: Phase III (AI coding, vibe coding and baseline validation) must be completed by 30 October; all phases and the implementation paper are due before the end-semester examination. The announcement does not specify an exact cutoff time or a new submission location.

The instruction sheet explicitly accepts carefully analyzed negative results and distinguishes course research quality from publication novelty. The user's approved output-based scope is compatible with that principle. It does not waive experiment-design or provenance requirements.

## Current status versus required work

| Requirement | Evidence already available | Remaining work |
|---|---|---|
| P01–P05: review-to-question | Earlier reports and decision history; revised output-study question | Consolidate a current one-page brief and an explicit source-to-question bridge |
| P06: dataset and comparators | Pinned BFCL data/code, three pilot conditions, working environment and real resource evidence | Consolidate current validation sheet and license/access records; qualify limitations of prompt comparators |
| P07: blueprint frozen before results | Pre-pilot condition design and notebooks; extensive dated decisions | No completed P07 freeze is established. Write a prospective protocol, architecture diagram, metrics, sample, budget and checklist. Existing inspected results are development data, not pre-frozen held-out evidence. A fresh post-freeze evaluation is the clearest way to satisfy the timing requirement; never backdate the protocol |
| P08: environment verification | Genuine Colab setup, diagnostics, dependency versions, traces and successful model serving | Organize these outputs into the named environment report; distinguish local CPU tests from Colab tests |
| P09: baseline implementation and understanding | Official BFCL model handler, executable notebooks, preserved raw outputs | Map code modules, inputs/outputs, tests and genuine prompt-to-code history; student must understand them |
| P10: baseline validation report | Official task scores, reference controls, dispatch audit, published scorer replay | Assemble a single VERIFIED / UNCERTAIN / NEEDS CORRECTION validation report, including deviations and discrepancies |
| P11: evidence-based debugging | Real dependency, context-budget and session issues; corrected code and authentic logs | Consolidate fixes, verification, impact on prior records and human decisions without inventing dialogue |
| P12–P14: contribution, evaluation and interpretation | Approved scope, real result CSVs, failure analysis, study draft | Formal mapping to prompt outputs; reproducible figures and any new frozen comparison outputs; maintain post-hoc labels |
| P15–P16: paper and review | Markdown study draft | Full 6–10-page target manuscript, LaTeX, verified BibTeX, figures, compiled PDF, technical review and revision log |
| P17: reproducibility | Code, raw archives, source locks, scripts, GitHub history | Unified entry README/configs/commands and reproduction checklist; mark cold-download or other unexecuted paths TEST REQUIRED |
| P18: accountability | Decision log, debugging records, authentic conversation and commits | Concise prompt/code/verification and reflection report, with actual human decisions and limitations |
| Final demonstration | Working pipeline and saved results | Student preparation for a five-minute code/results walkthrough and short technical viva |

## Prompts and automation

The assignment says to use the 18 prompts in sequence, adapt them to actual evidence and retain useful outputs. The assistant may help adapt and execute the remaining scaffolds; the student need not manually retype every template. Authentic requests and outputs must be retained. Work already performed out of the numbered order must be documented honestly, not retroactively presented as a sequence that occurred before experiments.

Immediate priority is a requirements-aligned Phase II/III package, not additional literature novelty screening. Freeze the next evaluation before any new generation. Existing baseline/pilot outputs should be reused as development and validation evidence, not erased. A new independent evaluation can retain negative outcomes; passing examples are not a requirement.

## Correction to previous completion language

The output-study README is a substantive study draft, not a completed assignment submission. Saying that no further Colab run was needed was accurate for drafting that retrospective report, but did not establish full compliance with P07's prospective protocol requirement. Full submission readiness is not claimed.

## Submission preparation update — 29 October 2026
P07 has now been frozen prospectively in commit `2d72394d1e725f7a80236661f600d995dd705b39` for fresh families 89/73. The full [submission folder](../submission/README.md) contains the compiled paper, reports, exact observed dependencies, current notebook, analysis/tests and demonstration guide. The corresponding new GPU outputs, student personal reflection and actual demonstration remain pending; consult its current deliverable-status page rather than interpreting earlier checklist rows as unchanged.
