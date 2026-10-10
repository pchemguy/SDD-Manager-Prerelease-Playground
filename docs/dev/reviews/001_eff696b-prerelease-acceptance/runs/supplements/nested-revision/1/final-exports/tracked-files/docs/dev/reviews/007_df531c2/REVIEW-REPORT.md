# Workflow branch identity and artifact storage proposal review

## Campaign and scope

- **Campaign:** `007_df531c2`; date 2026-10-02.
- **Starting and inspected baseline:** `df531c2cdd4b192832a1be4a7ab9f8c71ad16947`.
- **Input:** Proposed workflow-specific branch names, steering campaign storage, feature archival, phase branches, and backend involvement.
- **Mode:** Focused proposal/source review; no separate review plan, independent external research, consumer execution, or live hosting mutation.
- **Authorization:** Review and persistence of findings only. No new convention, revision plan, source implementation, branch migration, or artifact relocation is performed.
- **Scope:** Git workflow ownership; three-workflow model; review campaign identity; feature incorporation/source retention; task selection/hierarchy; current forge operation boundary.

## Assessment

The proposed branch names provide useful durable association with workflow artifacts. Revision and steering can share review-campaign identities; feature branches can share a feature-package identity. Main governing documents should remain in docs/dev while phase branches deliver the accepted whole incrementally.

Use a shared workflow identity/naming convention for invariant names, sequences, baselines, slugs, and storage. Extend sdd-manage's workflow/Git procedures to apply it at entry, continuation, and completion. A convention alone cannot resolve the new phase integration boundary, archive conditions, or backend lifecycle handoffs.

The primary operational change is phase-sized integration: a requested task/milestone range can finish and pause without merging the unfinished phase. The current default integrates the completed selected range. The archive proposal also changes current feature cleanup, which permits removing incorporated sources once no active work needs them. Backend ownership needs an explicit separation: local branch creation/checkout/merge are Git work, while optional hosted ref inspection or remote branch management can belong to sdd-forge when that capability is actually defined.

## Proposed naming and storage

| Workflow | Proposed branch | Artifact location / lifecycle | Integration target |
| --- | --- | --- | --- |
| Revision | `revision/###_xxxxxxx-<slug>` | `docs/dev/reviews/###_xxxxxxx/`; branch identity exactly matches campaign directory. | Established correction target; main integration branch or active phase as appropriate. |
| Steering | `revision/###_xxxxxxx-<slug>` | Same review campaign convention; a minimal amendment record can establish identity/context without mandatory review/plan stages. | Paused implementation branch; return control after integration. |
| Feature | `feature/###_xxxxxxx-<slug>` | Allocate stable identity at preparation; retain completed incorporated feature documents under `docs/dev/features/###_xxxxxxx/`. Resolve active-package placement explicitly. | Established feature target; do not infer it from the prefix. |
| Main phase | `phase/#-<slug>` | Full intended PROJECT/design/SPEC/PLAN/layout/TASKS remain in docs/dev; phase evidence follows existing owners. Phase number/name comes from accepted hierarchy. | Project's explicitly established main integration branch; do not infer a branch named main from workflow terminology. |

The full starting SHA remains inside artifacts; directory and branch retain the same stable abbreviated baseline as HEAD advances. Descriptive slugs should be concise, lowercase, and hyphen-separated; validate names with Git and preserve established identities on continuation. These are recommended articulation rules for the later plan, not implemented names.

## Findings index

| Finding | Type | Priority | Status |
| --- | --- | --- | --- |
| R-001 | Integration-boundary decision | P2 | Proposed |
| R-002 | Feature archive/ownership decision | P2 | Proposed |
| R-003 | Git/backend responsibility decision | P2 | Proposed |
| R-004 | Lightweight revision identity/record decision | P3 | Proposed |
| R-005 | Identity allocation and compatibility clarification | P3 | Proposed |

These priorities describe required policy precision, not demonstrated runtime defects.

## Canonical findings

### R-001 — Make phase completion the main integration boundary

- **Evidence:** git-workflows.md, Work and prepare the boundary and Merge/verify/publish; range-selection.md; workflows.md, bounded implementation operation. Current selected task count/milestone/phase boundaries normally integrate when completed.
- **Conflict:** Under the proposal, implementing two tasks inside an incomplete phase must not merge that phase into main or create the next phase branch. Treating every stop as an integration event would defeat phase isolation.
- **Recommendation:** For main development, execute bounded requests on the owning phase branch. Commit/push tasks and stop at the requested range; pause without integration until full phase scope and exit evidence are complete. Explicitly merge/verify/publish the completed phase, then create the next phase branch from the updated main checkpoint only when further execution is authorized. Never start the next phase merely because the previous phase ended.
- **Composition:** Steering targets the paused phase branch. A feature or correction targeting that phase does not by itself establish phase completion; phase acceptance must include incorporated effects. Cross-phase requests should be split into authorized sequential phase boundaries rather than using one implementation branch for multiple phases.
- **Recheck:** Next-two-task, milestone-only, phase-complete, phase-exit failure, cross-phase range, and interrupted phase merge cases retain scope and produce exactly the appropriate integration/continuation behavior.

