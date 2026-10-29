# PRE-P07 — Evaluation oracle specification (provisional)

## Purpose and boundary
Two deliberately separate levels:

1. **Official reference-aligned action oracle (supported):** for each turn, `REFERENCE_CALL` if the official expected call list is nonempty and `REFERENCE_NO_CALL` otherwise. This is not the complete BFCL scorer; full reference evaluation additionally executes calls and checks side-effect state and responses.
2. **Cause-of-noncall diagnostic (NOT yet verified):** candidate `CAPABILITY_UNAVAILABLE` versus `SPECIFICATION_MISSING` only when an explicit documented evidence record supports the cause. Otherwise `UNRESOLVED`. Do not rebrand source record type as gold per-turn labels.

## Proposed schema-evidence input (design only)
Fields: `upstream_commit`, `category`, `case_id`, `turn_index`, `history`, `initial_config`, `active_function_signatures`, `reference_calls`, `missed_function` (if present), `explicit_required_arguments`, `present_slots`, `recoverable_from_state`, and `evidence_paths`. Keep `reference_calls` and gold-only information out of *model prediction inputs* to prevent leakage.

### Rule checks
- Reject malformed turn/reference shape, duplicate IDs, unavailable field/type violations.
- Verify function exists in **current** available inventory; determine arguments from actual executable signatures, not guessed schema.
- For a documented required argument, distinguish absent from missing-but-recoverable using explicit available conversation/state evidence.
- For missing function, prove intended operation against a permitted function inventory; do not infer a universal negative from a terse description.
- When semantic evidence is insufficient, emit `UNRESOLVED` rather than force a three-class label.
- Preserve the original BFCL call/no-call reference independently of proposed cause metadata.

### Unit test evidence (executed locally 2026-10-29)
Artifact: `bfcl_oracle_checks.py`. A structural helper `reference_action(calls)` validates list-of-string form and maps empty/nonempty expected calls to `REFERENCE_NO_CALL`/`REFERENCE_CALL`. `validate_record_pair` checks turn lengths. Ran locally: `python bfcl_oracle_checks.py`; printed `5 structural oracle checks passed; no BFCL model execution or semantic label validation`. These are **synthetic structural fixtures**, NOT a test of real BFCL execution results, model predictions or semantic annotation accuracy.

### Required next validation
Use pinned authentic BFCL records to check exact schema conventions, turn indexing, category-specific active tool exposure and prior-state semantics, then run official evaluator on compatible recorded predictions. Construct cause labels only for rule-proven cases and measure oracle coverage / unresolved cases. Prevent derivation of predictions from answer labels. Test pair perturbations with one intended change plus identical executable context where feasible.

**Status:** structural unit tests passed. Full evaluation oracle, three-way labels and official BFCL scoring remain **UNKNOWN / not executed**.
