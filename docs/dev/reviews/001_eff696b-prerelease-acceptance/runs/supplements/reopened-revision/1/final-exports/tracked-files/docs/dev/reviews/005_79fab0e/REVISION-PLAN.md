# Repository token convention revision plan

## Campaign and scope

- **Campaign:** `005_79fab0e`; date 2026-10-02.
- **Starting and inspected baseline:** `79fab0e91a06fcc100a0e18cb0e1295085c4146c`.
- **Input:** Human-defined token storage and shell authentication convention; no separate review stage or review report is required.
- **Coordinator:** **sdd-manage**, the central skill of the SDD Manager plugin. No new sdd-manager skill is introduced.
- **State and authorization:** Subsequent user instruction authorized implementation of this plan and its permission amendment. V-001–V-005 completed, verified within recorded limits, explicitly merged, and target publication verified; see the revision report.
- **Revision evidence:** [REVISION-REPORT.md](REVISION-REPORT.md).

## Accepted protocol

1. **Attempt the operation:** Assume the shell's existing authentication is usable and attempt the authorized Git push to the established destination. Do not require token discovery, an authentication probe, or a user credential request before every push. Preserve implementation's push-first rule.
2. **Escalate failure:** On a 403, pass sanitized destination, attempted operation, transport/client, and indicated cause to sdd-manage. Provider-specific classification distinguishes authentication/access failures from rate limits and policy restrictions; escalation does not imply that every 403 is repaired by replacing a token. Other explicit missing/invalid-credential failures may use the same recovery path rather than leaving a noninteractive shell blocked.
3. **Find a local token:** sdd-manage checks for `*.tkn` within the eligible repository, preferring the conventional file beside its repository-level `.gitignore` for the active backend, such as `gh.tkn`. Select a suitable provider/repository credential; do not guess among ambiguous candidates, traverse unrelated repositories, or print token contents. A token's presence does not prove identity or permission.
4. **Reuse or request:** If a suitable file exists, use its token to authenticate the shell for the active backend and retry the affected authorized operation. If none exists, ensure `*.tkn` is in the repository-level `.gitignore` before requesting and saving a token. Create `.gitignore` if absent, preserving existing rules; if no suitable ignored file can be safely written, report the concrete blocker.
5. **Acquire repository-scoped access:** Prefer a fine-grained token when supported. For GitHub, request a fine-grained token enabled solely for the target repository with the permission profile below. Token permissions do not authorize operations outside the requested workflow. Other backends define equivalent access for their supported operations.
6. **Save and authenticate:** Save the provided token as `gh.tkn` for GitHub, or an equivalent unambiguous backend filename, next to the repository-level `.gitignore`. Verify the file is ignored and untracked before writing, and restrict file access where the platform supports it. Restore the active shell/client authentication through an available credential helper, secure process input, or equivalent supported mechanism. Do not embed tokens in command arguments, remote URLs, handoffs, reports, or output.
7. **Resume and report:** Retry with bounded attempts, then confirm actual operation success and remote containment for pushes. Keep local commits and pending publication on failure; report permission/policy/transport restrictions without exposing credentials or changing destination. Reauthentication does not authorize extra operations, force-pushes, or bypassing protections.

### GitHub fine-grained token permissions

Apply this profile when requesting or assessing the conventional target-repository GitHub token:

| Repository permission | Access |
| --- | --- |
| Commit statuses | Read and write |
| Contents | Read and write |
| Issues | Read and write |
| Pull requests | Read and write |
| Metadata | Read access, added automatically by GitHub |

Enable the token solely for the target repository. The profile supports the intended SDD integration; it does not introduce PR operations into the current backend or authorize unrequested hosted mutations.

The default credential file is the sole intentional project-local secret exception. Before reusing an existing token file, also verify effective ignore coverage and untracked status; repair the ignore rule when needed. An already tracked token is a blocker requiring explicit remediation, not permission to silently rewrite history or expose its contents. Existing unrelated token files and user changes remain untouched.

Git shell authentication and an API client's credentials are separate capabilities. Restoring Git authentication must not be reported as API authentication. A selected backend may consume the same suitable token through its supported protected channel for the separately requested operation. Direct sdd-forge callers remain supported; coordinate local storage consistently when persistence is requested.

