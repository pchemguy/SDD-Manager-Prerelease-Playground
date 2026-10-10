from pathlib import Path
import subprocess, json, hashlib, datetime, base64, re

B = Path('/workspace/scratch/46b31bb4dff6')
SRC = B / '037-a021-dirty-transfer'
OUT = B / '037-sup-qc-focused-setups'
BASE = '8036adbd71ffc1f04b98e689cc131781bc20cd1f'
PIN = 'ea515f5624c8a34cc4572731a2590223a5eb27f4'
OUT.mkdir(exist_ok=True)
calls = []

def run(args, cwd=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True)
    calls.append(dict(argv=args, cwd=str(cwd) if cwd else None,
                      exit_code=r.returncode,
                      stdout_base64=base64.b64encode(r.stdout).decode(),
                      stderr_base64=base64.b64encode(r.stderr).decode(),
                      stdout_sha256=hashlib.sha256(r.stdout).hexdigest(),
                      stderr_sha256=hashlib.sha256(r.stderr).hexdigest()))
    if r.returncode:
        raise RuntimeError(str(args) + r.stderr.decode())
    return r.stdout

def git(p, *args):
    return run(['git', '--no-optional-locks', *args], p)

def snapshot(p):
    files = {}
    for n in git(p, 'ls-files', '-z').decode().split('\0'):
        if n:
            f = p / n
            files[n] = dict(sha256=hashlib.sha256(f.read_bytes()).hexdigest(),
                            mode=f.stat().st_mode & 0o777)
    idx = p / git(p, 'rev-parse', '--git-path', 'index').decode().strip()
    return dict(head=git(p, 'rev-parse', 'HEAD').decode().strip(),
                status=git(p, 'status', '--porcelain=v1').decode(),
                refs=git(p, 'show-ref').decode(),
                index_entries=git(p, 'ls-files', '--stage').decode(),
                index_sha256=hashlib.sha256(idx.read_bytes()).hexdigest(),
                tracked_files=files)

