# Backend lifecycle baseline assessment

## Campaign and assessment

- Campaign: `010_3f56922`; starting/reviewed baseline: `3f56922a936c8fe039f906ed27566b5662b5440c`.
- Reviewer/date: Codex, 2026-10-04.
- Working branch: `revision/010_3f56922-backend-lifecycle`; established target: `feature/architecture-revision`.
- Scope: prompt-defined phase object creation, task and milestone closure, milestone/phase review and reports, explicit review tasks, interruption recovery and skill responsibilities.
- Evidence: static inspection of shipped instructions and TextStats acceptance criteria. No provider mutations or lifecycle execution trials performed.
- Assessment: task issue closure is implemented; the additional requested lifecycle is only partly covered. The [policy proposal](LIFECYCLE-POLICY.md) states the intended behavior; the [revision plan](REVISION-PLAN.md) identifies dependent changes. The baseline observations below are retained; subsequent source changes and consumer checks are recorded in [REVISION-REPORT.md](REVISION-REPORT.md).

## Coverage

| Concern | Baseline evidence | Assessment / finding |
| --- | --- | --- |
| Object mapping, identity and write recovery | `skills/sdd-forge/references/github.md`, `github-projection.md`; `skills/sdd-conventions/references/task-hierarchy.md` | Existing phase label / native milestone / task issue mapping, exact IDs, reuse, foreign-field protection and uncertain-write readback are useful foundations. R-001 concerns timing, not absence of projection. |
| Task closure and durability | `skills/sdd-forge/references/github-issue-lifecycle.md`; `skills/sdd-implement/references/completion-and-checkpoints.md` | Implemented: verify, reconcile owning task, commit, push/readback, close issue with evidence; offline closure remains pending. Preserve this protocol. |
| Parent completion / phase integration | `skills/sdd-implement/references/completion-and-checkpoints.md`; `skills/sdd-manage/references/workflows.md`, `branch-management.md` | Local exits and full-phase integration defined; hosted milestone closure and phase activation dependences absent. R-001, R-003. |
| PLAN / TASKS hierarchy | `skills/sdd-plan/SKILL.md`; `skills/sdd-tasks/references/task-derivation.md`; shared task hierarchy | Meaningful milestones and exit work exist, but no mandatory review task or final single-task phase review milestone. R-002. |
| Review, verification and ownership | `skills/sdd-manage/references/review-and-revision.md`; `skills/sdd-verify/SKILL.md`; `skills/sdd-implement/SKILL.md` | Campaign reviews and check execution exist; boundary code-review gate and explicit review owner need articulation. R-004. There is no sdd-review skill. |
| Boundary reports and TODO propagation | `skills/sdd-report/references/completion-reports.md`, `campaign-artifacts.md` | Current reports summarize capability/exits/evidence; no mandatory committed review report or deferred finding aggregation protocol. R-004. |
| Continuation | `skills/sdd-implement/references/startup-and-continuation.md`; GitHub failure protocols | Task/Git continuation and issue backlog reconciliation implemented; new milestone/report/phase transitions need corresponding recovery rules. R-003. |
| Acceptance | `acceptance/textstats/OBJECTIVES.md`; assessor A-003, A-005 and A-006 | Existing projection, bounded milestone, phase integration checks do not prove the proposed lifecycle. Extend scenarios and interruption assessments. R-005. |

## Finding records

### R-001 — Projection is not gated by phase activation

Priority: high for the requested policy. Status: Revised; source changes and local/consumer rechecks recorded in REVISION-REPORT.md; hosted execution remains pending.

`github-projection.md` reads the complete TASKS and active FEATURE-TASKS and creates requested projection objects without requiring prior-phase completion or restricting creation to the eligible phase. `task-hierarchy.md` describes complete-list hosted mapping. A caller can therefore project future-phase objects before the proposed activation gate.

Correction: separate complete local planning from eligible-phase projection; coordinator checks predecessor integration/publication and authorized range, backend creates/readbacks every object of the eligible phase before execution. Preserve first-phase bootstrap, stable identity and lookup-before-create. Recheck: future-phase objects remain absent during first-phase execution; partial projection resumes without duplication; next phase activates only after confirmed predecessor gates.

