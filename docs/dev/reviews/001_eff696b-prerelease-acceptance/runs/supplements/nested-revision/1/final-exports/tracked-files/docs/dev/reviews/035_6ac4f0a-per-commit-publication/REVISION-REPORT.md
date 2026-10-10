# Per-commit publication revision report

## Campaign and result

- Campaign: `035_6ac4f0a`; baseline: `6ac4f0a0b7d6fd198f9116d62c1084951f26ad5a`.
- [Accepted plan](REVISION-PLAN.md); branch: `revision/035_6ac4f0a-per-commit-publication`; target: `main`.
- The user authorized the focused change on 2026-10-09. Planning commit `32da6c3` was pushed/read back before source work, after restoring the missing temporary authentication helper from this repository's ignored credential file.
- State: shared rule and handoffs implemented; support suite, document/link and committed-package checks passed; final integration/publication is established by the containing Git merge boundary. Version remains `0.15.0`.

## Revision evidence

| Action | Actual changes | Evidence and limits |
| --- | --- | --- |
| V-001 | Added the canonical per-commit publication rule to Git workflows. Manager entry/coordination, review/revision handoffs, campaign report templates, implementation ancillary commits and steering now route to it; README and AGENTS expose the same cadence. | Source review confirms every owned commit must be pushed/read back before advancement or another commit, including independent work. Local-only exceptions are explicit and scoped; recovery and merge/acceptance boundaries remain intact. |
| V-002 | Ran the mandatory support suite and assessed the eight planned source scenarios. | [113 support tests passed](evidence/support-tests.log). Written-policy assessment is distinct from live consumer execution. Changed-document link/style and committed-package checks passed; merged-state checks follow the Git integration boundary. |

## Scenario assessment

| Scenario | Assessed current owner / result |
| --- | --- |
| SC-001 | Implementation's per-task barrier retained; shared rule also covers ancillary/report commits. Satisfied in source. |
| SC-002 | Coordination references the canonical rule for preparation/maintenance. Satisfied in source. |
| SC-003 | Review units and revision actions explicitly publish before independent as well as dependent work. Satisfied in source. |
| SC-004 | Canonical scope includes steering, feature incorporation, reports and merges; direct calls use the same Git protocol. Satisfied in source. |
| SC-005 | Pending/failed/uncertain publication retains the commit, reconciles readback/recovery and pauses advancement/further commits. Satisfied in source. |
| SC-006 | Eligible outstanding workflow commits are resolved first; branch/tool/workflow workarounds are prohibited. Satisfied in source. |
| SC-007 | Explicit user-directed local-only/deferred publication overrides cadence within its scope; unpushed state is reported accurately. Satisfied in source. |
| SC-008 | Inspection, push/readback and scoped recovery remain allowed; no per-commit merge or human-acceptance change. Satisfied in source. |

## Limits and integration

This is a source-policy revision, not a live agent acceptance run. No new tests that mirror prose, formatter, dependency, version change, release/tag or hosted tracking change was introduced. Other closed campaign records remain unchanged and outside routine context/validation. The complete report/navigation and evidence are committed and published before the explicit two-parent merge; the prospective merged result must equal that complete tip and pass required checks before target publication. No post-closure report commit should be left outside that merge.


## Composition and verified boundary

Source commit `78a6c2e` was pushed and read back before package/report work. [Source checks](evidence/source-checks.json) passed for 11 changed Markdown documents and 125 current local links/anchors; [the verification script](evidence/verify_documents.mjs) also checks block separation and list-marker spacing, including Markdown templates. Its first attempt incorrectly required a leading blank line after stripping YAML metadata; the checker was corrected to honor document-start behavior. No source repair was required for that false positive.

The [unmodified release workflow build](evidence/package-check.json) produced 131 files matching committed Git bytes and a verified SHA-256 checksum. Version/manifests remain `0.15.0`. Other closed package paths are unchanged. The eight planned scenarios are satisfied by source assessment; no fresh consumer behavior was tested.

V-001 and V-002 are verified for the written workflow policy, current document structure/links, mandatory support suite and committed package. The final merge includes this full report and all action commits; its parents and merged-state checks are recorded in the Git boundary, with remote readback establishing publication. No post-closure report commit is required. Live agent compliance remains unverified; no unresolved in-scope source finding remains.
