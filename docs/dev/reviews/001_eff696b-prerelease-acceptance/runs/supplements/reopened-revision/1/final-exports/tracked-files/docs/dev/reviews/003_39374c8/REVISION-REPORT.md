# SDD Manager revision evidence

**Campaign:** `003_39374c8`. Current record: `docs/dev/reviews/003_39374c8/REVISION-REPORT.md`. Established finding IDs and baseline evidence are retained. Archive paths in historical evidence describe earlier operations, not current storage.

## Campaign

- **Plan:** [REVISION-PLAN.md](REVISION-PLAN.md).
- **Baseline:** `39374c8ae60f92ce8dd874774ed69ab3cb15c459`; planning commit `aa2e09c4352caf803748d3c19e25c47bf092ea04`.
- **Working branch:** `revision/39374c8-branch-workflows`.
- **Target:** `feature/architecture-revision`, starting checkpoint `aa2e09c4352caf803748d3c19e25c47bf092ea04`.
- **State:** SDD-V-001–007 completed; campaign merged and published, with final plan/report archive. Each revision checkpoint was pushed before its successor.
- **Evidence limits:** Local structural and Git/provider fixtures are distinct from installed-client execution, live hosted mutations, and credential-channel validation.

## Revision checkpoints

### SDD-V-001 — Branch and merge lifecycle

- **Source:** Added the shared Git workflow reference; linked coordination/entry points and expanded orientation's branch/merge observation contract.
- **Observed checks:** `python /tmp/branch_workflow_fixtures.py`: eight tests passed. Actual Git fixtures cover forced two-parent merges from fast-forwardable history, two task commits/one merge, divergent target and already-integrated no-op, retained conflicts, failed check with target unpublished, rejected target push retaining merge, worktree isolation preserving staged/unstaged bytes, branch occupancy/collision, and missing destination.
- **Structure:** Package validator exit 0; heading/template, local-link, metadata/icon, and skill-reference checks reported zero errors.
- **Limits:** Reviewer-operated Git mechanics, not autonomous client execution. No protected-provider writes; a local rejecting receive hook exercises publication refusal.
- **Persistence gate:** Commit subject identifies SDD-V-001; verify remote containment before SDD-V-002.

### SDD-V-002 — Task and feature boundaries

- **Source:** Connected task startup/completion and coordinator feature sequencing to the shared branch lifecycle; added merge-message and branch-result formats; clarified hosted task closure versus target publication.
- **Checks:** Initial package validation rejected a cross-skill resource link; replaced it with named-skill reference loading, then package validator exited 0 and content/link/metadata checks reported zero errors. Source inspection confirms per-task push remains before advancement, selection-only does not enter branch mutations, narrow requests cannot incorporate or merge unrelated unfinished feature work, and complete feature incorporation precedes final verification/merge.
- **Executed foundation:** SDD-V-001's two-task fixture produced one two-parent boundary merge and published it to its bare remote. Fresh workflow-consumer execution is reserved for SDD-V-007; this checkpoint does not claim agent execution from source inspection alone.
- **Prior checkpoint:** SDD-V-001 `7077cde` pushed; remote-tip equality verified before this revision.
- **Persistence gate:** Commit subject identifies SDD-V-002; verify remote containment before SDD-V-003.

### SDD-V-003 — Steering isolation and continuation

- **Source:** Steering establishes/reuses an amendment branch targeting the paused implementation checkpoint, follows default explicit verified merge/publication, and resumes a blocked amendment only on a human command. Coordinated workflows/examples distinguish Git merge from feature-document incorporation.
- **Checks:** Package validator exit 0; heading/link/metadata checks zero errors. Inspection confirms production repair/reverification remains steering-owned, target publication is required, and no main-task continuation or feature overlay is introduced.
- **Forward execution:** A fresh consumer was started against a disposable classification project and its local bare remote, with a human-commanded contract reduction and project-required external facility check. Its actual outcome is recorded in the final composition checkpoint; no successful consumer outcome is claimed here.
- **Prior checkpoint:** SDD-V-002 includes `cfc5af3`, `36c8bda`, and `0b36550`; package resource-loading corrections are retained in history. Final remote-tip equality verified at `0b36550` before this revision.
- **Persistence gate:** Commit subject identifies SDD-V-003; verify remote containment before SDD-V-004.

