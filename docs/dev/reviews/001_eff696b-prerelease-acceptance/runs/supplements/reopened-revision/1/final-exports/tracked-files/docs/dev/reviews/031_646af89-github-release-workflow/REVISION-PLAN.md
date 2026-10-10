# GitHub Release Workflow

## Campaign and stopping boundary

- Campaign: `031_646af89`.
- Starting source: `646af8924cd06aedcf8c7edb1937ba887e40eab6`.
- Working branch: `revision/031_646af89-github-release-workflow`.
- Directory: `docs/dev/reviews/031_646af89-github-release-workflow/`.
- Integration target: actual repository default branch, verified as `main`.
- State: execution authorized by the user’s “Execute”; source revision in progress. Product workflow dispatch, tags and releases are outside this campaign’s execution effects.
- Authority: the user authorized planning publication and subsequently commanded execution. Implement the accepted plan, verify/publish checkpoints and explicitly merge/publish the complete verified campaign into the established default branch. Do not create a product release merely to exercise the new capability.

## Requested direction

Extend the GitHub backend to support release packages and GitHub release workflows. A simple request may provide a ZIP: assess its contents, establish the intended package layout, and prepare a GitHub Actions workflow that builds and verifies that package from the repository. A complex request may require interactive development of contents, variants, build dependencies, installation layout and release behavior over several turns. Preserve accepted decisions across those turns and resume the same work rather than rebuilding its design from scratch.

Use version-free release asset filenames and GitHub's latest-release download URLs. When several packages are needed, use recognizable, conventional suffixes for their actual distinguishing dimensions, such as operating system, architecture, package type or runtime. The user additionally requires **Workflows: read/write** in the conventional fine-grained repository token profile.

Release creation is a recommended part of this campaign. Preparing a workflow and actually creating a release are distinct requested operations; do not infer an instruction to publish a product release from an instruction to prepare its packaging. Once release creation is requested within established authority, perform its necessary steps without redundant permission questions.

## Current source and ownership

At the baseline, `skills/sdd-forge/SKILL.md` and its GitHub backend route task projection and issue/milestone lifecycle operations. The backend does not define package design, release creation or workflow dispatch. Its conventional token profile lacks Workflows permission, and current README and acceptance setup repeat that profile.

The repository's `.github/workflows/release.yml` already demonstrates a tag-triggered ZIP build, manifest/tag consistency, support tests, a version-free `sdd-manager.zip`, checksum and `gh release create`. Treat this current source as an example, not a universal package specification or proof of live execution.

| Owner | Planned responsibility |
| --- | --- |
| sdd-manage | Route package/workflow preparation versus actual release requests; retain decisions and stopping boundaries; coordinate file edits, Git persistence, credentials and any required integration. |
| sdd-forge and GitHub backend | Provider operations: repository and access resolution, release lookup/create/upload/publish/readback, eligible workflow dispatch and recovery. Extend triggers and handoff fields beyond task tracking without requiring TASKS for a standalone release request. |
| Focused release/package references | Define package assessment and preparation procedure, asset naming, generated workflow requirements and release lifecycle. Split by concern when useful; load only the selected operation's guidance. |
| sdd-verify | Select meaningful package, workflow and release checks; keep local inspection, actual build, CI execution and hosted download verification distinct. |
| sdd-report | Package/release summary and notes from actual features and evidence; report artifact identities, URLs and limitations. |
| Existing token convention and current consumers | Add Workflows read/write to the conventional profile; reconcile current README, backend and acceptance guidance. Keep conditional Actions access separate. |

The backend's restriction on creating local commits, pushing branches and implicit PR operations remains owned by the existing Git workflows. Workflow authoring is coordinated repository work; release API operations do not transfer Git persistence ownership to the backend. No new global authorization policy, mandatory registry or standalone CLI is required.

## Proposed capability contract

### Package assessment and interactive preparation

