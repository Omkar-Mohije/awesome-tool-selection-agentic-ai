# Prompting and Tool-Use Failures in a Resource-Constrained BFCL Pilot

**Current version: completed development evidence and reports; fresh prospective model results pending.** This repository accompanies an output-based empirical study on tool-calling reliability in multi-turn interactions under strict resource constraints. Publication novelty is not required.

## Repository Structure

- [paper/](paper/): Compiled 6-page IEEE-style manuscript ([main.pdf](paper/main.pdf)), LaTeX source ([main.tex](paper/main.tex)), BibTeX ([
eferences.bib](paper/references.bib)), class file ([IEEEtran.cls](paper/IEEEtran.cls)), and generated plots ([igures/](paper/figures/)).
- [
otebooks/](notebooks/): Pinned Colab execution notebook ([ATR_P07_Frozen_Evaluation_Colab.ipynb](notebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb)).
- [scripts/](scripts/): Inference runner ([policy_runner.py](scripts/policy_runner.py)), output analysis ([nalyze_run.py](scripts/analyze_run.py)), decision scoring ([score_decisions.py](scripts/score_decisions.py)), and submission test suite ([	est_submission.py](scripts/test_submission.py)).
- [configs/](configs/): Evaluation protocol ([protocol.json](configs/protocol.json)) and published scorer commit lock ([published_scorer_lock.json](configs/published_scorer_lock.json)).
- [
eports/](reports/): Research briefs, baseline audits, debugging logs, technical review, completed AI reflection, and viva guide.
- [
esults/](results/): Empirical task outcomes, CSV data tables, and decision metrics ([
esults/development/](results/development/)).
- [
uns/](runs/): Raw execution logs, manifests, and verified output archives for the smoke and recovery runs.
- [development_pilot/](development_pilot/): Pilot test fixtures, recovery scripts, reference controls, and diagnostic audits.
- [ssignment_prompts/](assignment_prompts/): Historical course prompt deliverables and decision records ([P01_P04/](assignment_prompts/P01_P04/), [P05/](assignment_prompts/P05/), [P06/](assignment_prompts/P06/)).

## Start Here

1. Read [paper/main.pdf](paper/main.pdf) (compiled six-page IEEE-style manuscript), [
eports/P05_current_research_brief.md](reports/P05_current_research_brief.md), and [
eports/P10_baseline_validation.md](reports/P10_baseline_validation.md).
2. Run the pinned [
otebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb](notebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb) in the existing T4 Colab runtime. Protocol freeze commit: 2d72394d1e725f7a80236661f600d995dd705b39. The one-cell launcher executes that exact notebook in the existing kernel; no second session is needed.
3. Keep and upload ATR_Frozen_Evaluation_Outputs.zip. The paper deliberately contains no new results until that archive is validated.
4. Review [
eports/P09_code_understanding.md](reports/P09_code_understanding.md) and [
eports/demonstration_and_viva.md](reports/demonstration_and_viva.md). Student personal reflection is completed in [
eports/P18_AI_use_and_reflection.md](reports/P18_AI_use_and_reflection.md).

## Deliverable Map

| Assignment component | Artifact |
|---|---|
| Current gap/question brief (P05/G1) | [
eports/P05_current_research_brief.md](reports/P05_current_research_brief.md) |
| Dataset/comparator validation (P06) | [
eports/P06_dataset_comparator_validation.md](reports/P06_dataset_comparator_validation.md) |
| Prospective blueprint, diagram, settings, checklist (P07) | [
eports/P07_protocol.md](reports/P07_protocol.md), [configs/protocol.json](configs/protocol.json) |
| Environment verification (P08) | [
eports/P08_environment_verification.md](reports/P08_environment_verification.md), [
equirements-colab-observed.txt](requirements-colab-observed.txt) |
| Baseline and code understanding (P09) | [
otebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb](notebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb), [scripts/policy_runner.py](scripts/policy_runner.py), [
eports/P09_code_understanding.md](reports/P09_code_understanding.md) |
| Validation/discrepancies (P10/G2) | [
eports/P10_baseline_validation.md](reports/P10_baseline_validation.md), [
uns/](runs/) |
| Debugging evidence (P11) | [
eports/P11_debugging_log.md](reports/P11_debugging_log.md), [development_pilot/](development_pilot/) |
| Contribution/evaluation/interpretation (P12–P14/G3) | [
eports/P12_P14_evidence_and_interpretation.md](reports/P12_P14_evidence_and_interpretation.md), [
esults/development/](results/development/), [scripts/analyze_run.py](scripts/analyze_run.py) |
| Manuscript and review (P15–P16) | [paper/main.pdf](paper/main.pdf), [paper/main.tex](paper/main.tex), [paper/references.bib](paper/references.bib), [paper/figures/](paper/figures/), [
eports/P16_technical_review.md](reports/P16_technical_review.md) |
| Reproducibility (P17) | [README.md](README.md), [configs/](configs/), [scripts/](scripts/), [
eports/P17_reproduction_checklist.md](reports/P17_reproduction_checklist.md) |
| Authentic AI provenance and reflection (P18) | [
eports/P18_AI_use_and_reflection.md](reports/P18_AI_use_and_reflection.md) (with completed student reflections) |
| Five-minute demonstration (G4) | [
eports/demonstration_and_viva.md](reports/demonstration_and_viva.md) |

