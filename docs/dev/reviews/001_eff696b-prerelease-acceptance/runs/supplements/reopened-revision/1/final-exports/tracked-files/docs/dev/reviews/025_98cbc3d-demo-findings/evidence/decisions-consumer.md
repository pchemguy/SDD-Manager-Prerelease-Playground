# Fresh consumer decisions

Read-only source: `/workspace/scratch/6420baa7afea`, observed HEAD `719540de681cb3cfcf3e8a06dbeb7f4940cc755a`. Each D-state is independent. These are proposed coordinator decisions, not executed repository/provider operations. No credentials, actual hosted writes, or publication were attempted. Root `AGENTS.md` and the relevant owner instructions/references were read; excluded campaign findings, baseline responses and assessments were not read. References below are repository-relative paths and source line numbers at this pin.

## D1 — New preparation, supplied token, no tracking choice

Next action/question: recommend enabling tracking, then ask “Confirm tracking for the established repository's eligible phase: its phase label, all accepted milestones and task issues, their associations, and verification-based closing/reopening?” Use accepted counts if known; do not invent counts before planning. Record **recommended enabled; confirmation pending**. Preparation and independently authorized local/Git work can proceed; no hosted projection before confirmation and readiness/eligibility checks.

Authority is the preparation request; token supply establishes available credential input, not optional-capability consent or another destination. Coordinator sdd-manage owns this choice and protected credential persistence/supply; after confirmation, sdd-forge owns GitHub objects. Any real credential persistence would follow root ignore/untracked/protection rules and keep values out of evidence. Record recommendation, actual choice, scope, activation and observed provider state separately in existing evidence. Provider objects/access remain unknown here.

Sources: `skills/sdd-manage/references/tracking-decision.md:3,7,11,13,15`; `skills/sdd-manage/references/credentials.md:13-16`; `skills/sdd-manage/references/phase-activation.md:5-8,14-18`; `skills/sdd-forge/SKILL.md:10-14`.

## D2 — Same preparation, explicit prior decline

Next action: carry forward **declined** for the matching repository/scope; continue authorized preparation and normal Git work. Do not offer tracking again or create objects because a token was later supplied. No further tracking question unless the user changes scope/choice. Record the explicit decline separately from the credential/access state and performed hosting state.

sdd-manage retains the decision; no sdd-forge hosted-write route is activated. Token handling, if authorized, remains protected and does not erase the decline. Source: `skills/sdd-manage/references/tracking-decision.md:9,13,15`; `skills/sdd-manage/SKILL.md:29` (respect ownership and decisions).

## D3 — Express confirmation after four of ten local tasks, two open issues

Next action: carry explicit confirmation forward without asking again. Recover exact repository/current phase and accepted hierarchy/readiness, discover all matching open/closed objects, then route eligible-phase reconciliation to sdd-forge. The old agent PLAN “inactive” records earlier performed state; it cannot override current user confirmation. Two open issues prove only that two issues were observed, not the full projection or which tasks are complete.

Read all ten owning tasks and their phase/milestone relationships; validate exact managed IDs/ownership for the two issues, reuse unique matches, reconcile missing eligible-phase labels/milestones/issues/associations and read back results. Do not assume exactly eight issues are missing before discovery. Attach retained evidence for the four locally completed tasks; close only tasks whose acceptance/check, commit, publication and required evidence support closure, and close milestones only after all constituent issues including review tasks and exits qualify. Local completion alone is not hosted closure evidence. Leave the remaining tasks open, preserving unrelated fields/material. Do not repeat completed product tasks or create future-phase objects. Incomplete projection/closure is recorded as pending; phase advancement remains subject to actual gates, while independently eligible work in an already activated phase follows dependencies and requested range.

Authority/choice: expressly confirmed maintenance of current phase objects. Observed state: four of ten locally completed, two discovered open issues, historic inactive PLAN. sdd-manage owns coordination/actual phase choice; sdd-forge owns provider reads/writes; sdd-implement owns implementation/publication/task-completion evidence. Sources: `skills/sdd-manage/references/tracking-decision.md:8,13,15,19`; `skills/sdd-manage/references/phase-activation.md:5-11,14-18`; `skills/sdd-conventions/references/backend-object-lifecycle.md:3,17-25,47-51`; `skills/sdd-forge/references/github.md:13,17,41-43`.

## D4 — No supplied token, shell authentication unknown

