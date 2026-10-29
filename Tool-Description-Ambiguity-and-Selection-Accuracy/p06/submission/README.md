# ATR implementation-study submission

**Current version: completed development evidence and reports; fresh prospective model results pending.** This folder does not claim that pending tests or personal reflection are complete. It accompanies the user's output-based course study; publication novelty is not required.

## Start here

1. Read `paper/main.pdf` (compiled six-page IEEE-style manuscript), `reports/P05_current_research_brief.md`, and `reports/P10_baseline_validation.md`.
2. Run the pinned `notebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb` in the existing T4 Colab runtime. Protocol freeze commit: `2d72394d1e725f7a80236661f600d995dd705b39`. The one-cell launcher supplied in chat executes that exact notebook in the existing kernel; no second session is needed.
3. Keep and upload `ATR_Frozen_Evaluation_Outputs.zip`. The paper deliberately contains no new results until that archive is validated.
4. Review `reports/P09_code_understanding.md` and `reports/demonstration_and_viva.md`. Complete the three personal-reflection paragraphs in `reports/P18_AI_use_and_reflection.md` in your own words.

## Deliverable map

| Assignment component | Artifact |
|---|---|
| Current gap/question brief (P05/G1) | `reports/P05_current_research_brief.md` |
| Dataset/comparator validation (P06) | `reports/P06_dataset_comparator_validation.md` |
| Prospective blueprint, diagram, settings, checklist (P07) | `reports/P07_protocol.md`, `configs/protocol.json` |
| Environment verification (P08) | `reports/P08_environment_verification.md`, observed dependency freeze, notebook preflights |
| Baseline and code understanding (P09) | notebook, `scripts/policy_runner.py`, `reports/P09_code_understanding.md` |
| Validation/discrepancies (P10/G2) | `reports/P10_baseline_validation.md`, software/control reports, original raw archives |
| Debugging evidence (P11) | `reports/P11_debugging_log.md` and original troubleshooting log |
| Contribution/evaluation/interpretation (P12–P14/G3) | `reports/P12_P14_evidence_and_interpretation.md`, `results/development`, analysis scripts |
| Manuscript and review (P15–P16) | `paper/main.pdf`, `main.tex`, `references.bib`, figures, `reports/P16_technical_review.md` |
| Reproducibility (P17) | this README, versioned configs, scripts, `reports/P17_reproduction_checklist.md` |
| Authentic AI provenance and reflection (P18) | `reports/P18_AI_use_and_reflection.md`; personal reflection pending student input |
| Five-minute demonstration (G4) | `reports/demonstration_and_viva.md` |

Earlier P01–P04 reports and historical decisions remain in the repository and are linked by the package index. The current brief explicitly reconciles the narrowed question with the previous review. Existing pilot outputs are development evidence, not a retrospectively frozen test.

## Observed execution environment

Model registry `Qwen/Qwen3-4B-Instruct-2507-FC`; checkpoint without `-FC`; pinned BFCL commit in config. The working Colab environment uses Python 3.12 in `/content/bfcl-py312`, torch 2.6.0, vLLM 0.8.5, transformers 4.51.3, numpy 1.26.4 and soundfile 0.14.0. Full observed pins are in `requirements-colab-observed.txt`. This is a recorded freeze, not a claim that every future pip/platform combination can resolve it unchanged.

Warm run reuses that environment and performs explicit version/import/CLI checks without upgrading. If absent, the notebook attempts an isolated cold replay from observed pins (TEST REQUIRED). Cold disk minimum is 25 GiB; record real memory/disk state. The original 12.7 GiB host RAM and 15 GiB T4 budget motivate FP16, one sequence, 85% memory, 24K cap, eager V0, 2048-token chunked prefill and zero offload/swap. Overlong requests are rejected without truncation or reducing the answer allowance.

## Reproduce completed development tables and figures

From `submission/` inside the complete package/repository:

```bash
python scripts/analyze_run.py \
  --archive ../runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip \
  --output results/reproduced_development
python scripts/score_decisions.py \
  --archive ../runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip \
  --output results/reproduced_development/decision
python scripts/test_submission.py
```

These scripts were executed against the genuine archive. The plotting script needs matplotlib (`requirements-analysis.txt` records the local version); `--no-plots` uses the standard library only. Run analysis in a separate CPU environment or existing compatible notebook kernel rather than upgrading the inference venv unnecessarily. The decision wrapper downloads and hash-verifies the original published scorer, manifest, labels, LICENSE and NOTICE. Warm-cache execution was tested; fresh downloads of these files remain TEST REQUIRED in another environment.

Expected development task results: 0/6 for each condition. Expected original published decision means on two eligible pairs: 50%, 25%, 75%. These are post-hoc development measures with different targets and denominators. Do not relabel either measure as useful clarification accuracy.

For a new genuine archive, use the same analysis commands with its path and a new output folder. Generation/scoring must be complete before task accuracy is calculated; inference exceptions block a completed-run accuracy report. Keep force-terminated tasks as failures. The decision wrapper marks missing raw anchors unavailable, rather than crediting them as abstentions. Review source/reference/parser compatibility before interpreting new secondary scores.

## Build the manuscript / Overleaf

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

This exact compilation sequence ran successfully. Import `paper/` as an Overleaf project and set `main.tex` as the main file. `IEEEtran.cls` is the CTAN class with original license text retained; template provenance is recorded. There is no claim of IEEE acceptance or a published paper. An instructor-selected alternative template takes precedence if one is specified later.

The compiled version reports only completed development evidence. After actual prospective outputs arrive, add a separate results table/section, update pending status and rerender/review; do not silently replace or backdate the pilot. The manuscript source, CSVs and figure script are editable for future work with any assistant or without a subscription.

## Evidence, licenses and credits

Raw smoke and recovery ZIPs are in sibling `runs/` folders in the complete package. The 203 outer and 62 nested recovery hashes were verified, and 11 reused records matched the original attempt. Development comparisons mix old valid 12K records and new 24K records with provenance; they are not a uniform-run speed benchmark.

BFCL code/data: [Gorilla](https://github.com/ShishirPatil/gorilla). Model: [Qwen checkpoint](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507). Published diagnostic, its labels and certification: [Liu and Han](https://github.com/YangzeLiu/asking-earns-nothing), pinned in `configs/published_scorer_lock.json`. Preserve upstream licenses/notices. Public access does not independently establish every constituent redistribution right; model weights are not included. This repository's existing LICENSE applies to original project material, subject to upstream terms for reused components.

## Before submission

- Confirm the latest announcement's submission location, exact cutoff and template; these are not inferred from the earlier deadline.
- Verify the fresh run's actual status and keep pending labels if it did not complete.
- Read and understand the principal code path; finish your authentic reflection.
- Submit the PDF, LaTeX/BibTeX/figures, repository, real CSV/log evidence, validation/provenance reports and prepare the demonstration. Preserve the conversation as supporting evidence; the concise authentic log does not pretend to be a full transcript.
