# CPU reference control and pilot trace audit — 2026-10-29

## Executed result
Six synthetic reference cases (families 2 and 3; base, missing-function, missing-parameter) passed the pinned official decoded execution/state/response and irrelevance checkers in the local CPU Python 3.12 environment. Both batched-per-turn and one-call-per-step layouts passed: 12 positive layout checks. All 6 empty-action negative controls were rejected. All 4 injected-call controls on required no-call turns were rejected. Author reference actions executed without `Error during execution` responses.

**These are deliberately supplied author references, not model predictions or a 6/6 model result.** No GPU, model server, or model weights were used. This is not a replay inside the user's Colab environment and does not validate CLI dispatch, decoding, tool exposure, or clarification prose.

Code imports the original pinned official checker and tool implementation without modification. `source_lock.json` locks all 12 fetched upstream files by SHA256 to commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`. The runner rejects mismatched files before importing them. The source subset is enough for these cases only. No package dependency installation is needed.

## Automated reproduction
From a checkout, run:

```bash
python Tool-Description-Ambiguity-and-Selection-Accuracy/p06/development_pilot/run_reference_control.py --output reference_replay_results.json
```

This downloads only the hash-locked sources into a temporary cache, skips already verified downloads, runs all controls, and saves the detailed report. The current run exercised the verified-cache path; fresh network downloading was not executed locally. Original sources were retrieved via GitHub. Results and audit files alongside this README are already executed outputs, not placeholders.

## Independent execution-error check
During development, an initial control used a UUID that could start with a digit as the synthetic model name. BFCL interpolates this into a Python identifier, producing invalid-decimal execution errors. Reference-vs-reference equality alone still passed, but the explicit execution-error check rejected the run. The corrected runner always prefixes the synthetic name with `p06_reference_`. Only the corrected run is reported as successful. This incident supports retaining the separate execution-error check; it does not describe the user model's correctly prefixed registry name.

## Post-hoc model trace audit
`first_failure_audit.csv` reads the preserved pilot's official score records and decoded actions. It covers all 18 condition/case outcomes. All 11 intervention records with available decoded outputs contain calls on the reference-required no-call turn (0/11 no-call passes). One generic-control missing-parameter record was force-terminated and has no usable decoded output; it remains an overall task failure and is explicitly unavailable for this secondary measure. The six base records have no reference-required no-call turn. This is descriptive development evidence, not a separate held-out sample or proof of semantic intent.

The first reported task failure is after the reference-required no-call turn in all 11 decoded intervention records. Ordinary directory/file-state and response errors coexist with intervention violations. For example, vanilla base family 2 calls `cd(folder='document')` although the configured directory is `documents`, then lacks the expected created file. These are execution observations, not inferred uncertainty-cause labels. Saved response-prefix error counts are incomplete for response-mismatch/force-termination records that omit execution prefixes; a zero is not proof of an error-free trajectory.

The official task result remains vanilla 0/6, generic control 0/6, checklist 0/6. The reference control supports the core scorer's ability to accept valid trajectories; it does not establish every part of the Colab generation pipeline or research novelty.

## Decision
Complete the planned evaluator check and failure audit before more GPU work. They are now complete at the decoded-checker level. Do not repeat the same three prompting conditions or claim checklist improvement. Keep Prompt 07 unfrozen while deciding whether a narrow, independently measured diagnostic contribution is sufficient. No new model intervention or expanded run is authorized by a positive reference-control result alone.
