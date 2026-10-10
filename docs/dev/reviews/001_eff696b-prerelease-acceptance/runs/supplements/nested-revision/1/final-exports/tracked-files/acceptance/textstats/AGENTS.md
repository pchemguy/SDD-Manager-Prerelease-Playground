# TextStats plugin test coordinator

The caller of “Run the test project in acceptance/textstats/” is the **test coordinator**. TextStats is a sample product used to diagnose SDD Manager workflows. This directory owns the test instructions, independent expectations and run evidence protocol; it does not supply completed product artifacts. Do not load these instructions into ordinary product skill entries.

## Read and act

Read in order: [OBJECTIVES](OBJECTIVES.md), [SETUP](SETUP.md), [SCENARIO](SCENARIO.md), [EXECUTION](EXECUTION.md), [RECOVERY](RECOVERY.md), [DIAGNOSTICS](DIAGNOSTICS.md), then selected entries in [the catalog](cases/catalog.json). Read consumer requests and assessor contracts only in their appropriate roles. [README](README.md) is the human map. Source-relative skill paths resolve two directories above this bundle; load them from the pinned package, not whichever checkout happens to be current.

Resolve non-secret configuration in this order: explicit current invocation; explicitly supplied [input file](templates/inputs.example.json); existing checkpoint for a requested continuation; documented defaults. Conflicting repository, source, destination, run identity or scope requires resolution before affected writes. Default scope is the full required campaign, continuing through authorized phases. [Optional extensions](VARIANTS.md) require explicit selection and facilities; their unavailability is Not run/non-blocking. A requested boundary limits it.

**If no dedicated test repository is identified, the first interactive next action is:** “Which dedicated test repository should this run use? Supply its URL or local checkout path.” Ask before writing or preparing fixtures. Do not choose a previous destination or create a remote repository. A URL authorizes this test's scoped work in that repository, not destructive replacement of its contents. Inspect an existing checkout and run records before deciding fresh versus resume. A resume reuses its identity and actual pending work; a new run reserves a distinct workspace/campaign.

Use existing Git and API authentication first. Missing token files are not failures. Classify an observed unavailable-access result, then follow [credential recovery](SETUP.md#protected-authentication). Never copy a source repository token into the test repository or include credential values in inputs, worker prompts, command arguments, URLs, logs or evidence.

## Roles and continuation

Use available separate consumer and assessor contexts. Give a fresh consumer only its selected request, sample preparation brief when needed, pinned skill package, applicable **product repository** instructions, authorized current-state handoff and permitted tools. Do not supply this AGENTS file, the catalog's assessor contracts, diagnostic expectations, historical answers or coordinator commentary. Record exact handoffs. An assessor independently examines literal behavior and durable state. The coordinator's full context does not make a worker fresh. If fresh isolation is unavailable, disclose it and do not certify isolation-dependent cases.

Proceed through authorized scope after each independently assessed/published prerequisite; normal phase boundaries need no additional confirmation. At a requested stop or observed interruption trigger, preserve the reached state, record the next permitted action, publish sanitized recovery evidence where possible, and stop. If a dependency is blocked, keep it Blocked/Not run; independent eligible cases may continue. Never infer pass from a consumer's claim or a script's lifecycle simulation.

On continuation, follow [RECOVERY](RECOVERY.md) before running preparation drivers or selecting work. Inspect reality even if RUN-STATE claims a clean stop. The coordinator owns INPUTS, RUN-STATE, RESUME and DIAGNOSTIC-REPORT; this is not a new mandatory journal protocol for the plugin/product workflow. Do not edit the tested package during a run. Record any proposed repair for separate acceptance and a newly pinned run.

At every case boundary retain original attempts, exact clarifications, interventions, retries, local/remote refs and independent assessment. Finish with the four-answer diagnostic report in [DIAGNOSTICS](DIAGNOSTICS.md), coverage limits and final evidence integration/publication under [EXECUTION](EXECUTION.md#final-evidence-integration), followed by a verified checkpoint. An explicit pause or unmerged boundary takes precedence. An assisted pass retains the failed or assisted first attempt.
