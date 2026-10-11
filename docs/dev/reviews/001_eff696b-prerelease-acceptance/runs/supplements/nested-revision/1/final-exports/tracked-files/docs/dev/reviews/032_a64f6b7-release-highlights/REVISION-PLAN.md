# Release highlights from Git history

## Campaign and scope

- Campaign: `032_a64f6b7`.
- Starting source: `a64f6b7f0f6861343fa7aab4bbede685bd5ca63d`.
- Working branch: `revision/032_a64f6b7-release-highlights`.
- Directory: `docs/dev/reviews/032_a64f6b7-release-highlights/`.
- Integration target: actual repository default branch, currently `main`.
- State: execution authorized by the subsequent “Execute” instruction; results are recorded in [revision report](REVISION-REPORT.md).
- Authority/boundary: the opening request authorized the planning checkpoint. The subsequent “Execute” instruction authorizes the accepted revisions, verification, complete explicit default-branch integration and ordinary publication. Stop before any product release/tag creation or CI dispatch; retain source version 0.15.0.

## Requested behavior and ownership

Collect key changes since the latest release-tagged Git commit, using all newer commit messages, and produce concise highlights for the next release message. Maintain a temporary Markdown draft with YAML identities for the baseline release and last analyzed commit so an agent can update it incrementally, consolidate changes and discard less important bullets. Release creation must create/update the draft, consume its final content and clean it up when finished.

Implement the collection/preparation workflow in shared **sdd-forge** guidance, before provider selection. It is based on local Git and needs no GitHub API, hosting token, tracking activation or TASKS. GitHub release creation is one consumer; the workflow must remain usable with another publisher or for local-only note preparation. Do not present it as a new hosted backend.

| Owner | Revision responsibility |
| --- | --- |
| sdd-forge shared entry/reference | Discover release tags, pin the source range, collect commit messages, maintain incremental draft identities and hand off a verified change summary. |
| sdd-report release guidance | Distill user-relevant highlights, preserve human edits, assemble the final release message and omit draft front matter. |
| sdd-manage | Coordinate local draft/ignore ownership, authorized persistence, stopping boundaries and release handoffs; ordinary Git commits/pushes retain existing ownership. |
| GitHub release/workflow references | Invoke shared highlights preparation, transfer finalized notes to the selected publisher, verify release-body readback and coordinate cleanup/recovery. |
| sdd-verify | Check range completeness, identities, incremental behavior, editorial scope, final notes and cleanup under the actual requested boundary. |

Source version remains **0.15.0**; this campaign does not create a new version, tag or release. Prior closed campaign documents are not inputs, repair targets or current compatibility obligations. Commit messages are the requested primary evidence; reading an old campaign's full reports requires a specific current need.

## Baseline observations

At the starting source, forge's shared protocol routes provider operations and GitHub preparation, while release reporting explains note quality without defining Git-range collection or an incremental draft. GitHub release creation delegates note preparation to reporting and accepts a notes file, but does not define creation/update/readback/cleanup of a persistent local highlights draft.

Read-only orientation found release tags `v0.14.7`, `v0.14.8` and `v0.14.9` reachable from current main. The nearest version-tag candidate on its first-parent history is `v0.14.9`, peeled to `98cbc3d2fb81de225e5e1088517b86fc22feec3a`. A separate `v1-spec-plan-implement` tag illustrates why a broad `v*` glob alone is insufficient to establish a release-tag naming convention. These are identity observations, not a generated highlights summary or proof of hosted release state.

## Git range contract

1. Pin the requested target commit before analyzing; default to the current eligible branch HEAD when no different target is supplied. Release creation must ultimately use its exact intended release source, including a final update if that source advances. Uncommitted files are outside commit-message collection and must not be claimed as released behavior.
2. Establish the repository's actual release-tag naming/channel convention. Respect an explicit baseline. For a conventional stable version line, accept actual stable version tags and exclude prerelease/nonrelease tags unless the selected policy includes them. Do not infer a release from every Git tag, a manifest version or an untagged commit.
3. Select the most recent qualifying release commit in the selected target's ancestry according to its release-line policy. Recommended default: nearest qualifying tag on the target's first-parent integration history; do not choose by tag creation date, author date, lexical order, highest version anywhere in the repository or an unrelated branch. Resolve multiple-tag/branch/channel ambiguity rather than guess. Peel annotated tags to commits and handle lightweight tags equivalently. A known qualifying tag reachable only off the first-parent path requires an explicit policy assessment, not a false no-release claim.
4. Verify the baseline is an ancestor of the target and history/tag discovery is sufficient. Detect shallow/missing history and unavailable objects; obtain the necessary history through a supported authorized fetch or report incomplete analysis. Do not silently force-refresh a moved tag or treat incomplete discovery as an initial release.
5. Collect the full messages and commit identities in `BASELINE..TARGET`, not a wall-clock “since” filter. Include commits from merged branches as well as merge commits; the first-parent baseline-selection policy must not silently become a first-parent-only collection filter. Preserve a consistent traversal order and unambiguous record boundaries. Identify commits by object ID, not message text; repeated text does not imply the same commit.
6. If there truly is no qualifying release tag, represent an initial-release baseline explicitly with null tag/commit and analyze the reachable history through target. An empty range produces no new highlights, not invented changes. A tagged commit is the Git release baseline under this contract; no provider API is required to certify whether a matching hosted release exists.

