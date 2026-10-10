# Per-commit publication revision plan

## Campaign and authorization

- Campaign: `035_6ac4f0a`; starting baseline: `6ac4f0a0b7d6fd198f9116d62c1084951f26ad5a`.
- Working branch: `revision/035_6ac4f0a-per-commit-publication`; target: `main`.
- The user accepted adding the shared rule after a focused current-source assessment on 2026-10-09. Planning, execution, verification and normal integration/publication are within scope; no additional review stage is invented.
- Assessment: task implementation already requires publication before the next task. General coordination says to push finished commits, while review/revision handoffs use dependent-work wording. These do not universally prohibit accumulating independent local commits.
- Version remains `0.15.0`; closed campaign records remain unchanged.

## Accepted rule

After each workflow-owned commit, push it to the established remote branch and verify remote containment before advancing project work or creating another commit. Do not accumulate local commits for later publication, including in temporary agent sandboxes. Apply this to preparation, reviews/revisions, maintenance, implementation, steering, feature incorporation, reports and merge commits, including direct focused calls.

Keep commit inspection, publication/readback and scoped recovery available to complete the pending push. If publication is blocked, preserve the commit, report its actual state and pause affected workflow advancement; do not use independent work as a reason to create more unpublished commits. Existing outstanding commits are reconciled/published before new commit-producing work. A new commit on another workflow branch is not a workaround for a publication blocker.

An explicit user instruction for local-only work or deferred publication is an exception within its stated scope. No exception creates remote persistence, grants publication outside authorization, guesses a destination, bypasses host/repository restrictions or permits force-pushing. Per-commit publication does not change branch integration gates or require per-commit merges.

## Ordered actions

| Action | Outcome | Recheck |
| --- | --- | --- |
| V-001 | Put the shared rule in Git workflows and expose it in manager coordination/entry. Reconcile review/revision and report handoffs, steering and direct implementation references; update current root guidance. | Single canonical rule, all workflow categories covered; independent review units cannot accumulate; inspection/recovery and explicit local-only exception are retained. |
| V-002 | Verify source handoffs, links/style, required support suite and committed package. Finish reports/navigation before the complete tip is explicitly merged, verified and published. | Eight scenarios below; no old campaign changes, version/manifests unchanged; actual package bytes and checksum; merged-state verification and remote containment. |

## Scenarios and evidence limits

| Case | Expected source behavior |
| --- | --- |
| SC-001 | Task commit is pushed/read back before next task. |
| SC-002 | Each preparation or maintenance commit is published before new work/commit. |
| SC-003 | Independent review units and revision actions obey the same per-commit barrier. |
| SC-004 | Steering, feature incorporation, report-only and merge commits obey the barrier. |
| SC-005 | Failed/uncertain push retains work, reconciles readback/recovery and blocks advancement. |
| SC-006 | Existing unpushed commits are resolved first, without branch/tool workarounds. |
| SC-007 | Explicit local-only/deferred-publication instruction is honored only within its scope; published status is not fabricated. |
| SC-008 | Commit-inspection and publication recovery remain possible; push cadence does not alter human acceptance or merge eligibility. |

Assess scenarios against written instructions and actual handoffs, not a live consumer. Run the mandated support suite and committed-source package build, check changed Markdown/links, and verify protected-path preservation from Git diffs. No new automated test that merely mirrors prose is required. Commit and verify each push before continuing, including this planning checkpoint. Stop after full verified integration/publication.
