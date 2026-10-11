# Review execution evidence

These synthetic fixtures execute Git, filesystem and test-runner primitives in disposable temporary repositories. The caller explicitly chooses transitions; passing does not demonstrate agent instruction compliance or client installation. They use local bare remotes and no real hosting token or API.

## Reproduce

From the repository root with Python and Git available:

```text
python docs/dev/reviews/008_98a5562/evidence/lifecycle_fixture.py
python docs/dev/reviews/008_98a5562/evidence/failure_fixture.py
```

The harnesses print results and write temporary JSON. Retained [lifecycle results](lifecycle-results.json), [failure results](failure-results.json), and [environment](environment.json) identify the actual review run; temporary directory paths are provenance, not durable dependencies.

## Harness corrections

The first failure-harness attempt cloned a bare remote without choosing main; its default HEAD was absent, so the second clone could not push main. The corrected harness selects main explicitly. A later attempt assumed zero-test unittest discovery exits zero; this Python version exits nonzero with NO TESTS RAN. The corrected assertion reports the actually observed outcome. These were fixture assumptions, not plugin source defects; both retained harnesses subsequently passed.

## Limits

No installed client, consumer-agent decision enforcement, real acceptance suite, concurrency allocation race, shell reauthentication, hosted permission profile, rate-limit timing or uncertain API-write replay was executed. Fixture checks isolate supported primitives; source scenario assessment is recorded separately in the review report.
