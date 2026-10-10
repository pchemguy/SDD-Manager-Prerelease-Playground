# Independent Task 2 review — initial implementation

Reviewed immutable implementation `fb5bbf13325a4fcbf546d32e03912dcdb0cd5536`, base `8afda4d`, against task-2-brief.md and task-2-review-brief.md. Later worktree fixes are outside this verdict. Read the full retained review diff, actual four CLI wrappers/shared core, support tests/utilities, input/run-state schemas, SETUP/EXECUTION/RECOVERY/helper interface contracts, implementation report, retained GREEN/behavioral RED logs and sensitivity script/logs.

## Specification verdict: Changes required

The support layer implements the intended bounded coordinator role: explicit repository inputs, no inherited destination, conservative capability claims, committed package pinning, explicit dirty mode, strict schema vocabulary, independent deterministic assessment limits and real Git/index recovery exports. Helpers do not push, authenticate, create hosted objects, invoke consumers or repair the tested package. Missing repository input precedes writes; ordinary occupied paths and run_id setup are rejected; actual remote refs rather than tracking refs determine ordinary publication. Assessment is nonempty, preserves bool/int distinction and rejects absent checkpoint bindings.

However, exact pending publication identity, occupied workspace handling and dirty-source path containment have demonstrated counterexamples. These violate the preservation and actual-evidence requirements. Standard SSH URI handling also rejects a non-secret supported transport address. Task 2 is not accepted at this commit.

## Quality verdict: Changes required

The implementation is compact and stdlib-only. The retained tests meaningfully distinguish staged/unstaged content, binary work, deletion intent and conflict stages and actually reconstruct recovery state. Generic error outputs avoid echoing supplied secrets/provider stderr; exclusive output creation retains attempts. Interface documentation appropriately separates deterministic helper checks from agent acceptance. The implementation report candidly explains RED errors, mutation sensitivity and facility limits.

The success path nevertheless has four missing boundary checks below. None is covered by the 33-test final support run. Fix these with focused behavioral RED/GREEN regressions, then obtain an independent re-review of the amended committed identity.

## Prioritized actionable findings

### T2-R1 — High: pending push reconciliation can certify the wrong destination

Location: `scripts/core.py:307–320`, particularly the current-branch publication fallback at 318, and checkpoint identity handling at 110–117.

An explicit pending destination ref is read initially, but a failed equality check falls back to `actual.publication` for the current branch. A pending push with `{branch: "main", ref: "refs/heads/missing-target", commit: HEAD}` returns `observed-published` when `main` is published even though `missing-target` does not exist. The operation's optional `identity.repository` is also ignored: a pending push to another repository returns `observed-published` against the configured repository's matching HEAD, even when top-level checkpoint repository identity correctly names the current repository.

Bounded CLI reproductions using disposable Sandbox local repositories returned:

```json
{"check":"pending-explicit-ref","exit":0,"publication":"published","reconciliation":{"effect":"observed-published","retry_safe":false},"actual_target":null,"stderr":""}
{"check":"pending-different-repository","exit":0,"effect":"observed-published","stdout":"","stderr":""}
```

Correction: bind readback to the complete recorded pending destination. An explicit ref must govern containment and cannot fall back to current-branch publication. Reconcile or reject a conflicting operation repository before claiming an effect. Missing ancestry/readback stays unknown; `retry_safe:false` alone does not make an incorrect effect safe. Add regressions for absent explicit target, different recorded repository, explicit target ancestor containment, and ordinary current-branch success.

### T2-R2 — High: dirty-source pinning follows a parent symlink outside the package

Location: `scripts/core.py:198–207`.

Dirty pinning checks only whether the final candidate file is a symlink. It then reads candidates through symlinked parent directories. An ignored parent symlink can evade enumeration as an untracked symlink while cached child names remain in `git ls-files`.

