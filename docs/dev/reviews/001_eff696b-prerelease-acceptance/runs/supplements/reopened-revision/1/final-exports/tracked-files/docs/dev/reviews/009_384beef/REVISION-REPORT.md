# TextStats diagnostic test-project integration revision report

## State and scope

Campaign `009_384beef`, baseline `384beefb6186348af9b100de9bec2f5a4a024692`. The user authorized execution of [REVISION-PLAN](REVISION-PLAN.md). Execution branch: `revision/009_384beef-textstats-test-project`, starting at `78d51c4`. Established target: `feature/architecture-revision`.

The reusable test bundle is implemented and independently reviewed through `584cfe0`. All 67 support/catalog tests pass. No new live consumer campaign has started. Live acceptance requires an explicitly supplied dedicated test repository; none has been supplied for this run. The previous AgentPlayground campaign is historical evidence and is not the new destination.

## Diagnostic summary

- **Demonstrated:** a complete reusable 27-case bundle, strict configuration, independent actual-output checks, and support tests that restore pending files/index/conflicted merge state in fresh clones. A fresh directory-only coordinator discovered the missing repository requirement and made no setup writes. These are infrastructure results; no new live SDD Manager consumer outcomes are claimed.
- **Issues observed:** reviews found ambiguous stop consumption, incorrect pending-destination reconciliation, symlink containment gaps, SSH URL over-rejection, shallow-ancestry uncertainty, lost failed-capture provenance and inconsistent recovery output paths. Each was corrected and independently rechecked. Original failures remain in the evidence ledger.
- **Actions taken:** added and reviewed the documents, schemas, helpers, all 27 case contracts/requests/guides and sensitivity/recovery checks; corrected the reported infrastructure defects. Both this report and the bundle README include the explicit live-acceptance TODO and copyable agent prompt. All 97 shipped plugin files remain unchanged.
- **Plugin changes proposed:** none on the basis of this infrastructure work. Live execution and its causal plugin diagnosis remain the documented follow-up; historical findings are provenance, not new outcomes.

## Interface rulings

| Boundary | Agreed contract |
| --- | --- |
| Documents / helpers | Strict version 1 inputs and run-state schemas. All helpers accept `--inputs` and `--output`; observation/assessment also require `--run-state`. Credentials are never configuration fields. |
| Documents / cases | Catalog IDs A-001–A-027; consumer preparation at `cases/consumer/preparation.md`; separate consumer and assessor assets. |
| Helpers / cases | Runtime identity checks bind actual validated checkpoint refs. Literal deterministic checks require independent actual evidence; `agent_behavior_assessed: false` prevents automatic case acceptance. |
| Bundle / live acceptance | Directory-only bootstrap must request a missing repository before setup writes. Build and verify infrastructure first; retain live execution pending its destination. |

Committed source is the default tested identity. Optional `source_mode: dirty` explicitly fingerprints a dirty snapshot. Optional `--workspace` selects a distinct fresh local workspace; preparation refuses occupied resources and never drives resumption. Initially empty dedicated remotes permit bounded setup without guessing completed product history, branch authorization or publication.

A reached, independently recorded `stop_after` is consumed on requested continuation inside the remaining authorized scope. Pending evidence/publication is completed first. Unreached stops persist; exhausted scope requires new scope. Original stop/input evidence remains retained.

Helpers never authenticate, push, mutate hosted resources or perform consumer workflows. Publication observation uses actual remote readback, with unavailable ancestry/access retained as unknown. Recovery exports remain local-only until their publication is independently verified.

## Execution ledger

### Task 1 — Documentation and schemas: complete

Commit `63322e6` added eight coordinator documents, strict inputs/run-state schemas and root README navigation. Independent specification review passed; quality review approved with low-severity DOC-001 stop clarification. Commit `cdd2451` implemented the agreed one-shot rule. [Implementation evidence](evidence/task-1-report.md) and [independent review](evidence/task-1-review.md) are retained.

Cross-task links to helpers and case assets are checked after their implementation, rather than treated as missing Task 1 work.

### Task 2 — Portable support: complete

Commit `fb5bbf1` added bounded preflight/preparation, actual-state observation/recovery exports and deterministic assessment. The full support suite collected and passed 33 tests using disposable local repositories/remotes. Tests reconstructed staged/unstaged/binary/symlink/deleted work and conflict state in fresh clones, including an incoming merge commit absent from named branches. Checker fault sensitivity evidence is retained separately. The first RED run demonstrated absent helper interfaces; it is not represented as behavioral failure evidence. Independent review reproduced four defects: pending-push readback could ignore its exact destination, dangling workspace symlinks could evade occupancy refusal, dirty-source pinning could follow external parent symlinks, and normal SSH URLs were rejected. Commits `24dc609` and `5fa622e` fixed these and passed 40 tests. Scoped re-review confirmed the concrete corrections but reproduced a remaining shallow-ancestry uncertainty defect in publication reconciliation. Fix round 2 (`3b4049e`) introduced conservative shared ancestry checks; all 41 support tests passed. Independent re-review accepted Task 2, with all four findings addressed and no new fix-diff breakage. Original implementation, review failures and correction evidence remain retained. [Implementation report](evidence/task-2-report.md), [independent reviews](evidence/task-2-review.md), [regression RED](evidence/task-2-shallow-red.log) and [final GREEN](evidence/task-2-shallow-full-green.log) are retained.

### Task 3 — Case catalog and isolated handoffs: complete