Earlier P01–P06 reports and historical decisions remain preserved in [ssignment_prompts/](assignment_prompts/):
- [ssignment_prompts/P01_P04/](assignment_prompts/P01_P04/)
- [ssignment_prompts/P05/](assignment_prompts/P05/)
- [ssignment_prompts/P06/](assignment_prompts/P06/)

The current brief explicitly reconciles the narrowed question with the previous review. Existing pilot outputs are development evidence, not a retrospectively frozen test.

## Observed Execution Environment

Model registry Qwen/Qwen3-4B-Instruct-2507-FC; checkpoint without -FC; pinned BFCL commit in config. The working Colab environment uses Python 3.12 in /content/bfcl-py312, torch 2.6.0, vLLM 0.8.5, transformers 4.51.3, numpy 1.26.4 and soundfile 0.14.0. Full observed pins are in [
equirements-colab-observed.txt](requirements-colab-observed.txt). This is a recorded freeze, not a claim that every future pip/platform combination can resolve it unchanged.

Warm run reuses that environment and performs explicit version/import/CLI checks without upgrading. If absent, the notebook attempts an isolated cold replay from observed pins (TEST REQUIRED). Cold disk minimum is 25 GiB; record real memory/disk state. The original 12.7 GiB host RAM and 15 GiB T4 budget motivate FP16, one sequence, 85% memory, 24K cap, eager V0, 2048-token chunked prefill and zero offload/swap. Overlong requests are rejected without truncation or reducing the answer allowance.

## Reproduce Completed Development Tables and Figures

From the project root:

`ash
python scripts/analyze_run.py   --archive runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip   --output results/reproduced_development
python scripts/score_decisions.py   --archive runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip   --output results/reproduced_development/decision
python scripts/test_submission.py
`

These scripts were executed against the genuine archive. The plotting script needs matplotlib ([
equirements-analysis.txt](requirements-analysis.txt) records the local version); --no-plots uses the standard library only. Run analysis in a separate CPU environment or existing compatible notebook kernel rather than upgrading the inference venv unnecessarily. The decision wrapper downloads and hash-verifies the original published scorer, manifest, labels, LICENSE and NOTICE. Warm-cache execution was tested; fresh downloads of these files remain TEST REQUIRED in another environment.

Expected development task results: 0/6 for each condition. Expected original published decision means on two eligible pairs: 50%, 25%, 75%. These are post-hoc development measures with different targets and denominators. Do not relabel either measure as useful clarification accuracy.

For a new genuine archive, use the same analysis commands with its path and a new output folder. Generation/scoring must be complete before task accuracy is calculated; inference exceptions block a completed-run accuracy report. Keep force-terminated tasks as failures. The decision wrapper marks missing raw anchors unavailable, rather than crediting them as abstentions. Review source/reference/parser compatibility before interpreting new secondary scores.

## Build the Manuscript / Overleaf

`ash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
`

This exact compilation sequence ran successfully. Import [paper/](paper/) as an Overleaf project and set [main.tex](paper/main.tex) as the main file. [IEEEtran.cls](paper/IEEEtran.cls) is the CTAN class with original license text retained; template provenance is recorded. There is no claim of IEEE acceptance or a published paper. An instructor-selected alternative template takes precedence if one is specified later.

The compiled version reports only completed development evidence. After actual prospective outputs arrive, add a separate results table/section, update pending status and rerender/review; do not silently replace or backdate the pilot. The manuscript source, CSVs and figure script are editable for future work with any assistant or without a subscription.

## Evidence, Licenses and Credits

Raw smoke and recovery ZIPs are in sibling [
uns/](runs/) folders in the complete package. The 203 outer and 62 nested recovery hashes were verified, and 11 reused records matched the original attempt. Development comparisons mix old valid 12K records and new 24K records with provenance; they are not a uniform-run speed benchmark.

BFCL code/data: [Gorilla](https://github.com/ShishirPatil/gorilla). Model: [Qwen checkpoint](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507). Published diagnostic, its labels and certification: [Liu and Han](https://github.com/YangzeLiu/asking-earns-nothing), pinned in [configs/published_scorer_lock.json](configs/published_scorer_lock.json). Preserve upstream licenses/notices. Public access does not independently establish every constituent redistribution right; model weights are not included. This repository's existing [LICENSE](../LICENSE) applies to original project material, subject to upstream terms for reused components.

## Before Submission

- Confirm the latest announcement's submission location, exact cutoff and template; these are not inferred from the earlier deadline.
- Verify the fresh run's actual status and keep pending labels if it did not complete.
- Read and understand the principal code path; finish your authentic reflection.
- Submit the PDF, LaTeX/BibTeX/figures, repository, real CSV/log evidence, validation/provenance reports and prepare the demonstration. Preserve the conversation as supporting evidence; the concise authentic log does not pretend to be a full transcript.