Reproduction: create a disposable source with committed `plugin.json`, force-tracked `skills/demo/SKILL.md` and `.gitignore` containing `/skills/demo`. Replace `skills/demo` with a symlink to a foreign directory containing `SKILL.md`. Run preflight with `source_mode: dirty` and that source root. `git ls-files --cached --others --exclude-standard plugin.json skills` yields only `plugin.json` and `skills/demo/SKILL.md`. Preflight returns exit 0 and the package hash for the latter equals the SHA-256 of external `EXTERNAL_SENTINEL\n` bytes.

```json
{"check":"dirty-parent-symlink","exit":0,"external_bytes_hash_in_snapshot":true,"stdout":"","stderr":""}
```

Correction: reject symlinked package ancestors and any resolved candidate outside the resolved source root before content is read. Keep the declared unsupported-symlink policy consistent with committed package mode handling. A regression must include an ignored ancestor symlink; the existing observer workfile symlink regression covers a different code path.

### T2-R3 — Medium: dangling workspace symlink bypasses occupied-path rejection

Location: `scripts/core.py:235–236`.

Preparation resolves the caller's workspace before testing existence/symlink status. A dangling symlink is an occupied requested path, but resolution turns it into an absent destination and permits clone/setup there.

Reproduction: create `dangling-workspace` as a directory symlink to absent `other-destination`, then invoke prepare with `--workspace dangling-workspace`. It succeeds and writes the resolved destination:

```json
{"check":"dangling-workspace","exit":0,"requested_symlink_still_exists":true,"resolved_target_created":true,"workspace":"/tmp/<fixture>/other-destination","stdout":"","stderr":""}
```

Correction: test lexical requested-path occupancy, including dangling symlinks, before resolving or making directories. The destination must remain absent and no output JSON/setup should be written on rejection. Add occupied regular file, directory and dangling symlink cases.

### T2-R4 — Medium: non-secret SSH URI username is classified as a credential

Location: `scripts/core.py:19`, `32–41`, `164`.

The blanket `://...@` secret pattern rejects `ssh://git@example.invalid/owner/repository.git`. `git` is the conventional SSH username and is not a password/token. This blocks configuration before discovery and also rejects the same normal URL read from an existing remote. SETUP explicitly supports retaining SSH authentication/transport rather than converting it to HTTPS.

Bounded configuration reproduction returned:

```json
{"check":"ssh-username","exit":2,"cause":"invalid_nonsecret_configuration","stderr":""}
```

Correction: classify repository URLs structurally. Permit username-only SSH transport addresses; continue rejecting passwords, token-bearing/userinfo HTTPS URLs, recognizable token strings and unsafe configuration. Add both permitted SSH URI and rejected credential-bearing URI tests without live network access.

## Evidence and checks actually executed

- Read-only repository status/HEAD and immutable diff/stat inspection. HEAD initially matched the full implementation SHA above. `git diff 8afda4d fb5bbf1 --check` executed successfully with exit 0 and no whitespace findings.
- Reviewed retained `task-2-full-green.log`: 32 tests passed before the observer parent-symlink regression. Reviewed `task-2-final-green.log`: 33 tests passed after commit. These are implementer execution evidence; the reviewer did not duplicate the routine full successful suite.
- Reviewed initial RED conclusion (28 collected; 18 failures/3 errors because helper entry points were absent), hardening RED (32; 2 failures/2 errors), path RED (33; 1 failure), final GREEN, and all three retained fault-injection sensitivity failures. They support collection, recovery and checker sensitivity but do not cover the counterexamples above.
- Executed three bounded Python reproduction cells, each using existing Sandbox support in temporary repositories and bare local remotes; inspected every result. They exercised explicit pending ref/different pending repository, dangling workspace symlink, ignored dirty-source ancestor symlink, and non-secret SSH URI rejection. All disposable state was cleaned afterward. Fixture pushes targeted only temporary local bare remotes.
- No source edit, branch switch, commit, push to a hosted destination, provider mutation, credential-store inspection, consumer run, live plugin/client operation or subagent delegation was performed by this reviewer. The only authored artifact is this requested review.

## Acceptance limits

Helper tests demonstrate support-tool behavior only. They do not demonstrate installed plugin discovery/routing, real GitHub API tracking, real hosted publication, fresh-consumer isolation, campaign interruptions or final plugin diagnosis. Those remain separate campaign checks and cannot be marked Passed from these logs. The retained report's explicit limits are appropriate; these four findings concern the harness/support implementation, not confirmed SDD Manager product defects.

