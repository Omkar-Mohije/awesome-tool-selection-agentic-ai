# Five-minute demonstration and viva preparation

**0:00–0:45 — Question.** Explain the connection to the review: selecting/attempting an appropriate tool is distinct from attaining the final state. State the three prompt conditions and modest sample.

**0:45–1:45 — Working code.** Open the Colab notebook and frozen config. Show the venv and pins, one-server profile, six IDs, prompt wrapper and context guard. Explain why the kernel and subprocess interpreter differ and why one sequence/no offload fit the T4.

**1:45–2:45 — Genuine outputs.** Show the development archive and the separately frozen ATR-P07-v1 archive, their manifests, and representative trajectories. The development pilot had 0/6 task successes in each condition. The prospective run had 0/6 vanilla, 1/6 generic control, and 0/6 schema evidence; trace `multi_turn_miss_func_73` for the single generic-control success. Do not conflate the two runs.

**2:45–3:45 — Deeper analysis.** For development, show 13 state mismatches, four response mismatches, one force termination, and descriptive scorer values on two pairs. For prospective P07, explain that all 17 failed records were first labeled state mismatches and that published decision scores were identical across conditions on four eligible pairs; distinguish attempted-action metrics from full-task success.

**3:45–4:30 — Validation.** Show CPU reference and injected-read dispatch controls. Reference actions were deliberately supplied; these checks are not 6/6 model accuracy. The standalone no-call checker is not called by the official multi-turn dispatch.

**4:30–5:00 — Limits and reproducibility.** Explain fixed order, unmatched instruction lengths, two correlated prospective families limited to vehicle control, recovery provenance, and the unverified cold replay/second-student rerun. Show the validated archive, reproduction checklist, and AI-use report.

Suggested CPU rerun: `python scripts/analyze_run.py --archive runs/20261029T122816Z-5e29a2e6/P06_BFCL_Development_Pilot_Recovery_Outputs.zip --output results/demo` from `submission/`. The source archive is already in the repository; no GPU needed for this demonstration. Plotting needs matplotlib.

Viva questions to rehearse: Why is the checklist not a new algorithm? Why is 75% not proven improvement? What is the experimental unit? What does the scorer ignore? Why preserve failed runs? How does the answer-budget guard work? What does pinning reproduce and what remains stochastic? What work did you personally perform and verify?