for slug in ['narrow-feature', 'missing-plan-contract']:
    p = B / ('037-sup-qc-' + slug)
    t = OUT / slug
    t.mkdir(exist_ok=True)
    if p.exists():
        # Only the interrupted, unchanged detached initialization may resume.
        assert slug == 'narrow-feature'
        assert git(p, 'rev-parse', 'HEAD').decode().strip() == BASE
        assert git(p, 'status', '--porcelain=v1').decode() == ''
        git(p, 'checkout', '-B', 'fixture', BASE)
    else:
        run(['git', 'init', '--initial-branch=fixture', str(p)])
        git(p, 'fetch', '--no-tags', str(SRC), BASE)
        git(p, 'checkout', '-B', 'fixture', BASE)
    original = {}
    for n in ['docs/dev/FEATURE-PLAN.md', 'docs/dev/FEATURE-TASKS.md', 'docs/dev/PLAN.md']:
        original[n] = (p / n).read_text()
        (t / ('ORIGINAL-' + Path(n).name)).write_text(original[n])
    baseline = snapshot(p)
    (t / 'BASELINE.json').write_text(json.dumps(baseline, indent=2) + '\n')

    if slug == 'narrow-feature':
        plan = original['docs/dev/FEATURE-PLAN.md']
        plan = plan.replace('## Accepted inputs and bounded objective',
                            '## Unaccepted proposal and retained accepted inputs', 1)
        plan = plan.replace('\n## Phase and milestone strategy',
            '\nThis modified draft is an unaccepted caller proposal derived from actual accepted preparation `' + BASE + '`. Historical acceptance and adjacent QC describe original objects only. No task, milestone, projection or implementation result is claimed.\n\n## Phase and milestone strategy', 1)
        begin = plan.index('| Parent / new milestone |')
        end = plan.index('## Baseline and integration dependencies')
        new = '''| Parent / proposed milestone | Useful outcome, prerequisites and objective exits |
| --- | --- |
| Phase 2 / 2.4 — Named-file ranges | One useful documented and distributable named-file capability: complete F-001–F-004 parser/selection/acquisition/text/JSON behavior, full public docs and runnable examples, nonempty unit/integration suites and real isolated extracted-module import provenance/exits. Depends on actual reviewed/published JSON 2.1 and compatible baseline/projection prerequisites below. Four bounded delivery tasks implement pure selection, integrate the real CLI, complete public documentation and independently verify extracted-source delivery. Dedicated T-020 performs complete code review, required checks, blocker repair, usefulness demonstration and milestone report after all four deliverables. |
| Phase 2 / 2.6 — Range feature review | Mandatory final single-task feature review T-024 after complete 2.4 delivery/review/closure. Review all F contracts and affected R obligations, component/docs/extraction coherence and accumulated findings/TODOs. Exclude its own still-open review milestone; preserve pending main 2.2/2.3 and T-013–T-017. |

The single delivery milestone provides one cohesive complete named-file capability. The earlier source split demonstrated CLI delivery from documentation/distribution; this proposal keeps internal progress and early runnable examples in four bounded tasks while treating accurate public explanation and independently portable source delivery as part of the same usable outcome. A separate public-docs phase would add handoff cost while withholding complete usability. Retain consequential human feedback after the first integrated path and extracted demonstration. Assess milestone size semantically, without padding to a count target. Mandatory delivery and final feature reviews are excluded from delivery counts.

Historical milestone 2.5 and task T-023 retain original identities in baseline `BASELINE`. They are reserved and outside this proposal's executable range: documentation and extraction move to 2.4 and review responsibilities to T-020. They are not completed, closed, deleted as done, renumbered, projected or archived. A later accepted change requires explicit ownership/hosted-history reconciliation. Accompanying caller evidence retains their original complete source text.

At T-019 demonstrate real middle/beyond-EOF/blank/mixed-terminator selections and exposed BOMs through text/JSON. At T-021/T-022 demonstrate complete public usage and the extracted package with unchanged API. These support actual continue/amend/simplify/stop choices without automatically changing scope or bypassing review.

'''.replace('BASELINE', BASE)
        plan = plan[:begin] + new + plan[end:]
        plan = plan.replace('2.5 user documentation and extraction', '2.4 complete user documentation and extraction')
        plan = plan.replace('isolated extracted module exits in 2.5', 'isolated extracted module exits in 2.4')
        (p / 'docs/dev/FEATURE-PLAN.md').write_text(plan)

        tasks = original['docs/dev/FEATURE-TASKS.md']
        start = tasks.index('## Phase 2 — JSON and stdin')
        stop = tasks.index('## Execution, ownership and integration rules')
        prefix = tasks[:start].replace('## Governing sources and preparation stop',
            '## Unaccepted proposal and retained original provenance')
        prefix += 'This modified hierarchy is an unaccepted caller proposal. Original PLAN/TASKS acceptance and adjacent QC do not accept these draft bytes. No unchecked work is treated as completed.\n\n'
        blocks = {}
        for task in ['018', '019', '020', '021', '022', '023', '024']:
            match = re.search(r'        - \[ \] T-' + task + r' —.*?(?=        - \[ \] T-|    - \[ \] Milestone|\n## Execution|\Z)', tasks, re.S)
            assert match
            blocks[task] = match.group(0).rstrip()
        blocks['021'] = blocks['021'].replace('Depends on: T-020 and reviewed/closed milestone 2.4.',
            'Depends on: T-019; consolidated delivery review/closure follows all four delivery tasks.')
        blocks['020'] = '''        - [ ] T-020 — Review, test and report complete milestone 2.4
            Scope: parser/selection/complete acquisition/named-file text/JSON, full public/runnable documentation, isolated extracted-source provenance and unchanged public API/core/file/resource/error behavior.
            Depends on: T-018, T-019, T-021 and T-022.
            Evidence: actual code review plus every F matrix, huge-endpoint/BOM/complete-decode/usage-before-acquisition regressions, nonempty unit/integration counts, all runnable public examples, independently imported extracted real module and retained signature/export/error/resource checks. Repair every blocker. Preserve usefulness demonstrations and original findings/TODOs with provenance/options/owners/limits; tests alone cannot complete review. Original T-020/T-023 review responsibilities consolidate here without claiming T-023 completed.
            Report: `docs/dev/features/002_e7cae5b-named-file-ranges/phases/2/2.4.md`.'''
        blocks['024'] = blocks['024'].replace('Depends on: T-020 and T-023; feature delivery milestones 2.4 and 2.5 completed/closed, excluding its own still-open 2.6.',
            'Depends on: T-020 and completed/closed consolidated milestone 2.4, excluding its own still-open 2.6.')
        blocks['024'] = blocks['024'].replace('from both feature milestones',
            'from all delivery tasks and their consolidated milestone review')
        body = '## Phase 2 — JSON and stdin\n\n- [ ] Phase 2 — JSON and stdin\n    - [ ] Milestone 2.4 — Named-file ranges\n'
        body += '\n'.join(blocks[k] for k in ['018', '019', '021', '022', '020'])
        body += '\n    - [ ] Milestone 2.6 — Range feature review\n' + blocks['024'] + '\n\n'
        body += '## Reserved historical identities\n\nT-023 and former milestone 2.5 remain reserved, unchecked in original source objects and outside this proposed executable range. Their original names, dependencies, reports and responsibilities remain in baseline `' + BASE + '` and accompanying original caller source evidence. No closure, deletion-as-done, duplicate ownership, new issue or archive follows. T-020 proposes combined delivery review; T-024 remains final feature review.\n\n'
        tail = tasks[stop:].replace("new milestone identities are the accepted plan's 2.4/2.5/2.6",
            'proposed active milestone identities are 2.4/2.6; original 2.5 is reserved and unexecuted')
        tail = tail.replace('follows both delivery closures', 'follows the delivery closure')
        (p / 'docs/dev/FEATURE-TASKS.md').write_text(prefix + body + tail)
        owned = ['docs/dev/FEATURE-PLAN.md', 'docs/dev/FEATURE-TASKS.md']
        purpose = 'Unaccepted cohesive single delivery milestone and four delivery tasks; stable history retained.'
        ask = 'Review the proposed feature PLAN and TASKS against unchanged feature specification, main design and current execution prerequisites. Assess whether outcomes, decomposition, dependencies, review boundaries and verification/report exits are coherent and useful. Modified drafts have not been accepted; inherited adjacent QC applies to original preparation objects. This is read-only: report technical findings and necessary owner/QC/acceptance follow-up without editing documents, statuses, refs or index. Do not implement, run task tests or perform provider operations.'
    else:
        plan = original['docs/dev/PLAN.md'].replace('## Objective and governing inputs',
            '## Unaccepted caller fixture and retained governing inputs', 1)
        plan = plan.replace('\nDeliver the accepted',
            '\nThis modified main PLAN is an unaccepted caller review fixture from actual preparation `' + BASE + '`. Adjacent QC retains historical identities and has not been refreshed for changed bytes. Governing SPEC/design/TASKS and product contracts are unchanged; no human acceptance or implementation result is claimed.\n\nDeliver the accepted', 1)
        replacements = {
            'extracted-source module-entry invocation independent of the original checkout': 'source-package module-entry invocation',
            'Source extraction checks must isolate imports from the checkout and installed copies.': 'Source-package checks run delivered module examples.',
            ' and accidentally importing the checkout during distribution verification': ''
        }
        for old, new in replacements.items():
            assert old in plan, old
            plan = plan.replace(old, new)
        (p / 'docs/dev/PLAN.md').write_text(plan)
        owned = ['docs/dev/PLAN.md']
        purpose = 'Single injected R-013 omission: proof imported extraction differs from checkout/installed source.'
        ask = 'Review the current main PLAN against accepted main specification and design. Assess whether it provides a complete feasible delivery and verification route for required contracts and whether adjacent QC supports dependent work. This modified PLAN is an unaccepted caller fixture; inherited QC describes original preparation. Work read-only: identify concrete gaps and owner/QC/acceptance follow-up without editing governing or unselected documents, statuses, refs or index. Do not implement, run task tests or perform provider operations.'
    reached = snapshot(p)
    reached.update(schema_version=1, observed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   actual_baseline=BASE, purpose=purpose, worktree=str(p),
                   fixture_actor='caller assessor; not consumer', fixture_accepted=False,
                   owned_fixture_paths=owned, plugin_pin=PIN,
                   publication_gate='Root review/publication before fresh consumer dispatch',
                   no_remote_configured=True, no_consumer_dispatched=True)
    (t / 'START.json').write_text(json.dumps(reached, indent=2) + '\n')
    (t / 'FIXTURE.diff').write_bytes(git(p, 'diff', '--binary', '--', *owned))
    for n in owned:
        (t / ('FIXTURE-' + Path(n).name)).write_bytes((p / n).read_bytes())
    (t / 'CONSUMER-INPUT.md').write_text('# Review TextStats document proposal\n\nWork read-only in ' + str(p) + ' at retained product ' + BASE + '. First read product AGENTS and use only pinned local SDD Manager package/current product sources. This read-only request supersedes inherited execution/publication requests; historical acceptance does not apply to modified draft bytes. Do not discover siblings, inspect caller assessments/cases/catalog/history, or use agents.\n\n' + ask + '\n\nRecord actual loaded hashes, commands, substantive findings, reasoning and limitations in ' + str(B / ('037-sup-qc-' + slug + '-consumer-observations.json')) + '. That requested external record is the sole output. Use Python -B/PYTHONDONTWRITEBYTECODE=1 if needed and stop after reporting.\n')
    changed = [n for n, d in reached['tracked_files'].items() if d != baseline['tracked_files'][n]]
    checks = dict(exact_actual_baseline=reached['head'] == BASE,
                  index_unchanged=reached['index_sha256'] == baseline['index_sha256'],
                  only_owned_bytes_changed=set(changed) == set(owned), changed_paths=changed,
                  upstream_unchanged=all(reached['tracked_files'][n] == baseline['tracked_files'][n] for n in ['docs/dev/SPEC.md', 'docs/dev/ARCHITECTURE.md', 'docs/dev/DECOMPOSITION.md', 'docs/dev/TASKS.md']))
    (t / 'AUTHOR-CHECKS.json').write_text(json.dumps(checks, indent=2) + '\n')

