# Proposed TextStats acceptance amendments

## Purpose and status

Batch 1 repairs the acceptance harness prerequisites, interruption controls and grading that left seven cases blocked. It prioritizes important behavior that can reasonably be tested and separates complex facility-dependent scenarios into optional, non-blocking coverage. These are proposed changes to the plugin repository's `acceptance/textstats/` bundle, not TextStats counting-code changes.

This document is requested follow-up to the [final diagnostic report](DIAGNOSTIC-REPORT.md). The assessed source remains SDD Manager 0.14.3 at `019eb354cf0921ebd6056e6579763ac33d0baec2`. The completed campaign's published stop checkpoint is `93a3428e23f0a3ba93ff45693a3793db3a102c8e`; its result remains **20 Passed / seven Blocked**. Creating this proposal does not implement the amendments, rerun cases, or retroactively regrade independent assessments.

## Batch 1 policy: required behavior and optional extended scenarios

Grade independently executable checks independently. Do not let an unavailable advanced scenario erase a verified core result, become a product failure, or block unrelated required work. Equally, do not turn missing evidence into a pass.

Each case or variant must declare its purpose, whether it is required or optional, evidence class, prerequisites, and execution requirements before dispatch. Ordinary completion, prerequisite refusal, controlled fault handling, interrupted recovery and live provider recovery are different claims and must have distinct criteria and results.

| Classification | Result and reporting | Effect on campaign readiness |
| --- | --- | --- |
| Required core check, executed | Passed or Failed from observed behavior and independent evidence | A failure prevents required acceptance. |
| Required core check, unavailable | Blocked, with the exact prerequisite or harness defect and repair action | Required acceptance remains incomplete; no product defect inferred merely from unavailable setup. |
| Optional extended scenario, executed | Passed or Failed, with evidence class and findings | Report separately; it does not automatically block core acceptance. A reproduced defect that also violates a required contract must be escalated against that contract. |
| Optional extended scenario, unavailable or not selected | Not run, optional/non-blocking, with reason and full-execution requirements | Excluded from required acceptance counts; never reported as Passed or as a required failure. |

Show required totals and optional totals separately. State which profiles and environments were actually covered. A required-core pass does not establish full native, installed-client, live-provider or cross-machine acceptance. Optional cases must not become prerequisite gates for required cases. Do not downgrade a difficult ordinary core check merely to obtain a green result; optional status is for clearly identified advanced scope with justified facility requirements.

## Ordered amendment queue

All paths below are relative to `acceptance/textstats/` in the owning plugin repository. Stable A-014 through A-026 IDs remain; distinguish variants beneath them rather than renumbering historical cases. Proposed variant names below are design labels, not existing catalog entries.

