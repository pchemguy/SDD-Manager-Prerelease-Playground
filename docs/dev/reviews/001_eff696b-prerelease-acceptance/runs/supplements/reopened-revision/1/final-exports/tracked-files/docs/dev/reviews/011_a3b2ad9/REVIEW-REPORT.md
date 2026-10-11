# Development document QC baseline assessment

Campaign: `011_a3b2ad9`. Starting/reviewed baseline: `a3b2ad9bdbe68d42c32cdcdf0bd80fc2a598dad9`.
Reviewer/date: Codex, 2026-10-04. Working branch: `revision/011_a3b2ad9-dev-docs-qc`; target: `feature/architecture-revision`.
Scope: prompt-defined SPEC/design, PLAN/SPEC and TASKS/PLAN conformance, decomposition quality and report/correction gates. Evidence: static instruction inspection; no consumer execution or source repairs.

## Assessment and coverage

Current owners already define many useful review criteria, but they do not consistently make completed document QC a required preparation gate, persist adjacent reports or append correction/recheck sections. The proposed [QC policy](QC-POLICY.md) retains existing meaningful incremental delivery and avoids numeric quotas.

| Area | Inspected source | Observation / finding |
| --- | --- | --- |
| SPEC / design alignment | sdd-specify SKILL; system-specification.md Design traceability / Acceptance and review; review.md | Existing bidirectional design traceability and contract checks. Missing required persisted review/correction gate before PLAN. R-001. |
| PLAN / SPEC alignment | sdd-plan review.md; delivery-plan.md | Existing contract delivery-route, meaningful MVP, incremental growth and exit checks. No count triggers or mandatory adjacent review/recheck report before TASKS. R-001, R-002. |
| TASKS / PLAN alignment | sdd-tasks SKILL; task-derivation.md; progress-review.md | Accepted input ownership, coherent work units, exit coverage and review tasks exist. Progress review mainly assesses completion evidence; explicit post-generation conformance/decomposition gate absent. R-001, R-002. |
| Shared quality criteria | sdd-conventions modularity.md; design-heuristics.md; task-hierarchy.md; backend-object-lifecycle.md | Cohesion, purposeful splitting and meaningful increments already defined. New count heuristics must exclude administrative review units and remain diagnostic. R-002. |
| Report and correction handoffs | sdd-manage workflows.md; sdd-report campaign-artifacts.md / completion-reports.md | General campaigns and implementation reports exist; dedicated adjacent document QC reports and appended revision cycles are not defined. R-003. |

## Findings

### R-001 — Conformance review is not a consistent preparation gate

Status: Open. Priority: high for this proposed policy. Existing specification/plan reviews can assess conformance, but authoring/routing does not require a retained successful review before dependent generation. Task review lacks a dedicated post-generation plan-conformance protocol distinct from progress assessment.

Correction: define mandatory SPEC→design, PLAN→SPEC and TASKS→PLAN gates with scoped corrections/rechecks, current source identity and dependency invalidation. Preserve read-only review and accepted governing-owner boundaries. Recheck: a missing contract, unexplained plan omission or task strategy drift blocks the correct downstream stage until corrected and rechecked; prior current equivalent evidence may be reused.

### R-002 — Decomposition has semantic guidance without explicit shape diagnostics

Status: Open. Priority: medium. Current modularity and delivery guidance addresses scope and cohesion, but gives no requested 3–5 heuristic or 1–2 / 10+ review triggers. Conversely, applying raw counts after campaign 010 would count mandatory review units and distort planning.

Correction: count delivery milestones/tasks separately; assess numerical triggers against actual capability/dependency breadth and checkpoint overhead. Recheck: justified small phase passes without padding; fragmented tiny phases and oversized in-range units are challenged; 10+ groups get explicit overload/drift review; excluded review units remain mandatory.

### R-003 — Adjacent QC reports and retained correction cycles are absent

Status: Open. Priority: medium. Current report formats cover campaigns and implementation status, not SPEC-REVIEW-REPORT / PLAN-REVIEW-REPORT / TASKS-REVIEW-REPORT beside reviewed roots. No defined append-only revision/recheck sections or stage readiness handoff.

Correction: define concise root reports covering children, stable findings, appended correction sections, current readiness and persistence/continuation. Recheck: corrections preserve original observations, current identity and objective evidence; a report-only draft or stale upstream source cannot imply a passed gate. Selected feature archive keeps reports beside their sources without conflating historical and current main-document readiness.

## Handoff and limits

Three source-policy gaps identified. Existing semantic criteria are foundations, not evidence that automatic gates already run. No runtime failure is claimed. Source revision, fresh consumer checks and acceptance-case updates remain planned in [REVISION-PLAN.md](REVISION-PLAN.md). Preparation report scope does not authorize unrelated code implementation or a project-wide audit.

## Policy record integration — 2026-10-04

The human commanded merging the policy revision. Published revision tip `8e25b52acbb77eb7ebbbc69e32e433130cc7b0d0` was explicitly integrated into `feature/architecture-revision` as two-parent merge `606f6eea7a0a21b49f9300ecf40c7e5b202db644`; target parent `a3b2ad9bdbe68d42c32cdcdf0bd80fc2a598dad9`. Prospective checks validated four documents, 37 local links, full campaign baselines, no whitespace errors and no conflicts. The diff contains policy/assessment/plan/index records only; skills and acceptance are unchanged. Target push succeeded and exact remote readback matched the merge SHA. This publishes the preparation records; source revision actions V-001–V-008 remain planned.

## Source implementation follow-up — campaign 019

The human requested a new revision implementing this policy. [Campaign 019 implementation report](../019_609d084/REVISION-REPORT.md) records the source changes, verification and publication. R-001–R-003 are resolved in that source revision; this campaign's original proposal, baseline findings and preparation-only history remain retained. Dedicated live/client acceptance remains separate and pending.
