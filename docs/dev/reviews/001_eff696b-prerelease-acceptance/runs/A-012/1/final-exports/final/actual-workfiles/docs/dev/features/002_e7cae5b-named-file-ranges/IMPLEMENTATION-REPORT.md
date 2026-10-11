# Named-file ranges implementation report

## Objective and reviewed source

Deliver accepted named-file ranges T-018–T-024 with text/JSON composition,
complete documentation and isolated extracted-source verification, preserving
silent whole-input API and pending stdin/final work. This final feature report is
part of T-024 at published source `4eeee9e9505b29b4a616292434561aab569dac7f`;
concrete report review and final task closing are pending. It measures the active
feature owning list, not the full main Phase 2.

## Delivered result and review

Both `--lines START:END` and `--lines=START:END` select available inclusive
one-based logical lines after complete strict file decode and once-only whole-input
BOM policy. ASCII positivity/order/repetition validation precedes access; endpoints
and leading zeros have no arbitrary conversion cap. Shared preserved CRLF/CR/LF
segments and normalized counting retain blank/final/EOF/Unicode/interior-BOM
semantics. Text/JSON compose with BOM/options/INPUT placement, and usage/input
errors retain status/streams without partial results. Public exports/signatures,
immutability, whole-input behavior, exceptions/silence and handle ownership remain.
Literal minus is still a named file; stdin acquisition remains deferred.

Full public/runnable guides and eleven-file source distribution describe the
actual product. Checker invokes the extracted real module with import provenance,
removed inherited import paths, disabled user-site and bytecode, running 315
whole-input/range cases and a silent unchanged API/signature probe. Literal
expectations and controlled range-only archive mutations guard against ignore-range
and second-normalization faults that the old 99-case checker accepted.

[Milestone 2.4](phases/2/2.4.md), [milestone 2.5](phases/2/2.5.md) and the
[feature-extent review](phases/2/PHASE-REPORT.md) record separate coherent code
review, actual check scopes, useful demonstrations, limits and findings. No
blocker/repair is unresolved. Existing architecture/decomposition/layout seams
were reused without creating another source owner or API.

## Task persistence and accepted decisions

| Task | Published result / concrete decision |
| --- | --- |
| T-018 pure normalized selection | `3bcd141b24bf0f655fa8c2f777c7c9eb0a24ba93` / `308ec9195abc6b8ecd04b708331e91f480354422` |
| T-019 real named-file range CLI | `46e1455a5aca1f86d385a6bed649c4331c5f7296` / `68f2bbbd56caa5210474fbc5fa4aef499b6d476f` |
| T-020 dedicated 2.4 review | `33f0ba2ed7ae187cce9643433f8f1f09282ef079` / `beac0a623d27056d6deb9854674a9307dba3f89d` |
| T-021 complete documentation | `96a562b6b3ca51f4aea6bb8e4f0b3a1a5f7c10b8` / `ff5c536e1f76cd79bbc4bb155a35963498953240` |
| T-022 isolated extraction | `f2dc46627c04b92e4d2990843927e52be63f2660` / `ce2df08c4a716b0a830077e23fc383b424299523` |
| T-023 dedicated 2.5 review | `4eeee9e9505b29b4a616292434561aab569dac7f` / `ee49eb727938ab671daf6f9944c9cf4c086373f0` |
| T-024 final feature review | Current report pair, concrete decision/closing commit pending; no unseen acceptance claimed. |

Actual-parent deltas of T-018–T-023 confirm one leading owning task ID, result and
current evidence together with exactly that task's initial checkbox; eligible
milestone parents close only with their dedicated review task. Every owned commit
was immediately pushed and its full remote ref exactly read back before dependent
work. Issues #19–#24 are uniquely marked, closed/completed with evidence/readback;
added delivery native milestones #7/#8 closed only after complete associated-issue
validation. Native #9/issue #25 remain pending this review. No foreign issue,
label/comment or main incomplete milestone is closed by this feature.

## Verification and failure provenance

Fresh T-024 repository-root full runner passed 31 unit/28 integration tests, both
OK/status 0, no skips/warnings. Fresh selected 27 usability/API/documentation
commands, temporary build and Bash extraction pass. T-023 executed all 32 runnable
guide commands including independent discovery/check fences against identical
product/docs bytes; current check scopes and extraction completion are detailed
in the extent report. Runtime Python 3.12.14 on supplied Linux; other supported
runtimes/platforms and performance remain unverified.

Genuine RED was retained: T-018 two tests/14 unimplemented-behavior errors after
minimal declaration, T-019 five tests/55 missing-range assertion failures, and
T-022 two expect-rejection failures because both faulty range-only archives passed
99 old cases. The simplified equivalent BOM mutant was rerun RED before checker
implementation; GREEN rejects both. No collection/import/setup failure substitutes
for behavioral RED. Later fresh GREEN/regressions prove the delivered result.

Resolved evidence interventions EVID-A010-001/002 retain original ambiguous
redirected log/ps error and overly narrow hosted helper assertion/diagnostic
lookup failure in the extent report. The helper correction did not change accepted
report bytes, and retry validated/closed/read back native8. Earlier governing
PLAN count finding and revision/anchor observation corrections remain in owning
QC/history; valid SPEC HTML anchor was preserved. No original failure was erased.

## TODO aggregation

TODO: None. Delivery milestone 2.4 and 2.5 each report no unresolved product defect
or admissible deferred item; final feature review adds none. Resolved findings and
evidence interventions are referenced above with provenance/resolution. There is
no eligible unresolved item requiring options/tradeoffs/follow-up owner. Main
stdin/final tasks retain original ownership and are independent planned work.

## Authorized conclusion and integration protocol

Preparation was published through explicit default merge
`fbe8bedf4c6cba1ab29d53d2da05e614603d76d1` before feature branch creation, then
compatible completed JSON checkpoint explicitly merged/published as
`806e989567aef425ddd933f33fbd8f9af5edae2a`; JSON source remains
`e63b8946bbb99347b0f73f070f9c728945ee5925`. The JSON merge resolved only owned
AGENTS navigation and retained the published JSON result/pending main work.

After concrete T-024 report acceptance and single task closing/publication/hosted
closure, the authorized remaining work is accepted sole-main task ownership/evidence
reconciliation, current QC, eligible feature source archive and navigation repair,
followed by verified/published explicit two-parent merge into paused
`phase/2-json-and-stdin`. Those steps require their own concrete changed-artifact
review and actual result verification; they are not claimed performed here.
Retain feature/design/phase branches and protected/foreign resources. Preserve
T-013–T-017, stdin 2.2/final 2.3 and whole Phase 2 unchecked; do not merge the
incomplete phase into default or publish a release.
