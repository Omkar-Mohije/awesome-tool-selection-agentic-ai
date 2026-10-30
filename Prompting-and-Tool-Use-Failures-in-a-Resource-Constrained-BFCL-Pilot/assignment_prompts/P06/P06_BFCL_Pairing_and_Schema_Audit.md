# PRE-P07 — BFCL pairing, state and schema audit

**Pinned upstream commit:** `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`. Source paths and blob hashes are in `P06_BFCL_Ground_Truth_Validation.md`.

## Source-derived pairing
200 numeric case indices occur across base, miss_func and miss_param. Initial configurations serialize identically in **190** triads. The ten differences below were established by recursive comparison of decoded JSON values, not inferred from filenames.

| Family index | Changed initial state relative to base | Handling |
|---|---|---|
| 0 | miss_param adds `GorillaFileSystem/root/workspace/contents/document/contents/report_final.pdf` | Hold out from strict matched-pair analysis until state dependence is justified |
| 38 | miss_param adds `BackupResearch` and `OldResearch` directories beneath researcher | Hold out |
| 76 | miss_param edits `TwitterAPI/tweets/4/content` and omits `mentions` | Hold out |
| 139 | miss_func removes `TradingBot/watch_list/1` (`ZETA`) | Hold out |
| 145 | both altered variants change `TradingBot/transaction_history/0/timestamp` from 2024 to 2026 | Hold out |
| 154 | both variants change `TravelAPI/credit_card_list/card1/expiry` from 12/25 to 12/26 | Hold out |
| 176 | both variants substitute booking key `JFK-LAX-20261015` with `JFK-LAX-20261215` | Hold out |
| 188 | both variants change primary travel-card expiry from 12/25 to 12/26 | Hold out |
| 189 | both variants change travel-card `card_5678/expiry_date` from 12/26 to 12/23 | Hold out |
| 193 | both variants change travel-card `credit_9988/expiration_date` from 12/25 to 12/26 | Hold out |

An equal JSON configuration does **not** prove equivalent runtime state at an intervention turn; earlier actions and results influence later turns. The same-index relationship alone does not prove strict one-field intervention or identical relevant contexts. The 190 are *candidate* families for stricter review, not 190 validated causal triplets.

## Reference behavior and schema constraints
The source reference has an ordered list of user turn slots and ground-truth function calls per slot. `path` and `involved_classes` name expected functions/classes; `initial_config` gives executable world state. `missed_function` appears in missing-function cases and points to functions withheld in that scenario. Function argument signatures are implemented in source classes in `eval_checker/multi_turn_eval/func_source_code/`; their availability must be checked against the active tool list, not inferred from a label string.

**Mechanically checkable:** JSON structure, indexed IDs, turn counts, lists of allowed functions, declared parameter names/types and explicit required fields where available, function-existence in supplied inventory, reference no-call/call status, and matched JSON changes.

**Not mechanically inferred from a schema alone:** whether arbitrary natural language unambiguously supplies a parameter, whether an omitted value is recoverable from previous turns, appropriateness of an explanation/clarifying question, and whether alternate actions have equal task effects. These require author-supplied behavior, narrowly specified templates or additional evaluation.

## Required exclusion rules (not silently discarded)
Retain all ten in source provenance. Exclude them **only from strict same-state matched causal estimates** pending explicit initial-state reconciliation. They remain eligible for category-level BFCL replication following the original official protocol. Additional exclusions need recorded reasons, IDs and counts.
