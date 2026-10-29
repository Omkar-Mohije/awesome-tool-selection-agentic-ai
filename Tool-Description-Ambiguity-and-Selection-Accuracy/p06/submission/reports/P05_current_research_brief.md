# Current one-page research brief

**Researcher:** Omkar Arjun Mohije, M.Tech, IIIT Allahabad. **Course:** AI Tools for Research. **Updated:** 29 October 2026.

**Review bridge.** The earlier review, *Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems*, distinguishes tool-selection decisions from argument filling, execution and full-trajectory success. BFCL evaluates stateful tool use; When2Call evaluates whether to call, clarify or acknowledge tool limitations. These verified sources support studying measurement and failure behavior, not a claim that abstention is a newly discovered research gap. Published paired BFCL act/hold scoring is attributed to Liu and Han.

**Question.** What differences are observed in complete-task success, tool-use decisions and execution failures across original, general-review and schema-evidence prompts on selected BFCL tasks? Primary prospective contrast: checklist minus general review in full-task success. The study is descriptive; it has no requirement to outperform existing methods.

**Pathway.** Controlled descriptive comparison plus attributed diagnostic reproduction. The user explicitly removed publication novelty as a completion requirement. The present question narrows the earlier retrieval-stage three-class proposal to benchmark-supported executable behavior.

**Data and comparators.** Pinned official BFCL multi-turn base, missing-function and missing-parameter variants. Qwen3-4B through its official handler. Original prompting and general review are executable controls; schema evidence is the intervention. They are not independent model architectures or calibrated abstention systems.

**Evidence and metrics.** Development families 1–3 are inspected; pilot families 2–3 yield 0/6 official task success per condition. Decision and strict no-call measures are secondary and explicitly different. Prospective families 89/73 are frozen separately under ATR-P07-v1; new model outputs are pending. Failure analysis supplies depth.

**Resources and risks.** T4 15 GiB, host RAM about 12.7 GiB, FP16, 24K context, one sequence, zero CPU offload. Context overflow, force termination, prompt-length/order confounds, correlated variants, incomplete decoding and benchmark/source-version differences are explicit.

**Decision rule.** Report raw successes/totals and a descriptive signed difference; do not infer significance from a two-family sample. Negative results answer the sample-specific question. New observations cannot be used for prompt tuning and then called unseen evaluation.
