import importlib.util,sys,time
from pathlib import Path
spec=importlib.util.spec_from_file_location("api","/workspace/scratch/46b31bb4dff6/037-a013-consumer-api.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);api=m.api
tid,num,milestone,sha,checks=sys.argv[1:];num=int(num);milestone=int(milestone)
issue=api(f"/issues/{num}");assert "pull_request" not in issue;assert issue["title"].startswith("["+tid+"] ");assert f"sdd-forge:task-id={tid}" in issue["body"];assert issue["milestone"]["number"]==milestone;assert "sdd-phase-2-Ranges-and-stdin" in [l["name"] for l in issue["labels"]]
preserved={k:issue[k] for k in ["title","body","labels","milestone","assignees"]}
comments=api(f"/issues/{num}/comments?per_page=100");body=f"{tid} verified on phase/2-json-and-stdin at published commit {sha}. {checks} Owning result, evidence and initial completion checkbox are atomic; exact origin branch readback verified. Target integration remains separate."
if not any(sha in c["body"] and tid in c["body"] for c in comments):
 time.sleep(1);created=api(f"/issues/{num}/comments","POST",{"body":body});read=api(f"/issues/comments/{created['id']}");assert read["body"]==body
if issue["state"]!="closed":
 time.sleep(1);api(f"/issues/{num}","PATCH",{"state":"closed","state_reason":"completed"})
read=api(f"/issues/{num}");assert read["state"]=="closed" and read["state_reason"]=="completed"
for k,v in preserved.items():
 if k=="milestone": assert read[k]["number"]==v["number"]
 else: assert read[k]==v,k
print(tid,num,"closed/completed; exact comment readback and native fields preserved",sha)
