# TextStats diagnostic test project integration revision plan

## Campaign, scope and state

- **Campaign:** `009_384beef`.
- **Starting baseline:** `384beefb6186348af9b100de9bec2f5a4a024692`.
- **Origin:** User-requested integration of TextStats as a reusable SDD Manager diagnostic test project, following the [008 campaign report](../008_98a5562/REVISION-REPORT.md).
- **State:** Tasks 1–3 implemented and reviewed: entry documents/schemas, portable helpers and case contracts complete; fresh directory-only bootstrap verified. New live acceptance remains an explicit follow-up awaiting its dedicated repository input.
- **Scope:** Self-contained test infrastructure, agent/human entry documents, phased execution, interruption recovery and diagnostic reporting. No plugin defect repair is implied by this plan.
- **Execution:** Coordinate accepted revision work through SDD Manager, preserving scope, verification, reporting and publication boundaries.

**Goal:** Add a self-contained TextStats diagnostic test project to SDD Manager so an agent directed only to its directory can obtain the context, resolve missing inputs, set up a test repository, execute phased tests, recover interruptions and report actionable plugin findings.

**Architecture:** A repository-owned test bundle at `acceptance/textstats/` contains agent/human entry documents, the scenario, ordered procedures, separated consumer/assessor inputs and portable support tools. Run-specific state and evidence live in the supplied test repository; fresh consumers receive only their selected scenario instructions and the exact tested plugin snapshot. The bundle is test infrastructure outside the plugin skill package.

**Tech Stack:** Markdown, versioned JSON manifests/schemas, Python 3.11+ standard-library helpers/unittest, Git, and the plugin's supported GitHub backend/credential mechanisms. Actual interpreter and client mode are recorded.

**Spec:** The Requirements section of this plan is the implementation brief. The delivered test bundle uses the repository's SDD skills and available agent tools.

## Requirements

1. A new agent receiving only “Run the test project in acceptance/textstats/” can discover its purpose, inputs, procedures, required skill references, checkpoints and diagnostic deliverables without previous conversation context.
2. TextStats is explicitly a plugin test project. Its capabilities are test material; development documents inside the consumer repository remain ordinary product artifacts generated through the tested workflows.
3. Request a dedicated test repository when none is supplied. Existing authentication is used first; request suitable GitHub credentials when required access is actually unavailable. Never assume the old AgentPlayground destination, a previous token or a previous session.
4. Support complete execution and bounded phase/case scopes, planned stops, injected interruption cases and unexpected interruption. Resumption preserves actual unfinished work and uses durable evidence rather than prompt memory.
5. Diagnose plugin behavior, including assisted or failed first attempts. A final report must state demonstrated outcomes, findings/root-cause confidence, actions taken and concrete proposed plugin changes, or explicitly state that no confirmed defect/no change is proposed.
6. A test run does not edit the tested SDD Manager package. Any plugin repair uses a separate accepted change and a new tested identity.

## Global constraints

- Put the bundle at `acceptance/textstats/`; link it from the root README. Do not insert its instructions/oracles into shipped skill entries.
- Default tested source is the committed SDD Manager HEAD at run start; an explicitly supplied revision overrides it. Record full SHA and package-file hashes before consumer execution. Handle requested dirty-source testing explicitly rather than calling it HEAD testing.
- Require an explicitly identified dedicated test repository, with `main`/`origin` defaults only after discovery confirms them. Preserve existing contents, instructions, staging, credentials and hosted objects; never reset an existing repository to start a test.
- Full coverage includes real Git publication and GitHub tracking plus isolated controlled failures. If facilities are unavailable, label affected cases Blocked/Not run; a local-only subset is not full acceptance.
- Reuse the pinned plugin's repository/credential/campaign protocols. Git transport and GitHub API authentication are distinct. Keep tokens out of prompts for workers, schemas, recorded input values, logs, URLs, arguments and committed evidence.
- Keep assessor expectations out of consumer contexts. A coordinator having full bundle context does not confer it on fresh consumers.
- Retain original attempts and all clarifications, reviews, external restorations and retries. A repaired case can pass with assistance; its first attempt remains visible.
- Run state belongs to the test coordinator. Do not introduce a mandatory transaction/journal protocol into SDD Manager's product workflow.

