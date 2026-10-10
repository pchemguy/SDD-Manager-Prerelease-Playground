import hashlib, importlib.util, json, sys, time, urllib.request, urllib.error
from pathlib import Path

sp = importlib.util.spec_from_file_location("capture", "/workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py")
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
base = "https://api.github.com/repos/pchemguy/SDD-Manager-Prerelease-Playground"
baseline = Path("/workspace/scratch/46b31bb4dff6/037-a013-consumer-late-foreign-baseline.json")
records = []
for endpoint in ["/issues/2", "/issues/2/comments?per_page=100", "/milestones/1", "/labels?per_page=100"]:
    token = Path("/workspace/scratch/46b31bb4dff6/SDD-Manager-Prerelease-Playground/gh.tkn").read_text().strip()
    request = urllib.request.Request(base + endpoint, headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(request) as response:
            raw = response.read()
            status = response.status
            headers = dict(response.headers)
    except urllib.error.HTTPError as response:
        raw = response.read()
        status = response.code
        headers = dict(response.headers)
    safe = {k: v for k, v in headers.items() if k.lower() in {"link", "x-github-request-id", "x-ratelimit-remaining", "x-ratelimit-reset"}}
    record = {"method": "GET", "endpoint": base + endpoint, "status": status, "response_sha256": hashlib.sha256(raw).hexdigest(), "response_bytes": len(raw), "headers": safe, "time": time.time(), "content_retained": False}
    if status != 200:
        m.append("late_foreign_guard", record)
        raise RuntimeError("Guarded provider GET returned status " + str(status))
    result = json.loads(raw)
    if isinstance(result, list):
        assert len(result) < 100 and not any(k.lower() == "link" for k in headers), "Unexhausted pagination"
        result.sort(key=lambda item: item["id"])
        record["ids"] = [item["id"] for item in result]
    else:
        assert result["number"] == (2 if endpoint == "/issues/2" else 1)
        record["id"] = result["id"]
        record["number"] = result["number"]
        record["state"] = result["state"]
    record["semantic_sha256"] = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()
    m.append("late_foreign_guard", record)
    records.append(record)
    del token, result, raw, request
if sys.argv[1] == "baseline":
    assert not baseline.exists(), "Preserve existing baseline"
    baseline.write_text(json.dumps({"scope": "Late pre-T017-closure/integration guard only; does not establish original startup contents", "records": records}, indent=2) + "\n")
elif sys.argv[1] == "compare":
    prior = json.loads(baseline.read_text())["records"]
    assert [(r["endpoint"], r["semantic_sha256"]) for r in records] == [(r["endpoint"], r["semantic_sha256"]) for r in prior]
else:
    raise ValueError("Unknown guard mode")
print(json.dumps({"mode": sys.argv[1], "late_boundary_only": True, "records": records}, indent=2))