| Action | Proposed amendment and affected owners | Objective recheck |
| --- | --- | --- |
| B1-001 | Add required/optional variant classification, evidence class and capability eligibility to `cases/catalog.json`, assessor contracts, configuration/checkpoint schemas where necessary, `cases/assessor/catalog_tools.py`, coordinator scripts and reporting. Update `OBJECTIVES.md`, `SETUP.md`, `EXECUTION.md`, `RECOVERY.md`, `DIAGNOSTICS.md` and role guidance consistently. | Validate every variant's metadata and dependency graph. Reject a required dependency on an unavailable optional variant. Demonstrate separate required and optional counts, including an unavailable optional scenario that leaves required readiness unchanged. |
| B1-002 — A-014 | Repair `cases/consumer/A-014.md`, its assessor guide/contract and catalog binding. Required cross-phase execution starts at an actual checkpoint with outside prerequisites complete; its selected scope permits required commits, pushes and integration. Keep the incomplete-prerequisite refusal as a separate required check. | Observe first-phase exits/review, explicit merge and publication before the next phase starts; stop at the selected range. Separately verify refusal without unauthorized prerequisite execution or mutation. |
| B1-003 — A-017 | Supply a deterministic, contract-valid acceptance failure at the starting checkpoint and an observed failure boundary. Update case setup, consumer request, assessor assets and interruption controls. Do not use an invalid assertion or arbitrary nonzero exit as the required product failure. | Independently establish why the starting implementation fails the valid contract. Observe the consumer encounter that failure, interrupt at the selected boundary, preserve state, and give a fresh consumer the continuation. Verify scoped repair, nonempty passing checks and publication; retain the original failure. |
| B1-004 — A-019 | Replace the incomplete A-005 milestone binding with a verified complete phase, such as the actual A-006 completion boundary or a separately established eligible boundary. Prepare controlled divergence in an isolated target while preserving the real source and target identities. Update the catalog dependency, renderer, requests and assessor expectations together. | Reject an incomplete-phase fixture in preflight. At the eligible boundary observe a real conflict or merged-state check failure, preserve pending state, then independently verify fresh recovery, two-parent merge, merged checks and exact target publication. |
| B1-005 — A-021 | Replace polling-dependent interception with a bounded control between actual selected transfer operations. The control belongs to the test fixture; it must not add mandatory journals or test hooks to ordinary product workflows. Update case setup, `cases/consumer/INTERRUPTIONS.md`, handoff controls and assessor evidence. | Capture a genuine state with at least one selected transfer completed and another pending, including actual owner/link/index evidence. Interrupt and resume in a fresh context; verify no lost or duplicate task ownership, correct links, preserved unrelated edits and coherent publication. |
| B1-006 — A-023 | Split ordinary uncertain-effect reconciliation from extended live-provider response-loss scenarios. Required core checks may use a disclosed controlled facility with independently observable effects; label their evidence accordingly. Actual GitHub write-applied/response-lost variants are optional and non-blocking when no suitable hosted setup is available. Update requests, contracts, catalog and publication criteria. | Core tests demonstrate readback before retry, reuse of an already-applied effect, bounded retry of an unapplied effect and no duplication. A separate optional live run must establish actual provider mutation, discarded response and independent provider readback; controlled tests never count as live acceptance. |
| B1-007 — A-024 | Split reasonably testable access classification and bounded handling from complex native credential/session failure and recovery. Required checks assess sanitized denial, rate-limit and unavailable-access handling. Native protected handoff, real expiry/revocation and fresh native recovery are optional/non-blocking extensions. See the detailed contract below. | Required checks pass independently of optional facility availability, with preserved state and no secret exposure. Missing native facilities produce an explicit optional Not run result, not an overall required Blocked result. |
| B1-008 — A-026 | Separate empty collection, genuine pre-existing baseline failure and verification-only preservation. Supply an isolated fixture with an independently reproduced assertion failure and no consumer repair authorization. Restrict local-only assessor helpers to local checks; remove implicit hosted reads from that mode. | Reject zero-test acceptance; show an actual nonempty failing baseline; verify accurate attribution and unchanged source/task/index state. Local assessment completes without hidden network reads. Passing ordinary baseline tests do not substitute for the failure variant. |

## A-024: required checks and optional native recovery

Retain A-024 as the parent identity, with independently graded core and extended variants. The current case couples classification and complex recovery; that coupling should be removed. If implementation review concludes its existing contract is entirely native recovery, classify that entire contract as optional/non-blocking and add a separately defined core classification variant. Do not mislabel the native contract as a core pass.

### Required core: access classification and bounded handling

Use separate actual consumer-visible controlled operations for permission denial, rate limiting and unavailable authenticated access. The fixture may inject sanitized faults through a documented adapter. The report must say that these are controlled faults, not actual provider denial or credential expiry.

Check that the consumer:

- Distinguishes access denial, rate limiting, transport failure and unavailable authentication from a product/test failure.
- Preserves valid work and identifies the exact pending operation and destination.
- Applies bounded retry/backoff or stops appropriately; a rate limit does not trigger credential replacement.
- Keeps Git publication recovery and API access recovery distinct.
- Uses an available supported protected mechanism when recovery is selected, without putting secret values into prompts, arguments, logs or reports.
- Resumes the same bounded operation after the controlled facility is restored, with independent readback where applicable and no duplicate effect.

