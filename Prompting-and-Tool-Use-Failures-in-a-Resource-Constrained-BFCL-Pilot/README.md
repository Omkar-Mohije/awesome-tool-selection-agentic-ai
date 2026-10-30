# Prompting and Tool-Use Failures in a Resource-Constrained BFCL Pilot

**Author:** Omkar Arjun Mohije (M.Tech, IIIT Allahabad)  
**Study Scope:** Empirical Implementation Study & Failure Analysis (Course Study)  
**Paper:** [Compiled 6-Page IEEE Paper (PDF)](paper/main.pdf) | [LaTeX Source](paper/main.tex)

> [!NOTE]
> **Study Status:** Completed development evidence and validation reports. Prospective held-out evaluation is frozen under commit `2d72394d1e72` with new GPU outcomes pending. Publication novelty is not claimed; this package provides an attributed, reproducible evaluation of prompt interventions and failure modes under hard hardware limits.

---

## Executive Summary

Connecting language models to external tools requires more than syntactically valid function calls—the agent must select appropriate tools, bind correct arguments, and reliably transition simulated environment states across multiple conversation turns.

This project investigates tool-calling failures on the **Berkeley Function-Calling Leaderboard (BFCL)** multi-turn benchmark using **Qwen3-4B-Instruct** served via vLLM on a single 15 GiB Tesla T4 GPU. We evaluated three prompting strategies:
1. **Vanilla Prompt:** Default model formatter and system instructions.
2. **General Review:** Generic instruction emphasizing step-by-step task review.
3. **Schema-Evidence Checklist:** Structured checklist verifying capabilities, required arguments, and state prerequisites.

### Core Empirical Findings

Across 18 recorded condition/task runs (evaluating base, missing-function, and missing-parameter variants across two task families):
- **Complete-Task Accuracy:** **0/6 (0%)** across all three prompting conditions. Neither prompt intervention enabled end-to-end task success.
- **Observed Failure Modes:** The 18 first-failure events comprised **13 state mismatches**, **4 response mismatches**, and **1 force termination**.
- **Root Causes:** Failures were driven primarily by ordinary path/state-tracking errors (e.g., calling `cd(folder='document')` instead of `documents`), rather than function hallucination or schema syntax errors.
- **Secondary Act/Hold Scoring:** Applying Liu & Han's reproduced paired decision scorer yielded post-hoc descriptive scores of 50%, 25%, and 75% on only two eligible pairs, which does not constitute evidence of systematic prompt improvement.

---

## Quick Navigation

| Deliverable | Key Artifacts | Description |
|---|---|---|
| **Research Paper** | [`paper/main.pdf`](paper/main.pdf), [`paper/main.tex`](paper/main.tex) | 6-page IEEE conference format manuscript |
| **Colab Evaluation** | [`notebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb`](notebooks/ATR_P07_Frozen_Evaluation_Colab.ipynb) | Pinned executable Google Colab evaluation notebook |
| **Pipeline Scripts** | [`scripts/policy_runner.py`](scripts/policy_runner.py), [`scripts/analyze_run.py`](scripts/analyze_run.py) | Inference wrapper, context guarding, and analysis scripts |
| **Configuration** | [`configs/protocol.json`](configs/protocol.json), [`configs/published_scorer_lock.json`](configs/published_scorer_lock.json) | Frozen experiment protocol and secondary scorer pins |
| **Reports (P05–P18)** | [`reports/`](reports/) | Research brief, baseline validation, debugging logs, AI reflection |
| **Experimental Runs** | [`runs/`](runs/) | Verified raw output archives, manifests, and execution logs |
| **Assignment Stages** | [`assignment_prompts/`](assignment_prompts/) | Isolated coursework prompts and decisions ([`P01_P04/`](assignment_prompts/P01_P04/), [`P05/`](assignment_prompts/P05/), [`P06/`](assignment_prompts/P06/)) |

---

## Repository Structure