## Scoped independent re-review — `5fa622e`

Reviewed fixed tip `5fa622e31075c2dca62600e6861b7977b386e13e` against original implementation `fb5bbf13325a4fcbf546d32e03912dcdb0cd5536`. This addendum preserves the original review above. Scope was T2-R1–T2-R4 and breakage introduced in their four-file fix diff; it was not a new broad campaign or implementation review. Read task-2-brief.md constraints, task-2-report.md correction addendum, task-2-fix-review.diff, actual changed helper/interface/test code and test fixtures. The positive explicit-target ancestor test is committed at `5fa622e`, after fix commit `24dc6095085d041efdaba8b4e9e18748ee0cf52b`.

### Specification verdict: Changes required

### Quality verdict: Changes required

Three findings are addressed. T2-R1's original wrong-ref and wrong-repository counterexamples are corrected, but its unavailable-ancestry requirement remains incomplete in the new target containment branch. The bounded reproduction below establishes an incorrect negative reconciliation for a valid shallow checkout. The retained 40-test run does not cover this boundary. No other new breakage was identified within the fix diff.

| Finding | Recheck | Evidence and remaining scope |
| --- | --- | --- |
| T2-R1 | **NOT ADDRESSED in full** | Explicit ref now governs readback, pending repository mismatch stays unknown, ordinary current-branch success remains covered, and the positive explicit-target test proves containment without borrowing current-branch publication. Missing endpoint objects stay unknown. However, both endpoint objects being present does not establish complete ancestry; the new fallback at `scripts/core.py:343–345` incorrectly treats incomplete shallow history as evidence of non-containment. |
| T2-R2 | **ADDRESSED** | Dirty candidates are checked for symlinked ancestors and resolved-parent containment before filesystem content reads. The retained regression recreates the ignored, force-tracked ancestor-symlink case and requires failure without output or external sentinel disclosure. Committed Git-object pinning remains intact. |
| T2-R3 | **ADDRESSED** | Preparation checks lexical requested-path existence or symlink status before resolution, then checks the resolved destination before writes. The dangling-symlink regression verifies no target/output creation and preservation of the symlink. The existing occupied-directory preservation test remains green; the same lexical guard also rejects regular files. |
| T2-R4 | **ADDRESSED** | Structural URL checks allow username-only SSH transport from both configuration and discovered remote, while preserving recognizable-token checks and rejecting URL passwords, HTTP(S) userinfo and credential queries. The regression covers the allowed SSH URL and four rejected credential-bearing forms without echoing the sentinel. |

### T2-R1 remaining boundary — Medium: shallow ancestry is reported as non-containment

The newly added reconciliation checks confirm that the recorded commit and actual remote tip exist locally, then interpret every nonzero `merge-base --is-ancestor` result as `not-observed-at-destination`. A valid shallow checkout can contain both endpoint commits while omitting the connecting ancestry. In that state Git's negative ancestry result is insufficient evidence that the pending commit was not published. The documented contract requires unavailable containment ancestry to remain `unknown`.

Bounded reproduction used only a disposable repository and bare local remote: create candidate A, then descendants B and C; publish C to the explicit `other-target` ref; clone that ref at depth 1; fetch A separately at depth 1. Both A and C are locally available, but the checkout cannot traverse A→B→C. Actual readback observes C at the recorded ref. The complete source proves A is an ancestor of C. Calling the actual observation/reconciliation functions with recovery export disabled returns:

```json
{"check":"explicit-target-shallow-ancestry","effect":"not-observed-at-destination","full_history_is_ancestor":0,"local_candidate_object":0,"local_remote_tip_object":0,"remote_observation":"observed","retry_safe":false,"shallow":"true","shallow_is_ancestor":1}
```

Correction: retain equality and proven positive containment; report `unknown` when a negative ancestry check is not backed by complete available history, and on ancestry command errors. Add a focused regression with both endpoints present in a shallow checkout. This concerns the newly added pending-target reconciliation, not a fresh review of unchanged current-branch publication logic. `retry_safe:false` remains correct but does not repair the inaccurate effect classification.

