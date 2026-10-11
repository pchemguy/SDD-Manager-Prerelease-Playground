# Accepted pre-release repairs

Campaign 024_ed2d571. Original reviewed source ed2d571d20aa8ad6ee77f25ad89602e82e6a653b (0.14.6); execution starts at review checkpoint 21d144057413473f7e402fa0ce679cf2e3095024. [Review](REVIEW-REPORT.md), [revision evidence](REVISION-REPORT.md).

User authorized fixes R-001–R-004 and explicitly excluded live testing. R-005 remains an evidence gap outside scope; no current-source live or installed-client readiness claim. Reuse revision/024_ed2d571-pre-release-review, target feature/architecture-revision. Preserve unrelated work; no clones, /pyenv execution, forced publication or installation.

| Action | Finding | Accepted correction | Objective recheck |
| --- | --- | --- | --- |
| V-001 | R-001 | Probe public textstats.count_text; validate package origin; disclose injector's narrower core.py layout and equivalent fixture option | Package-only literal baseline passes; broken public export fails despite correct private core; injected assertion failure stays nonempty with zero errors |
| V-002 | R-002 | Reject lexical receipt and parent symlinks before resolution on fresh/resume paths | Dangling/occupied symlink and symlink-parent rejected without mutation; ordinary hold/resume and drift/nonreplay checks pass |
| V-003 | R-003 | Include root notice files in committed/dirty package snapshots, align package documentation and bump synchronized manifests to 0.14.7 | Actual pinned README notice links and target links resolve; dirty notice changes affect fingerprint; assets still present and assessor material excluded |
| V-004 | R-004 | Restore missing 020 campaign and contiguous campaign table; add truthful current campaign links | Complete sequential navigation and resolving links; inspect GFM table structure |

No governing product contract or task-list change is selected. Public API requirements remain unchanged; only erroneous probe assumptions and package path selection change. Observe meaningful RED before behavioral fixes; verify GREEN and persist each action before dependent work. Finish with full support suite, package/catalog checks and fresh independent review, then explicit two-parent merge, merged-state verification and normal target publication/readback. Record actual repair dispositions without rewriting original review observations.

Execution status: V-001–V-004 verified and explicitly merged/published in 0.14.7; see [revision report](REVISION-REPORT.md). No live testing performed.
