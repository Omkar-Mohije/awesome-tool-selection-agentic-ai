# Portable continuation handoff

Current user-approved goal: finish an output-based ATR course study; publication novelty is optional. Do not restart the research from scratch or discard negative results.

## Established evidence

- BFCL source `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, Qwen3-4B official handler, T4/12.7 GiB host.
- Smoke family 1: 0/3 tasks; comparative development families 2/3: original, general review and checklist each 0/6. Recovery preserves 11 unchanged records and seven newly generated records; original full ZIPs remain available.
- First development failures: 13 state mismatch, four response mismatch, one force termination. Strict no-call 0/11 available decoded records, one unavailable. These are not three-way semantic labels.
- Published Liu/Han scorer gives 50%, 25%, 75% on only two eligible development pairs; post-hoc, not established improvement. Original code/labels/certification attributed and locked.
- Direct checker and dispatch controls distinguish state/response checks from strict no-call. Pinned multi-turn runner does not invoke its imported standalone irrelevance checker. Synthetic controls are not model predictions.

## Latest prospective experiment

Protocol ATR-P07-v1 was frozen before these model outputs. Families 89 and 73, their base/miss_func/miss_param variants, and all three exact prompt conditions were used; development cases were excluded. Both selected families are vehicle-control cases, so the domain limitation remains.

The user supplied `ATR_Frozen_Evaluation_Outputs.zip`. Run `20261117T100033Z-29245346` completed all 18 condition/task records. The archive analyzer verified all 202 manifest file hashes, selected IDs, complete generation/evaluation statuses, and no inference exceptions. The archived input/reference hash check and six reference preflight checks pass. The dated [P07 run analysis](reports/P07_run_analysis_20261117.md) records the archive SHA-256 and full results.

Primary complete-task outcomes: vanilla 0/6, generic control 1/6, schema evidence 0/6. The schema-evidence-minus-generic-control contrast is −1/6 (−16.7 percentage points). All 17 first failures are instance-state mismatches. The pinned published scorer ran on four eligible pairs per condition with every anchor available; act, hold, credited hold, decision, and pair-correct scores are identical across conditions. Strict no-call is 1/4 per condition. These remain descriptive sample results, not broad or causal claims.

The freeze-time `configs/protocol.json` still records `inference_status: NOT RUN`; it is preserved unchanged as the protocol snapshot. The user-supplied frozen ZIP is stored in `runs/20261117T100033Z-29245346/ATR_Frozen_Evaluation_Outputs.zip` and hash-verified.

## Paper status after prospective incorporation

1. Prospective tables, trace analysis, and qualified sample interpretations are incorporated into `paper/main.tex`, keeping the development pilot separate.
2. Separate prospective figures (`prospective_task_outcomes.pdf`/`.png` and `prospective_failure_types.pdf`/`.png`) are generated in `paper/figures/` and `results/prospective/ATR-P07-v1-20261117/`.
3. Local LaTeX compilation of `paper/main.pdf` is blocked by the absence of `pdflatex` in the Windows host environment; compile on Overleaf or Colab and inspect visually before submission.
4. Exact cold dependency replay and a second-student rerun remain unverified. Keep the run unchanged.
## Still human-dependent

The student must review the code walkthrough, review the completed authentic reflection paragraphs in [`reports/P18_AI_use_and_reflection.md`](reports/P18_AI_use_and_reflection.md), rehearse the five-minute demonstration and submit to Classroom. No personal understanding or independent human annotation is certified by these documents. Latest verified announcement: Phase III through P11 by 30 October 2026; all phases and implementation paper before end-sem. Exact cutoff/submission location should be checked in Classroom.

## Package state

The checked-in six-page PDF ([`paper/main.pdf`](paper/main.pdf)) remains the development version. The LaTeX source includes the prospective results, and separate prospective figures have been regenerated with valid PDF cross-reference offsets and labeled PNGs. The revised source has not yet been compiled or visually inspected as a complete paper; compile it on Overleaf or a host with pdflatex before submission. Reports map P05–P18 in [`reports/`](reports/), and prior P01–P06 prompts and decisions are organized in [`assignment_prompts/`](assignment_prompts/). Exact scope/status is in [`README.md`](README.md) and [`DELIVERABLE_STATUS.md`](DELIVERABLE_STATUS.md). Source repositories and licenses are credited. Continue from these files with any assistant; a particular chatbot subscription is not required to run the scripts or edit the LaTeX.
