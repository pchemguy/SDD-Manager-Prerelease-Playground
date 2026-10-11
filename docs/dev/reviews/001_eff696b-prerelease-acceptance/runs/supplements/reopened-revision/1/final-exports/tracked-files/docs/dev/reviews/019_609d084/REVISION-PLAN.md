# Development-document QC implementation plan

## Campaign and accepted inputs

Campaign `019_609d084`; baseline `609d08495fd28022eea133e560c7bd3842412585`.
Working branch `revision/019_609d084-dev-docs-qc`; target `feature/architecture-revision`.
The human requests a new revision implementing Campaign 011 QC. Authoritative preparation: [QC policy](../011_a3b2ad9/QC-POLICY.md), [assessment](../011_a3b2ad9/REVIEW-REPORT.md), and [source plan](../011_a3b2ad9/REVISION-PLAN.md). Retain these historical records and implement their R-001–R-003 actions in this new campaign.

## Ordered work and checks

| Action | Outcome | Acceptance |
| --- | --- | --- |
| V-001 | Canonical conventions, SPEC/PLAN/TASKS owner protocols and adjacent report format (011 V-001–V-005). | Design→SPEC→PLAN→TASKS conformance gates; semantic decomposition with diagnostic delivery counts; scoped corrections, appended rechecks and precise readiness. |
| V-002 | Coordinator and direct-entry readiness, projection, feature/archive and steering handoffs; README/capability alignment (011 V-006). | Current evidence gates dependent operations; no silent upstream changes, new administrative tasks, or scope expansion; preserve push-first and read-only behavior. |
| V-003 | TextStats assessor contracts/procedures and bounded local consumer checks (011 V-007). | Count exceptions/overload/in-range scope, omissions/drift, revision history and invalidation, scoped feature/archive represented. Catalog/support checks pass. |
| V-004 | Composition review, verified commits/pushes, explicit target integration and publication (011 V-008). | All changed links/skills checked, actual validation evidence and limitations reported, owned diff integrated with two parents. |

Persist source/report checkpoints before dependent work. Use focused local fixture assessments with the revised source where facilities permit; these do not constitute dedicated repository live acceptance or installed-client tests. Preserve unrelated pending paths. Do not implement Gemini integration or publish a release. Live/client acceptance remains a separate pending follow-up. Stop after this revision is verified and published.
