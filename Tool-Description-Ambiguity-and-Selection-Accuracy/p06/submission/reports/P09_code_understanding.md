# P09: code and data-flow walkthrough

1. **Protocol and IDs:** `configs/protocol.json` fixes two families, six task IDs, three conditions and serving settings. Data are JSONL, one dictionary per task. Ground truth is a list of turn-level lists of call strings; it is used offline only.
2. **Environment:** notebook calls `/content/bfcl-py312/bin/python`, checks versions/imports, CLI help, hardware and pip consistency. It can reuse a warm environment or attempt the labeled cold replay.
3. **Selection:** official loader resolves chosen IDs and tools; hashes check raw records. Initial formatted prompts are counted for all conditions. Synthetic author-reference execution checks test the selected simulation cases before model loading.
4. **Prompt wrapper:** `scripts/policy_runner.py` deep-copies history before inserting an instruction. Vanilla returns the original formatter behavior. Tool definitions and reference answers are not changed. Handler config/tokenizer loading is pinned to the server revision. The context guard preserves 4096 answer tokens and rejects oversize histories.
5. **Server:** one vLLM process group serves the 4B model on a free localhost port. BFCL uses `--skip-server-setup`; the notebook owns startup/readiness and shutdown. One request/sequence and no CPU offload limit memory use. A CLI exit code of zero is insufficient: records are checked for saved inference exceptions.
6. **Generation:** condition directories isolate predictions and scores. Each model record holds per-turn/per-step outputs and token counts. Force termination can occur after tool loops and remains a legitimate task failure.
7. **Evaluation:** official partial evaluation checks selected task trajectories. `analyze_run.py` checks archive hashes, IDs, score counts and incomplete status before exporting actual task CSVs and plots. The separately attributed scorer measures attempted state changes, a different target.
8. **Preservation:** fresh run IDs prevent overwrite. Status, source/script/config, logs and outputs are hashed into a ZIP. Exceptions stop execution and export diagnostics.

## Student explanation checklist (student must review)

- Explain why 0/6 task success does not mean the model produced no correct individual calls.
- Explain the difference between choosing a tool, supplying arguments, and attaining final state.
- Explain why same-family variants are correlated and why the current secondary percentages are not proof of improvement.
- Trace one genuine `cd` or `cp` failure from prompt through call and response to the score.
- Explain why increasing context corrected a serving-budget error without changing a failed task into a success.
- Explain why synthetic reference controls are not model predictions and why `pwd()` can pass state scoring but fail strict no-call.

Understanding is not certified by the assistant. Read the supplied code and rehearse these explanations before submission.
