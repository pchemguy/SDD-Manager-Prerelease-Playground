# Core development workflows revision plan

## Campaign and decisions

- **Campaign:** `006_0393fee`; date 2026-10-02.
- **Starting baseline:** `0393fee5382be42465c7089924f315f0f6f44f7e`.
- **Input:** Human-defined three-workflow model and accepted placement discussion; no separate review report is needed.
- **Authorization:** Plan and execute this documentation revision, including verification, checkpoint publication, and explicit boundary integration.
- **State:** Completed; V-001–V-003 verified within recorded limits, explicitly merged, and target publication verified. Evidence: [REVISION-REPORT.md](REVISION-REPORT.md).

## Intended model

| Workflow | Objective and typical path |
| --- | --- |
| Main / greenfield | Build the complete intended system: exploration, design, SPEC, PLAN/layout, TASKS, bounded implementation and verification. Existing projects may enter at an established stage. |
| Revision | Correct, simplify, or improve previously defined or implemented work, typically through review planning when needed, review/report, revision plan, execution, and revision report. A prompt may directly define a focused accepted revision. |
| Feature | Add a scoped capability, typically preparing feature design/specification/plan/task documents as needed before implementation, incorporation, verification, and integration. |

Steering is a lightweight revision path at a paused implementation checkpoint, not a fourth core workflow. The human defines and commands a focused amendment; existing documents/code/tests/docs are amended directly, without feature overlays or an obligatory formal campaign. It returns control after verification and explicit integration into the paused branch, without resuming task-list work.

The classification describes purpose and overall path; operation catalog entries and skills describe reusable stages. Main does not mean Git's main/default branch. Workflow classification alone grants no authorization and does not require repeating established stages, materializing every optional document, or broadening a selected implementation range.

## Authoritative updates and ordered actions

| Action | Scope / owners | Required outcome | Recheck |
| --- | --- | --- | --- |
| V-001 | sdd-manage/workflows.md; review-and-revision.md; sdd-steer entry | Canonical three-workflow model before the catalog; catalog explicitly identified as operations/stages; revision and steering link to the model without duplicating procedures. | Distinguish purpose from operation; preserve prompt-driven revision, optional feature package, checkpoint stop and ownership. |
| V-002 | README; docs/dev/CAPABILITY-MAP.md; affected examples if needed | Short coherent overview and cross-links; steering clearly a revision variant. | Readers can locate canonical model; existing project entry and branch meaning remain clear; no mandatory document ceremony. |
| V-003 | Campaign evidence; all affected source/navigation | Verify routing/stop scenarios, source composition, headings/links, package and metadata; persist dispositions and integration evidence. | Preparation/review stop correctly; all core implementation paths retain bounded scope and explicit integration; installed-client/runtime limits are stated. |

There is no consumer PROJECT/SPEC/PLAN set to amend here. Update existing instruction owners and navigation; keep the campaign plan/report as retained rationale/evidence. No new skill, backend, transaction protocol, or task ownership is introduced.

## Verification scenarios

| Scenario | Expected interpretation |
| --- | --- |
| SC-001: Greenfield preparation only | Main workflow prepares accepted design/spec/plan/tasks and stops before implementation. |
| SC-002: Existing project with accepted TASKS | Main workflow may enter bounded task execution without replaying exploration; main is a development purpose, not a branch name. |
| SC-003: Correct an implemented design issue | Revision typically uses review/revision artifacts; a focused accepted prompt can supply scope without an invented preceding review. |
| SC-004: Add scoped ZIP support | Feature prepares necessary deltas and active feature tasks; incorporates accepted documents within authorized scope before final integration. |
| SC-005: Reduce functionality at paused checkpoint | Steering is lightweight revision, amends existing documents directly, creates no feature package, integrates into paused branch, and stops without resume. |
| SC-006: Review-only or narrow task request | Taxonomy does not authorize repairs, full project implementation, unrelated feature incorporation, or an automatic switch to steering. |

Use source inspection and a fresh consumer interpretation assessment for these instruction changes; report these separately from runtime execution. Run affected-skill/plugin validators, package inspection, contained-link and heading checks (including template starts), metadata/icon consistency, and diff/credential checks. No consumer production implementation or new live hosted mutation is needed.

## Execution and persistence

1. Commit/push this plan and navigation, then establish a scoped revision branch targeting `feature/architecture-revision`. Record the actual checkpoint and branch identities.
2. Execute V-001–V-003 in order. After each action, update retained revision evidence, commit/push changes and report together, and verify remote containment before dependent work.
3. Preserve prior decisions: full intended design/SPEC, MVP-first incremental PLAN, phase/milestone/task identities, task completion ownership, token recovery, scoped selection, and human-controlled steering.
4. After successful boundary verification, refresh the target, perform one explicit non-fast-forward merge, check the prospective merged state, commit/push the target, and record actual merge parents/publication. Keep all campaign artifacts here and update navigation to actual state.
5. On a blocker preserve valid changes/commits and identify the unmet condition. Stop after the authorized completed boundary; do not start consumer task implementation or another revision.