## Placement and documents

The source bundle contains reusable instructions and tools. It does not contain a copied finished TextStats implementation or a new duplicate of the historical campaign.

| Proposed path beneath `acceptance/textstats/` | Responsibility |
| --- | --- |
| `AGENTS.md` | Agent entry: role, exact reading order, input resolution, automatic next action, isolation, stopping/resumption and reporting obligations. |
| `README.md` | Human entry: purpose, directory map, minimal invocation, required inputs, profiles, phases, outputs and recovery overview. |
| `OBJECTIVES.md` | Plugin capabilities under diagnosis, coverage criteria, evidence limits and meaning of outcomes. |
| `SCENARIO.md` | Why named-file counting, JSON, ranges, JSON removal and stdin exercise specific workflows; full chosen sample contracts and constraints. |
| `SETUP.md` | Repository resolution, supported operating environment, plugin pinning, protected credentials, publication destinations and fresh/resume discrimination. |
| `EXECUTION.md` | Ordered phase/case procedure, selected scope, role handoffs, gates, interventions and evidence publication. |
| `RECOVERY.md` | Controlled/uncontrolled interruption procedures, state reconciliation decision table and cross-machine restoration. |
| `DIAGNOSTICS.md` | Attribution to input, consumer, checker, environment or plugin; reproduction requirements; final summary and repair proposals. |
| `cases/catalog.json` | Stable case IDs, phase/order, dependencies, operating mode, consumer input path, assessor contract path and interruption trigger where applicable. |
| `cases/consumer/` | Exact reusable selected-case requests and product preparation brief; no expected routing answers or completed results. |
| `cases/assessor/` | Independent literal oracles and lifecycle/scope/ownership expectations; accessible to assessors/coordinator only. |
| `templates/inputs.example.json` | Non-secret run configuration with documented defaults; credential value is never a field. |
| `schemas/inputs.schema.json`, `schemas/run-state.schema.json` | Versioned configuration and coordinator checkpoint shape. |
| `scripts/preflight.py`, `scripts/prepare.py` | Read-only configuration/capability observation; bounded fresh workspace/fixture preparation after resolved authorization. |
| `scripts/observe.py`, `scripts/assess.py` | Sanitized state capture and deterministic checks. Agent behavior and final diagnosis remain independently assessed. |
| `tests/test_preflight.py`, `tests/test_recovery.py`, `tests/test_checkers.py` | Meaningful sensitivity and recovery tests for the reusable support tools. |

Source instructions outside this directory may be referenced through explicit relative paths because they are part of the same repository. No essential procedure may depend on a previous chat, scratch pathname, live GitHub artifact or the old AgentPlayground checkout. Historical records are cited as provenance, not required bootstrap inputs.

## Agent entry and missing-input behavior

`AGENTS.md` gives this reading order: OBJECTIVES, SETUP, SCENARIO, EXECUTION, RECOVERY, DIAGNOSTICS, then the selected catalog entries. It identifies the caller as test coordinator. It directs the coordinator to use available separate consumer/assessor contexts; if fresh isolation is unavailable, disclose that limit and do not certify the isolation-dependent cases.

Resolve configuration in this order: explicit current invocation, explicitly supplied input file, existing run checkpoint for a requested continuation, documented defaults. Conflicts affecting identity/destination/scope require resolution; do not guess. Default scope is the full supported campaign, with continuation through authorized phases; a supplied case/phase boundary limits it.

Required input is the test repository URL or an unambiguous existing checkout with its authorized remote. If missing, ask: “Which dedicated test repository should this run use? Supply its URL or local checkout path.” Do not create a remote repository or select AgentPlayground silently. If the repository already contains a run, distinguish resume from a new isolated run; use a new campaign/workspace without replacing prior work.

