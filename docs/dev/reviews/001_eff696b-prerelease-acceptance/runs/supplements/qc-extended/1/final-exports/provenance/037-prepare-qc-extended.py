import base64, hashlib, json, subprocess
from pathlib import Path
r=Path('/workspace/scratch/46b31bb4dff6'); origin=r/'037-sup-qc-narrow-feature'
setup=r/'037-sup-qc-extended-setup'; setup.mkdir()
def run(args, cwd):
    p=subprocess.run(args,cwd=cwd,capture_output=True)
    assert p.returncode==0,(args,p.stderr.decode(errors='replace'))
    return p.stdout
head=run(['git','rev-parse','HEAD'],origin).decode().strip()
assert head.startswith('8036')
states={}
for label in 'abcd':
    product=r/('037-sup-qc-extended-'+label)
    run(['git','clone','--no-hardlinks','--quiet','--no-checkout',str(origin),str(product)],r)
    run(['git','checkout','--quiet','-b','trial/qc-proposal-'+label,head],product)
    run(['git','remote','set-url','--push','origin','file:///dev/null'],product)
    name='docs/dev/FEATURE-PLAN.md' if label=='a' else 'docs/dev/FEATURE-SPEC.md' if label=='c' else 'docs/dev/FEATURE-TASKS.md'
    path=product/name; original=path.read_bytes(); text=original.decode()
    if label=='a':
        start=text.index('| Parent / new milestone |'); end=text.index('## Baseline and integration dependencies')
        rows=[('2.7','Logical segment infrastructure','completed JSON checkpoint'),('2.8','EOF clamping','2.7'),('2.9','BOM exposure handling','2.8'),('2.10','Spaced range parsing','2.9'),('2.11','Equals range parsing','2.10'),('2.12','Repeated-range validation','2.11'),('2.13','Complete-byte acquisition wiring','2.12'),('2.4','First usable named-file ranges CLI','2.13'),('2.5','Range public documentation','reviewed 2.4'),('2.14','Extracted source verification','2.5')]
        replacement='| Parent / new milestone | Proposed outcome and dependencies |\n| --- | --- |\n'
        for ident,title,dep in rows:
            replacement+=f'| Phase 2 / {ident} — {title} | Depends on {dep}; deliver this individual seam, then its dedicated code review/testing/report. Retain all F/R contracts. |\n'
        replacement+='| Phase 2 / 2.6 — Range feature review | Dedicated final review after all ten delivery milestones; main stdin/final work remains pending. |\n\nThe proposed ten delivery milestones expose the first real user-visible range invocation only at 2.4, after seven preceding seam-specific milestones. No intermediate seam provides a runnable changed CLI capability. The existing coverage table below remains required; dedicated review units are excluded from delivery count.\n\n'
        text=text[:start]+replacement+text[end:]
    elif label=='b':
        marker='        - [ ] T-020 —'
        pos=text.index(marker)
        additions=''
        for ident,title in [(25,'Register spaced range parser'),(26,'Register equals range parser'),(27,'Check ASCII endpoint characters'),(28,'Reject repeated range options'),(29,'Wire range BOM flag'),(30,'Edit one range help sentence')]:
            additions+=f'        - [ ] T-{ident:03} — {title}\n            Outcome: this narrow edit within the existing T-019 integrated range path.\n            Scope: `textstats/cli.py` and its existing tests.\n            Depends on: T-018; T-019 retains its current complete integrated acceptance scope.\n            Evidence: check this isolated edit; publish separately before proceeding.\n'
        text=text[:pos]+additions+text[pos:]
    elif label=='c':
        text+='\n## Proposed public API amendment\n\nF-005: Both public `count_text` and `count_file` must require positional `start` and `end` range arguments, and default to selected rather than whole-input counting. This changes their public signatures and whole-input semantics. Existing architecture/component ownership and accepted main contracts are unchanged in this proposal.\n'
    else:
        pos=text.index('        - [ ] T-020 —')
        text=text[:pos]+'        - [ ] T-025 — Add a third-party range benchmark dependency\n            Outcome: require an external benchmark package in normal TextStats runtime and establish a mandatory throughput target before first range CLI delivery.\n            Scope: runtime dependency configuration and a new benchmark subsystem.\n            Depends on: T-018; T-019 waits for this task.\n            Evidence: install the external package and enforce throughput acceptance.\n'+text[pos:]
    path.write_text(text)
    (setup/(label+'-original.bin')).write_bytes(original)
    (setup/(label+'-proposal.bin')).write_bytes(path.read_bytes())
    tracked=run(['git','ls-files','-z'],product).split(b'\0')
    files={p.decode():{'sha256':hashlib.sha256((product/p.decode()).read_bytes()).hexdigest(),'bytes':(product/p.decode()).stat().st_size,'mode':(product/p.decode()).stat().st_mode & 0o777} for p in tracked if p}
    index=run(['git','rev-parse','--git-path','index'],product).decode().strip()
    (setup/(label+'-index.bin')).write_bytes((product/index).read_bytes())
    states[label]={'product_root':str(product),'HEAD':head,'proposal_path':name,'files':files,'refs_base64':base64.b64encode(run(['git','show-ref'],product)).decode(),'status_base64':base64.b64encode(run(['git','status','--porcelain=v1','-z'],product)).decode(),'diff_base64':base64.b64encode(run(['git','diff','--binary'],product)).decode(),'index_sha256':hashlib.sha256((product/index).read_bytes()).hexdigest()}
(setup/'START.json').write_text(json.dumps(states,indent=2)+'\n')
request='Review the current proposed development-document bytes in each of these four independent checkouts against its governing accepted sources and current adjacent review evidence. Determine whether each can proceed to implementation, explaining concrete contract routes, dependencies, useful delivery boundaries, counts with review exclusions and required owner actions. Keep the review read-only: no product edits, commits, tests, provider operations or implementation. Prior accepted histories remain historical; proposals are not yet accepted. Read only selected/current product instructions and the pinned SDD package; no coordinator/assessor material. Record actual commands, separate output channels, inspected path hashes, findings and limits in /workspace/scratch/46b31bb4dff6/037-sup-qc-extended-consumer-observations.json.\n\n'+ '\n'.join(str(r/('037-sup-qc-extended-'+x)) for x in 'abcd')+'\n\nPinned package: /workspace/scratch/46b31bb4dff6/037-textstats-product/.codex/plugins/sdd-manager; verify its actual location through product SDD-MANAGER.md before loading.\n'
(setup/'ordinary-input.md').write_text(request)
print('Prepared four caller-authored read-only proposals from actual',head)
