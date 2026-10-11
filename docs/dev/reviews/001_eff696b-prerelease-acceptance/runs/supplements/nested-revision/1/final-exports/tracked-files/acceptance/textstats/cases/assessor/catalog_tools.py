#!/usr/bin/env python3
"""Validate reusable assets and render strictly isolated selected product requests."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

BUNDLE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BUNDLE / 'scripts'))
import core
import campaign

IDS = {f'A-{i:03}' for i in range(1, 28)}
PROTOCOLS = {'staged-work', 'unpublished-commit', 'failed-required-check', 'rejected-push',
             'conflict-and-prospective-failure', 'dirty-transfer', 'uncertain-hosted-effect', 'access-classification'}
LEAK = re.compile(r'assessor_contract|expected_ref|checkpoint_bindings|TST-\d+|A-0\d{2}|sdd-(?:steer|integrate-feature)|(?:expected|correct)\s+(?:routing|route|recovery)', re.I)
FIELDS = {'head','branch','parents','merge_heads','staged_paths','unstaged_paths','untracked_paths','conflict_paths','publication','remote_containment'}
REFS = set(core.load(BUNDLE/'schemas/run-state.schema.json')['properties']['checkpoint_refs']['properties'])


def require(condition, message):
    if not condition:
        raise ValueError(message)


def asset(root, name, prefix):
    require(isinstance(name, str) and name.startswith(prefix) and '\\' not in name, 'invalid asset location')
    path = Path(name)
    require(not path.is_absolute() and '..' not in path.parts, 'unsafe asset path')
    absolute = root / path
    require(not any(p.is_symlink() for p in [absolute, *absolute.parents] if p.is_relative_to(root)), 'symlink asset')
    require(absolute.is_file() and absolute.resolve().is_relative_to(root.resolve()), 'missing asset')
    require(absolute.stat().st_size > 0, 'empty asset')
    return absolute


def validate_contract(value, case_id):
    require(isinstance(value, dict) and set(value) <= {'schema_version','case_id','checks','required_agent_checks','variant_agent_checks'}, 'unknown contract field')
    require(type(value.get('schema_version')) is int and value['schema_version'] == 1 and value.get('case_id') == case_id, 'invalid contract identity')
    checks = value.get('checks')
    require(isinstance(checks, list) and checks, 'empty contract')
    criteria = value.get('required_agent_checks')
    require(isinstance(criteria, list) and criteria and all(isinstance(s,str) and s.strip() for s in criteria), 'missing independent criteria')
    variant_checks=value.get('variant_agent_checks',{})
    require(isinstance(variant_checks,dict) and all(re.fullmatch('[a-z][a-z0-9-]*',k) and isinstance(v,list) and v and all(isinstance(x,str) and x.strip() for x in v) for k,v in variant_checks.items()), 'invalid variant criteria')
    seen = set()
    for check in checks:
        require(isinstance(check, dict) and isinstance(check.get('id'), str) and check['id'] and check['id'] not in seen, 'duplicate/invalid check')
        seen.add(check['id'])
        kind = check.get('kind')
        allowed = {'literal':{'id','kind','key','expected'},'git':{'id','kind','field','expected','expected_ref'},'file':{'id','kind','path','exists','sha256'},'task_ownership':{'id','kind','documents'}}
        require(kind in allowed and set(check) <= allowed[kind], 'invalid DSL fields')
        if kind == 'task_ownership' and 'documents' in check:
            try: core.validate_task_documents(check['documents'])
            except core.Stop: raise ValueError('invalid task documents') from None
        if kind == 'literal':
            require(isinstance(check.get('key'),str) and check['key'] and 'expected' in check, 'invalid literal')
        elif kind == 'git':
            require(check.get('field') in FIELDS and (('expected' in check) != ('expected_ref' in check)), 'invalid git check')
            if 'expected_ref' in check:
                require(check['expected_ref'] in {'checkpoint_refs.' + r for r in REFS}, 'unknown checkpoint ref')
        elif kind == 'file':
            name = check.get('path')
            require(isinstance(name,str) and name and not Path(name).is_absolute() and '..' not in Path(name).parts and not core.protected(name), 'invalid file check path')
            require('exists' in check or 'sha256' in check, 'empty file check')
            if 'exists' in check: require(type(check['exists']) is bool, 'invalid file existence')
            if 'sha256' in check: require(bool(re.fullmatch('[a-f0-9]{64}',str(check['sha256']))), 'invalid file hash')


def validate_catalog(root=BUNDLE, value=None):
    root = Path(root).resolve()
    value = core.load(root/'cases/catalog.json') if value is None else value
    require(isinstance(value,dict) and set(value) == {'schema_version','cases'} and type(value['schema_version']) is int and value['schema_version'] == 1, 'invalid catalog version')
    cases = value['cases']
    require(isinstance(cases,list) and len(cases) == 27, 'exactly 27 cases required')
    names = [c.get('id') for c in cases if isinstance(c,dict)]
    require(len(names)==27 and len(set(names))==27 and set(names)==IDS, 'invalid/duplicate stable IDs')
    orders = [c.get('order') for c in cases]
    require(all(type(n) is int for n in orders) and len(set(orders))==27 and set(orders)==set(range(1,28)), 'invalid/duplicate order')
    by_id = {c['id']:c for c in cases}
    paths = set()
    protocols = set()
    for c in cases:
        require(c.get('phase') in {'P1','P2','P3','P4','P5'} and c.get('mode') in {'product','isolated-trial','independent-assessment'}, 'invalid phase/mode')
        campaign.variants(c)
        deps = c.get('dependencies')
        require(isinstance(deps,list) and len(deps)==len(set(deps)) and all(d in IDS and d != c['id'] for d in deps), 'invalid prerequisite ID')
        for field, prefix in [('consumer_input','cases/consumer/'),('assessor_contract','cases/assessor/'),('assessor_guide','cases/assessor/')]:
            name = c.get(field)
            require(name not in paths, 'duplicate selected asset path')
            paths.add(name)
            path = asset(root,name,prefix)
            if field == 'consumer_input': require(not LEAK.search(path.read_text()), 'consumer route-answer leakage')
            if field == 'assessor_contract':
                contract=core.load(path);validate_contract(contract,c['id'])
                if 'variant_agent_checks' in contract:require(set(contract['variant_agent_checks'])=={v['id'] for v in campaign.variants(c)}, 'variant criteria/catalog mismatch')
        require(isinstance(c.get('prerequisites'),list) and c['prerequisites'], 'missing prerequisites')
        start = c.get('checkpoint_bindings',{}).get('start',{})
        require(start.get('from_case') is None if not deps or c['mode']=='independent-assessment' else start.get('from_case') in deps, 'invalid starting checkpoint dependency')
        require(start.get('checkpoint_fields') and all(f in REFS for f in start['checkpoint_fields']), 'invalid checkpoint fields')
        for name, ref in c.get('input_bindings',{}).items():
            require(re.fullmatch('[a-z_]+',name) and ref == 'current.'+name, 'invalid input binding')
        overrides=c.get('variant_predecessors',{})
        require(isinstance(overrides,dict) and all(k in {v['id'] for v in campaign.variants(c)} and dep in deps for k,dep in overrides.items()), 'invalid variant predecessor')
        trigger = c.get('interruption_trigger')
        if trigger:
            require(trigger.get('protocol') in PROTOCOLS and isinstance(trigger.get('observe'),str) and trigger['observe'] and trigger.get('fresh_context') is True, 'invalid actual interruption trigger')
            protocols.add(trigger['protocol'])
            continuation = asset(root,trigger.get('continuation_input'),'cases/consumer/')
            require(not LEAK.search(continuation.read_text()), 'continuation leakage')
            asset(root,trigger.get('guide'),'cases/assessor/')
    visiting, visited = set(), set()
    def visit(identifier):
        require(identifier not in visiting, 'dependency cycle')
        if identifier in visited: return
        visiting.add(identifier)
        for dep in by_id[identifier]['dependencies']: visit(dep)
        visiting.remove(identifier); visited.add(identifier)
    for identifier in by_id: visit(identifier)
    for c in cases:
        for dep in c['dependencies']:
            require(any(v['requirement']=='required' for v in campaign.variants(by_id[dep])), 'optional prerequisite gates required work')
    require(all(by_id[d]['order'] < c['order'] for c in cases for d in c['dependencies']), 'prerequisite order invalid')
    require(protocols == PROTOCOLS, 'missing intended protocol')
    require(by_id['A-008'].get('focused_probe')=='dependency-inflation' and all(by_id[c].get('focused_probe')=='retired-task-selection' for c in ['A-012','A-013']), 'missing focused probe')
    require(not LEAK.search(asset(root,'cases/consumer/preparation.md','cases/consumer/').read_text()), 'preparation leakage')
    asset(root,'cases/consumer/uncontrolled-continuation.md','cases/consumer/')
    return by_id


def render(case_id, bindings, root=BUNDLE, bindings_root=None, variant=None):
    cases = validate_catalog(root)
    require(case_id in cases, 'unknown selected case')
    core.no_secret(bindings)
    require(isinstance(bindings,dict) and set(bindings)=={'checkpoints','current'}, 'invalid handoff bindings')
    current = bindings['current']
    require(isinstance(current,dict) and isinstance(current.get('summary'),str) and current['summary'].strip(), 'missing actual current-state summary')
    require(not LEAK.search(current['summary']), 'current-state assessor leakage')
    checkpoints = bindings['checkpoints']
    require(isinstance(checkpoints,list) and all(isinstance(c,dict) for c in checkpoints), 'invalid checkpoints')
    require(len({c.get('case_id') for c in checkpoints}) == len(checkpoints), 'ambiguous predecessor checkpoints')
    c = cases[case_id]
    if variant is not None:
        require(variant in {v['id'] for v in campaign.variants(c)}, 'unknown selected variant')
    source = c.get('variant_predecessors',{}).get(variant,c['checkpoint_bindings']['start']['from_case'])
    if source is not None:
        matches = [p for p in checkpoints if p.get('case_id') == source]
        require(len(matches)==1, 'missing/ambiguous selected predecessor')
        p = matches[0]
        require(p.get('status')=='Passed', 'predecessor not independently passed')
        require(bindings_root is not None, 'assessment base required')
        assessment = Path(bindings_root)/p.get('assessment_path','')
        require(assessment.is_file(), 'missing independent assessment evidence')
        graded = core.load(assessment)
        require(graded.get('case_id')==source and graded.get('status')=='Passed' and graded.get('agent_behavior_assessed') is True, 'deterministic result is not independent assessment')
        refs = p.get('checkpoint_refs',{})
        require(graded.get('checkpoint_refs')==refs, 'assessment checkpoint mismatch')
        for field in c['checkpoint_bindings']['start']['checkpoint_fields']:
            if field=='merge_parents':
                require(isinstance(refs.get(field),list) and len(refs[field])==2 and all(re.fullmatch('[a-f0-9]{40}',str(x)) for x in refs[field]), 'missing actual two-parent integration')
                continue
            require(isinstance(refs.get(field),str) and refs[field], 'missing predecessor ref')
            if field.endswith('commit'): require(bool(re.fullmatch('[a-f0-9]{40}',refs[field])), 'invalid actual commit')
        repository = p.get('local_checkout')
        require(isinstance(repository,str) and Path(repository).is_dir(), 'actual prerequisite checkout unavailable')
        remote, remote_ref = p.get('remote'), p.get('remote_ref')
        require(isinstance(remote,str) and remote and not remote.startswith('-') and isinstance(remote_ref,str) and remote_ref.startswith('refs/heads/'), 'missing actual destination')
        live = core.remote_read(repository,remote)
        tip = live['refs'].get(remote_ref)
        require(live['status']=='observed' and tip, 'destination readback unavailable')
        object_exists = core.git(repository,'cat-file','-e',refs['product_commit']+'^{commit}',required=False)
        containment = core.git(repository,'merge-base','--is-ancestor',refs['product_commit'],tip,required=False)
        require(object_exists.returncode==0 and containment.returncode==0, 'checkpoint not retained/published at exact destination')
        evidence = p.get('evidence_publication',{})
        require(evidence.get('status')=='published' and re.fullmatch('[a-f0-9]{40}',str(evidence.get('commit',''))) and isinstance(evidence.get('path'),str) and evidence['path'], 'missing published assessment provenance')
        evremote, evref = evidence.get('remote'), evidence.get('ref')
        require(isinstance(evremote,str) and evremote and not evremote.startswith('-') and isinstance(evref,str) and evref.startswith('refs/heads/'), 'missing evidence destination')
        evlive = core.remote_read(repository,evremote)
        evtip = evlive['refs'].get(evref)
        require(evlive['status']=='observed' and evtip and core.git(repository,'merge-base','--is-ancestor',evidence['commit'],evtip,required=False).returncode==0, 'assessment evidence publication unverified')
        published = core.git(repository,'show',evidence['commit']+':'+evidence['path'],required=False)
        require(published.returncode==0 and json.loads(published.stdout)==graded, 'published assessment differs')
    text = asset(Path(root),c['consumer_input'],'cases/consumer/').read_text()
    for name in c.get('input_bindings',{}):
        require(name in current and isinstance(current[name],str) and current[name].strip(), 'missing selected input value')
        require(not LEAK.search(current[name]), 'input assessor leakage')
        text = text.replace('{{'+name+'}}',current[name])
    require(not re.search(r'{{[^}]+}}',text), 'unresolved input value')
    return text+'\n## Actual product current state and authorization\n\n'+current['summary'].strip()+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['validate','render'])
    parser.add_argument('--case'); parser.add_argument('--variant'); parser.add_argument('--bindings',type=Path); parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        if args.command=='validate':
            cases=validate_catalog(); print(json.dumps({'schema_version':1,'catalog_cases':len(cases),'kind':'static asset validation','live_acceptance':False})); return 0
        require(args.case and args.bindings and args.output, 'render arguments required')
        text=render(args.case,core.load(args.bindings),bindings_root=args.bindings.parent,variant=args.variant)
        require(not args.output.exists() and not args.output.is_symlink(), 'output occupied')
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x') as stream: stream.write(text)
        print(json.dumps({'schema_version':1,'case_id':args.case,'rendered':True,'live_acceptance':False})); return 0
    except (ValueError, OSError, core.Stop, TypeError, KeyError) as error:
        print(json.dumps({'schema_version':1,'error':'invalid catalog or handoff','detail':error.cause if isinstance(error,core.Stop) else str(error)})); return 2

if __name__=='__main__': sys.exit(main())