```
Prompting-and-Tool-Use-Failures-in-a-Resource-Constrained-BFCL-Pilot/
├── README.md                          # Project documentation and reproduction guide
├── DELIVERABLE_STATUS.md              # Current deliverable compliance checklist
├── HANDOFF.md                         # Portable experiment continuation guide
├── requirements-colab-observed.txt    # Exact pinned Colab dependencies (Python 3.12, torch 2.6.0)
├── requirements-analysis.txt          # CPU analysis dependencies (matplotlib, standard library)
├── constraints-core.txt               # Hardware & memory constraints for Tesla T4
│
├── paper/                             # IEEE-style manuscript and figures
│   ├── main.tex                       # LaTeX paper source
│   ├── main.pdf                       # Compiled 6-page PDF manuscript
│   ├── references.bib                 # Verified bibliography
│   ├── IEEEtran.cls                   # CTAN IEEEtran document class
│   └── figures/                       # Empirical failure plots and task outcome charts
│       ├── failure_types.png / .pdf
│       └── task_outcomes.png / .pdf
│
├── notebooks/                         # Google Colab notebooks
│   └── ATR_P07_Frozen_Evaluation_Colab.ipynb # Frozen evaluation pipeline
│
├── scripts/                           # Core execution and analysis suite
│   ├── policy_runner.py               # History deep-copying and prompt policy injector
│   ├── analyze_run.py                 # Manifest verification and task outcome exporter
│   ├── score_decisions.py             # Attributed Liu & Han act/hold decision scorer
│   └── test_submission.py             # Offline syntax, lifecycle, and integrity tests
│
├── configs/                           # Experiment protocols and locks
│   ├── protocol.json                  # Pinned model revisions, task IDs, and serving profile
│   └── published_scorer_lock.json     # Pinned secondary scorer commit and SHA256 hashes
│
├── reports/                           # Comprehensive phase and reflection reports
│   ├── P05_current_research_brief.md
│   ├── P06_dataset_comparator_validation.md
│   ├── P07_protocol.md
│   ├── P08_environment_verification.md
│   ├── P09_code_understanding.md      # Code walkthrough & viva preparation
│   ├── P10_baseline_validation.md     # Observed discrepancies and controls
│   ├── P11_debugging_log.md           # Context overflow and dependency resolution
│   ├── P12_P14_evidence_and_interpretation.md
│   ├── P16_technical_review.md
│   ├── P17_reproduction_checklist.md
│   ├── P18_AI_use_and_reflection.md   # Completed student personal reflection
│   └── demonstration_and_viva.md      # 5-minute walkthrough and viva defense guide
│
├── results/                           # Evaluation outputs and metrics
│   └── development/                   # Verified CSV results and decision scores
│
├── runs/                              # Verifiable execution archives and logs
│   ├── 20261029T113521Z-d72a657e/     # Initial smoke run outputs
│   └── 20261029T122816Z-5e29a2e6/     # Full recovery run outputs and manifests
│
├── development_pilot/                 # Pilot diagnostics and recovery controls
│   ├── diagnostic_review/             # Published diagnostic reproduction logs
│   ├── reference_control/             # Reference action replay and dispatch audits
│   └── ...
│
└── assignment_prompts/                # Separated historical course prompt phases
    ├── P01_P04/                       # Prompts 1-4 PDFs and decision logs
    ├── P05/                           # Prompt 5 research brief and criteria
    └── P06/                           # Prompt 6 dataset mapping, runbook, and rubrics
```

---

## Assignment Deliverable Map

| Assignment Requirement | Primary Artifacts | Status |
|---|---|---|
| **P05: Current Research Brief** | [`reports/P05_current_research_brief.md`](reports/P05_current_research_brief.md) | Verified |
| **P06: Dataset & Comparator Validation** | [`reports/P06_dataset_comparator_validation.md`](reports/P06_dataset_comparator_validation.md), [`assignment_prompts/P06/`](assignment_prompts/P06/) | Verified |
| **P07: Prospective Protocol Blueprint** | [`reports/P07_protocol.md`](reports/P07_protocol.md), [`configs/protocol.json`](configs/protocol.json) | Frozen |
| **P08: Environment Verification** | [`reports/P08_environment_verification.md`](reports/P08_environment_verification.md), [`requirements-colab-observed.txt`](requirements-colab-observed.txt) | Verified |
| **P09: Baseline Code Understanding** | [`reports/P09_code_understanding.md`](reports/P09_code_understanding.md), [`scripts/policy_runner.py`](scripts/policy_runner.py) | Verified |
| **P10: Baseline Discrepancies & Controls** | [`reports/P10_baseline_validation.md`](reports/P10_baseline_validation.md), [`development_pilot/`](development_pilot/) | Verified |
| **P11: Evidence-Based Debugging Log** | [`reports/P11_debugging_log.md`](reports/P11_debugging_log.md) | Verified |
| **P12–P14: Evidence & Interpretation** | [`reports/P12_P14_evidence_and_interpretation.md`](reports/P12_P14_evidence_and_interpretation.md), [`results/development/`](results/development/) | Verified |
| **P15–P16: Implementation Manuscript** | [`paper/main.pdf`](paper/main.pdf), [`paper/main.tex`](paper/main.tex), [`reports/P16_technical_review.md`](reports/P16_technical_review.md) | Compiled |
| **P17: Reproduction Checklist** | [`reports/P17_reproduction_checklist.md`](reports/P17_reproduction_checklist.md), [`scripts/test_submission.py`](scripts/test_submission.py) | Verified |
| **P18: Human–AI Collaboration & Reflection** | [`reports/P18_AI_use_and_reflection.md`](reports/P18_AI_use_and_reflection.md) | Completed |
| **Demonstration & Viva Guide** | [`reports/demonstration_and_viva.md`](reports/demonstration_and_viva.md) | Prepared |

