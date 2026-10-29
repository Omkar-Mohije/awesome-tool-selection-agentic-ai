# P18: human–AI collaboration and integrity report

## Authentic activity ledger

Historical entries below are summaries of actual activity, **not reconstructed verbatim prompts**. Exact quoted requests are labeled separately. AI assistance was ChatGPT with source/file inspection, Python analysis and GitHub changes. Exact model version for every historical chat turn is not independently established; do not invent one. User-run model inference used the recorded Qwen checkpoint, distinct from the chatbot.

| Activity | Request/proposal and human decision | Verification / artifact | Outcome |
|---|---|---|---|
| Scope and feasibility | Research direction investigated through recorded prompts/decisions; original publication novelty not established | Verified primary sources and repository files | Scope revisions preserved rather than overwritten |
| Code and environment | AI prepared notebook; user executed Colab and supplied genuine failures/ZIPs | Python 3.12 stack, imports, dependency freeze, official scoring | Working model runs; no assistant-local GPU execution claimed |
| Recovery | AI proposed guarded 24K recovery; user ran it in the existing kernel | Raw context error, 11 unchanged reused records, seven new records, hashes | Completed development pilot; all task failures retained |
| Evaluation | AI inspected actual traces and executed CPU controls/offline scorers | Original ZIPs, CSVs, source locks, state/response and dispatch controls | Metric distinctions established; interpretations corrected |
| Human scope choice | Exact user request: “proceed with output based study. drop the publication only thing.” | Conversation and dated D023 decision | Output-based course scope adopted; no novelty gate |
| Requirements audit | User asked whether prompts/deliverables were complete | Original 18-prompt sheet and latest announcement read | Earlier broad completion language corrected; prospective freeze gap identified |
| Submission preparation | Exact user request: “Make sure the last generated experiment code is reproducible as per used colab environment.” | New version/import/source/hash checks, observed dependency freeze, frozen notebook | Prepared warm/cold paths; new GPU execution pending |

## Real AI limitations and corrections

1. A suggested working path initially missed a transitive Qwen-Agent soundfile dependency. Actual user traceback led to full CLI import preflight before loading weights.
2. Initial prompt checks alone missed later history growth beyond 12K. Real token-budget evidence led to synchronized context guarding and provenance-preserving recovery.
3. A source-level assumption about no-call checking was too broad: a checker being present did not mean the runner invoked it. Direct dispatch inspection and synthetic controls corrected the interpretation.
4. An initial synthetic-control UUID was an invalid Python identifier. A separate execution-error guard caught a false sense of success from reference equality; the corrected prefixed identifier was rerun.
5. Study drafting was initially described too broadly as readiness. Checking the original instruction sheet exposed the missing prospective P07 requirement and incomplete final deliverables.

## Human ownership and student reflection — to complete honestly

The user performed the Colab executions, supplied errors and output archives, requested checks, authorized scope choices and asked for reproducibility. This does not establish that all code is independently understood. Before submission, the student should write or confirm three short paragraphs in their own words:

- Explain one code path personally traced, including its inputs, model/tool calls and saved result.
- Explain one AI suggestion questioned or corrected, why the evidence mattered and what was learned.
- Explain what can and cannot be concluded from the measured negative task results and tiny secondary sample.

These are intentionally unanswered personal-reflection prompts. They are not a fabricated first-person account. Preserve the conversation as supporting evidence; the required concise prompt/code/verification log is supplied, but it is not a verbatim complete transcript. No use of Claude/Copilot/Gemini, independent human annotation panel, new training or successful held-out outcomes is claimed.
