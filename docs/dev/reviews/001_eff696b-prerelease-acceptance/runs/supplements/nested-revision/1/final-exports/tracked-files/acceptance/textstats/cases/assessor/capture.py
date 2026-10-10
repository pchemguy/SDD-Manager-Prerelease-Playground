#!/usr/bin/env python3
"""Observe actual TextStats output; literal expectations are never loaded here."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'scripts'))
import core

API_WORKER=r'''
import contextlib, io, json, pathlib, sys
import textstats
vectors=json.load(sys.stdin)
rows=[]
for v in vectors:
    out,err=io.StringIO(),io.StringIO(); result=None; exception=None
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            if v['operation']=='text': s=textstats.count_text(v['text'],strip_bom=v['strip_bom'])
            else:
                path=pathlib.Path(v['name']+'.txt')
                if v['operation']=='file': path.write_bytes(bytes.fromhex(v['hex']))
                s=textstats.count_file(path,strip_bom=v['strip_bom'])
            result=[s.lines,s.words]
        except Exception as error:
            exception='OSError' if isinstance(error,OSError) else type(error).__name__
    rows.append(dict(name=v['name'],result=result,stdout=out.getvalue(),stderr=err.getvalue(),exception=exception))
immutable=False
try:
    value=textstats.TextStats(1,2); value.lines=9
except (AttributeError,TypeError): immutable=True
print(json.dumps(dict(rows=rows,immutable=immutable,origin=str(pathlib.Path(textstats.__file__).resolve()))))
'''


def channels(entry,stdout,stderr):
    # Validate both channels before retaining either, including partial timeout bytes.
    stdout=stdout or b''; stderr=stderr or b''
    if isinstance(stdout,str): stdout=stdout.encode('utf-8')
    if isinstance(stderr,str): stderr=stderr.encode('utf-8')
    try:
        core.clean_bytes(stdout); core.clean_bytes(stderr)
    except core.Stop:
        entry['channels']='Withheld: sensitive content'
        raise
    entry.update(stdout_base64=base64.b64encode(stdout).decode(),stderr_base64=base64.b64encode(stderr).decode(),stdout=stdout.decode('utf-8',errors='replace'),stderr=stderr.decode('utf-8',errors='replace'))


def invoke(command, cwd, env, data, journal, runner=subprocess.run):
    entry={'command':command,'cwd':str(cwd),'environment':{'PYTHONPATH':env.get('PYTHONPATH'),'PYTHONUTF8':env.get('PYTHONUTF8'),'LC_ALL':env.get('LC_ALL')},'status':'Not completed','returncode':None}
    core.no_secret(entry)
    journal.append(entry)
    try:
        proc=runner(command,cwd=cwd,env=env,input=data,capture_output=True,timeout=30)
    except subprocess.TimeoutExpired as error:
        entry.update(status='Timed out',timeout_seconds=error.timeout)
        channels(entry,error.stdout,error.stderr)
        raise
    except OSError as error:
        entry.update(status='Not started',launch_error=type(error).__name__)
        raise
    entry.update(status='Completed',returncode=proc.returncode)
    channels(entry,proc.stdout,proc.stderr)
    return proc


def cli_observation(v, proc, before, after, filename):
    stdout=proc.stdout.decode('utf-8',errors='replace'); stderr=proc.stderr.decode('utf-8',errors='replace')
    row={'name':v['name'],'returncode':proc.returncode,'unchanged':before==after}
    if v['error']:
        row.update(stdout=stdout,stderr_nonempty=bool(stderr.strip()),no_traceback='Traceback (most recent call last)' not in stderr)
        if v.get('source_identification'):
            row['source_identified']=('stdin' in stderr.lower() or 'standard input' in stderr.lower()) if v['stdin'] else filename in stderr
    elif v['json']:
        try: row['json']=json.loads(stdout)
        except ValueError: row['json']={'invalid_output':stdout}
        row.update(stderr=stderr,single_object_newline=stdout.endswith('\n') and isinstance(row['json'],dict))
    else: row.update(stdout=stdout,stderr=stderr)
    return row


def _capture(root,suite,python,runner,journal):
    root=Path(root).resolve()
    if not root.is_dir(): raise ValueError('product import root unavailable')
    vectors=core.load(HERE/'inputs.json')['suites'][suite]
    env=dict(os.environ,PYTHONPATH=str(root),PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='0',LC_ALL='C')
    with tempfile.TemporaryDirectory(prefix='textstats-observation-') as temp:
        cwd=Path(temp)
        origin=invoke([python,'-c','import pathlib,textstats; print(pathlib.Path(textstats.__file__).resolve())'],cwd,env,b'',journal,runner)
        actual=origin.stdout.decode(errors='replace').strip()
        journal[-1]['origin_accepted']=origin.returncode==0 and Path(actual).is_absolute() and Path(actual).is_relative_to(root)
        if not journal[-1]['origin_accepted']: raise ValueError('actual import origin rejected')
        if suite=='api':
            proc=invoke([python,'-c',API_WORKER],cwd,env,json.dumps(vectors).encode(),journal,runner)
            try:
                body=json.loads(proc.stdout)
                actual={'returncode':proc.returncode,'stdout_rows':body['rows'],'stderr':proc.stderr.decode(errors='replace'),'immutable':body['immutable']}
            except (ValueError,KeyError,TypeError): actual={'returncode':proc.returncode,'invalid_api_output':proc.stdout.decode(errors='replace'),'stderr':proc.stderr.decode(errors='replace')}
        else:
            actual=[]
            for v in vectors:
                # Stable non-secret local fixture filenames, including dash-prefixed/literal option names.
                filename='--json' if v['name']=='literal-json-filename' else '-input.txt' if v['name']=='dash-filename' else v['name']+'.txt'
                path=cwd/filename; data=bytes.fromhex(v['hex'])
                if not v.get('missing') and not v['stdin']: path.write_bytes(data)
                before=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
                args=[filename if a=='{input}' else a for a in v['args']]
                proc=invoke([python,'-m','textstats',*args],cwd,env,data if v['stdin'] else b'',journal,runner)
                after=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
                journal[-1]['fixture']={'name':filename,'input_sha256':hashlib.sha256(data).hexdigest(),'before_sha256':before,'after_sha256':after,'stdin':v['stdin']}
                actual.append(cli_observation(v,proc,before,after,filename))
    evidence={'schema_version':1,'literals':{suite:actual}}
    return evidence


def capture(root,suite,python=sys.executable,runner=subprocess.run,provenance=None):
    provenance={} if provenance is None else provenance
    provenance.update(schema_version=1,suite=suite,product_import_root=str(Path(root).resolve()),commands=[],status='Running',kind='actual output capture; not agent lifecycle assessment')
    core.no_secret(provenance)
    try:
        evidence=_capture(root,suite,python,runner,provenance['commands'])
    except (ValueError,OSError,KeyError,core.Stop,subprocess.TimeoutExpired) as error:
        provenance['status']='Failed'
        provenance['failure']={'cause':error.cause if isinstance(error,core.Stop) else 'timeout' if isinstance(error,subprocess.TimeoutExpired) else 'launch_failure' if isinstance(error,OSError) else 'capture_or_import_unavailable'}
        raise
    provenance['status']='Captured'
    return evidence,provenance


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--product-root',type=Path,required=True); parser.add_argument('--suite',choices=['api','baseline','json','ranges','ranges-json','removal','stdin','distribution'],required=True)
    parser.add_argument('--python',default=sys.executable); parser.add_argument('--output',type=Path,required=True); parser.add_argument('--provenance',type=Path,required=True)
    args=parser.parse_args()
    provenance={}
    outputs_available=False
    try:
        if args.output==args.provenance or any(p.exists() or p.is_symlink() for p in [args.output,args.provenance]): raise ValueError('output occupied')
        outputs_available=True
        evidence,provenance=capture(args.product_root,args.suite,args.python,provenance=provenance)
        core.write_new(args.provenance,provenance); core.write_new(args.output,evidence)
        return 0
    except (ValueError,OSError,KeyError,core.Stop,subprocess.TimeoutExpired):
        retained=False
        if outputs_available and provenance.get('status')=='Failed':
            try:
                core.write_new(args.provenance,provenance)
                retained=True
            except (OSError,core.Stop): pass
        print(json.dumps({'schema_version':1,'error':'actual capture unavailable','failed_provenance_retained':retained})); return 2

if __name__=='__main__': sys.exit(main())