### SDD-V-004 — Interrupted document integration

- **Source:** Added artifact-based continuation of selected incorporation; orientation/coordinator now distinguish partial document integration from interrupted task execution. Standalone integration and incorporation inside a feature campaign share branch safety with different finish boundaries.
- **Checks:** Package validator exit 0; content/link/metadata checks zero errors. Inspection preserves SPEC-only scope, selected-list requirements for ownership transfer, pending reassessment and historical evidence, source retention, and blocked duplicate identities. No rollback/journal or automatic implementation is introduced.
- **Forward execution:** Fresh-session partial-incorporation execution and its artifacts are recorded under SDD-V-007; static inspection here does not claim that execution.
- **Prior checkpoint:** SDD-V-003 `fa19123` pushed; remote-tip equality verified before this revision.
- **Persistence gate:** Commit subject identifies SDD-V-004; verify remote containment before SDD-V-005.

### SDD-V-005 — GitHub failure classification

- **Source:** GitHub reference classifies access, rate-limit, transient/offline, invalid-input, and uncertain-write outcomes; shared credential routing now applies to access-related403 rather than every403. Projection/lifecycle require reliable re-read before replay and preserve pending local/hosted differences.
- **Provider references:** Official English GitHub REST best practices and troubleshooting pages retrieved on 2026-10-01; sources linked in the GitHub reference. They distinguish rate-limit403/429, Retry-After/reset timing, secondary-limit backoff, private-resource404, and repeated error handling.
- **Checks:** Package validator exit 0; content/link/metadata checks zero errors. A fresh consumer receives nine controlled raw response/state fixtures; dispositions are recorded under SDD-V-007. This checkpoint claims no live provider or autonomous API execution.
- **Prior checkpoint:** SDD-V-004 `e977a9f` pushed; remote-tip equality verified before this revision.
- **Persistence gate:** Commit subject identifies SDD-V-005; verify remote containment before SDD-V-006.

### SDD-V-006 — Evidence fallback and exceptions

- **Source:** Verification facts retain project policy, with a fallback to owning entries/existing linked evidence and ordinary taskless reports/commit bodies. TDD exception rationale/authorization, alternative checks, and missing chronology stay explicit; implementation, steering, and reporting carry these facts durably.
- **Checks:** Package validator exit 0; content/link/metadata checks zero errors. No new mandatory evidence artifact/schema or deletion requirement. Fresh task/steering consumers already produced owning-list command/state evidence and merge-message verification; final primary inspection records the actual artifact checks under SDD-V-007.
- **Limits:** Durable reporting cannot mechanically prove execution order. Authorized exception and historical evidence cases receive fresh consumer assessment in the final checkpoint; no claimed RED reconstruction.
- **Prior checkpoint:** SDD-V-005 `d965112` pushed; remote-tip equality verified before this revision.
- **Persistence gate:** Commit subject identifies SDD-V-006; verify remote containment before SDD-V-007.

### SDD-V-007 — Composition and validation

- **Source:** Updated README workflow examples, capability ownership, coordinator examples, presentation prompts, and target-versus-default-branch terminology. Orientation traces task commits through merge parents rather than treating aggregate merge-message IDs as new task completion.
- **Prior checkpoint:** SDD-V-006 `fcad16e` pushed; remote-tip equality verified before this revision.

#### Fresh execution results

