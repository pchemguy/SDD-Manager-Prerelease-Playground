# Task 1 completion report

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

## Scope and commit

Implemented only the assigned coordinator entry/scenario documents, configuration example/schemas and root README navigation. Commit: `63322e66087d16190890787545045869962d0e44` (`Add portable TextStats plugin test coordinator documents and schemas`). No push was performed. No consumer test run, remote operation, product implementation or plugin-package edit was performed. Unrelated root `.codex/` and revision report were preserved.

Owned paths:

- `README.md` (one test-project navigation link)
- `acceptance/textstats/{AGENTS,README,OBJECTIVES,SCENARIO,SETUP,EXECUTION,RECOVERY,DIAGNOSTICS}.md`
- `acceptance/textstats/templates/inputs.example.json`
- `acceptance/textstats/schemas/{inputs,run-state}.schema.json`

## Interfaces

Both schemas use `schema_version: 1`, Draft 2020-12 and strict known object properties. The package_hashes map accepts filename keys with SHA-256 values. Inputs require schema_version and a nonempty explicit test_repository; optional fields are local_checkout, plugin_revision (HEAD), source_mode (committed|dirty, committed default), scope ({}, full default; optional unique phases/cases arrays, nonempty arrays intersect), stop_after (null or phase/case), profile (full-github|local-only|installed-client, full-github default), run_id. Tokens/credential paths are not fields. Missing/blank repository must yield the prescribed interactive action from preflight rather than an inherited destination.

RUN-STATE required fields: schema_version, run_id, phase (P0–P5), case_id (A-001–A-027 or null), attempt (>=1), role (coordinator|consumer|assessor), last_completed_action, pending_operation, next_action, checkpoint_refs, evidence_paths. pending_operation is null or kind (task|commit|push|merge|api|checkpoint), status (in_progress|uncertain|blocked|interrupted), description and optional strict identity. Optional fields: plugin_source (revision, commit, source_mode, package_hashes, manifest_path, snapshot_path, dirty_diff_path), repository (identity/local_checkout/remote/remote_url/integration_branch/campaign_path), capabilities (git_publication/github_api/fresh_consumers/independent_assessor/interruption_control/installed_client/recovery_exports/protected_credentials plus notes), case_results array and updated_at. checkpoint_refs permits evidence/product/integration branch+commit, remote/ref/commit, merge_parents, bundle_paths and local_only_paths.

All helpers are documented with --inputs and --output. observe/assess additionally accept --run-state. prepare --workspace selects an explicitly chosen safe new workspace, required without an existing checkout; only bounded authorized fresh preparation may use it. Helpers do not authenticate or perform consumer workflow work. An authorized empty dedicated destination may receive an owned setup checkpoint; an unborn plugin source cannot count as committed HEAD.

## Verification and traces

- JSON parsing succeeded for both schemas and input example.
- Stdlib structural checks passed for Draft identity, schema_version, strict objects, required-property validity and absence of credential fields.
- Bounded stdlib schema-keyword fixture validation accepted input example, fresh P0 state and interrupted A-021 state. Seven invalid fixtures were rejected: token field, empty repository, invalid phase/case, credential_path field, invalid pending status and attempt zero.
- Neither available Python interpreter had jsonschema installed; no package was installed and no full meta-schema certification is claimed. Task2 owns runtime validation.
- git diff --check and git diff --cached --check passed before commit. Staged/committed paths were explicitly restricted to owned files.
- Relative link checks checked 67 targets. All source skill/provenance links and own-document/schema links resolve. Pending cross-task targets at verification: `cases/assessor/`, `cases/catalog.json`, `cases/consumer/`, `cases/consumer/preparation.md`, `scripts/`, `scripts/assess.py`, `scripts/observe.py`, `scripts/preflight.py`, `scripts/prepare.py`, `tests/`.
- Required entry reading order verified. No owned document requires a historical scratch path or shipped workflow-framework dependency.

Fresh directory-only trace: AGENTS identifies coordinator -> reads six ordered documents -> resolves explicit invocation/file/checkpoint/defaults -> no repository means exact dedicated-repository question before any writes. Supplied repository then discovery preserves contents/index/instructions, distinguishes existing run, uses existing separate Git/API authentication, pins committed source or explicitly dirty snapshot, initializes an authorized empty destination only with bounded setup, reserves/publishes evidence identity and begins scoped case handoffs. Assessor contracts do not enter fresh consumer context.

Resume trace: run_id/checkpoint selected -> identity/scope/source conflicts resolved -> actual files/index/HEAD/merge/provider state read before trusting cursor -> same case/task/campaign restored from exports or retained local state -> uncertain effects read back before replay -> original attempts/interventions retained -> pending commit/push/transfer/merge finished within scope, independently assessed/published before dependent selection. Cross-machine recovery explicitly fails at a missing pending-data boundary rather than replaying clean setup.

## Concerns and handoff

Pending links are exclusively Task2 helpers/tests and Task3 catalog/consumer/assessor paths; preparation path was confirmed as cases/consumer/preparation.md. Root should rerun link checks after those tasks land and inspect helper/schema compatibility. No unconfirmed plugin defect is asserted by this infrastructure task; historical TST-001–004 remain diagnostic lessons. No new execution campaign was attempted.


## Task 1 reviewer follow-up — one-shot stop boundary

Clarified SETUP.md, EXECUTION.md and RECOVERY.md in commit `cdd2451a357ec0696b30f1c6deee14308b937194` (`Clarify one-shot test stop boundaries on resumed scope`). Only those three owned documents changed; no schema/helper/plugin change, push, user question or live run.

`stop_after` is one-shot. Actual assessment/checkpoint evidence must establish the reached stop and its recording. A requested continuation consumes that prior stop, retains original input/stop evidence and records consumption in RUN-STATE/RESUME/continuation evidence. Pending checkpoint/publication is finished before dependent continuation. Execution then stays inside the remaining previously authorized scope. Exhausted scope reports completion and requests new scope; unreached/unverified stops remain active. A newly explicit current-invocation stop is a new active instruction, even if it matches the prior boundary. No new schema field is required.

Checks: all three documents explicitly cover one-shot consumption, exhausted scope, new-scope request, unreached/active stops and retained original evidence. Relative link inspection introduced no new unresolved target; remaining helper/catalog targets belong to other tasks. `git diff --check` and staged diff check passed. Manual traces: reached stop with remaining scope -> reconcile/consume/continue; reached stop with exhausted scope -> report completion/request scope; interruption before stop -> preserve original active boundary; new explicit same stop -> active instruction.
