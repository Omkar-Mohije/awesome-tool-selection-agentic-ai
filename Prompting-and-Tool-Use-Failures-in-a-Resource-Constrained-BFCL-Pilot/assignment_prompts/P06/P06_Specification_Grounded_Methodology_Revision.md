# P06 Methodology Revision — Specification-grounded validation (29 Oct 2026)

## Status
**CONDITIONAL GO for a schema-grounded pilot, NOT a frozen research protocol, benchmark result, or publication novelty claim.** This document supersedes the *proposed* two-independent-human-annotator requirement as the **primary labeling strategy**; it does not claim human review has occurred.

## New verification that materially affects novelty
- Official Berkeley Function Calling Leaderboard (BFCL) V3 benchmark explicitly includes **Missing Parameters** and **Missing Functions** categories, with 200 examples each, plus relevance/irrelevance categories. Primary benchmark documentation: https://github.com/gorilla-llm/Berkeley-Function-Calling-Leaderboard and https://gorilla.cs.berkeley.edu/leaderboard (verify exact release/commit and scoring details in implementation before use).
- BFCL's **Missing Parameters** requires recognizing information necessary to complete a function call; **Missing Functions** withholds functions necessary for an intended action. These are **direct prior art** for the two states formerly regarded as our distinctive benchmark design. The mere existence of these cases, or a deterministic checker for them, **is not a novel contribution**.
- Earlier prior-art risks remain: SAGE-Agent for clarification, AgentAbstain for abstention, ToolEX for multi-valid tools, Tool-REX/MFTR for richer capability evidence, and calibrated tool action models.

## Revised scientific question (provisional)
**Can explicit, schema-grounded evidence about required arguments and available functions reduce *cause-confusion* between missing-capability and missing-specification states, beyond strong calibrated and task-compatible tool-calling baselines, under matched inventory and request perturbations?**

Alternative *measurement-first* contribution: **How often do retrieval confidence and model-reported uncertainty misidentify the cause of an unsafe tool call, and how stable are those errors under controlled one-factor perturbations?**

Either contribution must be contrasted directly with BFCL's published missing-function/missing-parameter protocol and close contemporary papers; no novelty claim until differences are demonstrated.

## Methodology choices
1. **Primary empirical anchor**: evaluate BFCL V3 Missing Function / Missing Parameter cases and their original ground truth if accessible and license-compatible. Treat BFCL as prior art and an external anchor, not as our newly introduced dataset. Verify case semantics and release version by parsing actual data. ToolRet can be an optional retrieval-specific comparator; MetaTool can remain background and a retrieval domain, but **brief plugin descriptions do not support proof of missing capabilities**.
2. **Deterministic evaluation**: use executable schemas, required fields, supported operations and a predeclared *typed request representation* to determine suitability. A schema validator can check whether structured fields meet a schema. It **cannot infer from arbitrary natural-language text** whether the user truly supplied/omitted a requirement; that mapping needs source-provided labels, explicit controlled templates, or careful audited annotation.
3. **Three decisions**: SELECT, NO_VALID_TOOL and NEEDS_CLARIFICATION remain a proposed evaluation abstraction. In BFCL these may be evaluated at a *tool-call action* level, not pure retrieval. Report task differences; do not conflate BFCL multi-turn execution with a retriever score.
4. **Validity guardrails**: missing documentation ≠ unsupported; required schema argument ≠ always necessary to ask (may be inferable from context/defaults); multiple valid tools ≠ clarification; no-valid tool state requires full defined candidate inventory.
5. **Counterfactual protocol**: modify exactly one explicit field: remove eligible function vs remove necessary user slot, with source-backed and verifiable expected action. Keep whole query family in the same split; avoid generator-label leakage and overlap with BFCL public evaluation answers.
6. **Evaluation**: compare a forced-call diagnostic, a calibrated three-class baseline, task-compatible existing tool-calling model/policy, and a minimal transparent schema-evidence policy. Evaluate confusion matrix and pairwise transitions, selective risk, false tool selection, inappropriate clarification, latency and calibration. Predefine splitting and costs.
7. **No second human annotation required for the primary rule-defined cases** if ground truth is generated from verifiable rules with independently tested validators. **Do not claim independent human validation**. Add a manual spot audit if possible; failure to review natural-language-to-schema mapping must be transparently reported as a limitation.
8. **External validity**: controlled synthetic/rule-derived cases alone do not prove robustness to unconstrained natural requests. Validate on authentic BFCL cases, hold out tool families and prompt templates, and disclose limitations.
9. **Licensing**: review actual BFCL dataset-specific terms and MetaTool/plugin provenance before redistributing anything. Refer to upstream paths/checksums instead of republishing their complete data where rights are uncertain.

## Updated gates before Prompt 07
- G1: Fetch a pinned BFCL release and inspect actual missing-function/missing-parameter case files, reference labels and official evaluation code.
- G2: Implement a minimal schema/constraint oracle with explicit, independently checkable unit tests; evaluate its own coverage and failure cases.
- G3: Determine which authentic benchmark records support exact three-way action labels, and where clarification vs withholding means distinct semantics.
- G4: Build a small matched-pair pilot using mechanically controlled changes; preserve origin IDs, versions and all rejected cases.
- G5: Implement and run two task-compatible baseline policies; verify environment, weights/licenses, calibration splits and evidence.
- G6: Revisit full-paper novelty overlap with BFCL V3/V4, SAGE-Agent, calibration and no-tool research. Stop/redesign if proposed contribution remains only benchmark reformatting.

## Historical preservation
Previous P05 research question and P06 human-annotation proposal remain historical, not erased. The user approved exploring a no-second-reviewer specification-grounded alternative on 29 Oct 2026; **no empirical result or frozen protocol is approved yet**.

## Authentic evidence status
**VERIFIED from official published benchmark documentation:** BFCL covers missing parameters/functions as categories. **INFERRED:** schema-grounded tests may reduce subjective labels and permit a reproducible diagnostic. **UNKNOWN:** exact available compatible data, tool permissions, oracle correctness, baseline performance, and novelty of a calibrated cause-aware policy. No new BFCL run or annotation was performed in this action.