## Baseline conflicts and revision targets

These are located policy conflicts with the accepted prompt, not runtime defect claims.

| ID | Location / current rule | Required resolution |
| --- | --- | --- |
| C-001 | sdd-conventions lacks a shared token convention. | Add discoverable provider-neutral naming, ignore, handling, and reuse invariants; retain stage-specific procedure ownership elsewhere. |
| C-002 | sdd-manage credentials.md requires an approved store outside the project and says never invent a project-local token file. | Replace with assume-existing-authentication, local-token lookup, ignored persistence, shell recovery, and bounded retry protocol. |
| C-003 | sdd-forge entry and github.md prohibit any token in project files; coordinator examples repeat that prohibition. | Permit only the convention's ignored token files; preserve no-secret handling elsewhere and distinct Git/API access checks. |
| C-004 | Git push workflows lack a direct coordinator credential-recovery handoff; credential protocol is scoped to hosting through sdd-forge. | Wire failed pushes from implement, steer, and coordinated persistence/integration to sdd-manage without making sdd-forge own Git pushes. |
| C-005 | User-facing documentation does not describe shell-auth-first behavior and ignored local credential files. | Align README, capability map, entry descriptions/routing, and realistic coordinator examples. |

## Ownership and authoritative updates

| Owner / resource | Responsibility |
| --- | --- |
| sdd-conventions/references/hosting-tokens.md, new; Available conventions | Shared invariants: `*.tkn`, backend filename, location, effective Git exclusion, restricted access, suitability, and secret-free evidence. Convention does not execute authentication or own mutations. |
| sdd-manage/references/credentials.md and entry | Execute discovery, acceptance, persistence, shell authentication recovery, protected credential supply, and retry coordination. |
| sdd-manage Git workflows, coordination, workflows, examples | Receive push authentication failures, preserve scope/state, and resume the affected workflow. |
| sdd-implement and sdd-steer affected push/completion references | Attempt pushes using existing shell authentication; delegate recovery to coordinator and retain commit/publication ownership. |
| sdd-forge entry and GitHub backend | Apply permitted credential-file exception, consume suitable tokens securely, and identify repository/endpoint access requirements. GitHub-specific permission guidance belongs in github.md, not generic conventions. |
| README, docs/dev/CAPABILITY-MAP.md, affected presentation metadata | Describe the resulting behavior and boundaries accurately without including live credentials. |

No governing consumer SPEC/PLAN set exists in this repository to update for this instruction policy. Amend the existing skill owners and navigation; retain this campaign plan/report. Keep token file contents outside all committed artifacts and examples.

## Ordered revisions

| Action | Conflicts | Changes | Dependencies | Objective acceptance |
| --- | --- | --- | --- | --- |
| V-001 | C-001 | Add token convention and explicit trigger; adjust conventions discovery/metadata only where needed. | None | Naming/location/exclusion invariants are discoverable; generic convention neither owns operations nor dictates provider permissions. |
| V-002 | C-002 | Rewrite coordinator credential protocol for assumed shell authentication, repository token selection/reuse, ignore-before-save, request/store/authenticate/retry, and sanitized reporting. | V-001 | Existing authentication needs no token ceremony; suitable local token is reused; absent/unsuitable token reaches the user with the specific operation/access need. |
| V-003 | C-003, C-004 | Align Git push recovery, direct/managed forge credential paths, GitHub permission rules, and failure classification. Remove conflicting blanket project-file prohibitions while retaining ordinary secret exclusions. | V-002 | Push failure reaches coordinator; Git/API success is reported separately; rate limits and protected destinations are not treated as credential substitution problems. |
| V-004 | C-005 | Update examples, README/capability map, entry routing, and any stale presentation description. | V-003 | Documentation demonstrates authenticated push, ignored-token recovery, first-token acquisition, unsuitable access, and provider limitations with no real token values. |
| V-005 | C-001–C-005 | Verify source composition, controlled authentication/persistence cases, packaging, and publication boundary; reconcile dispositions in revision report. | V-001–V-004 | All applicable scenarios below have actual evidence and limits; one verified explicit merge publishes the accepted boundary. |

