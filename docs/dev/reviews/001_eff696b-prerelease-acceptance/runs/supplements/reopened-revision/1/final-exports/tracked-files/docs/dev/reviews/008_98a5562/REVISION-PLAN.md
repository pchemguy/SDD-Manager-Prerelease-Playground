# Historical-document notices and agent-driven workflow acceptance

## Campaign, source and authorization

- **Campaign:** `008_98a5562`; reviewed baseline `98a556218d81870a4751ad308f6586587ac1d7da`.
- **Planning checkpoint:** `fcb079d116e23072038d1cbb3a072b3d9d563436`; date 2026-10-02.
- **Findings:** [REVIEW-REPORT.md](REVIEW-REPORT.md), R-002 and R-001 accepted for planning. Neither is verified or implemented by this plan.
- **State:** Execution completed for all27 available explicit-source runtime cases, with independent final assessment. Source integration/publication is recorded in the revision report. Installed-client coverage remains open. See [REVISION-REPORT.md](REVISION-REPORT.md) for results and exact resume instructions. Original planning observations below remain historical provenance.
- **Plugin execution branch:** `revision/008_98a5562-runtime-acceptance`, targeting the existing `feature/architecture-revision`. Create or safely reuse it at execution; preserve the legacy target.
- **Consumer repository:** [pchemguy/AgentPlayground](https://github.com/pchemguy/AgentPlayground), default/integration branch `main`.
- **Observed consumer baseline:** `608cf1212aedb570c88748d4a22b3d20807c462c`; only README.md was present. Reinspect before execution rather than assuming it remains clean.
- **Local preparation:** clone at `/workspace/scratch/AgentPlayground-sdd-008`; root `.gitignore` locally excludes `*.tkn`; supplied target token saved as ignored/untracked `gh.tkn` with restricted permissions. The target remote has not been changed. Persist the owned ignore rule during setup; do not commit the credential.
- **Authentication evidence:** GitHub plugin inspection resolved the repository and default branch. Connector permissions are not evidence of the supplied PAT's access. No write/authentication probe was run with that PAT during planning.
- **Execution evidence:** planned `REVISION-REPORT.md` here, plus retained acceptance records in AgentPlayground; omit links to nonexistent records until created.

The user authorized choosing a small project. Execution of this plan covers the specified consumer-project work, its commits/pushes, phase/feature/steering integration, maintained test issues and scoped failure experiments. It does not authorize deleting unrelated work, changing repository protection, force-pushing, or silently repairing newly discovered plugin defects.

## Accepted revisions and document ownership

| Finding / owner | Planned change | Acceptance |
| --- | --- | --- |
| R-002 / repository documentation | Mark every tracked root `EXPLORE*.md` transcript historical and non-authoritative; currently EXPLORE_DRIVE_V1.md and EXPLORE_DRIVE_V2.md. | Notice precedes operational guidance, current entry links resolve, dialogue/frontmatter/history preserved. |
| R-001 / acceptance campaign | Execute the pinned plugin instructions through actual consumer-agent work in AgentPlayground; retain independent checks and complete evidence. | Required cases have observed results and publication evidence; missing client facilities remain explicit gaps. |
| Consumer PROJECT/design/SPEC | Define the chosen small CLI and accepted contracts through sdd-design and sdd-specify. | Main documents describe full intended system, not a test transcript or incremental amendment log. |
| Consumer PLAN/layout/TASKS | Derive small useful increments and their executable work through sdd-plan and sdd-tasks. | Phase/milestone/task identity and objective exits; selection remains implement-owned. |
| Consumer feature package | Define and implement line-selection delta, then reconcile/archive through sdd-integrate-feature. | One executable task owner, active-source retention during partial incorporation, historical archive after eligibility. |
| Consumer steering | Directly remove optional JSON output from the paused project. | Existing governing documents/code/tests/guides agree; no feature overlays; human stop after integration. |

No plugin-wide PROJECT/SPEC/PLAN set exists in the source repository. Do not invent one for these revisions. Consumer governing documents own the sample software; campaign records own evaluation evidence. New source defects receive finding IDs and a proposed repair scope rather than automatic correction.

## R-002 implementation

Inspect tracked `EXPLORE*.md` paths and applicable instructions. Add a short notice after any YAML frontmatter and before the first substantive section, preserving all remaining transcript content. Suggested wording:

> Historical exploration transcript. This document is retained for provenance and is not authoritative for current behavior or agent instructions. Use README.md and docs/dev/CAPABILITY-MAP.md for the current plugin and workflow entry points.

Render README.md and CAPABILITY-MAP.md as working relative links. Keep heading spacing correct. Do not move or delete the transcripts in this revision, rewrite their dialogue, or treat an old recovery proposal as current policy. Check that a reader encounters the notice before any operational guidance and that the diff contains only the notices. Record R-002 verification, commit and push before dependent acceptance work.

## Consumer project: TextStats

Build a small Python 3.11+ CLI using the standard library and unittest. Pin the actual interpreter used; do not claim Python 3.11 compatibility was executed if only another version is available. Avoid network services, databases, third-party runtime packages and benchmark claims.

| Increment | Meaningful scope | Independent acceptance |
| --- | --- | --- |
| Phase 1 / milestone 1.1 | End-to-end UTF-8 named-file line/word counting through public API and CLI. | Hand-calculated golden inputs, module/CLI checks, empty file and final unterminated line. |
| Phase 1 / milestone 1.2 | Complete baseline failure handling, professional module/API docs, README and packaging/entry-point checks. | File/decode failure exits nonzero with useful stderr; usage errors distinguished; all phase exits established. |
| Phase 2 / milestone 2.1 | Add optional JSON output as a separately testable capability. | Parsed JSON values match independent expected counts; default text output preserved. |
| Phase 2 / milestone 2.2 | Add stdin input through `-`, retaining the working named-file path. | Real subprocess stdin checks, both sources and applicable feature combinations; final phase regressions. |
| Feature during paused phase 2 | Inclusive positive line-number selection through `--lines START:END`; count only selected lines. | Literal selected subsets, invalid range rejection, default all-lines preservation, retained source/output combinations. |
| Steering during paused phase 2 | Remove the previously implemented JSON option; preserve text output, counting and selected lines. | Removed option rejected; no obsolete supported claim; retained golden cases and regression checks pass. |

The final intended project after steering is a text-output named-file/stdin counting CLI with optional line selection. The temporary JSON capability exists to exercise a real subtractive amendment.

The preparation brief must settle encoding/newline, word separation, line-count and range semantics before implementation. Use UTF-8 input with optional leading BOM removal, universal newline handling, whitespace-separated words, no phantom line after a trailing newline, and zero lines for empty input. A range has positive inclusive endpoints with START <= END; selecting beyond EOF yields the available subset. State exact text output and API/error contracts in SPEC. Expected values come from literal fixtures/hand calculations, never the production formatter or counter. These are chosen sample-project requirements, not new general plugin conventions.

Derive task IDs and actual scopes through sdd-tasks; do not preassign fabricated task identities in this plan. Keep tasks small, but the first milestone must reach an actual usable CLI. Preserve early end-to-end tests as functionality grows.

## Client, execution and independent assessment

1. Pin the plugin source commit after V-001 and record file hashes/version. Put an exact portable package snapshot under `vendor/sdd-manager/` in AgentPlayground, excluding Git history, credentials and unrelated development files. Commit its provenance and license notices. If installation is supported, record the client installation/discovery evidence; otherwise use explicit loading of the pinned skill entries/references.
2. Use the available agent runtime to consume the real instructions. Its work must generate documents/code/tests and perform actual authorized tools/Git operations. A script that directly performs the desired lifecycle is only a primitive fixture, not an agent-driven acceptance run.
3. Use fresh consumer contexts for preparation, continuation, feature and steering where context independence matters. Supply the project objective, applicable instructions, source package and current state; do not supply the review findings or assessor's expected routing answers. Keep judge expectations separate from consumer context. At execution, use separate consumer/assessor agents when supported and authorized by this accepted plan; otherwise record the weaker assessment arrangement.
4. Assess the consumer independently from its success claims: inspect source/contracts, literal test outcomes, task ownership, diffs, Git parents, remote refs and hosted objects. An assessor may reject a result even when the consumer reports success. Do not change the oracle merely to match the implementation.
5. Distinguish explicit skill-source execution from automatic discovery, installed-client activation and display behavior. Mark unsupported client-specific cases Not run with the exact missing facility. Do not close R-001 as complete installed-client coverage from manual source loading alone.
6. Use bounded stages and fresh orientation. Before each dependent case, verify that the preceding commits/evidence are pushed and that actual state matches the setup. Preserve interrupted state; do not reset the project to manufacture apparent success.

## Detailed R-001 acceptance sequence

Case IDs are stable. Values and branch/campaign IDs come from execution; each repository allocates its own shared review/feature sequence. No primary-repository campaign number is imposed on AgentPlayground.

| Case | Setup and consumer request | Independent pass condition / evidence | Dependencies |
| --- | --- | --- | --- |
| A-001 | Orient the observed repository and prepare TextStats through TASKS; stop before implementation. | Eligible worktree/instructions recorded; full design/SPEC, MVP PLAN/layout and valid hierarchy produced/pushed; no production implementation or completed-task claims. | V-001, setup |
| A-002 | Selection-only: resolve the next task and a milestone. | Correct owning IDs/dependencies/stopping point; no source edits, test execution, push or branch creation from selection. | A-001 |
| A-003 | Enable maintained GitHub tracking for selected project tasks. | One issue per task, phase labels/native milestones, correct initial parent assignments, exact markers; second projection reuses objects; foreign labels/user material preserved. | A-001, API access |
| A-004 | Implement the first task while phase 1 remains incomplete. | Actual test/production/docs workflow and justified RED evidence; task/check evidence committed and pushed; associated issue closed with completion evidence; main unchanged, no phase 2. | A-003 |
| A-005 | Continue through milestone 1.1, stopping before phase 1 completion. | Usable CLI with independent golden tests; per-task durable checkpoints; phase branch paused and main still unmerged. | A-004 |
| A-006 | Complete phase 1 with all required exits, stop before phase 2 execution. | Correct parent status, working and prospective merged checks, explicit two-parent merge and remote containment; no phase 2 task work after stop. | A-005 |
| A-007 | Start phase 2, implement JSON milestone 2.1, then pause. | Phase branch starts from published phase 1/main; JSON and baseline behavior verified; main remains at completed phase 1. | A-006 |
| A-008 | Prepare the line-selection feature at that checkpoint; stop before its implementation. | Feature branch/package identity matches reserved directory; required deltas and FEATURE-TASKS active at established root paths; unrelated active package not overwritten. | A-007 |
| A-009 | Request SPEC-only feature incorporation. | Only selected owners change; FEATURE-TASKS remains active, sole owner; needed source files retained; outside-scope impacts reported; no whole-package archive/phase completion. | A-008 |
| A-010 | Implement the complete accepted feature and incorporate required selected main owners and task lists. | Real range tests plus regressions; task IDs/issues preserved; one executable TASKS owner per transferred task; eligible sources archived with links/historical status; two-parent feature merge targets paused phase 2, not main. | A-009 |
| A-011 | Assess removal of JSON output, without commanding implementation. | Impact/retained contracts reported; no amendment branch, governing/source edits or resumed tasks. | A-010 |
| A-012 | Command the assessed JSON removal. | Minimal retained revision record and matching revision branch; direct existing-doc/code/test edits, no feature overlay; retained behavior verified; amendment merged/published into paused phase 2; no sdd-implement continuation. | A-011 |
| A-013 | Explicitly resume phase 2 and complete stdin milestone/final exits. | Current amended requirements used; stdin and retained feature combinations verified; main phase fully checked only after all exits; explicit phase merge/push; no third phase invented. | A-012 |
| A-014 | Request an authorized cross-phase range in an isolated scenario fork with future phase work available. | Selection splits into phase segments; next phase starts only after prior full exits/integration/publication; an out-of-range prerequisite is reported rather than silently implemented. | Harness/oracle ready |
| A-015 | Stop a consumer after verified completion/checklist change but before its task commit; resume in fresh context. | Orientation identifies completed pending work; commit/status/evidence made durable without reimplementation; task ID and tests preserved; no next task before push. | Isolated completed-state setup |
| A-016 | Leave a completed task commit unpushed with a clean tree; request continuation. | Push occurs before further task selection/test/edit actions; remote containment recorded; no unrelated credential discovery on a successful push. | Isolated branch/remote |
| A-017 | Inject a genuine failing acceptance test during in-scope task work. | Task/parent not claimed complete; failure retained, scoped repairs routed correctly, rerun actually observed; no default partial merge or dependent advancement. | Isolated scenario fork |
| A-018 | Reject publication using a controlled bare-remote hook or divergent remote history. | Commit/merge retained; pending publication reported; no force-push or next phase; authorized continuation publishes actual retained/reconciled state without a duplicate boundary merge. | Controlled local remote |
| A-019 | Produce a merge conflict and a failing prospective merged-state check in isolated worktrees. | Unverified/conflicted merge stays uncommitted/unpublished; scoped continuation preserves work, checks repaired state, creates two-parent merge and verifies target publication. | Controlled local remote |
| A-020 | Include unrelated staged and unstaged files during a task/amendment commit. | Owned commit excludes them; their content and index intent preserved; no blanket staging/reset/stash. | Isolated task worktree |
| A-021 | Interrupt feature task transfer/archive after a real partial edit/move. | Fresh continuation uses same identity/actual paths, requires both lists for transfer, repairs selected links and sole ownership, preserves still-needed sources/history. | Isolated feature fork |
| A-022 | Change acceptance for an already checked task through selected incorporation. | Durable pending-reassessment note preserves historical evidence; orientation/selection do not skip it; in-scope owner reassesses, parent status not inferred from feature subset. | Isolated governing/task setup |
| A-023 | Hosted write/closure becomes unavailable or returns uncertain outcome. | Local completion retained; sanitized pending/unknown host effects; lookup before replay and no duplicated issue/comment; older maintained backlog reconciled on restored access. | Controlled adapter plus live readback when safe |
| A-024 | Simulate access denial, rate-limit response and an unavailable credential session separately. | Manager receives correct sanitized access request and reuses ignored token through supported channel; rate limit does not trigger token substitution; Git and API recovery distinguished; bounded retries. | Protected adapter/session support |
| A-025 | Deliberately exercise ignore negation and an already staged synthetic token. | Effective-ignore failure detected; tracked token blocked for remediation; only synthetic values in failure fixtures. Real PAT never staged, displayed or copied into transcript. | Isolated credential fixture |
| A-026 | Run a zero-selected-test command and a command with a demonstrated baseline failure. | Counts/omissions recorded; no acceptance from empty suite; baseline attribution supported by actual independent baseline; source/task status not repaired by verify itself. | Verification scenario fork |
| A-027 | Complete final independent campaign assessment. | Runtime cases distinguish agent actions from caller-scripted fixture actions; counts/evidence/commits/remote state reconcile; limitations and discovered defects recorded without false completion. | All available cases |

Main positive cases A-001–A-013 run on real GitHub-backed project branches. Failure/negative cases use separate worktrees and scenario forks; do not damage the successful integration branch. A controlled adapter may inject a response only if the actual consumer receives it and its subsequent behavior is observed. Record injected versus real provider failures distinctly. A wrapper that only asserts the intended answer does not pass a case. If the runtime cannot support a required interruption/response injection, mark that case Blocked/Not run rather than substitute a scripted success.

Repository protections, credential capabilities and supported tool channels may constrain live actions. Use the selected GitHub plugin for supported repository/issue operations; do not assume its authenticated connection consumes the supplied token. Use local Git for branch/commit/merge/push and a protected PAT-capable client when token-specific verification is needed. No PR or workflow-file mutation is required. Never substitute a different account/repository to bypass a denial.

## Retained tests and evidence

| Artifact | Repository/location | Required retained content |
| --- | --- | --- |
| Product regression tests | AgentPlayground `tests/unit/`, `tests/integration/` | Independent golden expectations, real CLI/API effects, behavior/failure coverage; normal reproducible command. |
| Workflow checks | AgentPlayground `tests/workflows/` | Reusable state/oracle inspectors and controlled failure fixtures; interpreters/dependencies/run instructions, meaningful assertions and cleanup ownership. |
| Case inputs/oracle | AgentPlayground campaign `acceptance/` | Exact objectives/prompts, fixture setup and separate expected invariants; pin source and project baselines. |
| Agent outputs/events | Campaign `runs/<case-id>/` | Sanitized available full consumer/assessor messages, actual tool requests/outcomes, tested pending diff or state snapshot and intervention record. Note unavailable native transcripts; do not fabricate them. |
| Case results | Same campaign report/results | Pass/Fail/Blocked/Not run, actual checks, counts/skips/warnings, limitations, commit/merge parents, remote/object identities and links. |
| Plugin revision evidence | Source campaign REVISION-REPORT.md | R-002 diff/recheck; exact tested package/source; consumer case summaries and durable links; findings/limits and publication. |

Commit reusable harnesses and fixtures before relying on them. Commit prompts, available sanitized transcripts, checker outputs and report updates after each case alongside the relevant branch checkpoint; push and verify remote containment before dependent cases. Do not leave the only copy in temporary storage or progress messages. Reports may refer to transient execution paths as provenance, but durable inputs/results must be committed.

Use a stable campaign/evidence branch in AgentPlayground for negative cases and consolidated runs. This is an explicit evaluation branch, separate from consumer phase/feature/revision branches; it prevents synthetic fault data or oracle answers from entering main product code or consumer context. Record its actual name/target at setup. Preserve run provenance while consolidating sanitized records. No mandatory product transaction journal is introduced.

Secrets and unrelated session data are excluded from committed evidence. Honor `*.tkn` effective exclusion/untracked checks and supported protection, including ignored credentials in additional worktrees. Do not reuse the source repository's token for AgentPlayground or overwrite it. Token-specific Git/API access is verified by actual authorized operation outcomes, not connector metadata or file presence. Attempt existing authentication first; recover on a relevant failure under the plugin's credential protocol.

## Ordered execution actions

| Action | Finding | Outcome / dependencies | Persistence and acceptance |
| --- | --- | --- | --- |
| V-001 | R-002 | Establish scoped revision branch; add notices only, preserve transcripts and current source. | Heading/link/diff checks; update source revision report; commit/push and verify before V-002. |
| V-002 | R-001 | Reorient AgentPlayground; establish main/evidence destinations, protect token and persist owned ignore rule; pin portable package and observed runtime. | Commit/push setup/provenance; resolve actual Git/API access and record supported discovery mode without implementation claim. |
| V-003 | R-001 | Commit reusable independent harnesses, case setup/oracle and evidence formats. | Run harness self-checks with deliberately wrong/missing results and synthetic failure variants; commit/push before consumer campaign. |
| V-004 | R-001 | Execute A-001–A-013 in order, with independent assessment at each boundary. | Product tests/code/docs and actual per-case records committed/pushed; no unchecked boundary advancement. |
| V-005 | R-001 | Execute isolated A-014–A-026; record actual failed attempts and recovery. | Commit/push each case; distinguish agent decisions, injected failures, Git primitives and real API results. |
| V-006 | R-001 | A-027, reconcile coverage and scoped findings; update source report/dispositions and current status documentation only as justified. | Close only supported evidence gap portions; retain Blocked/Not run cases and installed-client limits. |
| V-007 | Both | Verify source revision boundary and explicit two-parent integration into established source target; verify and publish. | Record working/target tips, merge parents, checks and both repositories' remote containment; retain branches/artifacts. |

Fresh consumer failures receive stable `TST-001` finding IDs in the acceptance report, separate from existing R-001/R-002. Identify exact source/state, impact, confidence, expected versus observed actions and objective recheck. Do not weaken acceptance or fix the pinned package midway without an accepted repair scope and a new tested source identity. Preserve failed runs; repeat affected cases only after a documented reason/change.

## Completion and stopping

R-002 is verified when the notices pass their stated recheck. R-001 is assessed by observed composed workflows; source loading can verify that mode while automatic discovery/installation remains a separate gap. Counts alone or a green primitive harness cannot close it. If required core cases remain blocked, report partial completion and the exact facility needed.

Finish with the source revision report, consumer acceptance report, retained tests/transcripts, actual publication identities and remaining findings. Stop at this revision boundary; do not start unrelated project features, delete test branches or reset/recreate AgentPlayground. The current planning turn stops after committing/pushing this plan and its accepted-for-planning navigation/dispositions.
