# PRE-P07 — Comparator feasibility (research design, not reproduced benchmarks)

## Problem/scope
Official BFCL V4 is **multi-turn tool-calling action and execution evaluation**, not static retrieval. Any paper using it as the principal empirical anchor must say "tool-calling action selection / non-call reliability", or present a clearly separated retrieval stage followed by a call policy.

## Credible task-compatible comparators
| Comparator | Action space and information | Implementation status | Assessment |
|---|---|---|---|
| A. BFCL-compatible native tool-calling model with original prompt + exposed function inventory | Function call(s) or no function call, multi-turn state and context; original BFCL decoded/executed scorer | OFFICIAL framework inspected, no actual compatible weights/API run | Strong benchmark-aligned control, but free Colab may not support candidate model |
| B. Same tool-calling model with explicit, development-calibrated abstention / score or decision thresholds | Tool call or no call; any clarification text requires a separately justified evaluator; identical inputs/models for fair comparison | NOT RUN; calibrated logits/confidence availability UNKNOWN | Conditional comparator; cannot claim full three-way score merely from no-call |
| C. Transparent schema/function-existence evidence policy (proposed) | Calls only with evidence; no-call or unresolved otherwise. Uses permitted active inventory, schema and previous state; not answer files | Structural oracle unit tests only, NOT model policy execution | Proposed intervention, not baseline validation |
| D. Forced top-one BM25/dense retrieval | Ranked functions, no multi-turn executable call or clarification | NOT RUN | Diagnostic retrieval component only, **not comparable** by itself to BFCL agentic task |

At least **two credible executable classes** are A (BFCL function-calling model) and B (same model with calibrated decision policy), conditional upon weights/API access. An additional simple no-call/always-call diagnostic may be trivial to implement but cannot by itself support a strong paper. A stronger published comparator such as SAGE-Agent/AgentAbstain/calibrated action model requires exact task adaptation, public implementation and licensing checks; none reproduced.

## Requirements for a fair comparison
- Same *visible* user history, tool signatures and previous observations at each decision; don't allow proposed method to peek at ground_truth, withheld tool names or future turns.
- Fix model version, system prompt, decoding, exposed functions, tool-call budget, candidate ordering, context and state-reset protocol.
- Train/tune any threshold on a separate development group, never the official held-out evaluation families.
- Compare primary original BFCL task success on the **official evaluator**; auxiliary no-call confusion and attempted action type with separately validated cause labels.
- Report per-family and per-turn measures distinctly, latency/inference tokens/cost, and proper uncertainty; do not convert a bare no-call decision into a proven clarifying response.

## Resource/access
Code for the BFCL scorer is publicly inspected. Official `data/README.md` declares Apache-2.0; independently inspect any checkpoint and API usage terms. **UNKNOWN:** actual free Colab GPU allocation, model memory, native tool-call support, local checkpoint weights, and reference-score reproduction. A small function-calling model may fit in free Colab with quantization, but this is an estimate, not a validated runtime.

## Novelty and best scientific framing
BFCL already evaluates missing-function and missing-parameter categories. SAGE-Agent already studies clarification; AgentAbstain studies agent abstention; Tool-REX/MFTR study richer capability evidence; calibrated action research exists. A defensible possible addition is **error attribution: whether no-call mistakes reflect incorrect capability assessment or missing-specification handling, under same-state paired perturbations and calibrated action baselines**. Without independently verified cause labels and strong controls, this is not a novel demonstrated contribution.

**Decision:** CONDITIONAL GO for baseline feasibility checks, **NO-GO for Prompt 07 protocol freeze** until label/source state and model execution evidence are established.
