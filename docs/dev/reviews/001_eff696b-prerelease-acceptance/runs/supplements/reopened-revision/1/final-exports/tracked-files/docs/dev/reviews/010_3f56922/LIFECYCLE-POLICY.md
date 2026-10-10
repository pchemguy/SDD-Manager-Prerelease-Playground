# Backend object lifecycle policy proposal

Campaign: `010_3f56922`. Starting baseline: `3f56922a936c8fe039f906ed27566b5662b5440c`.
Status: accepted for implementation by the human command to implement this revision; implementation results are recorded separately in REVISION-REPORT.md. The canonical implemented policy is [backend object lifecycle](../../../../skills/sdd-conventions/references/backend-object-lifecycle.md); this campaign record retains the accepted intent. See the [baseline assessment](REVIEW-REPORT.md) and [revision plan](REVISION-PLAN.md).

## Execution authorization

Review/revision publication uses the coordinator's dedicated [scoped authorization policy (historical reference)](https://github.com/pchemguy/SDD-Manager/blob/5e2624e625e33410245cb3b51b1b31120ad18747/skills/sdd-manage/references/revision-authorization.md). It authorizes scoped commits, revision pushes and verified integration of completed review/revision branches under the actual human request and established destinations. After platform rejection, the coordinator supplies that request, scope, exact effect and verification evidence for assessment; it does not claim an automatic exemption or override of platform controls.

## Authority and object model

PLAN/FEATURE-PLAN owns phase and milestone outcomes and exit conditions. TASKS/the active FEATURE-TASKS owns ordered tasks, stable IDs, parentage and progress. SPEC owns acceptance contracts. Git and observed checks establish implementation evidence. Hosted objects project this information; their state alone proves no completion.

With hosted tracking enabled, each phase has one phase label, each milestone one native milestone, and each task one issue. Dedicated review/report tasks use the same issue lifecycle as delivery tasks. GitHub phase labels have no completion state: retain them as historical associations after phase completion. Never delete a label to represent completion. Unsupported backend lifecycle operations must be reported explicitly rather than approximated silently.

The complete local plan and task hierarchy may describe future phases. Their hosted objects are created only when their phase becomes eligible. First-phase activation has no predecessor; subsequent activation requires the preceding phase's verified completion, required integration/publication, and authorization to enter the next phase. An authorization to prepare a task list does not authorize its execution or hosted creation.

## Required task hierarchy

Every phase consists of one or more delivery milestones followed by exactly one dedicated phase review milestone. Every delivery milestone ends with an explicit milestone code review/testing/report task. The final phase review milestone has exactly one phase code review/testing/report task and no additional milestone review task.

```markdown
## Phase 1 — Initial capability

- [ ] Phase 1 — Initial capability
    - [ ] Milestone 1.1 — Foundation
        - [ ] T-001 — Implement foundation
        - [ ] T-002 — Review, test and report milestone 1.1
    - [ ] Milestone 1.2 — Integrated capability
        - [ ] T-003 — Implement integrated capability
        - [ ] T-004 — Review, test and report milestone 1.2
    - [ ] Milestone 1.3 — Phase review
        - [ ] T-005 — Review, test and report phase 1
```

The exception for the last milestone applies to this dedicated phase review milestone. The last delivery milestone still receives its own milestone review task. Review tasks are ordinary executable units with stable IDs, scope, prerequisites and concrete acceptance evidence; they count toward a requested next-N-task range. They may span the boundary under review rather than a single module.

PLAN must reserve the final review milestone and define review exits before TASKS derives its executable review tasks. Existing accepted lists require a scoped amendment preserving existing IDs; do not insert or renumber tasks during execution by implication.

## Activation, execution and closure

| Transition | Required evidence and action | Responsible owner |
| --- | --- | --- |
| Activate phase | Predecessor completed, required target integration published, next phase in authorized range; resolve hierarchy and identities. Create/reconcile this phase's label, all milestones (including phase review), and all task issues with initial associations before its first task. Verify readback. | sdd-manage gates activation; sdd-forge performs hosted operations. |
| Complete task | Acceptance, applicable tests and documentation verified; owning task completion and evidence committed with the result; commit pushed and remote containment verified under existing persistence rules. Then close its resolved issue with evidence. | sdd-implement owns completion/persistence; sdd-verify supplies checks; sdd-forge closes issue. |
| Review delivery milestone | All preceding delivery tasks complete; inspect the whole milestone implementation and relevant dependencies against contracts/exits. Run focused tests and needed regressions; repair blockers; produce and commit the milestone report as part of the review task. | sdd-implement executes the review task and repairs; sdd-verify owns review/check evidence; sdd-report drafts report. |
| Close delivery milestone | Every task issue, including its review/report issue, closed; review/tests and milestone exits established; report committed/pushed. Re-read issues and milestone, close the milestone, then verify its state. | sdd-implement coordinates; sdd-forge performs closure/readback. |
| Review phase | All delivery milestones closed; assess the whole phase, cross-milestone interactions and phase exits. Run phase tests/regressions, repair blockers and commit/push the phase report through the single phase review task. | Same execution, verification and reporting owners. |
| Close phase review milestone | Phase review task completed, report committed/pushed and its issue closed; phase review exits satisfied. Close/read back the final milestone. | sdd-implement and sdd-forge. |
| Complete phase and integrate | All milestones closed, local task/parent evidence and phase exits reconciled; follow existing working-branch verification, explicit merge, merged-state verification and target publication rules. Only then may an authorized next phase activate. | sdd-implement supplies completion; sdd-manage coordinates integration and transition. |

