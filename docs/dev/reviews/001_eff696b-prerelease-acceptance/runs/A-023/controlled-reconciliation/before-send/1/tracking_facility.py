import sys,json
from pathlib import Path
from fault_adapter import operation
import argparse
p=argparse.ArgumentParser();p.add_argument('--action',choices=['read','write'],required=True);p.add_argument('--identity',required=True);p.add_argument('--payload',type=Path);a=p.parse_args()
b=Path(__file__).parent;mode=json.loads((b/'CONTROL.json').read_text())[a.action];payload=json.loads(a.payload.read_text()) if a.payload else None
r=operation(b/'ledger',a.identity,a.action,payload,mode);print(json.dumps(r));raise SystemExit(0 if r['status'] in {'Observed','Applied'} else 2)
