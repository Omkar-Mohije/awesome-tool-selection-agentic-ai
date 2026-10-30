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

## Human ownership and student reflection

### 1. Code path personally traced
While running the benchmark on Google Colab, I stepped through how requests flow through scripts/policy_runner.py into BFCL and vLLM. Taking Family 2 (BFCL_v4_multi_turn_base_2) as a concrete case, the runner deep-copies the conversation history, injects the designated prompt instruction (vanilla, generic review, or schema checklist), and dispatches the payload to the local Qwen3-4B endpoint. When inspecting the resulting model outputs, I saw the model emit cd(folder='document') instead of the required folder name documents. Because BFCL validates against the live simulated environment, this single slip caused an execution error that registered as a state mismatch in score.json. Walking through this trace confirmed that the failure wasn't caused by JSON syntax issues or model hallucinations about nonexistent tools, but because the model lost track of exact argument references and directory paths across consecutive turns.

### 2. AI suggestion questioned and corrected
One key moment where I pushed back on the assistant was during the vLLM serving configuration. The assistant initially recommended a 12,288-token context window. Once we started running multi-turn interactions, turn history accumulated quickly to over 8,300 tokens, which combined with the 4,096-token generation allowance triggered a server context overflow error and crashed the run. The initial inclination was to simply truncate earlier turns, but I recognized that truncating history would corrupt the conversation state and invalidate the benchmark. Instead, I insisted on configuring a guarded 24,576-token ceiling with chunked prefill (2,048 tokens) and eager execution without CPU offload to fit our Tesla T4 budget. Similarly, when the assistant assumed BFCL's standalone no-call checker was evaluating our multi-turn tasks, we wrote a dispatch test and proved the runner wasn't even calling it, which stopped us from reporting unverified claims.

### 3. What can and cannot be concluded
Looking honestly at our results, all three prompt conditions (vanilla, general review, schema checklist) scored 0/6 complete-task success across the 18 evaluated task records. The dominant errors were 13 state mismatches and 4 execution-response mismatches. What we can conclude is that simply adding prompt guidelines or schema checklists does not bridge the gap when a 4B model struggles with multi-step environment state tracking under tight resource limits. However, we cannot conclude that prompt engineering doesn't work in general, nor can we extrapolate these results to the full BFCL leaderboard. Our sample only covered variants across two underlying task families, so the tasks within each family are closely correlated. Additionally, the secondary act/hold decision scores (50%, 25%, and 75%) came from only two eligible pairs—meaning they are merely descriptive post-hoc observations, not evidence of a statistically validated improvement.

Preserve the conversation as supporting evidence; the required concise prompt/code/verification log is supplied, but it is not a verbatim complete transcript. No use of Claude/Copilot/Gemini, independent human annotation panel, new training or successful held-out outcomes is claimed.