During implementation, verify exact fine-grained permission and authentication-tool behavior against current official GitHub documentation. Use the four-permission read/write profile above as the convention's required GitHub baseline, with Metadata added automatically. Verify permission suitability for the actual endpoint; the profile does not imply workflow-file modification access, protected-branch bypass, or exemption from repository policy. Report additional access only when the requested operation actually requires it. No unsupported token-injection mechanism for a connector is prescribed.

## Verification scenarios

Use disposable repositories, local remotes, and controlled fake credentials/clients where suitable. Never use the live token in fixtures, logs, or consumer context. Simulated authorization does not establish live provider permission.

| Scenario | Expected observation |
| --- | --- |
| SC-001: Already authenticated push | Authorized push succeeds without searching for token files or prompting; outstanding commits are published before further implementation work. |
| SC-002: Access 403 with suitable gh.tkn | Sanitized escalation reaches sdd-manage; ignored untracked token is loaded, shell auth is refreshed, retry succeeds, and destination remains fixed. |
| SC-003: No token or .gitignore | Preserve/create repository-level .gitignore with `*.tkn` before requesting/saving; saved token sits beside it, remains untracked, and reauthentication precedes retry. |
| SC-004: Existing unsuitable or ambiguous files | Prefer the active backend's conventional file; surface ambiguity or wrong provider/repository access rather than choosing randomly, exposing values, or overwriting unrelated files. A rejected credential permits a suitable replacement request. |
| SC-005: Git exclusion and preservation | Exercise missing ignore entry, a negating rule, an already tracked token, and unrelated staged/unstaged work. Validate effective exclusion, preserve unrelated work, and report tracked-secret remediation as blocked. |
| SC-006: Failure classification and retry | Rate-limit 403, repository policy denial, network failure, and repeated unchanged access denial produce the appropriate bounded/deferred outcome; local commits remain available and unpublished status stays visible. |
| SC-007: Git versus API | The token request specifies target-repository-only access and read/write for Commit statuses, Contents, Issues, and Pull requests, with Metadata added automatically. Git recovery does not imply API-client authorization, a forge-owned push, or permission to execute unrequested PR operations. |
| SC-008: Secret handling and portability | Tokens are absent from command arguments, URLs, normal handoffs, tracked files, and output. Supported shell credential mechanisms and filesystem restrictions are reported accurately; an unavailable mechanism is a concrete blocker. |
| SC-009: Package composition | Changed-skill/plugin validators, contained links, headings including template-start exemption, presentation metadata/icons, and credential-pattern checks pass; no contradictory outside-project-only instruction remains in active sources. |

## Execution and persistence

1. On later execution authorization, orient the current worktree and establish current branch, target, and checkpoint. Attempt any pending authorized push using existing authentication before new implementation work. Use the scoped branch for this revision, targeting the established `feature/architecture-revision` unless repository evidence establishes another accepted target.
2. Execute actions in dependency order. Update REVISION-REPORT.md with changes, scenario/check outcomes, conflict dispositions, blockers, and actual evidence limits after each action; commit and push it with the source changes and verify remote containment before dependent work.
3. Keep `gh.tkn` ignored and untracked throughout. Commit ignore-rule changes when needed, never credentials. Fixture credentials must be synthetic and kept outside production artifacts.
4. At the verified completed boundary, refresh the target, perform one explicit non-fast-forward merge, verify the prospective merged state, commit/push the target, and record parents/publication. Preserve completed local work and pending effects if access or checks block completion.
5. Retain campaign artifacts in `docs/dev/reviews/005_79fab0e/`; update index links/state to actual results. Stop after the authorized boundary. This planning-only request stops after the plan and navigation are committed, pushed, and verified.

## Limits

The plan introduces no credential service, transaction journal, mandatory auth probe, new backend, or universal shell integration. Existing authenticated sessions remain the default. Evidence must distinguish structural checks, controlled failure fixtures, consumer interpretation, shell push success, and live API access. No source changes or fresh authentication are performed merely to publish this plan when the current session already works.