Authentication is an operational prerequisite, not a compulsory token input. Use an authenticated supported client for API operations and existing Git authentication for authorized publication. On a classified access/authentication failure, follow sdd-manage's credential recovery: discover an eligible ignored/untracked `gh.tkn` only in the test repository, or request a protected credential supply for that repository and operation. GitHub backend documentation specifies the needed permission profile. Do not request a token for policy/quota failures or repeatedly before each push. A source-repository credential must not be copied to a different test repository.

The input schema defines `test_repository`, optional `local_checkout`, `plugin_revision` (default committed HEAD), `scope` (default full), `stop_after` (default none), `profile` (default full GitHub), and optional `run_id` for resume. Protected credential handoff is described in SETUP, outside the JSON. Record resolved non-secret inputs and actual capabilities once; re-resolve only changed/unavailable facilities.

## Phased execution

| Phase | Work and expected durable boundary |
| --- | --- |
| P0 — Resolve and initialize | Resolve repository/access/scope, determine fresh or resume, pin plugin/runtime, reserve run identity and publish reusable inputs/harness before use. No product implementation. |
| P1 — Prepare and select | Consumer generates governing documents/task ownership and demonstrates selection-only behavior. Independently assessed preparation checkpoint. |
| P2 — Deliver baseline | Incremental API/CLI work, failure/docs/deployment exits, hosted reconciliation and verified complete Phase 1 integration. |
| P3 — Increment, feature and steer | JSON increment, feature preparation/selected incorporation/implementation/archive, JSON removal and reassessment, stdin continuation and final phase integration. Each dependent case requires assessed/published predecessor state. |
| P4 — Failure and interruption trials | Isolated cases start at actual prerequisite checkpoints produced by P1–P3; controlled failures, partial transfers, unfinished staging/merge and fresh-agent recovery. No fabricated completed prerequisite. |
| P5 — Diagnose and publish | Independent coverage reconciliation and causal diagnosis; final diagnostic summary, findings/proposed changes, source/evidence links and a verified stop checkpoint. |

Import the original A-001–A-027 intents into the case catalog, retaining stable IDs. Exact replay identities/commit hashes/issue numbers are runtime discoveries. Negative cases may run when their real prerequisites exist; catalog dependencies determine placement rather than forcing an impossible phase order. Phases organize the coordinator's work; they are distinct from TextStats' product phases and do not create new product task IDs.

A controlled stop occurs at an explicit caller boundary or a catalog interruption trigger. Preserve/publish the reached state, report the next permitted action and stop. Normal phase transitions continue without extra confirmation inside the supplied scope. A blocked dependent case cannot be skipped as though it passed; independent cases may continue when their scope and prerequisites allow it.

## Interruption, resilience and resumption

### Durable coordinator checkpoint

Store the run under the test repository's convention-named `docs/dev/reviews/<campaign>/`. Reserve a stable evidence branch there using the current naming rules; retain it through the run. Keep:

- `INPUTS.json`: resolved non-secret repository/source/scope and run identity.
- `RUN-STATE.json`: schema version, phase/case, attempt, role, last completed action, pending/uncertain operation, next action, checkpoint refs and evidence paths.
- `RESUME.md`: brief human recovery entry pointing to actual observations and the permitted continuation.
- `runs/<case-id>/<attempt>/`: inputs, sanitized actual journal/logs, assessment, intervention record and relevant Git/file/index exports.
- `DIAGNOSTIC-REPORT.md`: progressively updated findings and final conclusions.

Write coordinator state through temporary-file replacement where supported; this does not make Git/provider effects atomic. Capture state before deliberate interruption and after material transitions. Commit/push sanitized checkpoints at case boundaries and before dependent execution. For mid-operation stops, retain recoverable pending files, index/stage data and required Git objects without turning the consumer's unfinished work into a completion commit. Clearly state which unpushed pending artifacts are local-only versus remotely recoverable.

### Actual-state reconciliation

