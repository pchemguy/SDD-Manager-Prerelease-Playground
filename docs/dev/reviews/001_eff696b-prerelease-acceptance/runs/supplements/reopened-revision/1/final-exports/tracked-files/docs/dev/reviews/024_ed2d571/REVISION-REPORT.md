# Pre-release repair execution

Campaign 024_ed2d571. [Accepted plan](REVISION-PLAN.md), [original review](REVIEW-REPORT.md). User authorized R-001–R-004; live testing explicitly out of scope. R-005 remains excluded/unexecuted.

Working branch revision/024_ed2d571-pre-release-review; integration target feature/architecture-revision. Original source ed2d571d20aa8ad6ee77f25ad89602e82e6a653b; repair baseline 21d144057413473f7e402fa0ce679cf2e3095024. State: **completed, verified, explicitly integrated and published**. All four accepted defects are resolved in source 0.14.7; live testing remains out of scope.

| Action | State | Evidence |
| --- | --- | --- |
| V-001 / R-001 | Implemented and focused recheck passed | [RED](probe-red.txt): two actual boundary assertions fail; [GREEN](probe-green.txt): five checks pass. Public package import/origin, package-only layout, broken public export, actual injected assertions and import/setup distinction tested. Injector/assessor guides disclose its narrower layout. |
| V-002 / R-002 | Implemented and focused recheck passed | [RED](receipt-red.txt): three behavioral assertion failures and two prior resume/load errors (not behavioral RED). [GREEN](receipt-green.txt): nine tests pass; fresh/resume dangling and occupied symlinks plus parent links rejected before effects; ordinary held continuation/drift/uncertain non-replay retained. |
| V-003 / R-003 | Implemented and focused recheck passed | [RED](package-red.txt): actual snapshot omitted linked notice. [GREEN](package-green.txt): two package-documentation checks pass including notice link closure and dirty fingerprint changes. Package paths/docs aligned; identical manifests now 0.14.7. Full actual-source snapshot audited after source commit. |
| V-004 / R-004 | Implemented; source/navigation recheck passed | [Campaign index check](campaign-index-check.json): 001–024 each occur once in one contiguous table; all record links exist. Restored truthful 020 entry, repaired row gaps and added current review/revision navigation. Initial new-row spacing failed the structural check and was corrected before commit. |

No live acceptance, installed-client activation or product changes selected.

## Whole-boundary recheck

Source e33949aded51c55013d2de6318e0564127a13d3d (0.14.7). Full documented support discovery passed **112 tests in 35.070 seconds**, Python 3.12.14; [output](repaired-support-suite.txt). [Catalog validation](repaired-catalog-validation.json) passes 27 static cases. [Actual committed package validation](repaired-package-validation.json) verifies 116 files, byte-identical manifests, root notices and dependent links, asset availability, XML SVG parsing and excluded assessor/development material. Package fingerprint 9415dc5e374ac5eacb79acc662ab43beb72efe7a5ecd239107912924820d6c82. Runtime skill instructions and assets are unchanged.

[Fresh independent review](independent/REPAIR-REVIEW.md) found no remaining issue and passed 16 focused tests plus additional origin, parent-link, committed/dirty package and index checks. R-001–R-004 are verified for this repair source. R-005 is excluded from execution by the user; no live or installed-client pass is inferred.

## Published repair checkpoints

| Boundary | Commit | Publication |
| --- | --- | --- |
| Accepted plan | c9b0d5cf499fcda6b05df906893d891903a0b27f | Normal review-branch push and exact ref readback |
| V-001 | 9263e344b2200353e3b7fd9b54d3ffa8fe068979 | Normal push and exact ref readback |
| V-002 | 4e8162f66cd97f3ad8ce81da1aebf7fbf1bca028 | Normal push and exact ref readback |
| V-003 | 347a35f46b727c7a76ebc4b7ce308bab78b9cae1 | Normal push and exact ref readback |
| V-004 | e33949aded51c55013d2de6318e0564127a13d3d | Normal push and exact ref readback |

Integration gate: all selected repairs have focused/full local rechecks and independent clearance. The branch's earlier commits contain only this requested review evidence, followed by accepted fixes; no unrelated implementation is included. Target remains feature/architecture-revision at original source ed2d571d20aa8ad6ee77f25ad89602e82e6a653b before integration. No main-branch or installed-package update is selected.

## Prospective merged verification

Target refreshed and still names ed2d571d20aa8ad6ee77f25ad89602e82e6a653b. Published working tip 85a2d3f39728af2445f37de831fc6f3ce526a092 merged using --no-ff --no-commit with no conflicts. Prospective merged source/package/harness/index paths exactly equal the verified working tip. [Merged checks](merged-repair-checks.txt): **34 focused tests passed in 11.034 seconds**, covering public probe, receipt control, notice package and all preflight regressions. [Integrity](merged-integrity.json) retains both ordered parent tips and exact source-tree equality. No source changed after those checks; following report additions are evidence-only.

The required two-parent merge commit and target push follow this verified boundary. Final publication/readback is recorded after its observed result. The revision branch is retained; main and installed clients remain outside this integration scope.

Merged diff whitespace check caught one trailing space emitted by unittest in the RED log. The final text log trims that formatting only; original raw bytes remain in V-002 commit 4e8162f66cd97f3ad8ce81da1aebf7fbf1bca028. [Normalization provenance](log-format-normalization.json) records both hashes. Test outcomes are unchanged.

## Completed integration and publication

Explicit merge **1b3ec542f16e266c13a00da34938a9a2896ee7e8** has ordered parents ed2d571d20aa8ad6ee77f25ad89602e82e6a653b and 85a2d3f39728af2445f37de831fc6f3ce526a092. Normal push published feature/architecture-revision; exact remote ref readback confirmed that merge. Post-commit package pinning gives the same verified 116-file fingerprint, and source/harness/navigation paths exactly match independently reviewed e33949aded51c55013d2de6318e0564127a13d3d. [Final revision evidence](FINAL-REVISION.json) retains observed identities and scope.

R-001–R-004 are verified and integrated. There is no remaining blocker within the accepted repair scope. R-005 remains an unexecuted evidence gap explicitly outside this request; no live test or installed-client activation occurred. Main and existing test repositories were unchanged. Revision branch retained; unrelated untracked work preserved. This final evidence-only checkpoint is normally published on the established target after its commit, with exact destination verification.
