# SPEC review report

## Current gate

State: **Blocked**. S-QC-01 is unresolved and blocks dependent planning readiness. Existing PLAN/TASKS can be assessed independently, but cannot acquire whole-chain Ready status from this SPEC.

Reviewed scope: `docs/dev/SPEC.md`; governing inputs: PROJECT, ARCHITECTURE and DECOMPOSITION. No children apply.

Git root/project: `/tmp/sdd-qc019-consumers/case-two`. Branch: `main`. Reviewed HEAD: `3c75b28d6eceed588f946cb415aecef9c32c2295`. Git worktree is eligible for the specifically authorized local report writes; initial status was clean.

Review date: 2026-10-04. Reviewer: local SDD document reviewer. Operation: preparation readiness review only. The user permits adjacent QC reports and prohibits governing-document edits, code implementation, commits, pushes and hosted-service access. No corrections or implementation checks were performed. No Revision section is warranted.

The exact identities below are the current roots and governing inputs at review time. No focused children, active feature documents, prior QC reports, code, tests or packaging files exist in the inspected fixture tree. All governing sources were tracked and unchanged before review. These documents are treated as the supplied governing baseline; separate evidence of human acceptance was not supplied.

## Exact source identities

| Source | Git blob at reviewed HEAD | SHA-256 of reviewed working bytes |
| --- | --- | --- |
| `docs/dev/ARCHITECTURE.md` | `57e4988c2edf3b21acd2b70c7a3b022192cf8e82` | `bf216226a4669380f32fea77a0a6c153a12fa5473c9e46a58fb90bb57c87276b` |
| `docs/dev/DECOMPOSITION.md` | `9d6298666608007e4fc140aabf4a83efad90735e` | `c8fb554e2e43d579334d87297303d95bcd1cca70c2252b150c91deef5f3a8f16` |
| `docs/dev/PLAN.md` | `9c19cf19d3bd2f45c9d73b3628f9a0431ce11daa` | `844ca4082ebe2c4a2dc19d56c0bb340e0d1e9530b7ccc19151398eea75110bd5` |
| `docs/dev/PROJECT.md` | `e07111d923ff1e115c623205bae663d77ae4edd3` | `126ce35b5c1950607c61afd109596e1d3672ee96b1b1d432551e62417c75945f` |
| `docs/dev/SPEC.md` | `7d65a67303a376c16f2f4980f4ffb10c7776c8d3` | `288fd3a7eb3a6d1254b21461a7d2377a951f1c123e9ad2b65cff56218c6a6292` |
| `docs/dev/TASKS.md` | `829ef0939bb712f6a346926dab45367bae405032` | `6d04b9419d99b035c36d62759da54a31eced509402a3357302ef4cf481f3ad74` |
| `docs/dev/layout.md` | `ee184c852664e74c1352616ab083d77145f05ab4` | `35526503ce8812911ae14e8bec8a7669cd00f7a6136eaff1365ba9fafba5561c` |

## Initial review

Performed static reading and SPEC/design/project comparison under sdd-specify and the shared development-document QC policy. No code or tests were run.

| Contract group | Structural/design coverage | Assessment |
| --- | --- | --- |
| S1 output/status | CLI renders output/status; pure counter supplies count | Consistent ownership and assessable output. |
| S2 empty/final line | Counter counts each yielded line, including final unterminated line | SPEC wording conflicts with the explicit design guarantee; see S-QC-01. Empty-file zero is coherent. |
| S3 errors/usage and resource lifecycle | CLI owns UTF-8 file context, file/error handling and rendering | File/decoding errors, usage status and success/failure close obligations are represented. |
| Project scope/non-goals | Local synchronous CLI; no counter dependency on CLI | Main scope fits design. SPEC excludes JSON/stdin/networking/archives; PROJECT also excludes GUI. No GUI behavior is introduced in SPEC. |

| Finding | Location / consequence | Correction owner / objective recheck | Current disposition |
| --- | --- | --- | --- |
| S-QC-01 | `SPEC.md:3` says “Count final unterminated lines and empty files as zero”; `DECOMPOSITION.md:3` says every yielded line counts once, including a final line with no newline. A one-line file without a newline has incompatible expected counts (0 versus 1), so tests/tasks cannot adopt a canonical expected result. | sdd-specify, coordinating with sdd-design/human if intended behavior changes: clarify S2 to agree with the accepted design, or obtain an explicit design decision. Recheck an empty file → 0 and a single nonempty unterminated line → the agreed exact count; then reassess impacted PLAN/TASKS. | Open; review-only scope forbids correction. |


## Scope and handoff

Adjacent report creation is authorized. Behavioral clarification/correction is outside this review request; no sources were changed. No remote evidence is required for this local review. No Ready exception was supplied.
