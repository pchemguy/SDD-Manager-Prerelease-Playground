# Revision report

## Campaign and result

- Campaign: `026_ad9c0c9`; [accepted plan](REVISION-PLAN.md).
- Starting baseline: `ad9c0c9a3990d7b19ace60c5b0596bb39d6a5289`.
- Working branch: `revision/026_ad9c0c9-preimplementation-baseline`; target: `main` (`origin/HEAD -> origin/main`).
- Working checkpoint: `0b57b29d57ace3ba0ce46e58b1d1f0768d1b78ef`.
- Result at this report checkpoint: requested instruction changes implemented and locally verified; final campaign integration/publication follows this revision commit under existing user authority.

## Revision evidence

| Action | Actual changes | Observed verification | Limits |
| --- | --- | --- | --- |
| V-001 | Workflow identity and branch-management policy establish design-docs project preparation, explicit default integration/publication before execution-branch creation, ancestry evidence, continuation and failure boundaries. Campaign records remain revision-owned. | Four disposable Git lifecycle exercises pass via `python docs/dev/reviews/026_ad9c0c9-preimplementation-baseline/verify_git_lifecycle.py`. Source inspection confirms separate preparation and execution identities. | Git mechanics exercise, not live agent compliance. |
| V-002 | Coordinator, QC persistence, document owners, implementation startup, phase activation, feature sequencing, campaign owners, examples and README share the preparation gate. Removed the example prescribing a single feature branch across preparation and implementation. | Changed-owner relative links/anchors checked outside fenced template examples; whitespace checks pass. Manual handoff inspection covers preparation-only, initial/feature implementation, campaign-only revision, revision project preparation, failed publication, already merged inputs and paused steering. | No installed-client consumer run. |
| V-003 | Support regressions and manifest compatibility verified; retained plan/report and repeatable Git exercise committed on the revision branch before final integration. | `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats`: 113 tests pass. Both manifests remain byte-identical and parse as JSON. | Final two-parent integration and remote containment are checked after this checkpoint; Git descendants and the final result identify their exact SHA. |

## Source composition assessment

Project preparation artifacts and QC reports are committed on design-docs. Before a dependent execution branch is created, their accepted tip is explicitly merged, verified and published on the actual default branch. A preparation-only request stops after its design-docs checkpoint. Failed checks, conflicts or target publication stop the transition. Already integrated inputs reuse proven containment. A feature preparation merge leaves active feature deltas and FEATURE-TASKS in place; final incorporation/archive and phase completion remain separate boundaries. Campaign plans/reports belong on revision, and paused implementation/steering evidence preserves its existing owner.

## Setup deviation and user correction

Before the user clarified campaign ownership, the agent incorrectly put the first campaign plan on `design-docs/026_ad9c0c9-preimplementation-baseline`, committed it as `df219df1d2ec0d8dcffd9569f3e525653362ed38`, and published preliminary merge `0b57b29d57ace3ba0ce46e58b1d1f0768d1b78ef`. The user then explicitly required campaign documents on the revision branch. The corrected plan, source revisions, exercise and this report are authored on that revision branch. The initial published history is retained and is not presented as the required campaign workflow.

## Integration and stopping boundary

Initial campaign integration completed as two-parent merge `92580c084987852863ce7ec4cc5f06b29886ed01`, with parents `0b57b29d57ace3ba0ce46e58b1d1f0768d1b78ef` and `6182148300c4d5e13151c2bb8ff597a21a61ea4e`, pushed to origin/main. Merged checks passed: 113 support tests, four Git lifecycle exercises, 202 local links/anchors, manifest equality and whitespace checks.

### Explicit default publication clarification

The user reiterates that the default branch may have any name and the design-docs merge must be pushed, claiming existing authorization when necessary. Branch management now names this push as mandatory, separates the design-docs/main convention from target discovery, and points directly to proactive authorization context. The authorization owner and README repeat the required default push before implementation branching. Campaign records remain revision-owned. Verification uses the existing Git exercise with nonstandard default `trunk` and the unpublished local merge case, plus scoped link/whitespace checks; no new product behavior or host-control bypass is introduced.

Commit and push the verified revision checkpoint, refresh main, inspect the complete owned branch difference, then perform `git merge --no-ff --no-commit` with merged-state checks before the two-parent commit and target push. Confirm actual parent tips and remote containment; preserve the revision branch. Stop at this campaign boundary without product task execution, new hosted objects, or changes to host approval controls. Live client acceptance remains unexecuted.
