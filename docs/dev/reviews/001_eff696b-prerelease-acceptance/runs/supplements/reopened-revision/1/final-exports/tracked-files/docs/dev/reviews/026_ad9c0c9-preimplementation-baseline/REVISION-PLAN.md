# Revision plan

## Campaign and accepted objective

- Campaign: `026_ad9c0c9`; baseline: `ad9c0c9a3990d7b19ace60c5b0596bb39d6a5289`.
- Authority: the user commands a revision campaign requiring preimplementation project documents on design-docs and a default-branch merge before dependent implementation branches. The user explicitly clarifies that campaign documents belong on the revision branch.
- Campaign branch: `revision/026_ad9c0c9-preimplementation-baseline`; campaign plans and reports are retained here through execution.
- Default target: `main`, established by `origin/HEAD -> origin/main` and refreshed remote state.
- Historical setup deviation: the first plan was incorrectly authored on `design-docs/026_ad9c0c9-preimplementation-baseline` and merged/published as `0b57b29d57ace3ba0ce46e58b1d1f0768d1b78ef` before the clarification. Preserve that Git history; this corrected plan and subsequent campaign work use the revision branch. The deviation is not a required workflow stage.
- Scope: workflow instructions, branch conventions, startup gates, user-facing examples, and retained campaign evidence. Existing client compatibility manifests remain synchronized and unchanged.

## Ordered revisions

| Action | Outcome / owners | Verification |
| --- | --- | --- |
| V-001 | Establish design-docs naming and a shared project preparation integration gate in sdd-conventions and sdd-manage. Cover initial, feature and revision-owned project preparation; retain campaign plans/reports on revision and preserve scoped steering and interrupted implementation ownership. | Inspect positive, preparation-only, failed merge/publication, campaign-only revision and continuation paths; exercise explicit Git ancestry in a disposable repository. |
| V-002 | Wire direct document owners, implementation startup, phase activation, feature sequencing, examples, and README to the shared gate. Remove conflicting same-branch feature preparation instructions. | Check all affected handoffs and relative links; verify no implementation branch is prescribed before the preparation merge. |
| V-003 | Verify source composition and support regressions, retain revision results, explicitly merge the revision into main, and publish the target. | Full support suite; manifest equality; whitespace/link checks; two-parent merge and remote containment evidence. |

## Execution and boundaries

Commit and publish campaign records with the scoped revisions on the revision branch. This campaign changes plugin instructions and needs no separate project design/SPEC/PLAN/TASKS preparation. Completed revisions and evidence are committed and pushed before final explicit integration into main. No product implementation, acceptance campaign, hosted issue creation, or changes to platform approval controls are included. This is a prompt-defined accepted revision; no preceding review report is fabricated.

## Evidence limits

Instruction consistency and local Git exercises establish their recorded coverage. They do not establish live installed-client compliance or disable host automatic review. Preserve existing unrelated work, branches, and historical records.