- Accept an existing package, current build definition or description of intended distributable as the seed. Inspect archive member names and contents safely before extraction; do not execute scripts merely because they are inside an input ZIP.
- Establish package purpose, intended users, archive format, root layout, required files, exclusions, version source, supported variants and installation/use expectations. Ask only for consequential unresolved choices; use ordinary defaults when sufficient.
- Compare a supplied ZIP with the selected repository/source identity. A supplied ZIP is evidence of desired layout, not automatic proof that every member belongs in a distributable. Account for generated and compiled files through declared build steps; do not require every package member to be tracked source.
- Validate required files, entry points, internal relative paths, applicable license/notices, platform files and executable modes where relevant. Exclude credentials, Git internals, unrelated development evidence and accidental local outputs. Address traversal paths, duplicate/conflicting entries and unsupported archive features before extraction or acceptance.
- Keep the accepted package contract with existing project/build documentation or the active record. Prefer one build procedure usable locally and in CI; do not impose a new schema or large packaging framework on a simple source ZIP.
- Record exact source commit, version and asset hashes for a build. Deterministic builds are desirable where practical; byte-for-byte reproducibility is a claim requiring evidence, not something inferred from matching ZIP member names.

### Asset naming and download URLs

Use `<project>.zip` for a single general package. Examples for actual variants include `<project>-windows-x64.zip`, `<project>-linux-arm64.tar.gz`, `<project>-macos-arm64.zip` and `<project>-source.zip`. Prefer the project's established ecosystem terminology; these examples are guidance, not mandatory platform names or formats. Use only dimensions that distinguish actual assets; avoid redundant suffixes and collisions. Keep filename spelling, case and extension consistent across releases. Never add version numbers to the normal asset names.

The stable published URLs are:

```text
https://github.com/{OWNER}/{REPO}/releases/latest
https://github.com/{OWNER}/{REPO}/releases/latest/download/{ASSET_NAME}
```

Tags and release metadata still identify versions. Specific-release URLs remain useful for pinned consumption. GitHub's automatically generated source ZIP/tarballs are distinct from explicitly attached, verified packages; Actions artifacts used between jobs are also distinct from release assets.

Define which assets each stable release supplies. The latest pointer is repository-wide; it does not search older releases for a missing platform variant. Validate the complete expected asset set before publishing/promoting latest. A change or removal of a public filename is a consequential compatibility decision. Drafts and prereleases do not become GitHub's latest stable release; do not advertise a fictitious latest-prerelease download URL.

### Generated workflow

- Inspect and extend suitable existing release/build workflows instead of creating competing publishers. Support a tag trigger and/or manual `workflow_dispatch` according to the accepted project procedure, with build-only validation available before publication.
- Pin the exact source being released; verify tag/version agreement where the project has a version source. Never silently package a moving default branch for an explicitly selected release tag.
- Run the relevant project checks, build every required variant, inspect actual generated archives, and generate SHA-256 verification files. A single package may use `<asset>.sha256`; multiple assets may use a stable `SHA256SUMS` file. Document the selected convention.
- Keep CI permissions and protected credential handling explicit. Normal release upload needs appropriate Contents write access. Add Actions permission only for operations that require it, and Workflows permission for modifying workflow files under the updated conventional PAT profile. Repository rules and actual endpoint requirements still apply.
- For matrix builds, collect the expected outputs before the single publishing stage. Avoid duplicate release creation, name collisions and races between tag/manual triggers; define concurrency and rerun behavior for the same release identity.
- A tag pushed by `GITHUB_TOKEN` does not normally trigger a second push workflow. Choose a supported direct build/publication or dispatch path rather than relying on that chain.
- Treat user inputs as data in generated scripts and use supported action/runtime versions. Optional signing or provenance requirements follow the project context; they are not mandatory for every ZIP.

### Create a release and recover it

Support requests such as “Create release v1.2.3 from the verified commit using the configured packages.” Resolve repository, exact commit/tag, version, title/notes, package set, draft/prerelease state and latest selection from supplied inputs and existing project policy. Unresolved consequential choices require a decision; do not guess a version or move an existing tag.

