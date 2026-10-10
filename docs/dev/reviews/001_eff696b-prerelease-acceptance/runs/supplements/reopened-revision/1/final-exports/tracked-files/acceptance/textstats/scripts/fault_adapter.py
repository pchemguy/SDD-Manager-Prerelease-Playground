"""Controlled access faults and durable effects, explicitly not a live provider.

A write can apply before its success response is suppressed; independent read
exposes the real fixture effect. Duplicate writes are refused rather than hidden.
No credential material, network service or scripted consumer recovery is used.
"""
import argparse
import json
from pathlib import Path
import re
import sys

sys.path.insert(0,str(Path(__file__).parent))
import core

MODES={'normal','before-send-unavailable','after-send-loss','denial','rate-limit','unavailable-access'}


def operation(root, identity, action, payload=None, mode='normal'):
    """Perform one caller-selected read/write against an isolated durable ledger.

    The caller selects restoration by using normal mode, then a fresh consumer
    decides whether to read/retry. This function never performs that recovery.
    Returned metadata always marks controlled evidence without agent acceptance.
    """
    root=Path(root).resolve()
    if not isinstance(identity,str) or not re.fullmatch('[a-zA-Z0-9][a-zA-Z0-9_-]*',identity):raise ValueError('invalid fixture identity')
    if action not in {'read','write'} or mode not in MODES:raise ValueError('invalid fixture operation/mode')
    if mode=='after-send-loss' and action!='write':raise ValueError('response-loss requires actual write')
    if action=='write' and not isinstance(payload,dict):raise ValueError('object payload required')
    core.no_secret(payload)
    path=root/(identity+'.json')
    if path.is_symlink():raise ValueError('symlink fixture object')
    result={'schema_version':1,'identity':identity,'evidence_class':'controlled','agent_behavior_assessed':False}
    faults={'denial':('Denied',403),'rate-limit':('Rate limited',429),'unavailable-access':('Unavailable',None),'before-send-unavailable':('Unavailable',None)}
    if mode in faults:
        status,http=faults[mode];result.update(status=status,http_status=http)
        if mode=='rate-limit':result['retry_after']=1
        return result
    if action=='read':return dict(result,status='Observed',http_status=200,object=core.load(path) if path.exists() else None)
    root.mkdir(parents=True,exist_ok=True)
    try:
        with path.open('x') as stream:json.dump(payload,stream,sort_keys=True);stream.write('\n')
    except FileExistsError:return dict(result,status='Duplicate refused',http_status=409)
    if mode=='after-send-loss':return dict(result,status='Uncertain',http_status=None,reason='Success response discarded after applied fixture write; read exact identity before retry')
    return dict(result,status='Applied',http_status=201,object=payload)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,required=True);parser.add_argument('--identity',required=True);parser.add_argument('--action',choices=['read','write'],required=True);parser.add_argument('--mode',choices=sorted(MODES),default='normal');parser.add_argument('--payload',type=Path);args=parser.parse_args()
    try:
        result=operation(args.root,args.identity,args.action,core.load(args.payload) if args.payload else None,args.mode);print(json.dumps(result));return 0 if result['status'] in {'Observed','Applied'} else 2
    except (ValueError,OSError,core.Stop) as error:print(json.dumps({'status':'Unavailable','cause':str(error),'evidence_class':'controlled'}));return 2


if __name__=='__main__':raise SystemExit(main())