### Evidence and scope limits

- Confirmed HEAD/full commit identity and read the actual immutable four-file diff. `git diff fb5bbf1 5fa622e --check` passed with exit 0.
- Reviewed retained `task-2-review-full-green.log`: 40 tests collected and passed, zero failures/errors. Checked its listed regressions against the actual modified test code; did not repeat the routine full suite.
- Executed one bounded Python reproduction using the existing Sandbox fixture and actual helper functions. Fixture commits/pushes/fetches involved temporary local repositories only, all cleaned afterward. Endpoint availability, shallow status, full-history positive ancestry, shallow negative ancestry and reconciliation effect were independently inspected.
- No implementation edits, branch changes, commits, hosted pushes/provider writes, credentials inspection, consumer runs or subagent delegation occurred. Only this requested review addendum was authored. All original campaign acceptance limits remain in force.

## Scoped shallow-ancestry recheck — `3b4049e`

Reviewed `3b4049e3371bb32e3714235e01445ad80c7788df` against preceding tip `5fa622e31075c2dca62600e6861b7977b386e13e`. Scope was the remaining T2-R1 shallow-ancestry boundary and new breakage in the two-file correction diff. Read task-2-shallow-review.diff, actual shared ancestry helper and both callers, the new regression, the report addendum and retained RED/GREEN evidence. Earlier review text and findings remain preserved above.

### Specification verdict: Accepted for Task 2 support scope

### Quality verdict: Accepted for Task 2 support scope

**T2-R1 is now ADDRESSED.** The shared tri-state ancestry helper preserves exact equality and successful positive containment. It accepts a negative only after Git returns a non-ancestor result, the repository reports non-shallow status, and traversal of both commit histories succeeds. Missing endpoints, shallow negatives, traversal/ancestry command errors and helper Git exceptions remain unknown. Both pending-target reconciliation and normal publication consume that result conservatively. Ref/repository binding and `retry_safe:false` remain intact. No new breakage was identified in this correction diff. T2-R2–T2-R4 retain their preceding ADDRESSED verdicts; all four review findings are addressed at this tip.

The new depth-2 regression is meaningful: it proves full-source ancestry, confirms both endpoint objects exist in a shallow checkout, exposes the locally unprovable relationship, and checks unknown publication/containment/pending effect through the actual observation function. It compares refs, status, shallow metadata and object inventory before/after observation, and also checks shallow equality and a visible positive ancestry path. It explicitly disables recovery export; it does not claim shallow bundle portability or a CLI/export result.

Independently reran the original bounded depth-1 reproduction against the corrected helper, without the routine full suite. The same published ancestor now remains unknown; complete-history positive/negative checks and a missing endpoint also retain their intended tri-state results:

```json
{"check":"original-depth1-reproduction-after-fix","complete_negative":false,"complete_positive":true,"effect":"unknown","full_history_is_ancestor":0,"local_candidate_object":0,"local_remote_tip_object":0,"missing_endpoint":null,"retry_safe":false,"shallow":"true","shallow_is_ancestor":1}
```

Reviewed retained `task-2-shallow-red.log`: one test with three expected assertion subtest failures and zero errors before the correction. Reviewed `task-2-shallow-green.log`: 17 recovery tests passed. Reviewed `task-2-shallow-full-green.log`: 41 tests collected and passed, zero failures/errors. These are retained implementer execution results; the independent reviewer did not repeat the routine successful suites. Confirmed actual HEAD and ran `git diff 5fa622e 3b4049e --check` successfully.

The independent reproduction used disposable local repositories only and was cleaned afterward. No source implementation edits, branch changes, commits, hosted/provider writes, credential inspection, consumer runs or subagent delegation occurred. Only this review addendum was authored. Acceptance is limited to the Task 2 support implementation: helper results do not certify installed-plugin behavior, real hosted/API execution, fresh-consumer isolation, interruption campaigns or final SDD Manager diagnosis.