| Fixture | Observed result | Primary artifact checks |
| --- | --- | --- |
| Main T-002 | RED reproduced zero-as-positive; repair retained positive/negative behavior. Three tests and external facility passed on working and prospective merged states. Task `c664d079b5624676fddafb55acb32552712b3d2a`; explicit merge `cf07b853979047c609b04df701643aedc529ec7c` pushed to local target. | Exactly classifier/tests/README/TASKS changed; two parents, remote-tip equality, clean worktree, task command evidence, supplied facility preserved. |
| Steering blocked | Fresh consumer changed negative classification to ValueError; observed RED then three GREEN tests. Required external facility failed; target remained at b1ed7a6 with amendment work preserved, uncommitted and unmerged. | Consumer output and resulting branch/worktree context retained for the separate continuation. No fabricated facility or main-task progression. |
| Steering continued | Another fresh consumer used the externally supplied facility, verified/reassessed amendment and parents, committed/pushed `1a13822ca3237e0e0819ac426c756d32679545de`, then verified/published two-parent merge `c4e6f0714bc1e4e6d593b1027fc5b3d8c0d01f43`. | Exact seven amendment paths; task and parent reassessment resolved; prior evidence retained; remote equality and clean worktree. Stopped without main-task continuation. |
| Document interruption | Fresh consumer recovered partial SPEC incorporation and unfinished TASKS scope from a branch commit. Changed TASKS only, preserving SPEC, checked status/history, stable T-001, and FEATURE-SPEC. Added three pending reassessment notes; pushed `a83e85e37eda1478d90425d99d87d6614abb5500`. Required facility failure blocked merge. | No code/tests/README/unselected document changes or source removal; target unchanged at 18c71f9. Passing old tests were explicitly not current zero acceptance. |
| Document publication | Another fresh consumer continued after operator supplied facility; required commands passed; explicit document merge `58ac510294219d59aa0535cbda9c3cb9fd22fd82` published. | Compared to checkpoint, only SPEC/TASKS changed; two parents, remote equality, clean tree, all three pending notes and historical evidence retained; source retained. No implementation claimed. |

#### Controlled response and boundary assessments

- **GitHub:** Fresh consumer assessed nine raw response/state fixtures: permission403; primary rate403; secondary429; transient503; offline lookup; timeout after creation, closure, or comment; incomplete duplicate lookup. It distinguished suitable-access escalation from deferred rate limits, calculated reset/retry times, preserved unknown effects, reused unique #12 after uncertain creation, avoided replaying matching closure/comment evidence, and blocked duplicate/incomplete identity. Retry policy stayed bounded; no credential change for outages/rate limits. These are read-only fixture dispositions, not API calls or measured retry execution.
- **Scope/evidence:** A separate fresh consumer assessed seven cases: narrow feature range with unrelated unfinished branch work; selection-only disputed checked task; duplicate partial transfer with TASKS-only scope; authorized vendor-update TDD exception; taskless work with designated evidence; failed target push after verified merge; publication-only steering continuation. It preserved scope, selected-list ownership, read-only selection, existing evidence priority, explicit exception/gap facts, and continuation without duplicate merges or main-task advancement.
- **Git regressions:** `python /tmp/branch_workflow_fixtures.py`: eight tests passed after revisions, covering forced two-parent boundaries, task batching, divergent/already-integrated state, conflicts, failed-check publication guard, rejected push, staging/worktree isolation, and destination/name blockers.
- **Orientation regression:** `python /tmp/verify_revised_orientation.py`: actual five source commands exercised seven states; all repository bytes preserved. Expected unborn/detached/non-Git exits retained; plain-status clean-mtime control reproduced index refresh.

#### Validation boundaries

All forward consumers started in fresh threads with raw requests/artifacts and focused skill sources, without this plan/report or preceding diagnoses. Primary inspected actual completed Git artifacts independently. The full-feature fixture and final package/merge results follow below.

