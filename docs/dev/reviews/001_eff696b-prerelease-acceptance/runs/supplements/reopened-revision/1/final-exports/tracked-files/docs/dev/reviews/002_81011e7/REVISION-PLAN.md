# Revision plan

**Campaign:** `002_81011e7`. Starting baseline: `81011e7db200f0eef89a52d35896bbf97575b6c1`; source revision starting checkpoint: `a9eaf57ca8c978111f94b0a4341ca117796d2d05`.

Companions: [review report](REVIEW-REPORT.md), [revision report](REVISION-REPORT.md). Extracted from the existing accepted follow-up plan; original SDD-R-001 / SDD-R-002 and R01–R03 identities are retained.

## Revision follow-up

Use the report's canonical finding records and retain their IDs, baseline evidence, and review coverage. Execute the two revisions separately. R01 and R02 are implemented and verified; R03 package checks passed. Actual evidence and pushed revision checkpoints are recorded in the companion report. The protocol below remains the revision procedure, distinct from its observed results.

### R01 — Preserve read-only Git inspection

- **Finding:** SDD-R-001, P2 defect.
- **Targets:** `skills/sdd-orient/SKILL.md` and `skills/sdd-orient/references/inspection-and-handoff.md` where needed to align the invariant and concrete commands.
- **Change:** Suppress optional Git writes during orientation with command-scoped `git --no-optional-locks` or an equivalent scoped `GIT_OPTIONAL_LOCKS=0`. Do not change repository or global configuration. Keep the documented examples consistent with the no-index-mutation requirement.
- **Verification:** In disposable repositories, compare index and worktree bytes before and after inspection for metadata-only clean, staged, unstaged, and conflicted states. Assert accurate status output and successful command outcomes. Reproduce the unguarded metadata refresh as a control; the corrected procedure must preserve the index. Recheck non-Git, unborn, and detached-state reporting without initializing or altering the repository.
- **Persistence gate:** Record exact revision and validation evidence in the finding's disposition, commit the bounded fix and report update with SDD-R-001 in the subject, push using the established saved credential, and verify remote containment before R02.

### R02 — Make completion reassessment durable

- **Finding:** SDD-R-002, P3 recommendation accepted for revision planning.
- **Targets:** `skills/sdd-integrate-feature/references/feature-incorporation.md` and the relevant `sdd-implement` selection, continuation, and completion references. Align entry points or coordinator handoffs only where necessary.
- **Ownership:** Integration reconciles accepted task scope and records a pending completion reassessment in each affected owning task list that is within its edit scope. It preserves the checkbox and historical evidence; **sdd-implement** owns completion assessment and checkbox correction. Direct checkpoint amendments retain **sdd-steer** ownership.
- **Durable handoff:** The task-local note identifies the stable task ID, changed acceptance and authoritative source, prior evidence that no longer establishes current completion, and required reassessment. Use the existing task list or its existing linked evidence location; introduce no journal or separate state artifact. If the owning list is outside scope, report the deferred update without editing it or silently expanding scope.
- **Consumption:** Orientation reports the pending reassessment. Range selection treats the affected checked claim as disputed and assesses its current eligibility rather than concluding that all work is complete. Selection-only remains read-only. Execution preserves push-first behavior, obtains current acceptance evidence or performs authorized remaining work, corrects unsupported status, and removes the pending note only when the reassessment is resolved. Preserve prior evidence as historical.
- **Scope:** Preserve stable IDs, unique executable ownership, unrelated completed work, and feature versus whole-project parent claims. Report out-of-range reassessment work as a scope conflict. Do not automatically run implementation from integration or change hosted issue state from the note alone.
- **Verification:** Integrate changed acceptance for a checked, committed task in a disposable fixture, stop and persist the documents, then give a fresh consumer only the repository and revised skills. It must discover the reassessment without chat history, preserve old evidence, and avoid skipping the affected task or claiming current completion. Exercise both main and feature owning lists, unchanged checked neighbors, stale parent claims, selection-only, and a list outside the integration edit scope. Observe the defined owner correcting status after actual reassessment.
- **Persistence gate:** Record the accepted protocol and actual checks in the finding's disposition, commit the bounded revision and report update with SDD-R-002 in the subject, push using the established saved credential, and verify remote containment before final validation.

### R03 — Validate the revised composition

- Run the skill validators for changed capabilities, the plugin validator and inspector, and heading, template, link, metadata, and skill-reference checks.
- Recheck the orientation → integration → implementation handoff and existing boundaries: selected integration, one executable task owner, read-only selection, push-first execution, preserved staging, and human-controlled steering stop.
- Preserve the completed review's fixed baseline and original findings. Append revision commits and observed evidence; mark a finding Verified only after its objective recheck passes. State any blocked or unexecuted check explicitly.
- Upon completion, archive this plan and its companion report under `docs/dev/reviews/`, updating paths and relative links. Commit and push the final validation/report checkpoint before reporting completion. Include direct GitHub links to the branch, report, and revision commits.

Client execution, live GitHub mutations, and independent pinned upstream provenance remain separate validation limits. These revisions do not require provider writes, credential replacement, dependency installation, or a new workflow-state artifact.
