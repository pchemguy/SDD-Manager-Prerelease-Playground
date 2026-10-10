# Shared Markdown style revision report

## Campaign and result

- Campaign: `034_c9cee3d`; baseline: `c9cee3dc61ab3362b30d449d25852e8f35ee70b5`.
- [Review](REVIEW-REPORT.md); [accepted plan](REVISION-PLAN.md).
- Working branch: `revision/034_c9cee3d-shared-markdown-style`; target: `main`.
- Planning checkpoint `185d0c4` was pushed and read back before execution. The user authorized campaign execution on 2026-10-09.
- State: all four actions completed and coherent source boundary verified; final explicit merge/publication is established by the containing Git merge and remote readback. Version remains `0.15.0`.

## Revision evidence

| Action / findings | Actual change | Evidence and limits | State |
| --- | --- | --- | --- |
| V-001 / R-001, R-002 | Added the shared Markdown reference and catalogue trigger. | Source inspection: heading separation, four-space nesting, continuation attachment, code/template boundary and scoped review are explicit. Live consumer behavior not tested. | Verified by the coupled source/parser checks. |
| V-002 / R-001, R-002 | Connected all 14 other skill entries, current root guidance, scoped QC/verification, documentation and GitHub draft guidance to the shared owner. | Direct relative paths resolve to the bundled reference; local generic heading rules reconciled; task-specific hierarchy unchanged. | Verified by direct-entry and link checks. |
| V-003 / R-001, R-002 | Inspected 98 maintained/current Markdown files, including templates; no further formatting changes needed. Added scoped parser/source verification evidence. | All ten planned scenarios passed local assertions; 428 local path links resolve; literal non-Markdown code contents and task-derivation template unchanged. | Verified locally; live consumer behavior untested. |
| V-004 / R-001, R-002 | Built the committed-source release package and completed campaign navigation and reports before integration. | Unmodified workflow build produced 131 files matching Git byte for byte, including the new reference; SHA-256 verified. 113 support tests passed. | Coherent working boundary verified; merged-state checks and publication follow the Git boundary. |

## Verification scope and limits

The evidence script uses preinstalled Node and marked 17.0.5, not a new plugin dependency. It scans current Markdown candidates and checks representative parsed heading/list structures, task checklist nesting, mixed and wide numbered markers, continuation paragraphs and fenced blocks. Its negative fixtures reject missing heading blank lines and two-space children. One initial fixture incorrectly counted a second unspaced heading; it was corrected. The initial link scan also treated generated-template paths as live source links; parser-based link traversal now excludes literal code templates.

The scan is not a complete general-purpose Markdown linter or browser rendering test. ATX and Setext cases are covered; literal code/data is preserved. Verbatim root conversation transcripts, closed campaigns and the separate acceptance harness documentation are outside the maintained plugin-document check scope. Preservation of closed packages is checked from Git diffs without reading their contents.

All 113 support tests passed. The shared convention passes the strict standalone skill validator. Other skills' cross-skill bundled references are rejected as resource escapes by that isolated validator; these remain explicit plugin dependencies whose actual package-local targets passed the independent link checks. No claim of all-skills standalone conformance is made. See [skill results](evidence/skill-validation.json), [source/parser checks](evidence/source-checks.json), [verification script](evidence/verify_markdown.mjs) and [support log](evidence/support-tests.log).

No version/manifest change, release/tag creation or live acceptance was performed. Package verification passed; the full campaign tip must undergo the required merged-state checks before its explicit integration commit and target push.

## Composition and integration

The shared reference owns the two formatting rules. Direct skill entries expose its bundled path, existing local generic heading guidance points to that owner, and TASKS retains its checklist identity and parentage rules. Existing scoped QC and verification check presentation without replacing substantive review or granting repair authority. Current root orientation and README describe the same scope. No new skill, formatter or runtime plugin dependency was introduced.

Working source `640f26c` passed [final source checks](evidence/final-source-checks.json) and the actual committed [package build](evidence/package-check.json). Completing this report/index does not change shipped source or package inputs. The integration target was read back as `c9cee3d`; the complete report and all action commits will be included in the two-parent merge. The containing merge records final parent identities and completion; no post-closure report commit is required.

R-001 and R-002 are verified at the written-policy and local fixture level. Live consumer acceptance, browser rendering and isolated-skill portability beyond the explicit bundled dependencies remain unverified. No unresolved source finding remains within this campaign's accepted scope.

## Reopened amendment

The user explicitly reopened campaign 034 on 2026-10-09 to add blank lines around non-indented top-level lists and code blocks. The published starting checkpoint for this continuation is `8b9749c75b56eff028fee1575fdeaf917fe5d7f0`; the original campaign identity remains unchanged. Actions V-005 and V-006 in the amended plan are authorized for execution. State: reopened amendment implemented; local and committed-package verification passed; final integration/publication follows the containing Git merge boundary.