### R-002 — Define active feature placement and archive eligibility

- **Evidence:** feature-incorporation.md, Scope and cleanup and interrupted incorporation; workflows.md, Feature sequencing. Active sources and FEATURE-TASKS are retained while needed; source cleanup currently permits removal rather than obligatory archive retention.
- **Gap:** The proposed completed-package archive does not yet specify active source location, partially incorporated features, link repair, or when archived checklists cease to be executable owners.
- **Recommendation:** Allocate feature identity before dependent work. Prefer retaining current active FEATURE documents in docs/dev for this revision, record their package identity/branch explicitly, and move them into the feature archive only after complete accepted incorporation and task/evidence disposition. An alternative is campaign directories from creation, but that broadens authoring/discovery paths across skills and should be a deliberate separate choice.
- **Archive gate:** No remaining task depends on a moved file as its sole active source; task transfer preserves one executable owner and stable IDs; accepted main documents are coherent; selected links and durable evidence are repaired; archive records explicitly identify historical status and main owners. An archive containing historical checkboxes is not an active task list. A narrow SPEC-only incorporation does not archive the whole feature package or retire FEATURE-TASKS.
- **Order:** Reconcile and archive eligible documents on the feature branch, verify the resulting links/ownership, then perform final Git integration so source incorporation and retained archive arrive in the same verified boundary. This operational ordering still represents archival after feature completion/document incorporation, not after an unrelated later merge.
- **Recheck:** Partial task implementation, document-only incorporation, incomplete task transfer, interrupted archive move, link preservation, and two successive features cannot overwrite active sources or duplicate executable ownership.

### R-003 — Keep local Git lifecycle independent of optional hosting

- **Evidence:** git-workflows.md assigns local lifecycle to sdd-manage and persistence to active owners. sdd-forge currently explicitly excludes commits, pushes, and PR operations; available GitHub references implement issue/label/milestone projection and issue lifecycle only.
- **Decision:** Making every local branch operation backend-owned would expand hosting scope and make an optional provider necessary for ordinary Git development. Names and artifact association are provider-neutral invariants.
- **Recommendation:** sdd-manage selects identities/targets and coordinates ordinary local Git creation, checkout, and explicit merge; implement/steer retain commit/push ownership. sdd-forge may own provider-specific remote ref/protection inspection and other explicitly supported hosted branch operations. Normal git push can publish a remote branch without a duplicate API create operation. Backend availability does not redefine the local naming convention.
- **Additional handoffs:** At entry, optionally ask the activated backend to resolve hosted repository/target constraints; publish the working ref through ordinary Git and report its verified SHA; before integration reconcile hosted target/protection information where needed; after target publication report source/target/merge refs and pending hosted effects. Define the supported API operations, auth/permissions, uncertain-result reconciliation, and offline behavior before advertising a hosted branch capability. Do not introduce implicit PR creation/merge/deletion.
- **Recheck:** Local bare remote without backend, normal hosted git-push publication, target protection, unavailable backend, uncertain remote ref creation, and resumed already-published branch remain coherent without duplicate effects.

### R-004 — Give steering a campaign identity without imposing a formal review

- **Evidence:** workflows.md and sdd-steer identify steering as lightweight revision without obligatory campaign artifacts; review-campaigns.md names directories from the first artifact, including optional stages.
- **Gap:** Branch-to-directory identity requires a directory and durable association, while steering currently can retain its scope only in existing task/change evidence.
- **Recommendation:** Allocate a review-campaign identity for a new steering amendment and retain a minimal revision record there: objective, affected scope, starting baseline, working/paused target identities, actual verification and publication. Use the existing revision report format with inapplicable sections omitted; do not require a fabricated review or revision plan. A later escalation to formal review/revision retains the same identity and existing evidence.
- **Recheck:** A short commanded reduction has the required branch/directory association, amends existing governing documents directly, and returns control. Formal escalation can add appropriate artifacts without renumbering or inventing historical stages.

### R-005 — Specify allocation, collisions, targets, and existing identities

