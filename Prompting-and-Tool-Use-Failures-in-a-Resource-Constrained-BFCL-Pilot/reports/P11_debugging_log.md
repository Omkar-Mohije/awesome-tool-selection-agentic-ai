# P11: authentic evidence-based debugging record

| Observed issue | Confirmed evidence | Correction and verification | Prior-result impact |
|---|---|---|---|
| Python/dependency incompatibility | BFCL pins numpy 1.26.4; original Colab kernel was Python 3.13 | Isolated Python 3.12 environment, pinned Transformers 4.51.3/vLLM 0.8.5, genuine import/version logs | Failed setup is not model performance |
| Missing soundfile | User supplied `ModuleNotFoundError: No module named 'soundfile'` through Qwen-Agent CLI import | Install soundfile in the BFCL venv and test full CLI import chain before GPU use | No model task output existed from the failed invocation |
| Late context overflow | 8302 input + 4096 answer = 12398 against cap 12288 | Synchronize handler/server budget; cap 24576; preserve full output allowance; reject oversize explicitly. Recovery completed genuinely | Keep original failure; reuse 11 unchanged valid records, retry exception separately, record seven newly generated records |
| Colab too many sessions | User screenshot showed active-session limit | Execute the pinned recovery notebook's code in the original kernel using a one-cell loader | Existing source run was retained; no assertion that a new session inherited local files |
| Synthetic reference identifier bug | A UUID beginning with a digit caused invalid-decimal execution exceptions; equality-only checks could still pass | Prefix identifiers alphabetically and separately assert no reference execution exception; corrected controls pass | Only corrected controls reported as successful; this was a local synthetic-control bug, not the user's model registry failure |
| No-call integration assumption | Original source imports an irrelevance checker but does not call it in multi-turn dispatch | Inspect original function and execute isolated identity-decoder controls; revise interpretation | Previous standalone tests remain valid; no-call compliance is separate from official complete-task scoring |

Expected behavior, fixes and verification are described from actual traces, source and executed tests. Earlier failed attempts and the force-terminated model task are preserved; no clean fictional run history is substituted. Detailed source logs remain in the original `P06_BFCL_Troubleshooting_Log.md` and archived runs.
