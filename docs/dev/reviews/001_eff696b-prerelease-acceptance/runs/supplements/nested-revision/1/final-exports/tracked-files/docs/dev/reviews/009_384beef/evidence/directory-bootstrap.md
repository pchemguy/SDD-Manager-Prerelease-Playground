# Fresh directory-only bootstrap observation

Layout note: Markdown paths were updated to `acceptance/textstats/` after the recorded run. Original commands/results remain in the referenced commits and unmodified raw logs; this path normalization does not claim the earlier run used the new layout.

## Invocation and observed result

A fresh coordinator context was started with a directory-only invocation (path displayed at its current location):

```text
Run the test project in /workspace/scratch/6420baa7afea/acceptance/textstats/.
```

No prior conversation, repository destination, expected answer or assessor correction was supplied. Source checkpoint: `f6fd96f`. The fresh context independently read bundle instructions and reported:

> Which dedicated test repository should this run use? Supply its URL or local checkout path.

It identified AGENTS/SETUP's before-write gate, the absence of a repository default, full-github/full-scope defaults after input resolution, and the distinction between support self-tests and the requested live campaign. Its final response stated that only documents had been read and no files changed. It did not substitute an earlier repository or request a token merely because none was supplied.

## Independent state observation

Root captured source state before dispatch and after completion: HEAD, current branch, SHA-256 for all 283 tracked files, and digests of refs and porcelain status. Every value matched. The checkpoint therefore supports documentation-only bootstrap with no source mutation or fixture/setup write. Full snapshots remain session verification inputs; this report retains the observed comparison rather than copying unrelated source state.

This is an actual fresh-context observation, not a scripted expected-answer assertion. The retained agent messages/final claim and Git/file observations are structured evidence; no complete native worker transcript is claimed.

## Coverage boundary

The required missing-repository discovery behavior is demonstrated. No destination was supplied, so authentication resolution, setup, product workflows, real GitHub tracking/publication, controlled partial-product interruption, unexpected product-worker termination and the 27 live outcomes were not executed here. They remain the explicit live-acceptance follow-up in the revision report and test-project README, with a copyable invocation prompt. Helper recovery/checker tests remain infrastructure evidence, not substitutes for those live cases.