Task 2 passed its support review gate. Task 3 implementation starts at `08b700b`: preserve all 27 original intents, runtime prerequisites and separate expectations; do not copy completed records or product implementation. Commit `909e7fc` added all 27 cases, isolated requests, independent guides/literals, catalog validation, handoff rendering and actual-output capture. All 58 support/catalog tests passed. Independent review found one blocker, T3-R1: failed/timed-out nested capture could discard first-attempt provenance. Commit `5bb917d` preserves sanitized failed-capture provenance, partial channels and prior attempts without successful literal evidence. All 64 support/catalog tests passed; independent specification and quality re-review approved Task 3. [Implementation report](evidence/task-3-report.md), [independent review](evidence/task-3-review.md), [original reproduction](evidence/task-3-review-repro.log), [regression RED](evidence/task-3-fixwave1-red.log) and [final GREEN](evidence/task-3-fixwave1-tests.log) are retained. Root retains this ledger.

### Task 4 — Fresh-context bootstrap verified; live acceptance follow-up open

A fresh coordinator received only the bundle directory pointer at `f6fd96f`. It independently identified the exact required repository question, no default destination and the before-write gate. Before/after HEAD, branch, 283 tracked-file hashes, refs and status matched. [Bootstrap observation](evidence/directory-bootstrap.md) retains the actual response, verification method and limits. Authentication, actual setup, fresh product consumers/assessors, controlled/unexpected product interruption recovery, hosted reconciliation and the final live diagnostic report remain the dedicated-repository follow-up. Task 4 is partially verified, not fully complete; missing facilities remain Blocked/Not run, never Passed.

## Final infrastructure verification and publication boundary

Whole-bundle review initially reproduced caller-relative recovery export failure and identified stale plan status. The single final fix wave (`584cfe0`) aligned Python/Git export paths, supported nested output parents, preserved occupied/symlink refusal and corrected the plan metadata. The reviewer independently reran both original path failures and accepted specification and quality with no new fix-diff breakage. [Whole review](evidence/whole-bundle-review.md), [original reproduction](evidence/whole-bundle-review-repro.log), [fix report](evidence/final-fix-report.md), [RED](evidence/final-fix-red.log), [67-test GREEN](evidence/final-fix-full-green.log) and [independent recheck](evidence/final-fix-review-repro.log) remain retained.

`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v` collects the relocated 67-test suite. The original pre-relocation verification collected 67 tests and passed all 67, with zero failures/errors. Final integration checks found 71 resolving local Markdown targets, no missing targets and all 97 plugin files byte-identical to the pre-revision snapshot. Revision-range whitespace checks passed. [Integration observation](evidence/final-integration-checks.json) records the checked implementation identity. No new installed-client, live provider, product-worker interruption or 27-case acceptance result is inferred.

The reviewed infrastructure and evidence are committed on `revision/009_384beef-textstats-test-project`. The user subsequently authorized merging this branch into its established target, `feature/architecture-revision`, with live acceptance retained as an explicit follow-up. Integration accepts the reusable infrastructure; it does not claim the live campaign ran. No unfinished consumer work exists in this revision because no new consumer destination was selected.

## Root-level acceptance layout correction

Following the user's layout correction, the bundle now lives at `acceptance/textstats/`, outside the repository's `tests/` tree. Removed the three higher-level package markers; the only retained `__init__.py` is `acceptance/textstats/tests/__init__.py`. Updated helper/source-root depth, schema identifiers, active links, invocations and live-acceptance prompts. Focused discovery uses `python -m unittest discover -s acceptance/textstats/tests -t acceptance/textstats -v`, so higher-level packages are unnecessary.

The relocated suite passes all 67 tests ([execution log](evidence/relocation-final-tests.log)); all 27 catalog entries validate. [Layout checks](evidence/relocation-checks.json) found 120 resolving local document targets, no stale active layout references, only the intended test package marker, and all 97 plugin files unchanged. Markdown references in earlier evidence were normalized to the current layout and labeled; raw logs preserve the original executed commands. Live acceptance remains the follow-up below.

## Follow-up

- [ ] **Live acceptance on a dedicated test repository.** Obtain an explicitly supplied repository URL or checkout path and execute the completed bundle through fresh consumers and independent assessors. Cover real Git/GitHub lifecycle, controlled partial-work interruption and unexpected termination/resumption, then publish the final diagnostic report with retained original attempts and explicit findings, actions and plugin proposals. This is outstanding live acceptance work; helper self-tests and infrastructure reviews do not complete it. The [test-project README](../../../../acceptance/textstats/README.md#follow-up-live-acceptance-on-a-dedicated-test-repository) records the same follow-up.

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
Do not modify the tested plugin package during the run. Record unavailable facilities as Blocked/Not run.
```

## Authorized integration

Refreshed target `feature/architecture-revision`: `78d51c48189a5bb734df638f0075a5071de61a4d`.
Verified working implementation: `96abd6a093a72c8b5aa2e1495d9cf43397b40dce`.
User authorized the merge after infrastructure review and relocation verification. Retain the revision branch, use an explicit two-parent merge, verify the prospective merged state and publish to the established target. Prospective integration is conflict-free. Target parent `78d51c48189a5bb734df638f0075a5071de61a4d`; working parent `bf70e4d2363733d83642c4777b232133ab0f4e0e`. All 67 tests pass, all 27 catalog entries validate, and all 97 plugin files remain unchanged. [Verification record](evidence/integration-verification.json) and [merged-state test log](evidence/merge-prospective-tests.log) retain the checks. The explicit merge commit records these two parents; its target publication completes integration. Live acceptance remains unchecked.

## Next action

Use the copyable prompt above when ready for live acceptance on the explicitly supplied dedicated repository. The reusable infrastructure is reviewed and verified; preserve this evidence and start a separately identified live run. Do not claim a new live campaign passed from infrastructure checks.