“After all milestones close, review the phase” means all **delivery** milestones. Including the review milestone in that prerequisite would make its only task impossible to execute. The final review milestone closes after its own phase report task, and before phase completion/integration.

Task issue closure does not wait for the phase merge: it records verified, committed work on the named working branch. Phase integration remains a separate completion gate. A later merge failure does not erase valid task completion.

When a final task's commit can include verified parent status, include it there. Otherwise use a focused parent-status reconciliation commit under the existing completion protocol. Do not require a commit to contain its own SHA or introduce a parallel lifecycle database.

## Review and report obligations

A milestone review covers the delivered capability as a whole, changed code and contracts, integration and failure paths, relevant tests/documentation, and applicable PLAN exits. A phase review adds cross-milestone interactions, dependency compatibility, overall phase acceptance and the remaining TODO backlog. A phase review remains mandatory even when every milestone review passed.

Fix bugs, critical code issues and any SPEC/PLAN violation before completing the review task. An unresolved required check blocks completion. A correction requiring a new contract or broader scope is referred to its governing owner through the coordinator; it cannot be relabeled as a non-critical TODO to bypass the gate. Repairs belong to the active implementation workflow, not the read-only verifier or reporter.

Only non-critical code issues that do not violate SPEC/PLAN may be deferred. Each report has a TODO section, explicitly `None` when empty. Each deferred item records a stable finding ID, location/evidence, impact and severity, why deferral preserves contracts/exits, proposed solution options and tradeoffs, and suggested follow-up owner/scope. “Later” without a proposed remedy is insufficient.

Reports are concise, evidence-based boundary records: identity and reviewed source, delivered capability, review coverage and findings, actual commands/outcomes and limits, repairs and commits, exit-condition assessment, TODO, and next boundary. Review and testing are separate activities; green tests alone are not a code review. Reports describe defects fixed during review and deferred findings without claiming checks that were not run.

### Report placement

Use the workflow's report prefix and filesystem-safe stable IDs. Link each report from its owning review task or revision/feature record.

| Workflow / report | Placement |
| --- | --- |
| Greenfield / main implementation — phase report | `docs/dev/reports/phases/<phase-id>/PHASE-REPORT.md` |
| Greenfield / main implementation — milestone report | `docs/dev/reports/phases/<phase-id>/<milestone-id>.md` |
| Greenfield / main implementation — final implementation report | `docs/dev/reports/IMPLEMENTATION-REPORT.md` |
| Steering revision at a phase checkpoint — revision artifacts | Prefix `docs/dev/reports/phases/<phase-id>/revisions/<revision-id>/`; the revision report is `REVISION-REPORT.md` within this directory. |
| Feature implementation — reports and associated feature records | Prefix `docs/dev/features/<feature-id>/`; keep feature milestone, phase and final reports within this feature directory. |

A steering revision uses the owning phase's nested revisions directory instead of `docs/dev/reviews/<revision-id>/`. Retain the revision's stable identity and applicable artifact filenames (`REVIEW-PLAN.md`, `REVIEW-REPORT.md`, `REVISION-PLAN.md`, `REVISION-REPORT.md`); a lightweight steering revision still needs only the applicable records. General review/revision campaigns that are not phase-checkpoint steering retain `docs/dev/reviews/<revision-id>/`. This backend lifecycle campaign is such a general revision and remains in its existing directory.

Feature reports stay under their feature prefix throughout execution and retention; do not place them in the main implementation's phase-report tree. If a feature spans multiple phases, qualify report paths within its feature directory by stable phase ID to avoid collisions. The feature implementation's final `IMPLEMENTATION-REPORT.md` belongs at the feature prefix. Feature document/task incorporation and archive eligibility retain their separate ownership rules.