Credential replacement is not necessary to prove classification, state preservation or bounded handling. Restoration of a controlled wrapper proves only that bounded continuation. Grade these checks from their own evidence rather than withholding their result because native protected handoff cannot be exercised.

### Optional extension: native credential/session recovery

Report this as **optional, non-blocking native authentication recovery**. Full execution requires a supported client/protected input facility, an isolated recoverable access configuration, a controlled genuine unavailable/expired/invalid credential condition, and independent same-destination observations before and after recovery. Where the contract specifically requires ignored/untracked credential reuse, demonstrate that eligibility through supported nonsecret evidence without reading or exporting the credential value.

Preserve the actual failure and use a separate fresh continuation when that is the scenario. Never invalidate ordinary campaign credentials simply to force a test. Do not substitute scripted error responses, wrapper restoration or token possession for demonstrated native recovery.

If facilities are missing, report: the precise unexecuted recovery behavior; the missing client/control; what was tested by the core variants; and what setup would enable the extension. Its status is optional Not run, with no reduction of required-core readiness. If it executes and fails, retain the failure and investigate its cause; optional classification does not conceal a confirmed contract defect.

## Other complex scenarios and capability reporting

A-023's optional live scenarios require a legitimately identified isolated hosted project/campaign, narrowly scoped operations and a mechanism that discards a response after the real write applies. A separate repository is one possible arrangement, not an automatic requirement; a separate campaign in the same repository is eligible only if its identity/object isolation is established. Do not reopen completed positive-campaign objects or create duplicate managed task identities as a substitute.

Keep safely reproducible local interruption/recovery behavior in required coverage. If a particular extension requires unavailable platform-native interruption, installed-client routing, hard filesystem isolation or another specialized facility, name that extension and its requirements explicitly and classify it separately before the run. A general environment limitation must not silently downgrade all checks in a case.

Preflight must establish the exact starting commit, actual dependency completion, legitimate integration boundary, permitted destination, required access and available trigger controls. Missing setup should produce a precise preparation diagnosis before consumer dispatch. It must not be presented as a product failure. Record successful eligibility separately from runtime acceptance.

Deterministic interruption controls must observe the selected action before holding it, retain the unfinished state, and support a fresh continuation. They must have sensitivity checks that reject a missing trigger or already-completed operation. Do not manufacture product completion records or alter the frozen plugin to inject a trigger.

## Implementation, regression and rerun boundary

Implement the proposals in a separate owning-source revision. Preserve this campaign's original inputs, assessments, frozen package and publication history. Record a new full source SHA and harness identity for any rerun; do not retrospectively mark the seven historical cases Passed or replace their grades with optional status.

First implement the classification/reporting and capability preflight, then repair the individual cases and deterministic controls. Run catalog/schema/renderer validation and meaningful sensitivity tests for unavailable optional scenarios, incorrect prerequisites, already-completed triggers, duplicate-effect recovery and local-only access. Changes to shared coordinator or grading behavior require targeted regressions of previously passing consumers or retained fixtures as appropriate; support tests alone do not demonstrate live plugin acceptance.

Rerun the affected required variants with fresh consumers and independent assessors. Execute optional extensions only when their declared facilities are available and selected. Publish required totals, optional executed totals, optional Not run totals, actual evidence classes and outstanding findings separately. Required acceptance may complete with optional coverage unavailable; the report must still state the narrower demonstrated scope.

This batch proposes no TextStats production-code changes. Existing [authorization amendments](runs/A-004/1/AUTHORIZATION-AMENDMENT-PROPOSAL.md) and their [supplement](AUTHORIZATION-AMENDMENT-SUPPLEMENT.md) remain separate proposals; they are not withdrawn or implemented by this document.

## Batch 2: final integration, host auto review and licensing

This batch records the user's additional requirements. The final integration requirement applies prospectively. **The current live acceptance branch must remain unmerged until the user specifically requests its integration.** Adding these proposals does not grant that current merge instruction.