Next action/question: offer supported tracking when relevant and ask for the concrete scope choice; do not probe authentication or demand a token just to make the offer. Retain **no decision yet/confirmation pending**, not declined or active. If tracking is confirmed, use available authenticated API client for its authorized operations; Git shell success would not prove API access.

For an otherwise authorized push, its owner attempts the normal push to the established destination using existing shell authentication, without a pre-push credential ceremony. Only an observed credential/access failure triggers sdd-manage's bounded, repository-local credential recovery, after classifying policy/rate-limit/transport causes. Unknown shell auth is not observed credential failure. Sources: `skills/sdd-manage/references/tracking-decision.md:10-13`; `skills/sdd-manage/references/credentials.md:5-9,13-16,21-27,31-35`; `skills/sdd-forge/SKILL.md:13-15`.

## D5 — Authorized verified report push, absent context, supported reconsideration

Next action: proactively prepare and submit the contextualized operation through the supported reconsideration/request channel; no repeated user grant. Supply normal verified push, established repository/ref, exact commit and owned report paths/content, actual existing user authorization/limits, observed checks, exact rejection reason and reliable remote readback where outcome may be unknown. The changed request remedies absent destination/payload context rather than repeating the same denial. Attempt the contextualized operation when that supported channel permits it; verify containment upon actual success.

Authority remains the explicit user push grant; verified local report and a host rejection are distinct from successful publication. Coordinator owns report publication; host control owns whether execution is permitted. Do not manufacture a reviewer-messaging API or promise success, replace credentials, change transport/account/tool to evade review, or advance through the unpublished dependency. Sources: `skills/sdd-manage/references/revision-authorization.md:5-7,23-27,29-38,43-58`; `skills/sdd-manage/references/coordination.md:16-17,33-35`.

## D6 — Genuine host prohibition, no reconsideration channel

Next action: stop the denied push, preserve local commits and report **publication pending: platform policy prohibition; no supported reconsideration channel** with the exact known reason. User authority is still present, but it cannot override the host prohibition. Do not ask the user to restate the same grant or attribute this to a plugin approval requirement; do not retry unchanged, change tools/accounts/transports or replace a token. No dependent advancement. No additional human confirmation is inferred unless the host explicitly requires it.

Route the blocker through the coordinator's result reporting; publication owner retains the pending operation for a later permitted continuation. Sources: `skills/sdd-manage/references/revision-authorization.md:29-38,58`; `skills/sdd-manage/references/coordination.md:45-47`.

## D7 — Grant revoked before push, token remains usable

Next action: do not push. Record **authority revoked; local work retained; publication not performed**. Token usability is access capability and cannot revive the revoked scoped grant. Respect the revocation's stopping boundary; a later push requires a renewed grant covering that effect. Preserve existing work and secrets; do not retry through another client/account. No presumption that token deletion was requested.

Coordinator reports the blocker; push owner remains paused. Sources: `skills/sdd-manage/references/revision-authorization.md:3,19,40,45,58`; `skills/sdd-manage/references/credentials.md:27`; `skills/sdd-conventions/references/hosting-tokens.md:19`.

## D8 — Why tracking omitted; agent PLAN inactive, no user choice

Next response: “The instructions call for establishing an optional tracking decision. The PLAN records inactive performed state; it does not record your decline. On the available evidence, the tracking-choice handoff was omitted or remains unestablished. I cannot claim you declined, that a provider denied access, or that objects exist.” Distinguish applicable instruction, actual missing user choice and observed agent-authored state. Inspect available request/session evidence before claiming the exact cause; acknowledge the limit. Correct any earlier assertion that inactive PLAN proves decline.

Next action/question: establish the missing scope choice using the applicable offer/recommendation rule (recommend enable if a repository workflow token was supplied; otherwise offer when relevant). Keep confirmation pending and continue independent authorized local work. This explanation does not authorize source repairs, projection or notes persistence. sdd-manage owns diagnosis/decision; sdd-forge is deferred until confirmed. Sources: `skills/sdd-manage/references/tracking-decision.md:3,7,10-15`; `skills/sdd-manage/references/review-and-revision.md:38-40`; `skills/sdd-manage/references/coordination.md:41-43`.

## D9 — Retain notes in existing backlog, no source edits

