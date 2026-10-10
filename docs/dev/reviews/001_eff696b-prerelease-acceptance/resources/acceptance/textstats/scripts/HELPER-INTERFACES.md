# Portable coordinator helper contracts

Python 3.11+ and Git are required. The preflight/prepare/observe/assess helpers use `--inputs INPUTS.json --output NEW.json`; observation/assessment additionally require `--run-state RUN-STATE.json`. Paths resolve from the caller, not a historical checkout. Inputs/checkpoints must satisfy the existing strict version 1 schemas. Credentials are never inputs. Username-only SSH transport URLs are allowed; HTTP(S) userinfo, URL passwords and credential queries are rejected. Invalid values yield generic JSON on stdout, exit 2, and no output JSON; missing repository yields the exact question from SETUP before writes. Output paths are exclusive: choose a new attempt path instead of replacing evidence. Success writes version 1 JSON, exit 0. Failed deterministic checks retain assessment JSON, exit 1.

`preflight.py` is read-only except its explicitly requested observation file. It discovers one matching authorized remote (multiple matching remotes block), local/default branch, retained run records, actual remote refs and source identity. Unavailable remote readback is recorded. Capabilities default false for publication/API/agent/client facilities because read access cannot certify them. These four helpers never authenticate, inspect credential stores, push, commit, invoke agents or run product workflows. Explicit disposable fixture controls described below have their own interfaces and may execute caller-selected commands.

`prepare.py --workspace NEW_PATH` creates an isolated clone only when the lexical requested path is absent (including no dangling symlink) and `run_id` is absent. A local checkout is cloned at committed HEAD; its original index/workfiles/instructions are preserved. Clone origin is set to the discovered authorized destination. Existing target contents and instructions are retained. Occupied run resources block. An initially empty dedicated remote receives only pinned vendor/provenance, new operating instructions and ignore rules; no author/integration branch/publication is guessed. Remote read/clone failure remains a prerequisite failure. Preparation is never a resume driver and contains no TextStats implementation.

Preflight/prepare optionally accept `--source-root CHECKOUT`; default is the package repository containing the helper. `plugin_revision` resolves to full SHA. Source package includes the shipped manifests (`plugin.json` and temporary legacy `.codex-plugin/plugin.json`), `.codex-plugin/**`, root `README.md`, `AGENTS.md`, `Greenfield Project Prompt Template.md`, `LICENSE`, `SDD-MANAGER.md` and `AI_DISCLOSURE.md`, `skills/**` and `assets/**` from Git objects: no historical review/dev/assessor artifacts or source credentials. `source_mode: dirty` is explicit, restricted to current source HEAD, and records exact working bytes, changed paths, package hashes, Git executable modes and a mode-sensitive fingerprint. Preparation records the snapshot, provenance manifest and tracked binary diff; untracked additions are represented by exact snapshot hashes. Package symlinks, symlinked package parents and submodules are unsupported and block pinning before external bytes can be read. Snapshot modes preserve executability. A provenance observation has extra diagnostic keys; copy only schema-allowed plugin_source keys into RUN-STATE.

## Observation and recovery

`observe.py` derives real HEAD/branch/parents, refs/worktrees, index entries `{path,mode,oid,stage}`, staged/unstaged/untracked/conflict paths, MERGE_HEAD and actual remote readback. `git.publication` is `published`, `unpublished` or `unknown`: exact destination equality or locally verifiable ancestor containment establishes publication; unreadable remote, detached/unborn state or unavailable remote ancestry remains unknown. Local tracking refs never establish publication. `reconciliation.effect` is `observed-published`, `not-observed-at-destination`, `unknown`, `unfinished` or `none`; `retry_safe` is always false because readback does not authorize replay. A pending push explicit ref overrides its branch field: only that destination readback establishes its effect. A recorded pending repository different from the observed destination remains unknown; unavailable containment ancestry also remains unknown. An uncertain API effect remains unknown pending exact hosted identity readback by the coordinator.