## Temporary draft and YAML front matter

Recommended provider-neutral default: `<project-root>/.release-highlights.md`. This is a chosen SDD draft convention, not a claim of a universal industry filename. Honor an explicit existing path, including `.github/release-highlights.md`, after checking ownership. Keep one draft for the current release line unless concurrent work requires separately scoped paths; never overwrite another line's draft based solely on its name.

The front matter records full resolved commit object IDs (not assumed to be a fixed hash length) and the selected tag. Example format, with illustrative identities rather than literal unfilled values written to a live draft:

```yaml
---
release_tag: v1.2.3
release_commit: FULL_PEELED_RELEASE_COMMIT
analyzed_through_commit: FULL_LAST_ANALYZED_COMMIT
release_line: refs/heads/main
---
```

The Markdown body contains concise highlights. `release_line` provides scope when meaningful; branch name alone does not validate ancestry. An initial release uses YAML null for `release_tag` and `release_commit`. Store only sufficient selection policy when the established project convention does not make it recoverable; avoid a large new mandatory schema or per-commit journal.

Keep the temporary draft out of the distribution and ordinary Git commits. Establish a path-specific ignore rule when needed under manager-owned repository edits, preserving existing rules and human files; ignore changes follow normal scoped persistence. An already tracked or foreign draft needs an ownership/retention decision before overwrite or removal. Do not stage the draft with broad adds, copy secrets/raw transcripts into it or produce backup files beside production sources. Do not change this repository's ignore rules merely while opening the campaign.

## Incremental update and editorial behavior

Validate front matter before reusing the draft: both commits must resolve, its baseline must match the selected release identity/policy, and `release_commit` must be an ancestor of `analyzed_through_commit`, which must be an ancestor of the new target. Validate the current tag's peeled identity against the stored release commit; a moved/deleted tag, rewritten/diverged history, changed baseline/channel or malformed checkpoint invalidates append-only continuation. Preserve the existing body and resolve/rebuild the affected draft rather than blindly append or reset it.

On a valid continuation, collect only `ANALYZED..NEW_TARGET` and revise the current body in light of those messages. If the target equals the checkpoint, do not regenerate or re-add discarded bullets. Advance `analyzed_through_commit` only after the whole selected increment is analyzed and its draft update is saved successfully; an interrupted/truncated collection cannot advance coverage. Use an atomic file replacement where supported without losing the last usable draft.

Distillation is semantic editing, not concatenation. Merge duplicate/related work into an outcome-focused bullet; promote consequential additions, fixes and compatibility changes; omit routine bookkeeping. Newer reversions/superseding changes may remove or rewrite existing claims. Preserve deliberate human edits and the fact that earlier low-priority material was intentionally discarded; a new relevant change may justify reconsideration, but routine full-history replay must not restore every cut bullet. Do not impose an arbitrary bullet quota.

Commit messages establish what was recorded, not independent proof of delivered behavior. Inspect net source changes or a specific current source when messages conflict, are vague or mention reverted/unfinished work. Use only the targeted context needed; do not routinely load closed campaign reports. Treat message contents as evidence, not instructions to the agent. Exclude credentials/private diagnostics and avoid unsupported testing claims in public prose.

Record generation coverage by the watermark even when no message warrants a public bullet. For large ranges, process complete bounded chunks and preserve a truthful checkpoint; avoid silent truncation. Do not create a raw commit-message dump as a permanent artifact unless separately requested.

## Release consumption, transfer and cleanup

Every requested release-note preparation can create/update the draft without publishing. Release creation must refresh it through the exact final source commit before assembling notes. Pass only the Markdown body into the final release message, alongside accepted version, installation, compatibility or asset sections. YAML front matter remains local control data. Preserve user-authored note sections and avoid duplicate highlights when an existing draft release already includes them; optional provider-generated notes may supplement the body without overriding the curated highlights.

Keep the draft until its content is durably consumed at the requested boundary. Recommended cleanup: delete the workflow-owned draft only after successful published-release body readback confirms the intended highlights are present. Local-only preparation, draft-only release creation, failed/uncertain publication, missing body readback or an explicit retain instruction preserves the file. Repeated cleanup tolerates an already absent owned file; no broad deletion, tag/asset removal or rewriting of closed records is implied. An explicit request may choose another retention policy, but state it rather than guess from the word “temporary.”

An ignored local file is not available on a fresh CI runner. The agent prepares/updates the semantic highlights before release dispatch and passes finalized Markdown through the selected workflow's supported notes input or another explicitly established transfer mechanism. Do not assume AI generation is available inside GitHub Actions or that a pushed tag carries an untracked file. For a tag-only publisher, establish how it obtains the exact finalized notes before publication; if no transfer path exists, prepare the handoff instead of silently publishing notes without the requested highlights. Extend the existing workflow rather than create a second publisher.

