# Backend lifecycle revision plan

## Campaign and scope

Campaign: `010_3f56922`. Full starting baseline: `3f56922a936c8fe039f906ed27566b5662b5440c`.
Working branch: `revision/010_3f56922-backend-lifecycle`. Target: `feature/architecture-revision`.
Inputs: user's lifecycle requirements, [policy proposal](LIFECYCLE-POLICY.md), [baseline assessment](REVIEW-REPORT.md).

State: implementation authorized by the human command to implement this revision, including the amended report placement. Routine scoped commits, revision pushes and verified integration use the coordinator's [scoped authorization policy (historical reference)](https://github.com/pchemguy/SDD-Manager/blob/5e2624e625e33410245cb3b51b1b31120ad18747/skills/sdd-manage/references/revision-authorization.md); after rejection the coordinator supplies actual authorization context without claiming a platform override. Observed progress and blockers are recorded in REVISION-REPORT.md.

## Ordered revisions

| Action | Findings | Change / owner | Recheck |
| --- | --- | --- | --- |
| V-001 | R-001–R-004 | Promote agreed lifecycle to a canonical `skills/sdd-conventions/references/backend-object-lifecycle.md`; link from shared hierarchy and relevant skills. Keep campaign proposal as retained rationale, referencing canonical authority after adoption. | One normative lifecycle owner; first-phase exception, review milestone ordering, optional hosting and phase label retention explicit. |
| V-002 | R-002 | sdd-plan defines review milestones/exits; sdd-tasks derives dedicated review tasks and dependencies. Amend examples and task-list review criteria. | Single/multiple delivery milestones, feature delta and pre-existing stable IDs; final milestone exactly one phase review task; count selection respects explicit tasks. |
| V-003 | R-001, R-003 | sdd-manage gates eligible-phase activation; sdd-forge limits projection to that phase, creates all its objects before first task and defines milestone closure/reopening/recovery. Update GitHub routing and capability descriptions. | Future objects absent; initial/partial/repeated projection; all issue closure before milestone close; foreign issues protected; ambiguous identity and uncertain write block replay. |
| V-004 | R-003, R-004 | sdd-verify gains read-only boundary code review; sdd-implement coordinates reviews, repairs, report persistence, issue/milestone closure and parent status. Update startup/continuation and phase-transition handoffs. | Bugs/critical issues/contract violations/failed required checks block; review task commits report; task push precedes issue closure; milestone closure precedes dependent phase review; phase report precedes final review milestone closure. |
| V-005 | R-004 | sdd-report defines concise milestone/phase/final reports, workflow-specific placement under the report prefixes below, TODO admissibility/options/provenance and aggregation. Update completion/campaign artifact guidance and generated report links. | Main phase/milestone paths, phase-nested steering revisions and feature report prefixes match policy; empty TODO explicit; non-critical items carried across milestone/phase/final reports; resolved items traceable; no final full-project report for a partial range. |
| V-006 | R-001–R-004 | Reconcile feature integration/steering invalidation and all workflow entry/routing descriptions with canonical policy. Update workflow identity, review-campaign storage and steering references for the phase-specific revision prefix; retain general campaign placement. Recheck complete handoffs rather than isolated files. | Steering branch/directory identity resolves its owning phase and revision; feature reports remain under their feature prefix; future-phase feature work stays unprojected; transferred IDs/issues reused; scoped feature parent cannot prematurely close project milestone; authorized reopening preserves history; no automatic continuation beyond requested range. |
| V-007 | R-005 | Update TextStats objectives, relevant consumer/assessor cases and dependencies, catalog validation and interruption criteria for this lifecycle. Add focused source/consumer checks where existing coverage cannot expose failure. | Positive ordering plus early creation/closure, missing review, critical/deferred finding, report/commit/push interruption and uncertain closure cases; old support tests remain green. |
| V-008 | R-001–R-005 | Run composed source review and local checks, then live lifecycle acceptance on a dedicated repository against a pinned revised source. Record observed results in REVISION-REPORT.md. | Provider readback and actual task/report commits prove ordering, identity reuse, closure and resumption. Missing repository/API access is Blocked, never a pass. |

V-001 establishes accepted rules before dependent source edits. V-002–V-006 share those rules and require composition review. V-007 follows resulting behavior; V-008 evaluates a pinned complete revision. No historical acceptance claim substitutes for these checks.

## Report placement to implement

- Main/greenfield phase reports: `docs/dev/reports/phases/<phase-id>/PHASE-REPORT.md`.
- Main/greenfield milestone reports: `docs/dev/reports/phases/<phase-id>/<milestone-id>.md`.
- Main/greenfield final implementation report: `docs/dev/reports/IMPLEMENTATION-REPORT.md`.
- Phase-checkpoint steering revision artifacts: `docs/dev/reports/phases/<phase-id>/revisions/<revision-id>/`, replacing `docs/dev/reviews/<revision-id>/` for this workflow. Retain applicable stage filenames, including `REVISION-REPORT.md`.
- Feature reports and associated records: `docs/dev/features/<feature-id>/`; the feature's final report is `IMPLEMENTATION-REPORT.md` under this prefix. Qualify phase report paths within the feature directory when needed for multiple phases.

V-005 implements report formats/links; V-006 reconciles storage conventions and coordinator/steering/feature handoffs. Check placement at generation, continuation and retention. General review/revision campaigns remain under `docs/dev/reviews/<revision-id>/`; this campaign's existing records stay in place. Preserve historical artifact paths and repair references only within an authorized migration scope.

## Execution and persistence

At implementation entry, inspect current orientation, outstanding commits, scope and dirty ownership; reuse this campaign identity and appropriate working branch. Source and corresponding revision evidence are committed/pushed at each coherent action before dependent work. Do not create a second progress registry, renumber existing task IDs, modify historical campaign results, or mutate a test repository during policy articulation.

REVISION-REPORT.md is created when source revision starts and records actual actions, checks, commit/push state and remaining findings. Complete authorized revision uses working-branch verification, explicit two-parent integration, merged-state checks and target publication under existing Git rules. Stop at the completed revision boundary or an unresolved external blocker; do not begin unrelated development.

Live acceptance requires a dedicated disposable test repository and authenticated provider access. The agent should follow `acceptance/textstats/AGENTS.md`, request missing repository/access inputs under its setup protocol, and retain sanitized readback. Do not silently reuse the historical TextStats repository or claim hosted lifecycle coverage from local harness tests.

## Policy choices made explicit

- Phase review follows all delivery milestones; its own dedicated final milestone closes afterward.
- Every delivery milestone, including the last delivery milestone, has its own review/report task.
- Code review is a proposed extension of sdd-verify; repairs remain with sdd-implement. No new skill is required.
- Active hosted tracking requires verified phase projection before first task; unavailable closure remains pending and prevents next-phase activation. Local-only mode remains usable.
- The last phase review produces the final implementation report when the full task list completes; selected partial ranges retain their scope.