### R-002 — Mandatory review units are not generated

Priority: high for the requested policy. Status: Revised; source changes and local/consumer rechecks recorded in REVISION-REPORT.md; hosted execution remains pending.

`task-derivation.md` includes milestone-exit work but never requires a last milestone review/report task or final one-task phase review milestone. Shared hierarchy and PLAN ownership do not establish this structure. Existing lists can exhaust delivery tasks without an executable review/report boundary.

Correction: PLAN reserves review milestones/exits; conventions specify structure; TASKS derives dedicated task IDs and dependencies without changing accepted IDs. Recheck: multi-milestone, single-delivery-milestone and feature-delta hierarchies contain the correct explicit review units, and next-N selection counts them.

### R-003 — Hosted milestone closure has no execution owner/procedure

Priority: high for the requested policy. Status: Revised; source changes and local/consumer rechecks recorded in REVISION-REPORT.md; hosted execution remains pending.

GitHub routing offers projection and issue lifecycle only. `completion-and-checkpoints.md` updates verified local parents but does not close hosted milestones after their issues close. Existing continuation reconciles task issues without a milestone closure backlog. A locally completed milestone may remain open indefinitely; new activation gates would have no reliable closure evidence.

Correction: forge defines milestone lookup, all-issue/exit/report preconditions, closure/readback and authorized reopening; implement coordinates this after review task issue closure; manage gates next phase. Recheck: closure ordering, foreign/open-issue blockers, local-only execution and uncertain closure/readback recovery all have explicit consumer evidence.

### R-004 — Review reports, deferral rules and owner handoffs are incomplete

Priority: high for the requested policy. Status: Revised; source changes and local/consumer rechecks recorded in REVISION-REPORT.md; hosted execution remains pending.

`completion-reports.md` asks for delivered capability, aggregate verification, exits and unresolved defects, but does not require a dedicated code review, report commit before closure, admissible non-critical deferral with solution options, or final TODO aggregation. Verify currently selects/runs checks and returns evidence; manage routes focused reviews, but no existing skill explicitly owns milestone/phase implementation code review.

Correction: adopt the proposed read-only review remit for verify; retain repair/status/persistence with implement, presentation with report and transitions with manage. Define committed milestone/phase/final reports and TODO provenance. Recheck: a critical finding or failed required check blocks closure; admissible deferrals carry options into the final report; completed tests without code review cannot complete a review task.

### R-005 — Acceptance lacks the new lifecycle checks

Priority: medium, required before claiming the revised policy works. Status: Revised acceptance criteria; live lifecycle execution remains pending.

TextStats assessor A-003 checks mapping/reuse, A-005 checks milestone capability/persistence and pause, A-006 checks phase exits/integration. None explicitly requires phase-gated object creation, milestone closure, generated review tasks or committed review reports/TODO aggregation. Historical campaign results and harness support tests do not establish these new behaviors.

Correction: revise affected consumer/assessor inputs, criteria and catalog dependencies coherently; add controlled/uncontrolled interruption points at activation, report persistence, issue/milestone closure and phase integration. Recheck against a new pinned plugin source on a dedicated test repository, with provider readback where hosted transitions are claimed.

## Handoff and limits

At the baseline checkpoint, five gaps were open and no shipped source repairs had been made. The later authorized revision addresses their source/criteria changes; see REVISION-REPORT.md for actual disposition and execution limits. These are gaps against the user's proposed policy, not retrospective claims that earlier task issue closure failed. Task completion/push/issue closure and uncertain-write recovery should be retained rather than replaced.

The phase-review ordering interpretation and ownership proposal are explicit in LIFECYCLE-POLICY.md. Current assessment inspected the listed handoffs; it is not an exhaustive unrelated plugin audit or an executed provider test. Provider execution and actual controlled/uncontrolled lifecycle trials remain unexecuted; local and fresh-consumer rechecks are recorded separately.
