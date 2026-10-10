# Comprehensive review plan

## Scope and identity

- Campaign: `017_54d55ed`.
- Exact reviewed baseline: `54d55edebd8a7af6499d625bdbb357f864a4db1d`.
- Working branch: `revision/017_54d55ed-comprehensive-review`.
- Established integration target: `feature/architecture-revision`; remote main currently shares the baseline.
- Objective: comprehensive source, packaging, workflow, documentation and TextStats support review after the lifecycle and presentation revisions.
- Authorization: review artifacts and their routine commit/push/verified integration under the coordinator policy; no source repairs. Preserve unrelated untracked work.

## Review units and criteria

| Unit | Scope | Criteria and scenarios | Dependencies |
| --- | --- | --- | --- |
| U-001 | Package, all 15 entry points/presentation assets, current README and capability map | Valid Codex manifest, contained/discoverable resources, truthful metadata, task ownership and claims. Compare installed source identity; distinguish rendering from structural checks. | Baseline |
| U-002 | Design, SPEC, PLAN/layout, TASKS, shared decomposition conventions and document QC | Full intent vs feature deltas, minimally meaningful increments, dependencies, conformance, review units and explicit scope. Inspect campaign 011 as pending policy, not implemented source. | U-001 |
| U-003 | Coordinator, implementation, feature incorporation, steering, verification, reporting, GitHub lifecycle and credentials | Phase gating, report-before-close ordering, milestone/phase transitions, bounded authorization, read-only ownership, interruption/uncertain-write recovery and stop boundaries. Trace bootstrap, partial range, full phase, feature and steering cases on both sides of handoffs. | U-001/U-002 |
| U-004 | TextStats setup/procedures, catalog/assessor contracts, helper code/tests and composed regressions | Both manifest layouts, exact source pinning, binary assets, controlled/uncontrolled recovery, independent evidence, no secrets or scope escapes. Execute support tests/catalog and focused counterexamples; assess coverage limits. | U-001–U-003 |

## Evidence and checkpoints

Inspect every shipped skill entry and reference, metadata and asset paths; assess meaning as well as local links. Read helper implementation and representative negative tests; run the full stdlib support suite and catalog validator. Findings need stable IDs, baseline path/section, consequence, confidence, bounded correction and objective recheck. Retain observed no-finding coverage and unresolved evidence gaps. After each unit, commit/push the report and relevant evidence before proceeding to dependent units.

Fresh consumer/assessor agents are not supplied for this review. Semantic scenario traces are this reviewer's source analysis, not fresh-client executions. No dedicated live acceptance repository was supplied: do not reuse historical destinations or certify new live GitHub/client behavior. External lookups are limited to official documentation when needed for format/provider facts. No proposed correction is implemented by this review.

## Completion

Consolidate actionable findings, known pending revisions and verification limits. Propose a bounded correction queue without marking it accepted or implemented. Verify the review-only branch difference, explicitly merge and verify records, publish the established target and stop.