| State encountered after interruption | Resumption strategy |
| --- | --- |
| Planned boundary; no pending work | Verify recorded identities/publication and select the next authorized phase/case. |
| Dirty task or partial document transfer | Inspect actual paths/diffs/owners; retain exact edits and needed sources. Resume the same task/identity before archive or next task. |
| Verified staged task, not committed | Preserve index and owned/unrelated separation; validate retained evidence, complete the pending scoped commit, then publish. |
| Existing local commit not published | Reconcile remote containment; publish the existing commit before task selection or new implementation. |
| Merge conflict or failed prospective check | Preserve MERGE_HEAD, original parents and index stages/resolution. Resolve/recheck within scope; no completion/publication while required checks fail. |
| Committed merge awaiting publication | Reconcile remote and publish the existing two-parent merge; do not recreate it. |
| Git/API operation with uncertain effect | Read destination refs/hosted identities before retry. An interrupted response is not proof the operation failed. Preserve provider IDs and foreign fields; prevent duplicate creation/comments/integration. |
| Coordinator report/checkpoint lags actual effects | Reconstruct from Git, retained files/index, observed hosted metadata and available logs. Record uncertainty; do not invent missing commands or replay setup. |
| Worker killed or context/session lost | Reorient the coordinator from the bundle/checkpoint, then restart a fresh worker with the selected current-state handoff and pinned skills; keep assessor expectations excluded. |
| Workspace missing on another machine | Clone recorded repositories/refs; verify recovery bundles and file/index exports, then restore only that recorded case state. Recover credentials separately. If necessary pending state was not saved, report the exact unrecoverable boundary instead of claiming resume. |

Controlled interruption cases need an actual observed partial action before suspension and a separate fresh continuation. Unexpected interruptions can occur during any phase, check, commit, push, API call or checkpoint write. Re-read reality before trusting the cursor. Never reset/delete branches, overwrite unfinished work, clear a merge or restore a clean fixture merely to make the next run easier.

## Diagnostic deliverable

The final report leads with four explicit answers: what plugin behavior was demonstrated; what issues were observed; what actions were taken in the test project/harness/plugin; what plugin changes are proposed or why none are proposed.

Each finding records stable ID, exact source/input/case/attempt, expected versus observed behavior, evidence, intervention, likely cause and confidence, reproduction, bounded proposal and objective recheck. Preserve assisted first attempts even when the eventual outcome is Passed. Input/consumer attribution requires evidence; it does not automatically dispose of a possible instruction weakness.

Carry forward TST-001–TST-004 as historical lessons, not pre-filled results of a new run. Supply the original test-directory requirement and distinguish future stdin compatibility from the named-file feature exit in consumer input. Add focused diagnostics for dependency inflation and retired-task selection (TST-002/003), inspecting the supplied input and skill guidance before attributing failure. No automatic source repair mid-campaign.

If no confirmed plugin defect is found, state directly: “No confirmed SDD Manager defects were identified; no test-derived plugin change is proposed.” List concrete unresolved investigations separately. Missing installed-client execution and other facilities are coverage gaps, not Passed cases or invented defects.

## Review focus

1. A directory-only invocation lacks a repository: request it before writes; never inherit an old destination.
2. Token absent or credentials unusable: use existing auth first, request protected credentials only where appropriate, preserve pending publication.
3. Fresh setup versus existing interrupted run: distinguish them without replaying fixture drivers or overwriting artifacts.
4. Worker/coordinator dies during an uncertain write or partial move: recover actual state/identity without duplicate operations or lost index intent.
5. Consumer sees assessor expectations or corrections vanish from results: enforce separate handoffs and retain original attempts/assistance in diagnosis.

## Implementation tasks and acceptance

### Task 1 — Self-contained entry and scenario documents

**Files:** AGENTS, README, OBJECTIVES, SCENARIO, SETUP, EXECUTION, RECOVERY, DIAGNOSTICS, templates and schemas at the paths above; root README test-project link.

**Interfaces:** Produces complete relative reading paths, input fields and phase/checkpoint contracts consumed by the support tools and coordinator.

- [x] Extract reusable requirements/procedures from the historical campaign; remove fixed machine paths, repository defaults, issue IDs and completed-answer content.
- [x] Write the entry/linked documents and configuration schemas, including every interruption state above.
- [x] Check all relative links and manually trace a fresh directory-only invocation and a resumed invocation without using historical chat context.
- [x] Commit the coherent documentation bundle with scope limited to the test infrastructure and its README navigation.

