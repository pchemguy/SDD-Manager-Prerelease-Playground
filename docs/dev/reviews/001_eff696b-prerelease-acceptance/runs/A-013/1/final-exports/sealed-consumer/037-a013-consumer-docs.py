import importlib.util,re,os,sys,hashlib
from pathlib import Path
spec=importlib.util.spec_from_file_location("capture","/workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
root=Path(m.root);trace="/workspace/scratch/46b31bb4dff6/037-a013-consumer-trace.py"
fixtures=[root/n for n in ["sample.txt","bom.txt","-sample","range.txt","bad-range.txt"]]
assert not any(p.exists() for p in fixtures),"Do not overwrite existing input"
count=0
try:
 for path in [root/"README.md",root/"docs/public-api.md"]:
  for language,body in re.findall(r"```(bash|python)\n(.*?)```",path.read_text(),re.S):
   count+=1
   if language=="python":
    p=m.run([sys.executable,"-B","-c",body]);assert p.returncode==0 and p.stdout==p.stderr==b"",(path,count,p)
   elif "example_dir=" in body:
    code=body.replace("python ","python -B ")
    p=m.run(["bash","-c",code]);assert (p.returncode,p.stdout,p.stderr)==(0,b"lines=3 words=5\nlines=2 words=3\n",b""),p
   else:
    for line in body.splitlines():
     if not line.strip():continue
     code=line.replace("python ","python -B ")
     if "tools/check_tests.py" in code or "tools/check_distribution.py" in code:
      code=code.replace("python -B tools/","python -B "+trace+" tools/")
     elif "python -B -m unittest" in code:
      code=code.replace("python -B -m unittest","python -B "+trace+" -m unittest")
     expected=2 if any(x in line for x in ["--lines 0:2","--lines 3:2","--lines=1:2 --lines","--lines"] ) and "missing.txt" in line else 0
     if line.strip()=="python -m textstats --lines":expected=2
     if "textstats" in line and ("bad-range.txt" in line or "printf 'ok" in line):expected=1
     p=m.run(["bash","-c",code]);assert p.returncode==expected,(line,p.returncode,p.stderr)
     if expected:assert p.stdout==b"" and p.stderr and b"Traceback" not in p.stderr
 print(f"{count} actual final README/API fences executed; all command outcomes verified")
finally:
 for p in fixtures:
  if p.exists():p.unlink()
