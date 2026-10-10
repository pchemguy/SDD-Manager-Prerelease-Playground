# Tasks

## Phase 1 — File line counter

- [ ] Phase 1 — File line counter
    - [ ] Milestone 1.1 — File line counter
        - [ ] T-001 — Implement pure line counter
            Scope: counter.py and unit checks for S1/S2, including empty/final line. Depends on: none. Verification: independent counts pass.
        - [ ] T-002 — Integrate CLI file and error handling
            Scope: cli.py, unit and integration tests for S1–S3/resource release. Depends on: T-001. Verification: actual stdout/stderr/status and close behavior.
        - [ ] T-003 — Package and document the usable CLI
            Scope: pyproject.toml, README and clean package smoke integration. Depends on: T-002. Verification: installed entry point retains all success/error contracts.
        - [ ] T-004 — Review, test and report milestone 1.1
            Depends on: T-001,T-002,T-003. Verification: code review, focused full milestone checks, blocker fixes, report docs/dev/reports/phases/1/1.1.md committed.
    - [ ] Milestone 1.2 — Phase review
        - [ ] T-005 — Review, test and report phase 1
            Depends on: milestone 1.1 completion/closure. Verification: phase code review/all exits, fixes and PHASE-REPORT.md plus final implementation report/TODO aggregation committed.