### B2-001 — Finish live acceptance by integrating its evidence branch

Update `acceptance/textstats/SETUP.md`, `EXECUTION.md`, `RECOVERY.md`, `DIAGNOSTICS.md`, A-027's guide/contract, coordinator checkpoint/reporting and related helper tests. A full live acceptance workflow must end by integrating its completed evidence branch into the established main integration branch, after publishing the final report and verifying its independent artifacts. The branch's role as an evidence branch does not exempt it from final integration.

Inspect the complete branch difference, refresh and pin the actual main and evidence tips, preserve unrelated work, and create an explicit two-parent merge. Verify the prospective and committed result: retain current product source/tests/governing documents, frozen resource identities and immutable assessment payloads; resolve evidence links; reconcile campaign status and branch containment. Publish main and verify the exact destination. Retain the evidence branch. Never substitute a fast-forward, squash, force-push or an implicit pull-request operation.

Avoid stale product rollback when the evidence branch descends from an older preparation checkpoint: assess the actual merged result, not merely its branch name or a clean worktree. Report product completion separately from evidence integration so the product's assessed merge remains identifiable even when main gains an evidence-only merge.

Record verified parent identities, merged checks and publication. Do not declare the full workflow complete while final integration/publication remains pending. A scoped pause or actual integration blocker preserves the pending operation and branch; optional unavailable test scenarios do not independently prohibit evidence integration. Use ordinary execution ownership for merge and push, with the existing scoped human authority. Recovery must recognize an already-created merge or lost push response and finish the retained operation rather than merge again.

Objective recheck: a complete campaign produces a published two-parent main merge containing final evidence without losing product changes. A current explicit unmerged boundary is respected. Recovery from a committed-but-unpublished final merge publishes the same commit once. Historical assessed product and evidence SHAs remain traceable.

### B2-002 — Separate host auto review from plugin workflow definitions

Revise `skills/sdd-manage/references/revision-authorization.md` and related Git, review, coordination and credential guidance; align the root README and any amendment records that would otherwise contradict the resulting policy. This proposal supersedes the explanation in P-004 and its extensions wherever that explanation separates pushes from workflows to avoid host review. Original reports remain historical evidence rather than being silently rewritten.

Required wording and behavior:

- Commits, prescribed pushes, eligible merges and target publication are parts of the complete workflows that require them. A reviewer may finish its assessment at the result/report commit; execution ownership of the subsequent push does not remove that push from the encompassing workflow.
- ChatGPT's automatic approval reviewer is a separate host agent/control for operations crossing that host's sandbox or permission boundaries. It is not an SDD Manager skill or a plugin-defined development/code review. Comparable controls may exist in other clients.
- The plugin does not select the host reviewer's triggering rules. Changing a workflow label or describing a push as outside the workflow does not resolve or disable host review. Remove instructions whose stated purpose is to evade a host review trigger through workflow reclassification.
- Preserve the real user authorization, observed repository/destination, exact effect and relevant checks across handoffs. Use supported host channels when execution is rejected; retain exact reasons and pending work. A host rejection does not itself establish absent human workflow authorization, authentication failure or a plugin defect.
- Retain the scoped authorization policy while its interaction with client settings is uncertain. Do not claim that credentials authorize arbitrary effects, that a README changes platform policy, or that a host rejection can be bypassed.

Objective recheck: instructions consistently describe pushes as workflow steps while distinguishing development review from host auto review. Direct and delegated execution use the same actual scope and destination context. A host denial preserves completed work and does not trigger workflow reclassification, duplicate operations or unrelated credential replacement.

### B2-003 — Add a dedicated README section for ChatGPT web permissions

Add the following appropriately revised section to the plugin root README. Treat UI labels as client-dependent. This section is proposed documentation, not a claim that settings were changed or that Git push behavior was verified under them.

#### Proposed README text: ChatGPT web permissions and automatic review

