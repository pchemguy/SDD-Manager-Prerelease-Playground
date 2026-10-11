# Workflow branch manager and artifact lifecycle revision plan

## Campaign and decisions

- **Campaign:** `007_df531c2`; date 2026-10-02.
- **Starting/reviewed baseline:** `df531c2cdd4b192832a1be4a7ab9f8c71ad16947`.
- **Planning checkpoint:** `b5a8e53f3e88d7feb907b17d25e06d94af962a85`.
- **Review:** [REVIEW-REPORT.md](REVIEW-REPORT.md); R-001–R-005 accepted with the Git-only follow-up.
- **Authorization/state:** Plan and execute the revision, including verification, commits/pushes, and explicit integration; Completed.
- **Evidence:** [REVISION-REPORT.md](REVISION-REPORT.md), including checks, limits and published merge evidence.

## Accepted implementation policy

| Concern | Decision |
| --- | --- |
| Owner | sdd-manage owns a focused branch-management reference; local Git lifecycle has no new forge/backend dependency. |
| Revision/steering identity | `revision/###_xxxxxxx-<slug>` matches `docs/dev/reviews/###_xxxxxxx/` exactly. Steering needs a minimal revision record, not fabricated review/plan stages. |
| Feature identity | `feature/###_xxxxxxx-<slug>` matches reserved `docs/dev/features/###_xxxxxxx/` package identity. Allocate at preparation and record full starting SHA. |
| Allocation | One next-unused repository-wide campaign sequence across reviews/features, preserving all established identities. Full baseline in records; abbreviated SHA stable and uniquely resolvable. |
| Main phases | `phase/#-<slug>`, using owning phase number/name from PLAN/TASKS. Main documents remain in docs/dev. Establish the actual main integration branch explicitly. |
| Phase boundaries | Bounded task/milestone requests commit/push and pause on the phase branch if the phase is incomplete. Merge only after verified full phase exits; create next phase from updated main only when further work is authorized. |
| Active feature files | Keep current active FEATURE documents in docs/dev, with package identity/branch recorded in existing context. Separate branches/worktrees isolate concurrent packages; never overwrite another active package in the same worktree. |
| Feature archive | Retain completed, incorporated documents under the allocated feature directory, preserving basenames, links and historical evidence. Archive on the feature branch after document/task incorporation and before final Git integration. Partial/document-only incorporation does not archive unrelated active sources. |
| Compatibility | Project/user naming overrides remain explicit; never rename legacy/in-flight branches or campaign directories automatically. Continue compatible existing branches; disambiguate colliding slugs without changing identity. |
| Selected targets | Steering targets paused branch; features/revisions target the established integration or active phase branch. Names select no target and do not imply completion. |

A feature package may have a small identity/navigation record at preparation in its reserved directory, while active FEATURE sources remain at their established root paths. This makes the directory/branch association durable without relocating all active authoring paths. Archived task snapshots are historical, never a second executable owner. No parallel state registry or new task identity is introduced.

## Ordered revisions

| Action | Findings | Owners and outcomes | Dependencies / acceptance |
| --- | --- | --- | --- |
| V-001 | R-004, R-005 | Add workflow identity/naming convention; align review allocator across reviews/features and discoverability. | Stable shared identity, valid names, minimal steering record, overrides/collisions and legacy continuity explicit. |
| V-002 | R-001, R-003, R-005 | Extract branch setup into sdd-manage branch-management.md; align Git protocol, workflow/range/completion and coordinator handoffs for phase-sized integration. | V-001; no backend dependency, push-first preserved, incomplete phase pauses, next phase needs authorization and published prior phase. |
| V-003 | R-002, R-004 | Align feature preparation/package identity, incorporation/archive gates, steering record, and reporting fields. | V-002; active sources retained until safe, historical archive not executable, partial integration does not broaden scope or force archive. |
| V-004 | R-001–R-005 | Align README/capability/examples; run source, consumer, Git/archive fixtures and package checks; retain revision evidence and dispositions. | V-001–V-003; record actual outcomes and limits, then explicitly merge/publish the verified boundary. |

No consumer PROJECT/SPEC/PLAN set exists here. Update existing skill/document owners; preserve earlier review evidence and all campaign records. This repository revision uses `revision/007_df531c2-workflow-branches`, targeting its established `feature/architecture-revision`; it does not rename that legacy development target to main.

## Verification

| Scenario | Objective recheck |
| --- | --- |
| SC-001: Identity allocation and names | Inspect both campaign collections; preserve existing numbers; baseline and branch/directory match; validate Git names; resolve collision/override without automatic legacy rename. |
| SC-002: Partial phase range | Task/milestone request pushes completed work and pauses; main remains unchanged and no next phase branch appears. |
| SC-003: Phase complete and next phase | Verify exits, explicit two-parent merge and publication; authorized next phase branches from resulting main tip. Failed exits or absent authorization prevent transition. |
| SC-004: Steering | Minimal review-directory record matches revision branch; direct amendment merges into paused phase branch and stops without completing phase or resuming tasks. |
| SC-005: Feature preparation | Active root documents and reserved package identity coexist; full branch/source context is recoverable; concurrent package cannot overwrite active files. |
| SC-006: Archive | Completed incorporation transfers task ownership once, moves eligible documents and updates links, retains historical evidence, verifies archive as non-executable, and publishes via same final feature boundary. |
| SC-007: Partial/interrupted incorporation | SPEC-only or unfinished feature task request retains active package/tasks; interrupted moves resume from actual Git paths, preserving unknown/unselected sources. |
| SC-008: Git-only operation | Disposable bare remote supports branch publication and explicit integration without a hosting backend; normal push remains owned by execution/coordinator persistence. |
| SC-009: Composition | All affected source/metadata/links and package validators pass; generic merge-on-any-range instructions no longer contradict phase pauses or narrow feature scope. |

Use fresh consumer interpretation, disposable local Git repositories and synthetic feature documents. Separate actual primitive/fixture execution from complete installed-client behavior; do not infer policy enforcement from a helper that merely encodes the expected answers. No live host mutation, production migration, or branch deletion is required.

## Execution and publication

1. Persist plan, then establish the named scoped revision branch from the current accepted target checkpoint, preserving unrelated work and current credentials.
2. Execute actions in order. Update revision report after each, run appropriate checks, commit/push and verify remote containment before dependent work.
3. Recheck full scope and all applicable scenarios. Preserve verified results and report blocked/untested surfaces precisely.
4. Refresh target, perform one explicit non-fast-forward merge with prospective merged-state verification, commit/push and verify target containment. Record parents and actual publication; retain all artifacts in this campaign directory.
5. Stop at this revision boundary. Do not execute a consumer phase, relocate legacy campaign records, delete branches, or create a hosted branch-management capability.