The observer writes a new adjacent `NEW.json.recovery/` export at the caller's output location, creating missing output parents and recording an absolute export path. Occupied output or recovery paths, including dangling symlinks, are refused; consumer Git/index/workfiles remain unchanged. Its manifest records HEAD/branch/parents, original tracked paths, full eligible index stages, pending files/deletions/modes/symlink targets, staged/unstaged patches, merge metadata (`MERGE_HEAD`, `MERGE_MSG`, `MERGE_MODE`, `ORIG_HEAD`), retained commit roots and artifact SHA-256s. Blob exports preserve index object identities; workfile content is binary-safe and separately hashed. A verified Git bundle includes named refs, HEAD and available merge/checkpoint/pending commit roots. Protected paths are omitted without reading their content; protected historical paths or unavailable required commit roots make the export incomplete. Recognizable secret content blocks evidence export with a generic cause. All recovery artifacts are `local-only` until an independently verified evidence publication contains them. Ignored noncredential workfiles and submodule working state are outside the export; retain them separately if required. `complete` describes the declared Git/index/nonignored-file export, not arbitrary machine state or credentials.

Restoration remains coordinator-owned: validate every artifact hash and path, clone/fetch into a new isolated workspace at recorded HEAD, import blob objects with `hash-object -w`, rebuild index with NUL-safe `update-index -z --index-info` stage records, restore workfiles separately, remove original tracked paths absent from retained index/workfiles and apply explicit deletions. Restore merge metadata only when recorded and required objects exist. Compare actual index stages, staged/unstaged diffs, file hashes/modes, HEAD and merge parents before continuing. Never restore over occupied work or treat partial exports as successful recovery. Self-tests actually reconstruct staged/unstaged/binary/symlink work, deletion intent and conflict state (including unreferenced incoming merge commit).

## Deterministic assessor contract

`assess.py` optionally accepts `--contract CONTRACT.json --evidence EVIDENCE.json`. No contract yields `status: "Not run"`. A supplied contract must contain a nonempty check array; missing/invalid evidence cannot pass. It reads actual Git/file/task evidence but executes no product commands. Independent assessors must capture real command results separately and retain their provenance; a JSON literal alone does not prove which command ran.

Contract version 1:

```json
{
  "schema_version": 1,
  "case_id": "A-004",
  "checks": [
    {"id": "cli", "kind": "literal", "key": "named-file", "expected": {"returncode": 0, "stdout": "lines=3 words=2\n", "stderr": ""}},
    {"id": "head", "kind": "git", "field": "head", "expected_ref": "checkpoint_refs.product_commit"},
    {"id": "owners", "kind": "task_ownership"}
  ],
  "required_agent_checks": ["Independently assess actual routing, scope, checks and assistance."]
}
```

`case_id` and `required_agent_checks` are optional, descriptive assessor context. Check IDs must be unique. Unknown contract/check/evidence fields fail. Kinds:

| Kind | Required fields and meaning |
| --- | --- |
| `literal` | `key`, `expected`: exact JSON equality including type, array order, stdout/stderr whitespace and exit code; bool differs from integer. |
| `git` | `field`, exactly one of `expected`/`expected_ref`; fields are `head`, `branch`, `parents`, `merge_heads`, `staged_paths`, `unstaged_paths`, `untracked_paths`, `conflict_paths`, `publication`, `remote_containment`. |
| `file` | Relative safe `path`; at least one of boolean `exists` or lowercase `sha256`. No absolute/escaping/protected/symlink paths. |
| `task_ownership` | Optional additive `documents` array for explicit child lists; parse active TASKS/FEATURE-TASKS owners, reject empty collections/duplicates/malformed candidates; exclude history/vendor resources and fenced examples. Ordinary links are not traversed. |

Runtime `expected_ref` resolves exactly one existing schema-validated checkpoint field such as `checkpoint_refs.product_commit`, `checkpoint_refs.integration_commit` or `checkpoint_refs.merge_parents`; it never hardcodes historical identities and does not certify checkpoint freshness. Evidence shape is exactly `{"schema_version":1,"literals":{"named-file":{"returncode":0,"stdout":"lines=3 words=2\n","stderr":""}}}`. Literal keys and values are independently retained actual observations, not a case registry or consumer claims. No automated agent-case result is accepted.

Assessment shape: `{"schema_version":1,"status":"Checks passed"|"Checks failed"|"Not run","checks":[{"id":"...","status":"Passed"|"Failed","reason":"..."}],"agent_behavior_assessed":false,"required_agent_checks":[...]}`. Deterministic success never confers case Passed or full acceptance. Agent routing, ownership decisions, assistance, interruption/fresh-context behavior and causal diagnosis require independent assessment.