Select one publication route: dispatch and monitor the established workflow, or publish already verified assets using a supported authenticated GitHub client/CLI/API. Do not dispatch a workflow and independently create the same release. Document usable commands, including `gh workflow run` for configured manual workflows and `gh release create` with `--verify-tag` for an already published tag. These are operation recipes, not a new SDD executable.

Create or reuse the uniquely matching draft, attach all required verified assets/checksums, and publish only when the complete set is ready. Respect existing immutable-release settings; do not enable them or change repository settings merely to create a release. Read back tag target, release state, expected asset names/sizes/digests and latest selection. Verify actual downloaded bytes when supported; distinguish metadata confirmation from download verification.

Before replaying an uncertain write, look up the existing tag, release and assets. Resume missing work in a matching draft; report conflicts, unexpected assets or incompatible source identity. Do not silently clobber published assets, delete releases, move tags or force-push. Published corrections follow the project's version/release policy. Retain partial outcomes and sanitized failure evidence through existing recovery owners.

Release notes should explain delivered behavior, compatibility changes and necessary installation/use guidance. Keep generation and editing proportional; do not paste internal campaign transcripts or development reports into public release notes.

## Permission amendment

The conventional fine-grained token remains scoped to the selected repository. Retain Commit statuses, Contents, Issues and Pull requests read/write and automatic Metadata read; add **Workflows read/write** as explicitly requested. Reconcile the obsolete claim that the profile does not grant workflow-file modification access and any hardcoded count of write permissions. Do not edit prior closed campaign artifacts or expand the minimal greenfield prompt with a duplicate permission table.

Document **Actions read/write** as conditional for workflow dispatch and run-management operations, and actual read requirements for monitoring private runs. Distinguish user PAT permissions from a workflow job's `GITHUB_TOKEN` permissions. Inspect provider-indicated endpoint permissions before credential recovery. This campaign updates instructions; it cannot mutate permissions on an existing PAT or establish that `gh.tkn` already has Workflows access.

## Ordered revisions

| Action | Intended outcome and affected owners | Dependency | Verification |
| --- | --- | --- | --- |
| V-001 | Finalize release/package operation boundaries, discoverability and simple/interactive request routes in manager and forge entry points. Confirm the accepted recommendations without treating them as already executed. | Accepted campaign scope. | Package preparation and actual release requests select appropriate guidance; tracking activation is not a release prerequisite; existing Git ownership remains clear. |
| V-002 | Add focused package assessment/build-workflow preparation guidance and the package/asset naming contract. | V-001. | Supplied ZIP and description-only scenarios reach a concrete package/workflow result; multi-turn decisions persist; generated package checks inspect actual contents. |
| V-003 | Add GitHub release lifecycle, workflow dispatch/monitoring, command recipes, provider permission checks and interrupted-operation reconciliation. | V-001 and V-002. | Exact source, draft/upload/publish order, latest selection and single publication ownership are observable; retries reconcile existing objects. |
| V-004 | Add Workflows read/write to the conventional token profile and reconcile all current consumers; document conditional Actions access. | Explicit user amendment; V-003 endpoint mapping. | Current permission descriptions agree; workflow modification, release upload and dispatch are distinguished; no false claim of changing existing token access. |
| V-005 | Align verify/report responsibilities, current README/examples and actual packaged skill navigation. Add focused support coverage only where executable behavior changes. | V-002 through V-004. | Users can discover preparation and release commands; local/CI/hosted evidence remains distinct; package inclusion and current links pass. |
| V-006 | Exercise representative positive, negative and interrupted cases; finish the report, publish checkpoints and explicitly integrate the complete accepted verified tip. | V-001 through V-005; authorized execution. | Scoped support suite and structural checks pass, prior closed records are untouched, complete campaign tip is merged and remotely verified. Live release evidence requires a separately established test destination or explicit release request. |

