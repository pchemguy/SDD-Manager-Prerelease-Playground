# Resolve and initialize a run

Setup is coordinator-owned **plugin test infrastructure**. Perform discovery before mutation. Never replay fresh preparation against an interrupted run.

## Inputs and defaults

Use [inputs.schema.json](schemas/inputs.schema.json), schema version 1. Resolve current invocation > explicit input file > checkpoint for requested continuation > defaults. Record resolved non-secret values once in INPUTS.json; never put credential values or credential-file paths in configuration/checkpoints. A missing/empty repository is unresolved, not a default.

| Field | Meaning/default |
| --- | --- |
| `schema_version` | `1` |
| `test_repository` | Required explicit URL or unambiguous existing checkout with authorized remote; no default |
| `local_checkout` | Optional existing checkout associated with the identified repository; discover/verify rather than assume |
| `plugin_revision` | `HEAD`: full committed source HEAD observed at run start; supplied revision resolves to full SHA |
| `source_mode` | `committed`; explicit `dirty` testing snapshots requested package edits and records base SHA plus hashes/diff |
| `scope` | `{}` means full supported campaign; optional `phases`/`cases` arrays bound selection |
| `stop_after` | `null`; optional one-shot P0–P5 or A-001–A-027 boundary; stop after its assessment/checkpoint |
| `profile` | `full-github`; `local-only` is partial acceptance, `installed-client` additionally requests installed execution |
| `run_id` | Optional existing campaign identity when explicitly resuming; allocate a fresh identity otherwise |

If no repository is supplied, ask exactly: “Which dedicated test repository should this run use? Supply its URL or local checkout path.” No writes or fixture setup precede this resolution. Conflicting identity, destination, source or scope requires a concrete decision. Non-GitHub repositories can support local cases only; do not call them full GitHub acceptance.

Inspect checkout eligibility, applicable instructions, branches/remotes, default branch, HEAD, worktrees, tracked/untracked paths and index ownership. URLs and remote displays must be sanitized; reject credential-bearing URL inputs rather than record them. Confirm repository identity against the requested destination. `main` and `origin` are defaults **only after discovery confirms them**; preserve explicit/legacy branches, transport and remote. Multiple plausible remotes require selection before writes. Preserve all existing files, instructions, staging, hosted objects and credentials. Do not reset/clean/stash/force-push or repurpose an unrelated checkout.

## Fresh or resume

A stored `stop_after` is a **one-shot boundary**, not a permanent ceiling on every continuation. A requested resume consumes that prior boundary only when actual assessment/checkpoint evidence establishes it was reached and the stop was recorded. Continue only within the remaining previously authorized scope; if that scope is exhausted, report completion and request new scope rather than inventing more work. An unreached or unverified boundary stays active. Preserve the original INPUTS and stop evidence; record consumption in RUN-STATE/RESUME and the continuation evidence instead of deleting history. A newly explicit boundary in the current invocation is a new active instruction and is not consumed merely because a prior stop had the same value.

Search retained campaign records and relevant local/remote branches. A named existing `run_id` is a continuation, not permission to recreate it. Verify INPUTS/RUN-STATE/RESUME identity and [reconcile actual state](RECOVERY.md). If records exist but intent is ambiguous, resolve resume versus distinct new run before writes. A new run gets a new convention campaign/evidence branch and isolated workspace; it must not overwrite an existing campaign/product. An unborn source cannot supply a committed HEAD identity. Detached/conflicted or insufficiently identified work blocks affected actions until identity/ownership is established; an empty dedicated destination can receive the bounded setup below.

A newly supplied dedicated remote may be empty/unborn. After verifying that it is genuinely the authorized empty repository, the coordinator may select a safe new local workspace and use `prepare.py --workspace <explicit-new-path>`; the user need not choose every local path. Bound initial setup to the pinned vendor/harness, operating instructions/provenance and owned ignore rules, without product implementation. Resolve author, integration branch and publication destination using ordinary SDD/Git protocols and actual remote/API discovery; do not silently configure a global identity or overwrite a branch. Publish/verify the owned setup checkpoint, then use its full SHA as the consumer baseline for campaign allocation. This coordinator initialization is outside the product skill's implementation scope. If access/author/default-branch facts remain unavailable, report the particular blocked operation rather than treating every empty repository as ineligible.

For a fresh run reserve the consumer repository's shared review/feature sequence using the pinned [branch rules](../../skills/sdd-manage/references/branch-management.md). Keep full baseline SHA, campaign directory, evidence branch, product working branch and integration target distinct. Evidence belongs under `docs/dev/reviews/<campaign>/`; the stable branch uses `revision/<campaign>-<slug>` according to current naming/collision rules. Phase and feature branches are consumer-produced workflow objects, not this evidence branch. Avoid using the same branch in two worktrees.

## Pin source and runtime before consumers

Resolve source from the committed package checkout. Record full 40-character commit SHA and SHA-256 for the shipped manifests (`plugin.json` and temporary legacy `.codex-plugin/plugin.json`), every shipped skill/reference/asset, root AGENTS.md, root README, root `Greenfield Project Prompt Template.md`, root usage/disclosure notices and required package metadata/license. The package snapshot under the test repository's isolated run resources contains the exact resolved version, licenses and provenance, excluding Git metadata, credentials, this assessor bundle and unrelated source development files. Preserve a separately accessible harness version/commit/hash manifest. Commit/push reusable run inputs and harness before use; do not claim an unpushed harness was published.

