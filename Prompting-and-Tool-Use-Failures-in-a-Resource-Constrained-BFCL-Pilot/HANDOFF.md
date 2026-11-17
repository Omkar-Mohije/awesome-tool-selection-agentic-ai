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

The freeze-time `configs/protocol.json` still records `inference_status: NOT RUN`; preserve it as the protocol snapshot rather than silently rewriting the frozen record. The compiled paper remains the development-only version.

## Remaining work after archive validation

1. Incorporate the prospective table and qualified interpretation into `paper/main.tex`, keeping the development pilot separate.
2. Regenerate prospective figures from the verified case-level data, compile and visually inspect the revised paper. The current assistant workspace lacks Matplotlib, so its analyzer export used `--no-plots`.
3. Update the remaining activity/validation records and submission bundle. Exact cold dependency replay and a second-student rerun remain unverified.
4. Keep the run unchanged; any prompt, case, or metric change after viewing results requires a dated amendment and separate reporting.
## Still human-dependent

The student must review the code walkthrough, review the completed authentic reflection paragraphs in [`reports/P18_AI_use_and_reflection.md`](reports/P18_AI_use_and_reflection.md), rehearse the five-minute demonstration and submit to Classroom. No personal understanding or independent human annotation is certified by these documents. Latest verified announcement: Phase III through P11 by 30 October 2026; all phases and implementation paper before end-sem. Exact cutoff/submission location should be checked in Classroom.

## Package state

Six-page IEEE-style paper PDF ([`paper/main.pdf`](paper/main.pdf)) and LaTeX/BibTeX/figures compile. Reports map P05–P18 in [`reports/`](reports/), and prior P01–P06 prompts and decisions are organized in [`assignment_prompts/`](assignment_prompts/). Exact scope/status is in [`README.md`](README.md) and [`DELIVERABLE_STATUS.md`](DELIVERABLE_STATUS.md). Source repositories and licenses are credited. Continue from these files with any assistant; a particular chatbot subscription is not required to run the scripts or edit the LaTeX.
