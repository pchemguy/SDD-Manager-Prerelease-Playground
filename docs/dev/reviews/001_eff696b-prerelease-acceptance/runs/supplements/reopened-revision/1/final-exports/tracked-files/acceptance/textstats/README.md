# TextStats acceptance test project

This portable project diagnoses **SDD Manager plugin behavior** by having consumer agents prepare and deliver a small Python TextStats product, then independently assessing scope, task ownership, verification, Git/GitHub lifecycle and recovery. Product documents produced in the dedicated consumer repository remain ordinary development artifacts. This bundle supplies reusable requests and assessors; it contains no finished implementation.

Minimal invocation:

```text
Run the test project in acceptance/textstats/.
Use the dedicated repository <URL or existing checkout>.
```

Without the repository, the coordinator asks for it before writes. No old repository, token or session is a default. For bounded work add `scope` or `stop_after`; for continuation name the existing `run_id` and checkpoint. See [agent entry](AGENTS.md) for reading order and [setup](SETUP.md) for configuration/authentication.

## Directory map

| Path | Purpose |
| --- | --- |
| [OBJECTIVES.md](OBJECTIVES.md) | Capabilities, evidence and outcome criteria |
| [SCENARIO.md](SCENARIO.md) | Chosen sample contracts and incremental scope |
| [SETUP.md](SETUP.md) | Repository/source identity, tools and access |
| [EXECUTION.md](EXECUTION.md) | Ordered execution, roles and checkpoints |
| [RECOVERY.md](RECOVERY.md) | Planned, injected and unexpected interruptions |
| [DIAGNOSTICS.md](DIAGNOSTICS.md) | Attribution, reproduction and final report |
| [cases/catalog.json](cases/catalog.json) | Stable A-001–A-027 intents and dependency selection |
| [cases/consumer/](cases/consumer/) | Reusable consumer inputs, without assessor answers |
| [cases/assessor/](cases/assessor/) | Independent oracles; coordinator/assessor access only |
| [templates/inputs.example.json](templates/inputs.example.json) | Non-secret configuration example |
| [schemas/inputs.schema.json](schemas/inputs.schema.json) | Version 1 configuration |
| [schemas/run-state.schema.json](schemas/run-state.schema.json) | Version 1 coordinator checkpoints |
| [scripts/](scripts/) | Preflight, bounded preparation, observation and checks |
| [tests/](tests/) | Harness sensitivity/recovery checks |

## Support-test discovery

From the repository root, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v
```

Only `acceptance/textstats/tests/` contains a package marker. The acceptance directories are not regular Python packages.

## Configuration and profiles

Required: `test_repository` (explicit URL or unambiguous existing checkout). Optional: `local_checkout`, `plugin_revision` (committed HEAD), `scope` (full), `stop_after` (none), `profile` (`full-github`), `run_id` (existing identity for resume), and `source_mode` (`committed`). Credential values are never JSON fields. [SETUP](SETUP.md) defines defaults and precedence. Do not run the placeholder example unchanged.

`full-github` includes actual Git publication, live GitHub tracking and controlled isolated failures. `local-only` is a bounded coverage subset, never full acceptance. `installed-client` additionally requests actual installed-client discovery/routing/activation evidence; missing installation facilities are Not run, even if explicit source loading succeeds. Every profile records actual facilities and omitted cases.

## Phases and outputs

| Phase | Durable boundary |
| --- | --- |
| P0 | Resolved inputs, pinned source, observed capabilities and published harness |
| P1 | Prepared product documents, task ownership and selection-only assessment |
| P2 | Verified/published baseline product phase |
| P3 | JSON increment, line feature, steering removal, stdin and final integration |
| P4 | Actual prerequisite forks, failures and fresh continuation trials |
| P5 | Required/optional reconciliation, final report, evidence-only merge into main, verified main publication and checkpoint |

Coordinator evidence lives in the dedicated test repository at `docs/dev/reviews/<campaign>/`: `INPUTS.json`, `RUN-STATE.json`, `RESUME.md`, `runs/<case-id>/<attempt>/`, `DIAGNOSTIC-REPORT.md` and retained recovery exports. Reserve one convention-named evidence branch. [EXECUTION](EXECUTION.md) defines publication gates. Record capabilities/source once; update only changed facts.

A stop preserves unfinished work rather than turning it into a completion commit. A resumed run reads actual Git/files/index/hosted state before trusting its cursor or retrying uncertain operations. Cross-machine continuation requires exported pending files, index intent and Git objects as well as published refs. [RECOVERY](RECOVERY.md) specifies each case and the exact unrecoverable-boundary report when an export is missing.

## Fresh full live acceptance on a dedicated test repository

- [ ] **Live acceptance on a dedicated test repository.** Supply an explicitly identified repository URL or checkout path, then run this bundle through fresh consumers and independent assessors. Exercise real Git publication and GitHub tracking, controlled partial-work interruption and resumption from retained state. Native termination and complex live/native recovery are optional extensions with separately reported facilities and outcomes. Publish the diagnostic report with original attempts, assistance, findings, actions and proposed plugin changes.

Bundle self-tests and document reviews verify the reusable infrastructure. They do not complete this live acceptance follow-up. Report unavailable required facilities as Blocked and optional extensions as Not run/non-blocking; retain exact scope and evidence classes. See [variants](VARIANTS.md) and [controls](TRIAL-CONTROLS.md). Use existing authentication first; request protected credentials only after a classified access failure, following [SETUP](SETUP.md#protected-authentication).

Copyable agent prompt (replace the placeholders):

```text
Run live acceptance for SDD Manager using <SDD-Manager-checkout>/acceptance/textstats/.
Use the dedicated test repository <repository URL or existing checkout path>.
Read AGENTS.md in the bundle and follow its linked setup, execution, recovery and diagnostic procedures.
Use the full-github profile and the full supported case scope. Continue through authorized phases;
preserve actual state at interruptions and resume from retained evidence. Use fresh consumer and
independent assessor contexts, keeping assessor expectations out of consumer handoffs.
Use existing authentication first. If the repository is omitted, request it before setup writes;
request protected credentials only when required access is actually unavailable.
Publish the diagnostic report with coverage, original attempts and assistance, observed issues,
actions taken and concrete proposed SDD Manager changes, or the supported no-defect/no-change conclusion.
Do not modify the tested plugin package during the run. Record unavailable required facilities as Blocked
and optional extensions as Not run/non-blocking. Finish by merging final acceptance evidence into test main
and verifying its publication, unless an explicit earlier stopping boundary applies.
```

Historical provenance: [campaign 008 plan](../../docs/dev/reviews/008_98a5562/REVISION-PLAN.md) and [report](../../docs/dev/reviews/008_98a5562/REVISION-REPORT.md). These explain derivation and limits; they are not bootstrap inputs or expected new-run results.