## Planned verification scenarios

| Scenario | Expected outcome |
| --- | --- |
| Simple source ZIP with clear contents | Verify members against selected source, produce a proportional build/verify workflow and stable asset name. |
| Complex binary package with several variants | Resolve material build/layout choices interactively, retain decisions, and build the agreed variants. |
| ZIP includes a credential, traversal entry or conflicting paths | Reject the affected package inputs; preserve safe independent assessment without executing archive scripts. |
| Required file missing or undocumented generated member | Explain the mismatch and establish its build origin or correction before claiming package equivalence. |
| Names contain versions or collide across variants | Use version-free conventional distinguishing suffixes; preserve meaningful established ecosystem names. |
| Expected latest-release platform asset missing | Do not claim a working stable variant URL or promote an incomplete asset set. |
| Draft or prerelease | Preserve the intended state; do not select it as latest stable or invent prerelease aliases. |
| Release tag differs from built commit/version | Stop publication and identify exact mismatch without silently moving the tag. |
| Existing suitable workflow | Extend/reuse it; avoid a duplicate publisher and distinguish tag/manual execution. |
| GITHUB_TOKEN tag push expected to chain workflows | Choose a documented supported execution route; do not claim the downstream run was triggered. |
| PAT has Contents but lacks Workflows or Actions | Separate workflow modification from dispatch permission failures and release-only access. |
| Failure after one matrix asset or draft upload | Retain matching draft and successful assets; resume only pending work after readback. |
| Timeout after release publication | Read remote state before replay; do not create another release. |
| Existing conflicting tag or published/immutable asset | Preserve it and report conflict; no implicit clobber, deletion or tag movement. |
| Authorized workflow-only or local-only preparation | Produce the permitted files/checks and stop; do not create a release. |
| Completed hosted release | Return exact tag/source, release URL, stable asset URLs, hashes and actual verification limits. |

Scenarios are planned, not executed. During implementation, choose appropriate disposable local fixtures and provider mocks where useful; source inspection alone does not prove live CI or publication. Do not create a live product release merely to validate the plugin.

## Deferred extensions and decisions

Signing, SBOMs, custom provenance, installers, package-registry publication, release channels beyond GitHub latest, automatic version bumping and changelog generation are optional future/project-specific work. Support their declared requirements without making them universal prerequisites. Automatic release creation after every phase is not proposed.

Recommended defaults in this plan are draft-first publication, checksums, retained asset names, an exact verified source and supported release creation on request. They were accepted for execution by the user’s “Execute” instruction. A target project's actual release version, platforms and packaging choices are resolved in that project's request rather than hardcoded into SDD Manager.

## Provider sources

English primary sources inspected on 2026-10-09; implementation must recheck material provider details as needed:

- [Linking to releases](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases): latest-release and attached-asset links.
- [GitHub CLI release creation](https://cli.github.com/manual/gh_release_create): tag verification, assets, notes, draft/prerelease/latest options.
- [GitHub CLI workflow dispatch](https://cli.github.com/manual/gh_workflow_run): workflow_dispatch requirement, inputs and selected workflow ref.
- [GitHub release REST endpoints](https://docs.github.com/en/rest/releases/releases): release fields, latest eligibility and endpoint permissions.
- [Immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases): draft, attach assets, publish; existing tag/asset restrictions.
- [Fine-grained token permissions](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens): operation-specific permissions.
- [GITHUB_TOKEN](https://docs.github.com/en/actions/concepts/security/github_token): workflow-trigger behavior.

## Persistence and limits

The opening checkpoint was published on the revision branch without changing `main`. Authorized execution retains source/evidence there until the complete verified explicit merge. The repository’s own release workflow and existing PAT permissions/tags/releases need no mutation to implement this instruction capability. Execution records actual evidence in `REVISION-REPORT.md`. Prior closed review/feature records remain outside routine context and validation. Identity discovery inspected names/refs only.
