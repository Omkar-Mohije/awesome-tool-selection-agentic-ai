# P06 — Annotation Rubric (PROPOSED; NOT EXECUTED)
## Unit and provenance
One `source_query_id × inventory_version` case; store parent family ID, exact source file/commit SHA, original query, immutable tool IDs, full available tool metadata, proposed modification and annotator identity. Counterfactuals inherit parent group and must remain in same data partition.

## Decision ontology
- **SELECT:** User states all mandatory information needed for a justified available-tool choice, and one or more available tools demonstrably meet mandatory requirements. Record full valid-tool ID set; select is correct if returned ID belongs to this set.
- **NO_VALID_TOOL:** Tool documentation/schema and inventory scope provide positive evidence that *none* supports mandatory capability or constraints. Mere missing documentation does not establish non-support.
- **NEEDS_CLARIFICATION:** One or more plausible available tools could satisfy the task, but a specific missing user detail determines which operation/tool or parameters should be selected; construct a targeted clarification question and list disambiguating information. Multiple valid tools alone do NOT imply clarification.
- **MULTI_VALID:** Boolean property of SELECT examples with >=2 independently supported suitable tools, not a fourth action.
- **INSUFFICIENT_EVIDENCE:** Neither documented support nor documented incompatibility resolves suitability; abstain from assigning a scored action and request additional source evidence.

## Evidence rubric
For each mandatory requirement: transcribe the exact request text, map to an operation or argument, identify document/schema excerpt and source path, assign `supported`, `contradicted`, `not_documented`, or `depends_on_missing_input`. Mandatory vs optional conditions are separately recorded. Document a tool's output type, input constraints, scope, and any absence of executable specification. External assumptions cannot silently become source facts.

## Counterfactual construction
A. **Capability-removal pair:** remove an existing valid tool from inventory (do not change actual API behavior or asserted capability); ensure remaining tools are independently ruled out before labeling NO_VALID_TOOL.  
B. **Specification-removal pair:** remove precisely one essential user condition (not all context); establish that differing answers genuinely follow from this missing condition and at least two plausible options exist.  
C. **SELECT reference:** retain sufficient request and a documented valid tool; record all alternatives.  
No semantic-only claim of equivalence. No automatic label updates without adjudication. Include paired integrity checks and counterexamples that must *not* flip class.

## Independent review and adjudication
Two independent annotators first label without model predictions, score, or the other's decision. On mismatch, collect evidence and obtain third-person adjudication where available; unresolved cases excluded from primary evaluation. Measure raw label agreement and Cohen's kappa for decision labels when valid; for valid-tool sets report per-case set Jaccard and disagreements. Report sample coverage, missing-evidence rate, rejected items, provenance and time per case. Avoid model-generated ground truth; AI suggestions may only flag candidates for human scrutiny. No human annotation has been completed.

## Proposed table columns
`case_id | family_id | source_repo | source_sha | source_path | query | inventory_hash | tool_ids | mandatory_requirements | tool_capability_evidence | input_slots | valid_tool_ids | multi_valid | decision_label | missing_specification | counterfactual_parent | counterfactual_operation | annotator_id | annotation_time | confidence | disagreement_reason | adjudicated_label | exclusion_reason | split`.

## Quality gates (not yet met)
Check 30–50 genuine families; class existence and separability; ID mapping; blinded independent agreement; confidence and exclusion distributions; meaningful paired transitions. If no-valid negatives cannot be proven, do not force ontology. Proposed examples are not official data and none are represented here as collected labels.
