# P10: baseline validation and discrepancies

| Item | Status | Evidence / interpretation |
|---|---|---|
| Official source and model-handler path | VERIFIED | Pinned Gorilla; original Qwen formatting/decoding and task scorer |
| Real model inference and partial scoring | VERIFIED | Smoke 3 records; comparative pilot 18 condition/task records; raw ZIPs preserved |
| Output/archive integrity | VERIFIED | 203 recovery hashes and 62 nested source hashes; 11 reused records unchanged |
| Scorer accepts author references | VERIFIED for tested cases | Six development reference cases in two layouts; six new selected reference cases; no reference execution exceptions |
| Negative controls | VERIFIED for synthetic controls | Empty actions rejected; standalone irrelevance rejects inserted calls |
| Production no-call enforcement | NEEDS CORRECTION in interpretation | Pinned multi-turn evaluation function omits invocation of the standalone irrelevance checker; synthetic dispatch demonstrates the distinction |
| Exact published accuracy replication | NOT CLAIMED | Tiny selected subset, different model/serving profile and mixed development recovery provenance; official full-benchmark numbers are not comparable |
| Two learning-method baselines | NOT PRESENT | We compare prompt conditions within one model. This is a small descriptive design with two executable prompt controls |
| Calibrated three-way labels/policy | NOT PRESENT | No semantic oracle or independent clarification-quality scoring |
| Stable environment for fresh run | PREPARED / TEST REQUIRED | Source, versions and revision pinned; new notebook not yet GPU-executed |
| Fresh prospective results | PENDING | Protocol frozen before new results; do not merge pilot outcomes into its table |

The official full-task score is trusted only for its documented state/response/termination target. For development records, original 12K-valid trajectories and new 24K recovery trajectories were combined with provenance; this is acceptable for exploratory debugging but not a uniform-run benchmark comparison. Only 0/6 per-condition sample outcomes are reported.

Additional required check is the actual prospective Colab run and archive validation. Repeat the exact config as recorded; preserve any runtime exception and distinguish it from model task failures. Additional runs are not required merely to produce a positive outcome. Do not compare the pilot's 0% to an official leaderboard percentage as numerical replication failure.