- **Evidence:** review-campaigns.md already requires a stable sequence/start SHA and remote collision checks; Git protocol respects project naming policy, rejects unsuitable reuse, and uses a generic fallback. Task hierarchy supplies stable phase identity.
- **Recommendation:** Establish whether sequences are global across reviews/features or separate by collection; a single repository-wide campaign sequence is a coherent default, while directory/prefix identifies workflow type. Preserve all existing IDs. Allocate identity at first artifact/branch preparation and record the full baseline, using enough abbreviated SHA characters to resolve uniquely.
- **Compatibility:** Define whether workflow conventions are project-overridable defaults, and how explicit branch names are handled. Recommend defaults with explicit user/project overrides recorded in evidence. Do not rename historical campaign directories or existing in-flight branches automatically. Reuse only matching identity/scope/history; on name collision retain campaign identity and disambiguate the slug. A reused phase ID with an occupied historical branch needs an explicitly suitable continuation or distinct slug, not blind reuse.
- **Targets:** Name main integration branch explicitly during orientation; feature/revision prefixes do not select a target. Main governing artifacts stay in docs/dev on the relevant branches and become integrated at their authorized boundaries. Phase number comes from owning TASKS/PLAN hierarchy, not a new campaign counter.
- **Recheck:** Existing conventions, explicit branch override, collision, continuation, SHA ambiguity, concurrent allocation, and preserved historical records have deterministic dispositions.

## Recommended revision placement

1. Add a focused workflow identity/branch naming convention to sdd-conventions; align existing review-campaign identity rules rather than introducing a competing allocator.
2. Extend sdd-manage Git/workflow procedures for branch naming, phase-sized main integration, campaign allocation, backend handoffs, and retained stop behavior.
3. Align implement startup/range/completion, steering entry/report, feature authoring/discovery/incorporation/archive rules, and sdd-report artifact fields.
4. Expand sdd-forge only for selected concrete hosted branch operations; preserve current local Git ownership unless an explicit architectural change is accepted.
5. Align README/capability map and recheck scenarios before any migration of this repository's own branches or artifacts.

## Scope and readiness

The naming/storage direction is coherent. A revision plan should resolve R-001–R-005 into explicit actions and acceptance cases, particularly phase pause versus merge, active feature placement/archive gates, and the concrete hosted capability boundary. Recommendations above supply practical defaults for that plan; no source implementation or revision plan is performed in this review. No runtime bug, provider support, or consumer execution result is claimed.

## Follow-up decisions and branch-manager placement

The human clarified that branch management belongs to Git operations, not sdd-forge. R-003 is accepted with that resolution: no hosted branch capability or additional forge-driving steps are included in the proposed revision. The optional hosted-operation discussion above records the initial proposal assessment, not accepted implementation scope.

Recommended placement is a focused `sdd-manage/references/branch-management.md` reference, discoverable from the coordinator entry and workflow catalog. This is the coordinator's branch-management procedure, not a new independently invoked skill or a separate state store.

| Owner / reference | Responsibility |
| --- | --- |
| sdd-conventions workflow identity/naming reference | Stable campaign/phase identity, naming patterns, allocation/collision rules, and associated artifact locations. |
| sdd-manage branch-management.md | Resolve working/target identities and starting checkpoint; allocate or recover campaign association; create/reuse/check out eligible local branches; handle occupancy, continuation, collisions, and authorized phase transitions. |
| sdd-manage git-workflows.md | Coordinate verification, explicit merge, target publication, conflict/blocker continuation, and integration evidence. Link branch setup to the branch manager rather than duplicate it. |
| sdd-implement / sdd-steer / coordinated persistence | Retain task/amendment execution and scoped commits/pushes, invoking branch management through the coordinator's shared protocol. |
| sdd-orient | Observe repository/branch/worktree state; branch setup remains mutating coordinator work. |

An appropriate revision can extract current Establish the working branch rules from git-workflows.md, extend them with the accepted naming and phase lifecycle, and leave integration in its existing reference. Read-only selection/review does not create branches; implementation push-first remains before branch setup; steering still targets the paused branch and returns control. Artifact incorporation/archive decisions stay with their document owner, while branch management carries the shared identity and prerequisites.

This follow-up records placement recommendations only. No branch-manager source or revision plan is created yet.

## Implementation disposition

R-001–R-005 are Verified for accepted source policy, consumer interpretation, and the recorded Git/file fixture surfaces. Original proposal observations and follow-up decisions above remain retained. Actual revisions, scenarios, checks, integration state, and limits: [REVISION-REPORT.md](REVISION-REPORT.md).