Run the complete nonempty support suite from the package root: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`. Tests use only disposable repositories and local bare remotes; no hosted writes occur.

## Task ownership document model

`task_ownership` reads active TASKS.md/FEATURE-TASKS.md roots, excluding archive, features, reviews and vendor/run-resource history. It does not follow ordinary Markdown links. An optional additive `documents` array names explicit active child lists by repository-relative Markdown path; default roots still participate. Paths must be nonempty, unique, normalized with `/`, safe and nonprotected. Missing files, symlinks in the path and historical documents block the check. Catalog validation checks the option's syntax; runtime assessment additionally checks actual files. Naming a document does not establish that the assessor selected every required child list.

Task IDs are case-sensitive ASCII tokens beginning with a letter, with alphanumeric segments separated by single hyphens or underscores. An ID must contain a digit or a separator: `T-001`, `F-001`, `TASK_001`, `ABC42` and `BUILD-alpha` are supported. Checkbox IDs may be plain, inline-code or bold tokens. Recognized `Phase <id>` and `Milestone <id>` checkbox parents are excluded; other checkbox candidates require a valid task ID. Task tables use exactly one `ID` or `Task ID` column and a `Status` column, with a separator row and nonempty status values. Malformed candidates fail instead of being silently skipped; the checker reports ownership, not completion eligibility.

Backtick and tilde fenced examples are excluded, including fences indented inside task details. A closing fence uses the same marker, at least the opening length and no non-whitespace suffix. An unmatched opening fence fails the collection rather than concealing later work. General prose, headings and non-owning links are not task entries. Unsupported/ambiguous candidate rows produce a sanitized validation failure. Every actual duplicate task ID across the selected active documents fails. Repeated discovery of one document is deduplicated; duplicate explicit option entries are invalid. Empty executable collections fail. Independent assessment remains necessary for task hierarchy, scope, dependencies and selection coverage.

Example additive child-list contract:

```json
{"id":"owners","kind":"task_ownership","documents":["docs/dev/tasks/streaming.md"]}
```

## Selected variants and fixture support

Version 1 inputs optionally accept `variants: {"A-024": ["denial", "rate-limit", "unavailable-access"]}`; the map bounds case/variant scope and must agree with case/phase filters. Checkpoints optionally record `variant`. Contracts may include `variant_agent_checks` mapping each declared variant to its nonempty independent criteria. A selected checkpoint variant adds only its own criteria to common checks; deterministic observations are not independently graded results. An unselected split contract returns `variant_selection_required: true`, the available variant criteria and an explicit assessment limit; deterministic Checks passed cannot complete variant grading. Select a variant before independent variant grading; historical contracts/checkpoints remain usable without retroactively inventing variant outcomes.

Local-only assessment contracts do not read remote refs implicitly. Contracts requesting `publication` or `remote_containment` do read the established destination. `catalog_tools.py render --variant <id>` selects a declared variant's prerequisite binding, including the A-014 refusal start. All binding provenance/live prerequisite checks still apply.

- [campaign.py](campaign.py): read-only `--catalog`, `--results`, optional `--selection`; supplied independent grades produce separate required/optional totals. See [VARIANTS](../VARIANTS.md).
- [trial_control.py](trial_control.py): explicit eligibility/command hold/resume interfaces in [TRIAL-CONTROLS](../TRIAL-CONTROLS.md). Commands run only in the caller-authorized disposable root; the control never chooses product actions or claims agent acceptance.
- [contract_probe.py](contract_probe.py): `--root` executes independent literal TextStats API probes in a fresh interpreter; `--inject-isolated --expected-head <full SHA>` explicitly creates the disclosed off-by-one fixture in a clean disposable implementation. Missing imports/zero checks are unavailable setup, not the required assertion failure.
- [fault_adapter.py](fault_adapter.py): controlled disposable effect ledger, not a live provider. See the [A-023 guide](../cases/assessor/A-023.md) for operation/fault/readback interfaces and [A-024](../cases/assessor/A-024.md) for classified access faults.
- [evidence_merge.py](evidence_merge.py): read-only exact-parent/campaign-only-delta/report-presence audit with full object IDs. [Final integration](../EXECUTION.md#final-evidence-integration) independently verifies source/assessment hashes and remote publication.

Fixture effects and support checks never supply runtime acceptance. Preserve historical grades, source packages and original attempts. Optional live/native execution requires the named facilities and actual consumer/independent evidence.
