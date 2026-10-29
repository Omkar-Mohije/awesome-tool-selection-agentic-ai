# Portable continuation handoff

Current user-approved goal: finish an output-based ATR course study; publication novelty is optional. Do not restart the research from scratch or discard negative results.

## Established evidence

- BFCL source `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, Qwen3-4B official handler, T4/12.7 GiB host.
- Smoke family 1: 0/3 tasks; comparative development families 2/3: original, general review and checklist each 0/6. Recovery preserves 11 unchanged records and seven newly generated records; original full ZIPs remain available.
- First development failures: 13 state mismatch, four response mismatch, one force termination. Strict no-call 0/11 available decoded records, one unavailable. These are not three-way semantic labels.
- Published Liu/Han scorer gives 50%, 25%, 75% on only two eligible development pairs; post-hoc, not established improvement. Original code/labels/certification attributed and locked.
- Direct checker and dispatch controls distinguish state/response checks from strict no-call. Pinned multi-turn runner does not invoke its imported standalone irrelevance checker. Synthetic controls are not model predictions.

## Latest prospective experiment

Protocol freeze commit `2d72394d1e725f7a80236661f600d995dd705b39`, ID ATR-P07-v1. Families 89/73, each base/miss_func/miss_param, exact three policies, 18 records. Source/input/reference/model revision pinned. Development excluded. Both new families are vehicle-control cases; no broad domain claim.

The user received a one-cell loader for the pinned notebook to execute in the existing Colab kernel. Await `ATR_Frozen_Evaluation_Outputs.zip`. No genuine new GPU outcome has yet been supplied. Do not invent one or report this experiment as completed. The notebook was syntax/lifecycle checked locally; cold install remains TEST REQUIRED. Never tune prompts or substitute cases after outputs without a dated amendment.

## On receiving the archive

1. Verify every manifest hash, selected IDs, original protocol, source/revision, all generation/evaluation statuses and inference exceptions. Confirm no old-case reuse and no missing/duplicate task records. Separate infrastructure errors from force-terminated tasks.
2. Run `scripts/analyze_run.py` into a new prospective output folder. Run the attributed `scripts/score_decisions.py`; review eligibility, raw anchor presence and reference/parser compatibility before interpretation. Keep family dependence and all denominators explicit.
3. Add prospective results as a separate section/table in `paper/main.tex`; retain development history. Regenerate figures from actual CSVs, compile and render/inspect the paper. Update pending labels without implying that pilot design was frozen before it occurred.
4. Update validation, AI-use and decision logs with actual activity, then rebuild the submission bundle and sync GitHub. No positive result is required.

## Still human-dependent

The student must review the code walkthrough, write/confirm the three authentic reflection paragraphs, rehearse the five-minute demonstration and submit to Classroom. No personal understanding or independent human annotation is certified by these documents. Latest verified announcement: Phase III through P11 by 30 October 2026; all phases and implementation paper before end-sem. Exact cutoff/submission location should be checked in Classroom.

## Package state

Six-page IEEE-style paper PDF and LaTeX/BibTeX/figures compile. Reports map P05–P18, and prior P01–P04 PDFs are included where downloaded. Exact scope/status is in `README.md` and `DELIVERABLE_STATUS.md`. Source repositories and licenses are credited. Continue from these files with any assistant; a particular chatbot subscription is not required to run the scripts or edit the LaTeX.
