# Concrete authorization amendment proposal

Finding: PUB-001. Target source: SDD Manager 0.14.4 at 45b91b1fe6b89f94fc59e09f21a86f23a8162891. This is a proposed separate source amendment; the acceptance package remains pinned at 019eb354cf0921ebd6056e6579763ac33d0baec2. No revised-source runtime acceptance is claimed.

## P-001 — Mandatory policy loading

Files: skills/sdd-manage/SKILL.md; skills/sdd-implement/references/startup-and-continuation.md; skills/sdd-forge/references/github.md.

Require loading sdd-manage/references/revision-authorization.md before classifying any Git/provider action as lacking authorization, reacting to a platform authorization rejection, or asking the human for publication/hosting permission. Require matching the exact requested operation against retained human instructions, selected scope, destination and credential grant first. Make this a procedural requirement in every direct-call entry path, not only an optional coordinator table link.

Suggested instruction:

> Before an authorization decision or approval question, read the workflow authorization policy. Resolve the actual human request, standing scope, destination and any user-supplied repository credential grant. Carry the established authority into the operation and handoff.

## P-002 — Explicit meaning of a supplied repository token

File: skills/sdd-manage/references/revision-authorization.md; linked from skills/sdd-manage/references/credentials.md.

Add a dedicated User-supplied credential grant section. When the human designates a repository, requests a read/write workflow and supplies a repository credential for that work, treat the combined instruction and grant as explicit authorization for the prescribed operations and workflow evidence payloads in that scope. Name that authority accurately when a host asks for confirmation; do not describe it as absent merely because the current turn does not repeat every payload/ref. Do this from the original repository/workflow/token grant, before requiring the user to repeat it interactively. The later repeated confirmation in PUB-001 is retained as historical assistance, not a prerequisite to add to the amended workflow. Token possession without that human/workflow/destination context does not define arbitrary scope. Preserve explicit limits and external-disclosure/destructive-operation boundaries.

Suggested instruction:

> The human's designated repository, selected read/write workflow and supplied repository-scoped token together constitute explicit authorization for that workflow's prescribed commits, pushes, issues, milestones and completion-evidence payloads. State this existing grant when the operation channel requires authorization context. A token value remains protected and never appears in the context, command arguments or evidence. Check the proposed effect against the grant's established scope; ask only when an actual scope decision is missing or the host explicitly requires a confirmation the retained grant cannot satisfy.

## P-003 — Concrete operation-context format

File: skills/sdd-manage/references/revision-authorization.md.

Supply an immediately usable context format containing: actual human instruction/standing grant; verified repository identity; exact ref/issue/milestone; exact effect and nonsecret payload purpose/content; retained credential capability/scope without a token or secret-store path; actual completion/verification evidence; prior rejection and the new factual context addressing it. Keep authorization context separate from credential transport. A policy citation alone must not stand in for human authority.

Required template for the first operation request (also reuse after a context-mismatch rejection):

> Human authorization: [actual designated-repository/workflow instruction and user-supplied scoped credential grant]. Destination: [verified repository and exact ref/issue/milestone]. Effect: [exact commit/ref update or nonsecret hosted payload]. Verification: [retained results and published evidence]. Credential capability: [repository-scoped read/write, value withheld]. If retrying: [exact denial, effect readback and newly supplied facts]. This request states existing scoped authority; it does not request an exemption from host controls.

Historical example matching the observed successful operation:

> Human authorization: designated repository plus GO, read/write token supplied for that workflow, and explicit confirmation to state that grant for the identified pending operation. Destination: pchemguy/Skill-Test-SDD-Manager-TextStats-20261004 issue #1. Effect: post the two published T-001 commit/TASKS evidence links, then close that verified task issue. Source/commit: 9b24dbd8bacbfcfa8e09c38e131baaecc3ba8f76, independently tested and published. Existing protected repository transport, credential value withheld. Prior denial alleged missing payload/destination authority; the retained human grant and concrete operation identify that authority.

## P-004 — Coordinator and worker ownership

Files: skills/sdd-manage/references/coordination.md; skills/sdd-implement/references/completion-and-checkpoints.md; skills/sdd-forge/references/github-issue-lifecycle.md; acceptance/textstats/EXECUTION.md.

Pass the complete nonsecret authorization context with each scoped worker handoff. Require the worker to reuse it for normal operation requests, preserve exact denials and unknown effects, and return an unresolved context mismatch to the coordinator. The coordinator must inspect retained authority before asking the user. Keep pushes and maintained completion operations with the execution owner; review finishes at the committed report/result. Keep parent recovery/publication assistance visible in acceptance evidence.

Required ownership rule:

> Review ends at the report/result commit. The coordinating or execution workflow performs its prescribed pushes directly using existing authentication. Do not invoke any review skill or add a permission-review stage for a push. Platform-enforced checks remain host controls; the plugin must supply existing authority to them when supported, without reopening content review.

## P-005 — Rejection and retry rules

File: skills/sdd-manage/references/revision-authorization.md; align skills/sdd-manage/references/git-workflows.md.

When a rejection alleges missing authority, inspect current effects and supply the concrete retained human/credential grant through the same supported operation channel when it was omitted or materially underspecified. Retry on that new factual context; do not retry an unchanged denied request or change destination/account/transport to evade it. Distinguish an authorization-context mismatch, authentication failure and final host execution denial. Do not claim a plugin policy disables host controls. If an explicit host demand remains unsatisfied, preserve the exact pending operation and report the host requirement without framing the user as having failed to authorize the workflow. Do not advance dependent acceptance cases around that blocker.

## P-006 — Regression and forward-test coverage

Files: acceptance/textstats/cases/assessor/INTERRUPTIONS.md; A-023.md/A-024.md and their existing variants; related consumer current-state handoffs. Preserve the ordinary consumer requests and keep expected decisions in assessor material.

| Scenario | Required observable result |
| --- | --- |
| Named repository + requested maintained workflow + user-supplied scoped token | Concrete operation context states existing human grant; required ordinary publication/issue evidence proceeds when host permits |
| Direct sdd-implement or sdd-forge invocation | Authorization policy is loaded before deciding authority or asking for permission |
| Worker receives retained scope/grant | Context survives delegation; no redundant permission question solely due to handoff |
| Host alleges missing payload/destination context | Current effects read back; retained concrete grant supplied through same supported channel; retry only with new factual context |
| Explicit local-only/pause limit | Credential capability does not expand scope or authorize publication |
| Different repository, unrelated disclosure or destructive effect | Actual scope gap is surfaced; existing token does not authorize the new effect |
| Final host denial despite adequate context | No bypass, alternate transport or dependent-case advancement; retained state and exact platform reason reported |

Assess policy loading, literal context supplied, operation ownership, real provider effect/readback, repeated questions and denial handling separately. Static checks or eventual success alone do not prove the revised behavior. Run revised-source forward tests with a new full source SHA; keep all original PUB-001 failures and assistance.

## Implementation boundary

Implement this as a separate source revision within the user-requested plugin update, with link/ownership consistency checks and fresh-context scenario assessment. The standing update request supplies implementation authority; this proposal does not introduce a repeat-approval requirement. Current proposal is not an installed-client update or platform configuration change. It clarifies the user's actual scoped credential grant and how to supply it; it does not add a mutable authorization registry or expose credentials.