Earlier P01–P06 reports and historical decisions remain preserved in [`assignment_prompts/`](assignment_prompts/):
- [`assignment_prompts/P01_P04/`](assignment_prompts/P01_P04/)
- [`assignment_prompts/P05/`](assignment_prompts/P05/)
- [`assignment_prompts/P06/`](assignment_prompts/P06/)

The current brief explicitly reconciles the narrowed question with the previous review. Existing pilot outputs are development evidence, not a retrospectively frozen test.

---

## Observed Execution Environment

The model inference pipeline was deployed and verified on **Google Colab** on a single **15 GiB Tesla T4 GPU** with ~12.7 GiB host RAM:
- **Model Checkpoint:** `Qwen/Qwen3-4B-Instruct-2507` (served locally via vLLM 0.8.5 with BFCL official handler).
- **Python Runtime:** Python 3.12 virtual environment (`/content/bfcl-py312`).
- **Core Dependencies:** PyTorch 2.6.0, Transformers 4.51.3, NumPy 1.26.4, SoundFile 0.14.0 (full freeze documented in [`requirements-colab-observed.txt`](requirements-colab-observed.txt)).
- **Serving Parameters:** FP16 precision, 85% GPU memory utilization cap, max 1 concurrent sequence, eager execution (V0), 2,048-token chunked prefill, 0 GiB CPU swap/offload.
- **Context Budget Guard:** Max sequence length capped at 24,576 tokens, enforcing an explicit 4,096-token completion allowance while rejecting overlength requests without destructive history truncation.

---

## Reproduction Guide

All reproduction commands can be executed directly from the project root directory:

### 1. Reproduce Task Outcomes & Figures
```bash
python scripts/analyze_run.py \
  --archive runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip \
  --output results/reproduced_development
```
*Outputs:* Manifest validation checks, per-case outcomes CSV, score summaries, and figures (`failure_types.png`, `task_outcomes.png`). Use `--no-plots` to run without matplotlib.

### 2. Reproduce Attributed Decision Scoring
```bash
python scripts/score_decisions.py \
  --archive runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip \
  --output results/reproduced_development/decision
```
*Outputs:* Downloads, hash-verifies, and executes Liu & Han's published paired decision scorer against the recovery outputs.

### 3. Run Submission Verification Suite
```bash
python scripts/test_submission.py
```
*Outputs:* Offline checks validating notebook AST syntax, subprocess timeouts, lifecycle recovery, and byte-level hash integrity.

---

## Manuscript Compilation (Overleaf / Local LaTeX)

The manuscript is written in standard IEEE conference format using CTAN `IEEEtran.cls`:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

To compile on **Overleaf**:
1. Upload the entire [`paper/`](paper/) directory to Overleaf.
2. Ensure [`main.tex`](paper/main.tex) is selected as the main document.
3. Choose the standard pdfLaTeX compiler.

---

## Citation & Upstream Attribution

- **BFCL Benchmark:** Gorilla Function Calling Benchmark ([Patil et al., 2025](https://gorilla.cs.berkeley.edu/leaderboard.html)). Source pinned at commit `6ea57973c7a6`.
- **Model Checkpoint:** [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507).
- **Secondary Scorer:** Attributed paired act/hold decision scorer from [Liu & Han (2026)](https://github.com/YangzeLiu/asking-earns-nothing), pinned in [`configs/published_scorer_lock.json`](configs/published_scorer_lock.json).
- **Project License:** Original project code and documentation are released under the repository's [MIT License](../LICENSE), preserving all upstream notices.
