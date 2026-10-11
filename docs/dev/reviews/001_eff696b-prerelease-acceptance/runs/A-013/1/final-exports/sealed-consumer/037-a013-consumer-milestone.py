import importlib.util,sys,json
from pathlib import Path
spec=importlib.util.spec_from_file_location("api","/workspace/scratch/46b31bb4dff6/037-a013-consumer-api.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
num=int(sys.argv[1])
expected={5:("sdd-2.2-UTF-8-stdin-and-final-delivery",{14:"T-013",15:"T-014",16:"T-015",17:"T-016"}),6:("sdd-2.3-Phase-2-and-final-review",{18:"T-017"})}
title,owners=expected[num]
before=m.api(f"/milestones/{num}")
assert before["number"]==num and before["title"]==title
issues=m.api(f"/issues?milestone={num}&state=all&per_page=100")
ledger=json.loads(Path("/workspace/scratch/46b31bb4dff6/037-a013-consumer-observations.json").read_text())
assert not any(k.lower()=="link" for k in ledger["provider"][-1]["headers"]),"Unexhausted pagination"
assert len(issues)<100 and all("pull_request" not in i for i in issues)
assert {i["number"] for i in issues}==set(owners), "Unexpected association set"
for issue in issues:
 tid=owners[issue["number"]]
 assert issue["title"].startswith("["+tid+"] ") and f"sdd-forge:task-id={tid}" in issue["body"]
 assert issue["milestone"]["number"]==num
 assert issue["state"]=="closed" and issue["state_reason"]=="completed"
 assert "sdd-phase-2-Ranges-and-stdin" in [label["name"] for label in issue["labels"]]
assert before["open_issues"]==0 and before["closed_issues"]==len(issues)
if before["state"]!="closed":m.api(f"/milestones/{num}","PATCH",{"state":"closed"})
after=m.api(f"/milestones/{num}")
assert after["state"]=="closed" and after["open_issues"]==0
for k,v in before.items():
 if k not in {"state","closed_at","updated_at"}:assert after[k]==v,k
print("native milestone",num,"closed/readback; all-state associations",sorted(owners),"all closed/completed; all remaining fields preserved")