No installed-client campaign, live GitHub lifecycle, real credential-channel test, cross-platform execution, or independent pinned upstream verification is claimed. Protected-publication behavior is modeled with a rejecting local Git receive hook. Provider behavior is assessed from official guidance and raw controlled traces; server-side execution and actual backoff timing remain untested.

#### Full-feature execution and final source checks

- **Full-feature consumer:** Observed zero-classification RED, then three passing tests and facility checks. Task commit `7d9e238`, incorporation `ed7db34`, explicit merge `bb38339ed89bcbcb27ee8fe64073dc9d31d281fa` published to the local target after merged-state verification. SPEC/PLAN/TASKS/FEATURE-TASKS incorporated before merge; positive/negative contracts retained.
- **Primary inspection:** Exactly classifier/tests/README and the four selected document owners changed; T-002 occurs once as an executable task in TASKS and is retired from FEATURE-TASKS. Historical T-001 evidence and the supplied facility remain; merge has two parents, remote tip equals local target, and worktree is clean.
- **Final structural checks:** `validate_plugin.py .` exited 0; `inspect_package.py .` enumerated all 15 skills with zero errors/warnings. `/tmp/revised_package_checks.py` checked 101 package/review files, 68 Markdown files, five template headings, 93 local links, all 15 metadata/SVG sets, skill references, manifest consistency, and credential-pattern absence; zero errors. User EXPLORE_DRIVE documents and local tool state remain excluded and unchanged. `git diff --check` passed.
- **Persistence gate:** Commit subject identifies SDD-V-007. Push and remote containment must precede the campaign merge. The campaign's explicit merge will be verified before commit and target publication, followed by plan/report archive.

## Campaign integration and archive

- **Working tip:** `cf456b5b9fcad0fbed42551b65c9e3fa9ca33b40`, pushed and remote-tip equality verified before integration.
- **Explicit merge:** `37ea99359e9b34a202f7e922b0d1b1bc8e62cf3f` into `feature/architecture-revision`; parents are target checkpoint `aa2e09c4352caf803748d3c19e25c47bf092ea04` and the working tip above. No conflicts.
- **Merged-state verification:** Package validator and inspector passed with zero errors/warnings; content/link/heading/template/metadata checks and staged diff check passed before commit. Prospective merged tree equals the verified working tree. Merge commit pushed; target remote-tip equality verified before archive.
- **Archive:** Completed plan and this report moved to `docs/dev/revision_plans/`; relative links adjusted. Final archive checkpoint is identified by its commit subject and must be pushed/remote-verified before delivery. Working branch retained; no source campaign is restarted by bookkeeping.

### Source checkpoints

| Revision | Commits | Publication |
| --- | --- | --- |
| SDD-V-001 | `7077cdea1e6f3ff53755c90c77b7d414e1a68630` | Pushed before dependent revision; retained in published campaign merge. |
| SDD-V-002 | `cfc5af339f379f948a3ec94a5f6f5a0717b22877`, `36c8bdacdc0d2e69dd33f7b1db2e74c9ee1ed75b`, `0b36550c803dc74c261fdcc5d883a2ccbf53d6a0` | Pushed before dependent revision; retained in published campaign merge. |
| SDD-V-003 | `fa19123ae7a6d9297e729017b9463d3b5fe8b487` | Pushed before dependent revision; retained in published campaign merge. |
| SDD-V-004 | `e977a9f3a7ff0b1619d8c6deb129c0a5f4acb36e` | Pushed before dependent revision; retained in published campaign merge. |
| SDD-V-005 | `d96511257a1d72bf023c32baf93df3b944a9e513` | Pushed before dependent revision; retained in published campaign merge. |
| SDD-V-006 | `fcad16e1aacebbe45dde48ea7cf1b01b2923d8ec` | Pushed before dependent revision; retained in published campaign merge. |
| SDD-V-007 | `cf456b5b9fcad0fbed42551b65c9e3fa9ca33b40` | Pushed before dependent revision; retained in published campaign merge. |