### Task 2 — Portable setup, observation and recovery support

**Files:** scripts/preflight.py, prepare.py, observe.py, assess.py; tests/test_preflight.py, test_recovery.py, test_checkers.py; interpreter package discovery files as needed.

**Interfaces:** Scripts accept `--inputs <path>` and `--output <path>`; execution helpers additionally accept `--run-state <path>` where needed. Non-secret structured observations return exit 0 on success, nonzero with a sanitized cause on failure. Preflight is read-only; prepare creates only a resolved fresh workspace. Observers never resume/mutate consumer work.

- [x] Write failing tests for missing/ambiguous repository input, existing-run preservation, secret-value rejection in configuration, pending-publication recognition and uncertain-operation reconciliation.
- [x] Port only the reusable Git/task/oracle/fixture primitives from the old harness; parameterize repository roots/endpoints/refs and exclude historical review snapshots from current ownership.
- [x] Implement the documented script interfaces; recovery reads actual state rather than trusting RUN-STATE alone. Restrict credential handling to plugin-owned protected mechanisms.
- [x] Run the support suite with intentionally invalid evidence and nonempty collection. Verify no real hosted writes in self-tests.
- [x] Commit the tested helpers before a consumer run relies on them.

### Task 3 — Case contracts and isolated worker handoffs

**Files:** cases/catalog.json, cases/consumer/, cases/assessor/, EXECUTION and DIAGNOSTICS refinements.

**Interfaces:** Each catalog case resolves its dependency checkpoints, selected worker input and independent assessor contract. Input rendering substitutes resolved non-secret identities; expected results never enter consumer input.

- [x] Port all 27 original case intents with real prerequisite/interrupt triggers; literal expectations remain independent of application code.
- [x] Define controlled stop/resume pairs and uncontrolled interruption injection points, covering dirty transfer, staged work, rejected push, conflict, failed required check and uncertain hosted effects.
- [x] Define the two focused diagnostic probes for dependency inflation and retired-task handling, without coaching consumers toward assessor answers.
- [x] Verify catalog dependency consistency, resolvable input paths and separation of worker/assessor context; commit the complete case bundle.

### Task 4 — Fresh-context bootstrap, interruption and diagnostic acceptance

Directory-only missing-repository discovery was verified at `f6fd96f`; [the observation](evidence/directory-bootstrap.md) records unchanged source state. Authentication and live execution below remain the explicit dedicated-repository follow-up in the report and bundle README; the compound acceptance steps are intentionally unchecked.

**Files:** New run records in the explicitly supplied test repository; source bundle changes only for evidenced fixes.

**Interfaces:** Consumes the completed bundle plus caller-provided repository/credential capabilities. Produces durable actual case evidence, resumption proof and DIAGNOSTIC-REPORT.

- [ ] Start a fresh coordinator with only the directory pointer; demonstrate discovery and request of the missing repository input, then resolution of authentication under the stated protocol.
- [ ] Execute setup and the authorized case scope through fresh consumers/assessors. Verify each dependency checkpoint before advancement.
- [ ] Demonstrate controlled partial-work interruption and resume; separately terminate a worker unexpectedly and resume from actual retained state without extra explanatory prompt context.
- [ ] Verify no setup replay, duplicate hosted writes, lost unrelated staging, replacement unpublished commits or assessor-oracle leakage.
- [ ] Publish an independent final diagnostic report with explicit actions/proposals and all original failures/assistance. Record scope gaps accurately, verify publication and stop cleanly.

## Completion criteria

The directory alone supplies the reusable context; the agent requests only missing external inputs. Fresh and resumed execution use the same entry point. Phase boundaries, controlled triggers and unexpected termination have observed recovery evidence. Test outcomes remain separate from diagnosis, and proposed plugin fixes are causal, bounded and verifiable. No essential runtime dependency remains on the old chat, scratch workspace or AgentPlayground repository.

The reusable test bundle is implemented and reviewed. New live acceptance remains unexecuted and pending as the explicit dedicated-repository follow-up.
