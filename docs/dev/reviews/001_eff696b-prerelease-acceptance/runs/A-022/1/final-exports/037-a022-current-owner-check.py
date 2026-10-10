import contextlib,io,itertools,json,pathlib,subprocess,sys,unittest.mock
from textstats import cli
missing='/workspace/scratch/46b31bb4dff6/037-a022-nonexistent-input.txt'
assert not pathlib.Path(missing).exists()
rows=[]
for equals,keep,jsonmode in itertools.product((False,True),repeat=3):
    argv=([ '--lines=²:³'] if equals else ['--lines','²:³'])+(['--keep-bom'] if keep else [])+(['--json'] if jsonmode else [])+[missing]
    command=[sys.executable,'-B','-m','textstats']+argv
    r=subprocess.run(command,capture_output=True,text=True)
    row={'command':command,'stdout':r.stdout,'stderr':r.stderr,'exit_code':r.returncode}
    out,err=io.StringIO(),io.StringIO()
    with unittest.mock.patch.object(cli,'_read_file_text') as read, unittest.mock.patch.object(cli,'count_file') as count, contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        status=cli.main(argv)
    row['seam']={'argv':argv,'status':status,'stdout':out.getvalue(),'stderr':err.getvalue(),'read_file_calls':read.call_count,'count_file_calls':count.call_count}
    row['passed']=r.returncode==2 and r.stdout=='' and 'positive ASCII decimal START:END' in r.stderr and 'Traceback' not in r.stderr and status==2 and out.getvalue()=='' and 'positive ASCII decimal START:END' in err.getvalue() and 'Traceback' not in err.getvalue() and read.call_count==count.call_count==0
    rows.append(row)
p=pathlib.Path('/workspace/scratch/46b31bb4dff6/037-a022-specimen-results.json');p.write_text(json.dumps({'runtime':sys.version,'specimen':'U+00B2:U+00B3 (²:³)','rows':rows},indent=2,ensure_ascii=False))
print(p.read_text())
assert all(row['passed'] for row in rows)
print('PASS: 8 actual module cases and 8 controlled acquisition cases')