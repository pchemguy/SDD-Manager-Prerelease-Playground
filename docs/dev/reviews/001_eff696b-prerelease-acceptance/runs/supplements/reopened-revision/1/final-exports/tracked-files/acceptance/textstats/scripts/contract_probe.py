"""Literal API probe and explicit isolated count-regression fixture.

The fixture changes only a caller-authorized disposable product checkout. Its
failure is test setup, never evidence that the unmodified plugin/product failed.
"""
import argparse
import contextlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

sys.path.insert(0,str(Path(__file__).parent))
import core


def child(root):
    """Run two independent literal requirements against the actual imported API."""
    root=Path(root).resolve();output=io.StringIO()
    try:
        sys.path.insert(0,str(root))
        with contextlib.redirect_stdout(output),contextlib.redirect_stderr(output):
            import textstats as product
        if not Path(product.__file__).resolve().is_relative_to(root):raise ValueError('outside import origin')
        class Counts(unittest.TestCase):
            def test_crlf_and_final_segment(self):
                value=product.count_text('one two\r\nthree');self.assertEqual((value.lines,value.words),(2,3))
            def test_bom_empty_and_trailing_line(self):
                value=product.count_text('\ufeffa\n');self.assertEqual((value.lines,value.words),(1,1))
                value=product.count_text('');self.assertEqual((value.lines,value.words),(0,0))
        with contextlib.redirect_stdout(output),contextlib.redirect_stderr(output):
            result=unittest.TextTestRunner(stream=output).run(unittest.defaultTestLoader.loadTestsFromTestCase(Counts))
        status='Unavailable' if result.errors else 'Failed' if result.failures else 'Passed'
        return {'status':status,'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'import_origin':str(product.__file__),'diagnostic':output.getvalue(),'agent_behavior_assessed':False}
    except (Exception,SystemExit) as error:
        return {'status':'Unavailable','tests':0,'failures':0,'errors':1,'cause':type(error).__name__,'diagnostic':output.getvalue(),'agent_behavior_assessed':False}


def probe(root):
    """Launch a fresh interpreter and retain actual counts, errors and channels."""
    proc=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--child',str(Path(root).resolve())],capture_output=True,timeout=30)
    raw=core.clean_bytes(proc.stdout);core.clean_bytes(proc.stderr)
    try:value=json.loads(raw)
    except ValueError:value={'status':'Unavailable','tests':0,'errors':1,'failures':0,'cause':'invalid child observation'}
    value['child_returncode']=proc.returncode;return value


def inject(root, expected_head):
    """Introduce a disclosed off-by-one count fault in an explicitly isolated copy.

    This injector supports a module-level count_text in textstats/core.py whose
    public export delegates to that implementation. Other valid public layouts
    use an equivalently documented, caller-authorized regression fixture instead.
    The layout-independent public probe remains their baseline acceptance check.

    The clean starting Git identity must match the caller's independently pinned
    baseline. A repeat injection, missing count function or escaping path fails.
    The coordinator records this fixture change and actual failed probe separately
    before dispatch; it does not fabricate consumer repair or task completion.
    """
    root=Path(root).resolve()
    if not re.fullmatch('[0-9a-f]{40}',expected_head) or core.git(root,'rev-parse','HEAD').stdout.strip()!=expected_head:raise ValueError('fixture baseline identity mismatch')
    path=core.relative(root,'textstats/core.py')
    if path.is_symlink() or not path.is_file():raise ValueError('fixture count implementation unavailable')
    source=path.read_text()
    if '_fixture_original_count_text' in source or not re.search(r'^def count_text\(',source,re.M):raise ValueError('repeat/unsupported fixture')
    if core.git(root,'diff','--quiet','HEAD','--','textstats/core.py',required=False).returncode:raise ValueError('unrelated count edits')
    changed=re.sub(r'^def count_text\(', 'def _fixture_original_count_text(',source,count=1,flags=re.M)
    changed+='\n\ndef count_text(*args, **kwargs):\n    """Disclosed isolated fixture: deliberate line-count regression."""\n    stats = _fixture_original_count_text(*args, **kwargs)\n    return type(stats)(lines=stats.lines + 1, words=stats.words)\n'
    path.write_text(changed);return {'path':'textstats/core.py','baseline':expected_head,'fixture':'disclosed line-count off-by-one','agent_behavior_assessed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path);parser.add_argument('--child',type=Path);parser.add_argument('--inject-isolated',action='store_true');parser.add_argument('--expected-head');args=parser.parse_args()
    if args.child:
        value=child(args.child)
        try:core.no_secret(value)
        except core.Stop:value={'status':'Unavailable','cause':'Sensitive diagnostic withheld','tests':0,'errors':1,'failures':0}
        print(json.dumps(value));return 0
    if not args.root:parser.error('--root required')
    try:
        if args.inject_isolated:
            if not args.expected_head:raise ValueError('explicit isolated baseline required')
            print(json.dumps(inject(args.root,args.expected_head)));return 0
        value=probe(args.root);print(json.dumps(value,indent=2));return 0 if value['status']=='Passed' else 1 if value['status']=='Failed' else 2
    except (OSError,ValueError,core.Stop,subprocess.TimeoutExpired) as error:print(json.dumps({'status':'Unavailable','cause':str(error)}));return 2


if __name__=='__main__':raise SystemExit(main())