### Amendment execution evidence

| Action | Actual changes and evidence | State |
| --- | --- | --- |
| V-005 | Shared rule now requires blank lines around each entire non-indented top-level list and all code blocks, with compact nested lists and code attachment preserved. All 14 dependent skill summaries, root guidance and scoped QC checks carry the rule. Nine current documents/templates received separator lines; executable code contents and task identities are unchanged. | Implemented and locally verified. |
| V-006 | Extended verification with SC-011–SC-014 for list/code boundaries, compact nested lists, indented/fenced code and nested-code attachment. All 14 scenarios and 113 support tests pass. The shared convention passes its standalone validator. | Local and committed package checks passed; merged-state checks and publication follow the Git boundary. |

The source verification script reports its Git HEAD and working-tree changes separately. [Spacing helper](evidence/verify_spacing.mjs) is development-only verification using preinstalled marked; it adds no shipped formatter or runtime dependency. [Amendment support log](evidence/amendment-support-tests.log) retains the observed suite result. Tests for task-template preservation now compare its trimmed Markdown contents because the amendment deliberately adds a trailing separator blank line.

The scoped scan covers the same 98 current/active Markdown documents. Blank lines were inserted around whole top-level lists, not nested list boundaries. Marked confirms nested code contents and attachment; source/code preservation remains covered. EOF separator blank lines are intentional, so the diff check disables only Git's blank-at-EOF warning. Other whitespace checks remain active. Prior closed packages, version and manifests are unchanged; live consumer behavior remains untested.


### Amendment completion and integration

Committed source `229194a` passed [amendment source checks](evidence/amendment-source-checks.json): 98 scoped files, 439 local path links and all 14 scenarios. The [unmodified release build](evidence/amendment-package-check.json) produced 131 files matching that commit byte for byte, with a verified SHA-256 checksum. The support suite passed 113 tests. The complete amended report and evidence are committed before integration; the required prospective merge must match this complete campaign tip and pass the suite and scoped checks before commit/publication.

Actions V-005 and V-006 are verified for the written policy, source examples, local parser cases and committed package. The final two-parent merge records the continuation's parents and includes all amendment artifacts. No post-closure evidence commit is required. No unresolved in-scope source finding remains; live agent/browser acceptance and isolated-skill portability beyond explicit bundled dependencies remain unverified. Version is `0.15.0`.

## Reopened amendment — list-marker separator

On 2026-10-09 the user reopened campaign 034 from published main `77a82e04842f6f80bf770b359fc85ab40b77a74f` to require one space after each list marker. V-007 and V-008 are authorized; implementation, local checks and committed-package verification complete; integration/publication follows the containing Git merge boundary. The completed earlier boundaries remain retained as evidence.


### List-marker amendment evidence

| Action | Actual changes and evidence | State |
| --- | --- | --- |
| V-007 | Added exactly-one-ASCII-space marker separators to the shared convention, 14 dependent skill summaries, root guidance and scoped QC. Inspection found no existing violations in the 98 current documents/templates, so no content normalization was necessary. | Implemented and verified by current-source and parser checks. |
| V-008 | Added SC-015 and SC-016: bullet, numbered, nested and task-marker spacing; multiple-space/tab rejection; Markdown-template inclusion; code/data and horizontal-rule exclusions. All 16 local scenarios and 113 support tests pass; the shared convention passes its standalone validator. | Local and committed-package checks passed; merged-state verification and publication follow the Git boundary. |

The [marker checker](evidence/verify_markers.mjs) traverses parsed list tokens and explicitly labeled Markdown templates. It preserves indentation before markers, task checkbox states, literal code/data and non-list constructs. [Support evidence](evidence/marker-support-tests.log) records the suite result. This development-only checker adds no runtime plugin dependency. Current source check scope, historical-record preservation and live-consumer limitations remain unchanged.


### List-marker amendment completion

Committed source `966bc94` passed [marker source checks](evidence/marker-source-checks.json): all 16 scenarios, 98 scoped Markdown files and 443 local path links. The [unmodified release build](evidence/marker-package-check.json) produced a verified 131-file byte-for-byte package and checksum. All 113 support tests passed. The complete report and evidence are committed before the explicit merge; the prospective merged tree must equal the campaign tip and pass the suite and scoped checks before publication.

V-007 and V-008 are verified for source policy, local parser scenarios and committed packaging. The containing two-parent merge establishes final integration and includes all amendment artifacts. Version remains `0.15.0`; other closed records are unchanged. Live agent/browser behavior and isolated-skill portability beyond bundled dependencies remain unverified. No unresolved in-scope source finding remains.
