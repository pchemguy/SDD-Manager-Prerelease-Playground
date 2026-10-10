# Standalone authorization policy removal

Campaign `028_5e2624e`; baseline `5e2624e625e33410245cb3b51b1b31120ad18747`. Working branch: `revision/028_5e2624e-remove-authorization-policy`; target: `main`. The [accepted plan](REVISION-PLAN.md) entered directly from the user's removal request; no separate review or conversation copy was created.

## V-001 results

Deleted `skills/sdd-manage/references/revision-authorization.md` and its manager navigation row. Removed the standalone-policy prerequisites and reconciled callers in coordination, credentials, Git integration, default preparation, review/revision, implementation startup/completion/environment recovery, forge, root AGENTS and README.

Existing owners retain concise operational guidance: coordination carries request scope and limits; credential recovery keeps the same destination/payload and distinguishes authentication failure from denial; Git recovery preserves blocked work and reports actual remote effects. No replacement policy file, first-request approval protocol or new authorization registry was added. Project preparation/default publication gates, partial-phase stopping, optional hosted tracking confirmation and protected credentials remain with their established owners.

Six historical Markdown links now point to the immutable pre-removal source commit; historical observations, proposals and source inventories remain baseline evidence rather than current dependencies.

## Verification and limits

- Standalone file absent; no active path references or separate authorization-policy prerequisites remain in skills, README or AGENTS.
- Actual local Markdown links and heading anchors resolve across 81 active/campaign files at the source check; code examples are excluded from link parsing.
- Canonical and temporary legacy manifests remain byte-identical, version `0.15.0`.
- Whitespace checks pass. All 113 existing support tests pass on the revised working source.
- Source composition inspection confirms the retained handoff/recovery owners and unchanged preparation/integration/hosting boundaries. This is source and support verification, not fresh consumer or live host acceptance.

Planning checkpoint `401a42e8b9a3c9f3b179643d1a30f0527edfcb83` was published before source edits. Source and this report are committed/published together before the explicit two-parent merge. Merged-state checks, actual merge SHA and target publication are recorded in Git and the completion response; no extra report commit is created after final integration. The complete campaign tip, including these records, must be contained in published main before reporting completion.
