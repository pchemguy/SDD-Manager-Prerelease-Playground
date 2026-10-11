from pathlib import Path
import contextlib, hashlib, importlib.util, io, json, platform, time

sp = importlib.util.spec_from_file_location("capture", "/workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py")
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
prefix = Path("/workspace/scratch/46b31bb4dff6")
source = "c05b65958e2a386cf2ae8782dca3e749ed9b60ff"
target = "fbe8bedf4c6cba1ab29d53d2da05e614603d76d1"
merge = "549a25f4f1bc7702afa0b729fc0894918ec9d16d"
tree = "190b6865846d66933bcdcd112e1fcfa7ca2f04ef"

def git(*args):
    with contextlib.redirect_stdout(io.StringIO()):
        result = m.run(["git", *args])
    assert result.returncode == 0
    return result.stdout.decode()

assert git("rev-parse", "HEAD").strip() == merge
assert git("show", "-s", "--format=%P", merge).strip().split() == [target, source]
assert git("show", "-s", "--format=%T", merge).strip() == tree
assert git("status", "--porcelain=v1") == ""
remote = git("ls-remote", "origin", "refs/heads/main", "refs/heads/phase/2-json-and-stdin")
refs = {line.split()[1]: line.split()[0] for line in remote.splitlines()}
assert refs == {"refs/heads/main": target, "refs/heads/phase/2-json-and-stdin": source}
observations = prefix / "037-a013-consumer-observations.json"
ledger = json.loads(observations.read_text())
late = ledger["late_foreign_guard"]
assert len(late) == 8 and [event["semantic_sha256"] for event in late[:4]] == [event["semantic_sha256"] for event in late[4:]]
records = sorted((prefix / "037-a013-consumer-command-records").glob("*.json"))
digest = hashlib.sha256()
for path in records:
    digest.update(path.name.encode() + b"\0" + hashlib.sha256(path.read_bytes()).digest())

def identity(path):
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size}

seal = {"kind": "A-013 BLOCKED publication checkpoint", "sealed": time.time(), "requested_completed_phase_publication_reached": False, "workflow_blocked": True,
        "local_accepted_merge": merge, "ordered_parents": [target, source], "tree": tree, "clean": True, "remote_refs": refs,
        "working_phase_published": True, "main_merge_published": False, "retry_policy": "No further retry or substitute; explicit platform-recognized user request required",
        "integration_acceptance_reported_by_coordinator": "b187f05e3c78cffcde61a7ce52a97a7197bffdaa", "narrowed_recovery_assessment_reported_by_coordinator": "29e9ff2525d1796ce6befac85f459ccd18299456",
        "rejections": [identity(prefix / "037-a013-consumer-main-push-rejection.json"), identity(prefix / "037-a013-consumer-main-push-narrowed-rejection.json")],
        "push_effect": "Both attempts rejected before Git launch; no command process streams/status or provider write exist",
        "verified_exits": {"runtime": platform.python_version(), "unit": 37, "integration": 34, "real_module_cases": 478, "docs_fences": 12, "merged_python_children_all_explicit_B_env": 1628, "TODO": "None", "broader_runtimes_platforms": "unverified"},
        "accepted_candidate_checks": identity(prefix / "037-a013-consumer-integration-candidate.json"),
        "archive": identity(Path.cwd() / "dist/textstats-source.zip"), "merge_message": identity(prefix / "037-a013-consumer-phase2-merge.txt"),
        "report_artifacts": [identity(Path.cwd() / relative) for relative in ["docs/dev/reports/phases/2/2.2.md", "docs/dev/reports/phases/2/PHASE-REPORT.md", "docs/dev/reports/IMPLEMENTATION-REPORT.md"]],
        "native_closure_chronology": [{"argv": command["argv"], "status": command["status"], "completed": command["time"]} for command in ledger["commands"] if any(str(arg).endswith(("037-a013-consumer-close.py", "037-a013-consumer-milestone.py")) for arg in command["argv"])],
        "late_foreign_guard": {"passed": True, "scope": "Pre-T017 closure/integration through BLOCKED publication checkpoint only; no original-startup inference and no post-main-publication claim", "semantic_hashes": [event["semantic_sha256"] for event in late[4:]]},
        "original_observations": identity(observations), "immutable_children": {"directory": str(prefix / "037-a013-consumer-command-records"), "count": len(records), "aggregate_sha256": digest.hexdigest(), "aggregation": "sorted filename UTF-8 + NUL + exact file SHA256 raw digest"},
        "surviving_race_checkpoint": identity(prefix / "037-a013-consumer-observations-surviving-race-checkpoint.json"),
        "limitations": ["Missing overwritten first channels and original transient truncated bytes are not reconstructed", "Earlier explicit argv gaps and fixture-cleanup discrepancy remain; fresh corrected checks alone establish acceptance", "No universal original raw-channel/startup-manual preservation claim; independently retained coordinator proof and late own guard are distinct"],
        "final_command_record": str(prefix / "037-a013-consumer-blocked-seal-command.json")}
out = prefix / "037-a013-consumer-blocked-seal.json"
with out.open("x") as stream:
    stream.write(json.dumps(seal, indent=2) + "\n")
print(json.dumps({"seal_path": str(out), "seal_sha256": hashlib.sha256(out.read_bytes()).hexdigest(), "main_merge_published": False, "remote_main": target, "local_merge": merge}))