Next action: orient to the established backlog and applicable instructions/ownership, then append the authorized notes there, keeping stable IDs, context/evidence, proposed correction, owning capability, validation and disposition. Preserve original observations separately from later decisions/results. Verify the scoped artifact update and apply only the authorized persistence/publication boundary, reporting written/committed/pushed states truthfully. Do not edit reviewed source or installed skills, create a revision campaign to hold notes, mark proposals implemented/Verified, or fabricate executable task IDs.

Authority is notes persistence at the existing location, not source repair. sdd-manage coordinates the findings procedure; sdd-report presents evidence/persistence. Actual backlog contents and Git status are unknown in this fictional state, so those checks precede a write. Sources: `skills/sdd-manage/references/review-and-revision.md:7,42-46`; `skills/sdd-manage/references/coordination.md:5-9,27-35,41-43`; `skills/sdd-manage/SKILL.md:26-32`.

## D10 — Conversation-only notes, read-only analysis

Next action: continue read-only analysis and return observations in conversation. State **conversation-only; not written, committed, pushed or implemented**. Writing is outside scope, so do not create backlog/report/feature documents or change source; identify persistence as a pending decision only if it becomes needed, without blocking authorized analysis or repeatedly asking. Route concerns to relevant focused reviewers for analysis only; no repair/projection/publication route.

Authority is read-only analysis; no write consent is inferred from mature discussion. Sources: `skills/sdd-manage/references/review-and-revision.md:7,44-46`; `skills/sdd-design/SKILL.md:16`; `skills/sdd-manage/references/coordination.md:41-43`.

## D11 — New piece-controls identity after reserved legacy 007

Next action: inspect repository-wide reservations across reviews, features, phase-nested revisions and relevant refs before reservation. Given highest reserved sequence 007, allocate next sequence **008**, not a gap or a separate feature counter. Assuming `abcdef1` uniquely resolves the supplied baseline, stable ID **`008_abcdef1`**, branch **`feature/008_abcdef1-piece-controls`**, package **`docs/dev/features/008_abcdef1-piece-controls/`**, navigation **`README.md`** under that package. Record full baseline **`abcdef1234567890abcdef1234567890abcdef12`**, actual target/destination, scope and active source links. If seven characters do not uniquely resolve, extend the baseline abbreviation before establishing identity; full SHA stays recorded.

The legacy `docs/dev/reviews/007_df531c2` counts as a reservation despite having no slug. Validate the branch with `git check-ref-format --branch`; inspect local/remote collisions and worktree occupancy. For unrelated occupied branch suffix, keep `008_abcdef1` and choose/record a distinct slug, e.g. `piece-controls-2`; both branch and new package use the full matching suffix. If another reservation conflicts on sequence 008, reconcile concurrent identity/ownership before publication rather than accepting two campaigns or silently renumbering established records. Unknown remote state is not proof of availability. Preparation reserves identity, not implementation authority. sdd-manage owns allocation/Git setup; convention supplies naming rules. Sources: `skills/sdd-conventions/references/workflow-identity.md:9-21,25-28,32-38`; `skills/sdd-manage/references/branch-management.md:7-18,34-38`.

## D12 — Resume established unsuffixed package; later explicit rename

Resume next action: recover the recorded branch **`feature/008_abcdef1-piece-controls`** and actual existing package **`docs/dev/features/008_abcdef1/`**; verify full baseline/target/scope/history/pending work and reuse their association. Stable ID remains **`008_abcdef1`**. Do not allocate a new sequence, infer a suffixed directory, rename the unsuffixed package or repeat completed work merely because new defaults differ.

Separate explicit rename next action: orient/check ownership and collisions, then make a coherent scoped rename to the explicitly selected path (if aligning with current default: **`docs/dev/features/008_abcdef1-piece-controls/`**). Keep the same campaign ID/full baseline and existing branch unless the user also requested branch renaming. Update all affected incoming/outgoing navigation, archived source paths and evidence references, record the actual association, verify active owners and archive links, and honor the requested verification/commit/publication boundary. Explicit rename authority covers this scoped migration; it does not authorize feature implementation, archive-ineligible moves or deletion of unrelated packages. Do not overwrite a conflicting destination. sdd-manage owns coordinated rename/Git persistence; sdd-integrate-feature retains incorporation/archive eligibility ownership.

Sources: `skills/sdd-conventions/references/workflow-identity.md:3,19-21,28-38`; `skills/sdd-manage/references/branch-management.md:14-18,34-38`.