The phase report carries forward unresolved milestone TODO items and adds phase-review findings, preserving IDs and provenance. After the full authorized task list is complete, the final implementation report aggregates all unresolved/deferred milestone and phase items, deduplicated by ID, with solution options retained. Resolved items remain traceable to their earlier report and resolution evidence. The last phase review task includes this final report when it completes the full task list; a bounded partial request produces no full-project completion claim.

## Ownership and workflow boundaries

| Skill | Assigned responsibility | Boundary |
| --- | --- | --- |
| sdd-conventions | Canonical object lifecycle, task hierarchy and report identity conventions. | Shared rules; no execution or mutations. |
| sdd-plan | Delivery/review milestones and meaningful milestone/phase review exits. | Strategy; no checklist ownership. |
| sdd-tasks | Derive/validate explicit review tasks, dependencies, unique IDs and links to reports. | No automatic execution or hosted projection. |
| sdd-manage | Authorization, phase activation, workflow transitions, credentials and integration coordination. | Does not replace executor, verifier or backend. |
| sdd-implement | Run selected delivery/review tasks, coordinate review/testing, fix findings, update owning status, commit/push, request closures. | Never silently extend a selected range or change governing contracts. |
| sdd-verify | Read-only milestone/phase implementation review and check selection/execution; return findings and acceptance evidence. | Proposed extension of its current check-focused remit; no repairs or completion writes. |
| sdd-tdd / sdd-docs | Test strategy/design/changes and documentation maintenance respectively. | Support execution; neither owns hosted lifecycle. |
| sdd-report | Task, milestone, phase and final report composition, TODO aggregation and evidence presentation. | Drafts facts; no completion decisions or hosted writes. |
| sdd-forge | Provider identity/access, object lookup/create/update, issue/milestone state transitions and readback, pending-effect reconciliation. | No Git commits, integration or declaration of verified completion. |
| sdd-orient | Observe actual Git/task/report/hosted handoff state for continuation. | Read-only; no replay of writes. |
| sdd-steer / sdd-integrate-feature | Authorized amendments and accepted feature task/document reconciliation respectively. | Preserve IDs/history and invalidate affected completion where required; no automatic implementation resumption. |

No new review skill is required by this proposal. Extend sdd-verify's boundary assessment to explicit read-only code review, and have sdd-manage route specialist concerns to existing focused owners as needed. The implementation owner remains accountable for resolving findings before closure.

## Failures, interruptions and amendments

Hosted tracking is optional. Local-only work follows the same review/report gates without hosted objects. With tracking enabled, a projection/access failure leaves activation pending: do not start that phase's first task until its objects are created and verified, unless the user explicitly authorizes continuing without hosted tracking. A closure outage preserves local verified work but leaves hosted milestone/phase closure pending; no next phase activates on an assumed closed state. Independent work within an already activated phase may continue within the authorized range when dependencies permit; dependent review/closure gates remain blocked.

On resume, inspect owning lists, existing reports, task/report commits and pushes, and actual hosted states. Finish the earliest unmet authorized transition. Reconcile older pending effects as well as the latest task; do not repeat a finished review or recreate objects because execution was interrupted.

| Interrupted state | Recovery |
| --- | --- |
| Some phase objects created | Look up exact identities in all relevant states; reuse confirmed objects; create only missing objects. |
| Review/report partly written | Inspect retained work and actual coverage; finish missing review, repairs, tests and report before completion. |
| Result/report committed but unpushed | Publish and verify containment before new task work or issue closure. |
| Issue closure or milestone closure response uncertain | Read actual state and evidence before replay; preserve unknown outcome if readback is unavailable or contradictory. |
| Closed milestone, local parent state pending | Reconcile verified parent evidence/status; persist it without repeating completed tasks. |
| Phase review complete, merge/publication pending | Resume existing integration, not a second review or new merge; next phase stays inactive. |

Do not close, relabel or reassign foreign issues to make a milestone appear complete. Unexpected open issues, conflicting identity or ownership in a managed milestone block closure until their disposition is resolved. Reconciliation preserves user text, unrelated labels/comments/assignees and historical evidence.

Accepted amendments invalidate affected task/milestone/phase completion claims when current acceptance no longer holds. Explicitly reconcile reopening of affected managed issues and milestones as needed; do not erase earlier reports or treat retired/cancelled work as verified completion. Added work in an already active phase is projected before execution; work assigned to a future phase remains unprojected. Feature transfer retains stable IDs and original issues. A feature's scoped parent checkbox cannot alone close a whole-project milestone with unfinished tasks in another owning list. Changes to a previously completed phase require a scoped accepted amendment and dependency reassessment, not silent next-phase activation.
