"""Variant selection and coverage accounting for independently assessed campaigns.

Controlled helper evidence and unavailable optional facilities never supply an
independent pass. Legacy case grades remain visible without retrospective split.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

STATUSES = {'Passed', 'Failed', 'Blocked', 'Not run', 'Pending', 'Running'}
CLASSES = {'consumer', 'controlled', 'live-provider', 'native', 'inspection'}


def variants(case):
    """Return validated variants; an unextended historical case has required core."""
    rows=case.get('variants',[{'id':'core','requirement':'required','evidence_class':'consumer','facilities':[]}])
    if not isinstance(rows,list) or not rows:raise ValueError('empty variants')
    seen=set()
    for row in rows:
        if not isinstance(row,dict) or set(row)!={'id','requirement','evidence_class','facilities'}:raise ValueError('variant fields')
        if not isinstance(row['id'],str) or not re.fullmatch('[a-z][a-z0-9-]*',row['id']) or row['id'] in seen:raise ValueError('duplicate/invalid variant')
        seen.add(row['id'])
        if row['requirement'] not in {'required','optional'} or row['evidence_class'] not in CLASSES:raise ValueError('variant classification')
        if not isinstance(row['facilities'],list) or any(not isinstance(x,str) or not x for x in row['facilities']) or len(row['facilities'])!=len(set(row['facilities'])):raise ValueError('variant facilities')
    return rows


def select(cases, selection=None):
    """Select required variants by default; optional variants require explicit names.

    An explicit mapping bounds both case and variant scope. Unknown or empty
    selections are errors; callers filter phase/case scope before this function.
    """
    if selection is not None:
        if not isinstance(selection,dict) or not selection:raise ValueError('empty selection')
        if any(k not in cases for k in selection):raise ValueError('unknown selected case')
    rows=[]
    for identifier,case in cases.items():
        available=variants(case)
        if selection is not None:
            if identifier not in selection:continue
            names=selection[identifier]
            if not isinstance(names,list) or not names or len(names)!=len(set(names)) or any(n not in {v['id'] for v in available} for n in names):raise ValueError('unknown/duplicate selected variant')
            available=[v for v in available if v['id'] in names]
        rows.extend(dict(v,case_id=identifier,id=identifier+'.'+v['id']) for v in available if selection is not None or v['requirement']=='required')
    return rows


def coverage(cases, results, selection=None):
    """Summarize selected grades, retaining unavailable optional coverage separately.

    Missing required evidence is Blocked. Missing optional evidence is Not run.
    Passed requires independent assessment and the declared evidence class;
    legacy unsplit case grades are retained rather than promoted to variant passes.
    """
    if not isinstance(results,dict):raise ValueError('invalid results')
    # Reporting the default scope also lists unselected optional extensions as
    # Not run so users see their facilities, without making them readiness gates.
    rows=select(cases,selection)
    if selection is None:
        rows.extend(dict(v,case_id=k,id=k+'.'+v['id']) for k,c in cases.items() for v in variants(c) if v['requirement']=='optional')
    known={k+'.'+v['id'] for k,c in cases.items() for v in variants(c)}
    if any(k not in known and k not in cases for k in results):raise ValueError('unknown result')
    counts={'required':Counter(),'optional':Counter()};details=[];unexecuted=[]
    for row in rows:
        actual=results.get(row['id']);status=(actual or {}).get('status','Blocked' if row['requirement']=='required' else 'Not run')
        if status not in STATUSES:raise ValueError('invalid result status')
        reason=(actual or {}).get('reason','No independent variant evidence supplied')
        if status=='Passed' and (actual.get('agent_behavior_assessed') is not True or actual.get('evidence_class')!=row['evidence_class']):status='Blocked';reason='Independent grade/evidence class missing or incompatible'
        counts[row['requirement']][status]+=1
        detail=dict(row,status=status,reason=reason);details.append(detail)
        if status in {'Blocked','Not run','Pending','Running'}:unexecuted.append(detail)
    return {'schema_version':1,'required':dict(counts['required']),'optional':dict(counts['optional']),'required_ready':bool(counts['required']) and set(counts['required'])=={'Passed'},'variants':details,'unexecuted':unexecuted,'legacy':{k:v for k,v in results.items() if k in cases},'runtime_acceptance_from_support_checks':False}


def main():
    """Render coverage from explicit catalog/results JSON without mutating a run."""
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--catalog',type=Path,required=True);parser.add_argument('--results',type=Path,required=True);parser.add_argument('--selection',type=Path)
    args=parser.parse_args()
    try:
        value=json.loads(args.catalog.read_text());cases={c['id']:c for c in value['cases']}
        result=coverage(cases,json.loads(args.results.read_text()),json.loads(args.selection.read_text()) if args.selection else None)
        print(json.dumps(result,indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError) as error:print(json.dumps({'error':str(error)}));return 2


if __name__=='__main__':raise SystemExit(main())