protocol = '''# Caller and assessor protocol

Do not supply protocol, guide, START, purpose fields, author checks or diffs to consumers. Root reviews/publishes exact fixture and ordinary input before fresh dispatch. Original actual source/QC is retained; no modified proposal has fabricated Ready/acceptance. Synthetic local assessment sensitivity is separate from live repository acceptance.

Narrow proposal: independently review complete F-001–F-004, affected retained R contracts and design. Four delivery IDs T-018/T-019/T-021/T-022; mandatory review T-020 and final extent review T-024 excluded from counts. Semantic usefulness/dependencies/cohesion justify one delivery milestone; do not force count-padding. Check oversized/subsystem tasks and trivial edits. Retain huge endpoints, complete strict decode, usage-before-acquisition, once-only BOM, unchanged API, JSON baseline, docs/examples/extracted-import provenance, nonempty suites and review/report/TODO exits. T-023/2.5 are reserved, not completed or duplicated. Any unexpected coverage/dependency flaw is an actual fixture finding, never excused to force positive outcome. Stale original QC cannot certify changed proposals; a substantive count conclusion and current readiness gate are separate.

Missing-contract proposal: independently detect the single caller-injected R-013 extraction-origin verification omission, correct PLAN owner and dependent refusal. Do not rewrite accepted SPEC/design/TASKS to excuse omission. Original stale QC does not establish current coverage. This is caller fixture sensitivity, not a consumer-generated product failure.

Final seal requires exact START files/modes, dirty diffs, HEAD/refs/index entries/raw index bytes and no untracked additions. Only requested external observations allowed. Preserve all original attempts/interventions/commands and independently grade outside 32 required variants. Shared-filesystem isolation/native transcript/provider audit remain uncertified. Publish exact and safe screened evidence separately if necessary; base64 command channels preserve actual NUL bytes.

Remaining overload/fragmentation, SPEC/design conflict and TASKS strategy-drift scenarios require separate coherent transparent fixtures, not stacked defects here. Ten or more meaningful delivery milestones/tasks cannot be authored honestly by inventing unrelated TextStats functionality; root must select a realistic bounded contract/decomposition scope and distinguish overload from merely large counts. Repeated tiny phases may use the same actual scope only with a disclosed fragmented proposal. Governing conflicts must preserve accepted intent and remain owner-specific.
'''
(OUT / 'ASSESSOR-PROTOCOL.md').write_text(protocol)
(OUT / 'SETUP-COMMANDS-BASE64.json').write_text(json.dumps(dict(schema_version=1, encoding='all stdout/stderr base64 with exact raw hashes', commands=calls), indent=2) + '\n')
guide = subprocess.check_output(['git', 'show', PIN + ':acceptance/textstats/cases/assessor/DOCUMENT-QC.md'], cwd=B / 'SDD-Manager')
(OUT / 'GUIDE-PROVENANCE.json').write_text(json.dumps(dict(pin=PIN, path='acceptance/textstats/cases/assessor/DOCUMENT-QC.md', sha256=hashlib.sha256(guide).hexdigest(), role='caller/assessor only'), indent=2) + '\n')
(OUT / 'INTERVENTIONS.json').write_text(json.dumps(dict(schema_version=1, interventions=[
    dict(scope='prior tracking setup', actor='root screening', result='Rejected before copies/staging/commit', reason='Original SETUP-COMMANDS.json NUL stdout at /commands/11/stdout and /commands/30/stdout, 154 NUL each', original_untouched=True, recovery='Root retains original hash/manifest and narrow binary sidecars/screened derivative/separate publication manifest'),
    dict(scope='this caller setup first attempt', actor='caller assessor', result='Stopped before authoring edits', reason='Detached-only initialized repository had no refs; git show-ref exited 1', recovery='Verified exact baseline/clean files, created explicit LOCAL fixture branch at actual baseline; no source/evidence/live refs changed')
]), indent=2) + '\n')
(OUT / 'AUTHOR-SCRIPT.py').write_bytes(Path(__file__).read_bytes())
manifest = dict(schema_version=1, actual_baseline=BASE, plugin_pin=PIN, author='caller assessor; no consumer run', artifacts=[dict(path=str(f.relative_to(OUT)), sha256=hashlib.sha256(f.read_bytes()).hexdigest(), bytes=f.stat().st_size) for f in sorted(OUT.rglob('*')) if f.is_file() and f.name != 'MANIFEST.json'])
(OUT / 'MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(dict(artifact_count=len(manifest['artifacts']), setup_root=str(OUT), consumers=0)))