Default source is committed HEAD even when the source working tree is dirty: copy from the committed tree. Only explicit `source_mode: dirty` authorization tests working-tree changes. Then record base commit, changed package paths, exact hashes and sanitized diff; label the identity **dirty-source snapshot**, never HEAD-tested. If source changes after pinning, keep the run snapshot unchanged. A repair requires a separate accepted change/new identity.

Record interpreter, Git, available API/client versions, client loading mode and facilities: fresh worker contexts, independent assessor context, interruption control, Git publication, hosted read/write, protected credential channel, recovery exports and installed-plugin mechanism. Use Python 3.11+ for the sample/harness and ordinary filesystem/Git tools. Execute only available checks and record actual versions. Explicit skill-source loading is supported without installation, but cannot certify automatic discovery/routing/activation. Missing facilities label affected cases Blocked/Not run. No API write probe or unrelated auth probe is needed simply because no token file exists.

## Consumer repository disclosure

The pinned package must contain `assets/AI_DISCLOSURE.md` and `assets/SDD-MANAGER.md`. Preparation vendors those assets; the harness must not create the target root copies or README links on the consumer's behalf. Inspect the first consumer-owned SDD commit (normally A-001 preparation): root disclosure matches the pinned asset bytes when newly added, root usage notice names/links SDD Manager and links the disclosure, and the root README links both. With existing records, verify truthful preservation/reconciliation and the reported retention reason. If the repository already has an SDD checkpoint, assess idempotent reuse or scoped backfill instead of claiming first-commit bootstrap.

For isolated follow-up fixtures, cover read-only no-write, explicit selected-path conflict, differing existing disclosure preservation, interrupted pending copies/index, and committed-but-unpushed continuation. These are live follow-up checks, not established outcomes of this source revision.

## Protected authentication

Use current session Git authentication for authorized publication and an available authenticated API client for hosted operations. Git success does not prove API authentication; API success does not prove Git transport. Follow the **pinned** [sdd-manage credential protocol](../../skills/sdd-manage/references/credentials.md) and [GitHub backend](../../skills/sdd-forge/references/github.md). Request protected credentials only after classified unavailable access for the target operation. Rate limits, outages, quota, validation and policy restrictions need their actual remedy, not token substitution.

On eligible auth failure, identify sanitized provider/repository, operation, endpoint/destination, client/transport and cause. Discover an eligible ignored/untracked `gh.tkn` only inside the dedicated test repository, beside its root `.gitignore`; check effective ignore including negations and tracked/index status before reading/saving. Preserve existing rules/staging and restrict permissions/ACLs. Tracked credentials require explicit remediation; never clear staging broadly. A source-repository credential is not transferable authorization.

If no suitable credential exists, request a repository-scoped protected supply using a supported secure input/client mechanism. GitHub's pinned conventional fine-grained profile selects only the target repository with read/write Commit statuses, Contents, Issues, Pull requests and Workflows; Metadata read is automatic. Actions access is conditional for requested workflow dispatch/run operations, not implied by Workflows access. This grants no PR operation, policy bypass or new destination. Never ask for the token in a worker prompt, JSON, journal, argument, remote URL or public report. Keep any accepted token only in its conventional ignored/untracked protected store; transient helper input uses a protected channel. HTTPS Git helper recovery and API client recovery are separate; an SSH transport is not silently converted to HTTPS.

After recovery retry the affected authorized operation within pinned retry bounds (default at most three), then verify actual remote/object effects. Uncertain effects require readback first. If protection/storage/client support is unavailable, preserve pending local work and report the exact blocker. Credential-free evidence records capability/outcome, not a path or value of the secret store.

## Helpers and publication

All support helpers use `--inputs <resolved-inputs.json>` and `--output <observation.json>`. [preflight.py](scripts/preflight.py) observes configuration/source/repository/facilities; [prepare.py](scripts/prepare.py) performs bounded fresh workspace/fixture preparation only after identity/authorization is resolved. Observation is read-only; preparation is not a substitute for consumer work and must distinguish fresh from resume. Helpers do not authenticate or perform consumer workflow work; actual scope and protected authentication remain coordinator responsibilities. `prepare.py --workspace <explicit-new-path>` selects an authorized new workspace and is required when no existing checkout is configured; it must not select a random ephemeral destination or overwrite an occupied path. [observe.py](scripts/observe.py) and [assess.py](scripts/assess.py) additionally accept `--run-state <RUN-STATE.json>` for current-state capture/checking. Treat their JSON as evidence, not an independent agent diagnosis. Exact machine formats, source pinning limits and restoration guidance are in [helper interfaces](scripts/HELPER-INTERFACES.md). See [EXECUTION](EXECUTION.md) for handoff/checkpoint ordering.

Resolve helper paths from the pinned harness location, not a previous scratch checkout. Example from the source root (with a real resolved input file):

```sh
python acceptance/textstats/scripts/preflight.py --inputs /path/to/INPUTS.json --output /path/to/preflight.json
python acceptance/textstats/scripts/observe.py --inputs /path/to/INPUTS.json --run-state /path/to/RUN-STATE.json --output /path/to/observed.json
python acceptance/textstats/scripts/assess.py --inputs /path/to/INPUTS.json --run-state /path/to/RUN-STATE.json --output /path/to/assessment.json
```

Commit/push sanitized evidence on the reserved evidence branch at case boundaries and before dependents. Verify destination containment; label pending local artifacts and unpushed evidence accurately. Product commits and integration remain consumer/plugin-owned. Mid-operation preservation must not create a false product completion commit. Store protected credentials separately from all recovery exports.
