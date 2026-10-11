import importlib.util,re,os,sys,hashlib
from pathlib import Path
spec=importlib.util.spec_from_file_location("capture","/workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
root=Path(m.root);trace="/workspace/scratch/46b31bb4dff6/037-a013-consumer-trace-immutable.py"
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
     if expected==0 and "textstats" in line and "--help" not in line:
      outputs = {
       "python -m textstats sample.txt":(3,5),
       "python -m textstats bom.txt":(0,0),
       "python -m textstats --keep-bom bom.txt":(1,1),
       "python -m textstats -- -sample":(1,2),
       "python -m textstats --lines 2:3 sample.txt":(2,3),
       "python -m textstats sample.txt --lines=0002:0099":(2,3),
       "python -m textstats --lines 2:2 range.txt":(1,0),
       "python -m textstats range.txt --keep-bom --lines=2:2":(1,0),
       "python -m textstats --lines 2:99 range.txt":(3,3),
       "python -m textstats --keep-bom --lines 3:3 range.txt":(1,1),
       "python -m textstats range.txt --lines 99:100":(0,0),
      }
      if line in outputs:
       n,w=outputs[line];assert p.stdout==f"lines={n} words={w}\n".encode() and not p.stderr
      elif line.startswith("printf"):
       n,w = ((0,0) if "printf ''" in line else (2,3) if "2:99" in line else (1,1) if "--keep-bom" in line or "2:2" in line else (3,5))
       assert p.stdout==f"lines={n} words={w}\n".encode() and not p.stderr
 print(f"{count} actual final README/API fences executed; all command outcomes verified")
finally:
 for p in fixtures:
  if p.exists():p.unlink()
