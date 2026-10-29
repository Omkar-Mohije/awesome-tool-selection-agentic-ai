# Verified BFCL smoke run — 20261029T113521Z-d72a657e

Date: 2026-10-29. **Execution pipeline PASS; official task outcomes 0/3.**

## Evidence and provenance
- Complete original user-uploaded archive: [P06_BFCL_Smoke_Outputs.zip](P06_BFCL_Smoke_Outputs.zip).
- SHA-256: `400db99fea9069d9acc87f85981aa1afdb70b54c67a3dcb69e3df28b00dc18fc`; archive size 252913 bytes.
- All 36 manifest-listed files verified byte-for-byte against their recorded SHA-256 hashes. The original archive contains raw model predictions, detailed per-case scores, all logs, serving profile, selected IDs, environment freeze and status. Readable key extracts accompany it here.
- Official BFCL commit: `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`.
- Notebook preparation commit: `efe70d1fada25544d1ebc4761ee541d1bae2959c` matches the recorded 12K serving profile; the manifest does not itself prove which browser notebook copy was executed.
- Model registry ID: `Qwen/Qwen3-4B-Instruct-2507-FC`.
- Model checkpoint: `Qwen/Qwen3-4B-Instruct-2507`; resolved config revision recorded by preflight: `cdbee75f17c01a7cc42f958dc650907174af0554`. Model revision provenance is observed metadata, not proof that every remote artifact was explicitly pinned in the launch command.
- Python 3.12; Transformers 4.51.3; vLLM 0.8.5; Torch 2.6.0; NumPy 1.26.4; Qwen-Agent 0.0.34; SoundFile 0.14.0. See complete [environment freeze](logs/pip_freeze.log).

## Verified execution
All three requested IDs occur exactly once. Raw output turn counts are 4 (base), 5 (missing function), 5 (missing parameter). No top-level inference exceptions are recorded. Generation and official partial evaluation completed. The evaluator emitted per-category detailed score files and CSVs; status flags agree with the actual outputs/logs.

| Case | Official success | Official failure type |
|---|---|---|
| multi_turn_base_1 | 0/1 | multi_turn:instance_state_mismatch |
| multi_turn_miss_func_1 | 0/1 | multi_turn:empty_turn_model_response |
| multi_turn_miss_param_1 | 0/1 | multi_turn:instance_state_mismatch |

[Machine-readable score summary](score_summary.csv). These are the official scorer's task outcomes, not a relabelled three-way decision dataset. Do not report 0% as representative model accuracy: this is one indexed family, not three independent sampled families.

## Trace-based diagnosis
- **Base:** the model navigated and inspected the directory, then received an error because archive already existed. It subsequently announced a move in ordinary text without issuing the required mv tool call. The resulting file-system state failed the official comparison.
- **Missing parameter:** the same earlier move failure appears before the line-count intervention. Its task failure cannot be attributed solely to clarification behavior.
- **Missing function:** while mv was withheld, the model invoked cp and described copying as a successful move. When mv was subsequently introduced, it produced no executable call for that turn. The official scorer reported an empty turn-2 response list. This means empty decoded calls, not absent natural-language text.
- These observations come from this run's raw trajectories and official error details. They are descriptive diagnoses, not controlled causal estimates or independently validated cause labels.
- No code/prompt/tool inventory has been modified to make these three examples pass. Genuine model errors remain part of the baseline evidence.

## Resource evidence
GPU: Tesla T4, 15360 MiB total, 14913 MiB free before server start. Host RAM: 12.67 GiB total and about 11.47 GiB available before server launch. Disk: about 50.15 GiB free at that snapshot.

Server profile: FP16, max context 12288, GPU budget 0.85, one sequence and one request thread, eager V0, chunked prefill 2048, zero CPU KV swap and zero CPU weight offload.

Actual server profile reports: model weights **7.61 GiB**, activation peak **0.16 GiB**, non-Torch memory **0.05 GiB**, KV-cache reservation **4.57 GiB**, 2078 CUDA blocks and 0 CPU blocks. These values come from the server profiler; they are not continuous peak-memory monitoring of the complete experiment.
Maximum observed prompt token counts were 4066 (base), 4239 (missing function), 4195 (missing parameter). With the official 4096-token answer allowance, these remain within the 12288 limit. No context overflow appears in the inference records.

## What is established
The repaired software stack can execute and officially score this small BFCL workload within the user's T4 resource budget. One baseline-model smoke execution is now verified. The previous Python/soundfile/tokenizer/context setup blockers are resolved for this run.

## What remains open
No second calibrated comparator, schema-evidence intervention, held-out results, validated cause-of-nonexecution oracle or novelty claim has been established. The single-family pilot does not establish general runtime success across BFCL or overall model quality. BFCL's official task scorer remains the primary outcome reference; cause-specific labels remain a separate methodological problem.

**Research status: CONDITIONAL GO. Prompt 07 remains unfrozen.**

## Next work
1. Audit the observed tool-call and state failures, including what was exposed before/after the missing-function intervention.
2. Preserve this run as an execution check; do not use this case for later held-out performance claims after inspecting it.
3. Define a small family-separated development pilot and a fair baseline/intervention comparison before expanding GPU execution.
4. Use the known working resource profile and resolved environment versions; preserve full traces and official scores. Do not rerun this identical smoke test merely to obtain a passing model score.