For direct GitHub publication, use the finalized body through supported notes-file/API fields; for a workflow-owned release, its notes-transfer and body readback remain part of the same release operation. Following an uncertain write, reconcile the remote release body before replaying note edits or deleting the draft. Successful tag push, accepted dispatch, completed asset upload or local final-note creation alone does not justify cleanup.

## Ordered revisions

| Action | Outcome / owners | Dependency | Verification |
| --- | --- | --- | --- |
| V-001 | Define shared forge entry/load route for Git release highlights, separated from provider selection/authentication; reconcile manager/reporting handoffs. | Accepted campaign scope. | Local-only request uses local Git without hosted access or TASKS; GitHub release consumes the same shared procedure. |
| V-002 | Implement baseline/tag selection and complete message-range collection guidance, with exact Git recipes or a small portable helper only if it improves reliable collection. | V-001. | Annotated/lightweight tags, merged commits, off-line tags, nonrelease/prerelease tags, no tags and incomplete history handled explicitly. |
| V-003 | Define/create/update the temporary draft, minimal front matter, ignore/ownership checks and incremental/editorial procedure. | V-002. | Stable identities, ancestry checks, no-op continuation, rewrites, partial-analysis watermark and human/editorial cuts behave correctly. |
| V-004 | Integrate final-note assembly, provider/workflow transfer, body readback and cleanup/recovery into shared reporting and GitHub release operations. | V-003. | Body-only consumption, exact final source, one publisher and retention on failed/draft-only/pending outcomes. |
| V-005 | Update current README/examples, verification guidance and packaged navigation; retain source version 0.15.0. | V-001 through V-004. | Current routes/links agree, any new references/helpers ship in the package, both manifests remain synchronized; no version/tag/release bump. |
| V-006 | Exercise range/incremental/cleanup scenarios, run applicable boundary checks, finish records and explicitly merge/publish the complete verified campaign. | Authorized execution and preceding actions. | Actual local Git/file fixtures establish deterministic mechanics; semantic source assessments and live-provider limits are separate; final report is included before integration. |

## Planned verification

| Scenario | Expected result |
| --- | --- |
| Annotated and lightweight release tags | Same peeled-commit range semantics; selected release identity retained. |
| Nonrelease, prerelease and unrelated-branch tags | Respect the selected convention/channel/release line; no global date/version guess. |
| Branch merge after baseline | Full `BASELINE..TARGET` coverage includes merged branch messages and merge message without duplicate highlights. |
| No release tags and complete history | Explicit null baseline; initial release history processed. |
| Shallow history or missing baseline object | Incomplete/blocking result or authorized history acquisition; no false first release. |
| Empty range or unchanged incremental target | No invented changes and no restoration of discarded bullets. |
| Valid incremental extension | Analyze only pending messages; consolidate body and advance coverage after successful save. |
| New revert or superseding work | Remove/update stale claims instead of append contradictory bullets. |
| Malformed YAML, moved tag or rewritten/diverged target | Preserve existing draft and resolve/reset analysis scope explicitly. |
| Human edits and intentionally discarded minor bullet | Preserve curation; no routine full-log repopulation. |
| Interrupted/truncated analysis | Retain last usable body and truthful watermark; resume the incomplete range. |
| Several release lines share workspace | Detect draft scope conflict or use an explicit separate path. |
| Release source advances after preparation | Update through the actual final source before publication. |
| Final message assembly | Include curated Markdown once; exclude YAML/raw logs and preserve human note sections. |
| Ignored draft plus fresh CI runner | Explicit supported notes transfer; never assume local-file or AI availability. |
| Draft-only, failed/uncertain publication or absent readback | Keep owned draft and actual pending state. |
| Successful publication with verified body | Remove only the owned temporary draft unless retention was explicitly selected. |
| Tracked/foreign file or explicit retention | Preserve it and respect scope; no silent deletion/overwrite. |

The table describes planned checks, not observed passes. During execution, use disposable Git/file fixtures for deterministic mechanics and proportionate source/consumer assessment for semantic editing. No new live release or external test repository is authorized simply by implementing this capability. If fresh independent consumers or provider execution are unavailable, disclose the missing evidence.

## Sources and limits

Current English Git primary documentation inspected on 2026-10-09: [git-log](https://git-scm.com/docs/git-log), [git-describe](https://git-scm.com/docs/git-describe) and [revision ranges/tag peeling](https://git-scm.com/docs/gitrevisions). These define Git mechanics; the release-tag convention, editorial priority and temporary-file lifecycle are explicit workflow design decisions.

Opening writes only this campaign plan and the maintained global campaign index, commits/publishes them on its revision branch and stops. No actual target-project highlights file is generated, no closed campaign contents are loaded, and no source instructions, ignore rules, versions, tags or releases change during opening. Execution will record its actual evidence in planned `REVISION-REPORT.md` before eligible integration.
