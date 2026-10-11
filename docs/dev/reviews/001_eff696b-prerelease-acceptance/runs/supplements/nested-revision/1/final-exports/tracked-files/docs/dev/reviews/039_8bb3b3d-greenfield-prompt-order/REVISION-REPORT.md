# Greenfield prompt order revision report

## Campaign and execution

- Campaign: `039_8bb3b3d`; baseline `8bb3b3da38471b21a385261edda898da191b86c9`; [accepted plan](REVISION-PLAN.md).
- Working branch: `revision/039_8bb3b3d-greenfield-prompt-order`; target: `revision/037_a6c42dd-prerelease-review`.
- V-001: moved “Preliminary project description:” and its complete fenced placeholder after the explicit GitHub tracking instruction, immediately before the copied prompt’s outer closing fence. Operating instructions now precede the description as one contiguous group. Wording and placeholders are preserved.
- Original completion state: V-001 complete; direct source and local support checks pass. Final integration/publication facts are recorded in Git. No separate findings or review report are fabricated for the directly accepted amendment.

## Verification and integration

- Exact baseline comparison verifies that only the complete description block’s position changed; its heading, fenced text and trailing blank line moved verbatim. All instructions and placeholder counts are unchanged.
- Inspected inner three-backtick and outer four-backtick fences, blank lines after the header/around code blocks, active campaign links and Markdown markers. Current README link resolves and no navigation target changed.
- Release-workflow archive selection still includes the same root template; actual staged-tree archive extraction matches the revised file. Canonical and legacy manifests are byte-identical.
- Declared support suite: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`; 113 tests passed in 16.100 seconds, exit 0, Python 3.12.14. The subsequent trailing blank-line adjustment was directly rechecked; support code/assets were unchanged.
- Whitespace check and full path diff verify the change is confined to the template, this campaign and current index. Earlier campaign files remain unchanged. Final action identity, explicit two-parent merge, merged-state evidence and target publication are retained in Git. No live consumer comparison or client loading is selected; an ordering change does not establish improved compliance.

## Stopping boundary

Campaign 037 remains suspended and its records are unchanged. Main integration, product release and changes to earlier campaigns are outside this amendment.

## Authorized reopening: V-002

The human reopened this campaign for the accepted prompt improvements and token clarification. Amendment source/target checkpoint: `7f06904ea47eb1f7f2243e34d24b74f2aa7c24fa`. Original V-001 observations/results above remain historical evidence.

V-002 revises persistent authorization while preserving human reviews, execution boundaries and later scope changes; states eligible-phase projection/readback before implementation with a concrete blocker; and explains optional token supply outside the copied prompt. Guidance separates Git access from API access and authentication/permission recovery from unsupported adapter operations. The five-block order and all placeholders remain intact. State: V-002 complete with local checks passed; final action/merge/publication identities are retained in Git.

- Direct inspection and assertions verified all five blocks in their accepted order, unchanged placeholder set, description-last nested fences, explicit checkpoint/scope preservation, required readback/blocker wording, and separate optional-token/capability guidance. Aligned with current tracking-decision and phase-activation owners; no second enable question or automatic future-phase projection introduced.
- Active campaign links resolve; Markdown heading/marker/fence separation and whitespace checks pass; root manifest copies remain identical. Release-shaped staged-tree archive contains the revised template exactly.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: 113 tests passed in 16.351 seconds, exit 0, Python 3.12.14.
- Full amendment diff is limited to four owned paths: template, current index and this explicitly reopened campaign’s plan/report. Other campaigns remain untouched. No live agent/provider acceptance is selected or inferred. Prospective merge checks and final target publication are retained in the integration commit/Git refs.

## Authorized reopening: V-003

The human accepted the explicit phase activation reference and reopened campaign 039. Amendment source/target checkpoint: `f64e7eb3e6286f9d7ed74d74401e45ee24d3a6f1`. V-001/V-002 results remain retained as historical action evidence.

V-003 names sdd-manage’s phase activation workflow in the tracking paragraph, applies it before each eligible phase and explicitly stops affected implementation when the prerequisite cannot be satisfied. State: V-003 complete with local checks passed.

- Exact comparison against the reopening checkpoint verifies the accepted tracking paragraph is the only template change. All other wording, token guidance, placeholders, five-block order and final description/fences are unchanged.
- Inspected current phase-activation owner: eligible-phase projection/readback precedes affected execution; incomplete/unknown projection blocks execution and later phases are not activated in advance. The prompt now names that owner without duplicating its detailed procedure.
- Markdown/links and whitespace checks pass; manifests remain byte-identical. Release-shaped staged-tree archive extraction matches the amended template; four authorized paths only, no other campaign edits.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`: 113 tests passed in 16.022 seconds, exit 0, Python 3.12.14.
- Final prospective merged-state evidence, parents, merge and target publication/containment are recorded in Git. Campaign 037 remains suspended; no live agent/provider acceptance, main merge or release is implied. Final action and explicit parent integration/publication facts are retained in Git. No live compliance claim is made.
