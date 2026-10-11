# Comprehensive plugin review plan

## Campaign and scope

- Campaign: `008_98a5562`; starting and reviewed source: `98a556218d81870a4751ad308f6586587ac1d7da`.
- Requested: comprehensive review of the complete plugin, all 15 skills/references, metadata, navigation, and cross-skill protocols.
- Date: 2026-10-02. Review artifacts are written on the existing `feature/architecture-revision`; source repairs, branch migration, hosted mutations and client installation are excluded.
- Evidence: static source/contract assessment and offline packaging/navigation checks; synthetic local checks where useful. No live credentials are read. No installed-client behavior is claimed.
- Report: [REVIEW-REPORT.md](REVIEW-REPORT.md).
- State: Completed; all 18 units assessed and retained in the report.

## Criteria

- C-001: portable packaging, discovery, metadata, contained resources and navigation.
- C-002: scoped authorization, Git eligibility, preservation, authentication and publication.
- C-003: artifact ownership, dependency/authority consistency and progressive disclosure.
- C-004: robust design/SPEC separation, practical MVP/increments and task hierarchy.
- C-005: acceptance, test quality, documentation and truthful completion evidence.
- C-006: recovery, failure handling, phase transitions, feature archives and human stop boundaries.

## Review order

| Unit | Owner / resources | Dependencies | Criteria / checks |
| --- | --- | --- | --- |
| U-001 | Packaging: manifest, inventory, presentation and navigation; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-002 | sdd-orient: read-only authority and recovery handoff; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-003 | sdd-conventions: design, hierarchy, tokens and workflow identity; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-004 | sdd-report: formats, evidence and campaign templates; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-005 | sdd-design: exploration, architecture and decomposition; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-006 | sdd-specify: behavioral contracts and scoped deltas; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-007 | sdd-plan: MVP delivery strategy and physical layout; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-008 | sdd-tasks: task derivation and progress review; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-009 | sdd-tdd: strategy, test-first cycle and test quality; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-010 | sdd-docs: in-code and standalone documentation; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-011 | sdd-verify: selection, execution, evidence and failure routing; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-012 | sdd-integrate-feature: document/task reconciliation and archive; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-013 | sdd-forge: GitHub projection, authentication and lifecycle; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-014 | sdd-implement: startup, ranges, execution and completion; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-015 | sdd-steer: human-directed amendment and stop; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-016 | sdd-manage: routing, branches, credentials and Git boundaries; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-017 | Composition: cross-skill positive/negative scenario assessment; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |
| U-018 | Consolidation: full coverage, findings, readiness and revision queue; all applicable local references | Foundations before document owners, then execution/coordinator; composition after all owners | C-001–C-006 as applicable; source positive/negative cases and tooling evidence |

## Scenarios

Assess missing/non-Git/conflicted state; dirty completion and invalidated checkboxes; missing optional report/backend; partial and cross-phase selection; failed exits/publication; test-first exceptions and uncovered acceptance; governing-document conflicts; partial/complete/interrupted feature incorporation; uncertain hosted writes and credential failures; steering stop; explicit merge and verification failures. Distinguish source interpretation from actually executed checks.

## Persistence and stopping

After every unit, update the canonical report, commit and push, then verify remote HEAD equality before dependent review. Findings use stable `R-001` IDs with priority (P1 serious blocker, P2 material defect, P3 recommendation), type, confidence, baseline location, impact, bounded correction and objective recheck. Preserve no-finding coverage. Subsequent checkpoint records identify the preceding verified commit to avoid self-referential SHA fields. Finish with counts, readiness and proposed revision queue; stop before source revision.