SDD Manager's workflows include their prescribed commits, pushes and eligible integration. ChatGPT may independently review tool requests at host permission or sandbox boundaries through an automatic approval reviewer. That host review is separate from the plugin's development review and workflow definitions; other agent clients may apply comparable controls.

In the ChatGPT web interface observed by the user on 2026-10-06, the controls appear under **Profile → Settings → Integrations → Cloud computer**, with **ChatGPT Work website approvals** and **Add website**. Other versions may present them under **Settings → Cloud browser**. Check the labels available in your client.

The more narrowly scoped configuration described by the user is **Auto approve** as the default and a GitHub website exception set to **Always allow** through **Add website**. **Always allow** as the default applies to all websites rather than only GitHub. OpenAI documents that Auto approve lets ChatGPT review website access requests, whereas Always allow permits website access without that review; per-site permissions override the default.

Website access settings are distinct from approval of consequential actions. Their effect on automatic review of shell Git pushes, protected tool calls or other sandbox crossings has not been established here. Do not promise that a website exception disables every host approval review. The plugin retains its scoped workflow-authorization guidance; whether a particular client setting changes the need to supply that context remains uncertain.

Reference: [OpenAI — Using cloud browser in ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt). The documented permission choices support the descriptions above; the user's longer settings path and its connection to shell auto review remain observations requiring verification in the relevant client.

Objective recheck: the README distinguishes observed labels from documented behavior, scoped website exceptions from a global setting, and website access from action/tool approval. Verify the actual target UI and a bounded authorized operation before claiming a setting remedies the recorded shell-push rejection. Do not change the user's settings as part of documentation authoring.

### B2-004 — Root MIT license in the plugin repository

Add the standard MIT text at repository-root `LICENSE`, with `Copyright (c) 2026 PChemGuy`, matching the plugin manifest's author identity. Link it from the README. Preserve the existing `skills/sdd-tdd/LICENSE` and upstream attribution; a root license does not replace third-party notices. The user directly requested this repository metadata change separately from future harness and policy implementation.

Objective recheck: the root text matches the standard MIT terms, the README link resolves, existing third-party license bytes are unchanged, and the scoped commit is published to the established plugin development branch. No current acceptance-branch merge is included in this action.

### B2-005 — Brief README testing overview and maintained test repository list

Add a concise **Testing with TextStats** section to the plugin root `README.md`. Explain that TextStats exercises SDD Manager through a small sample product, fresh consumers, independent assessors, Git/GitHub workflows and interruption/recovery scenarios. Distinguish live acceptance from harness self-tests; do not imply that every listed campaign passed all cases or that source loading proves installed-client behavior.

Link to [the TextStats README](https://github.com/pchemguy/Skill-SDD-Manager/blob/feature/architecture-revision/acceptance/textstats/README.md) for invocation prompts, prerequisites, profiles, execution and reporting details. In the actual plugin README use the relative link `acceptance/textstats/README.md`, so navigation follows the checked-out branch/version. Keep the overview short rather than duplicating the detailed instructions or embedding a second acceptance prompt.

Include a running list of prior dedicated test repositories, initially:

- [Skill-Test-SDD-Manager-TextStats-20261003](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261003)
- [Skill-Test-SDD-Manager-TextStats-20261004](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004)

Retain earlier entries when adding later campaigns. Repository links provide discoverability, not assumed results; link a campaign's final report when a verified location is known. Do not infer a tested version, run date, full pass or integration status solely from its repository name. Avoid making this historical list the default destination for a fresh run.

Suggested concise README wording:

> SDD Manager is tested through TextStats, a small sample project used to exercise development, Git/GitHub and recovery workflows with fresh consumers and independent assessors. Live campaign reports record the tested source, actual coverage and remaining limitations; harness self-tests check the test infrastructure. See [TextStats acceptance testing](../../../../acceptance/textstats/README.md) for setup, profiles and running instructions.

Follow that paragraph with the maintained repository list above. Objective recheck: the overview and local README link are present, both initial repository URLs are retained, adding a later repository preserves earlier entries, and no unsupported acceptance verdict or automatic destination selection is introduced.
