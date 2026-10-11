from pathlib import Path
import contextlib, hashlib, importlib.util, io, json, platform, re, sys, time, zipfile

sp = importlib.util.spec_from_file_location("capture", "/workspace/scratch/46b31bb4dff6/037-a013-consumer-runner.py")
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
root = Path.cwd()
prefix = Path("/workspace/scratch/46b31bb4dff6")
merge, acceptance = sys.argv[1:]
source = "c05b65958e2a386cf2ae8782dca3e749ed9b60ff"
target = "fbe8bedf4c6cba1ab29d53d2da05e614603d76d1"
tree = "190b6865846d66933bcdcd112e1fcfa7ca2f04ef"

def git(*args):
    with contextlib.redirect_stdout(io.StringIO()):
        result = m.run(["git", *args])
    assert result.returncode == 0, (args, result.returncode)
    return result.stdout.decode()

assert git("branch", "--show-current").strip() == "main"
assert git("rev-parse", "HEAD").strip() == merge
assert git("show", "-s", "--format=%P", merge).strip().split() == [target, source]
assert git("show", "-s", "--format=%T", merge).strip() == tree
assert git("status", "--porcelain=v1") == ""
remote = git("ls-remote", "origin", "refs/heads/main", "refs/heads/phase/2-json-and-stdin")
refs = {line.split()[1]: line.split()[0] for line in remote.splitlines()}
assert refs == {"refs/heads/main": merge, "refs/heads/phase/2-json-and-stdin": source}
protected = ["textstats-run-resources", ".github", "docs/testing/publisher-037", ".gitignore", "docs/dev/reports/phases/1", "docs/dev/reports/phases/2/2.1.md", "docs/dev/reports/phases/2/revisions", "docs/dev/features"]
assert git("diff", "--name-only", "77e7106e3134cc7053a2b1a045cf1a76cf0361ea", merge, "--", *protected) == ""
message = git("show", "-s", "--format=%B", merge)
message_path = prefix / "037-a013-consumer-phase2-merge.txt"
assert message.strip() == message_path.read_text().strip()
plugin_tree = git("rev-parse", merge + ":textstats-run-resources/plugin").strip()
task = (root / "docs/dev/TASKS.md").read_text()
owners = re.findall(r"^\s*- \[([ x])\] (T-\d{3})", task.split("## T-001 completion evidence", 1)[0], re.M)
assert len(owners) == 21 and all(status == "x" for status, _ in owners)
archive = root / "dist/textstats-source.zip"
archive_sha = hashlib.sha256(archive.read_bytes()).hexdigest()
assert archive_sha == "d3f2d3f11698405eefc317a8ca048de5f3fe1964b3c390fc11e7def6c20242ed"
with zipfile.ZipFile(archive) as package:
    members = []
    for name in package.namelist():
        relative = name.removeprefix("textstats-source/")
        data = package.read(name)
        assert data == (root / relative).read_bytes()
        members.append({"path": relative, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    assert len(members) == 11
records_dir = prefix / "037-a013-consumer-command-records"
digest = hashlib.sha256()
record_files = sorted(records_dir.glob("*.json"))
for path in record_files:
    digest.update(path.name.encode() + b"\0" + hashlib.sha256(path.read_bytes()).digest())
observations = prefix / "037-a013-consumer-observations.json"
ledger = json.loads(observations.read_text())
native = [{"ordinal": ordinal, "method": event["method"], "endpoint": event["endpoint"], "status": event["status"], "response_sha256": event["response_sha256"], "response_bytes": event["response_bytes"]} for ordinal, event in enumerate(ledger["provider"]) if event["method"] in {"PATCH", "POST"}]
closures = [command for command in ledger["commands"] if any(str(arg).endswith(("037-a013-consumer-close.py", "037-a013-consumer-milestone.py")) for arg in command["argv"])]
assert all(command["status"] == 0 for command in closures)
assert any(command["argv"][-1] == "6" for command in closures)
preservation = ledger.get("late_foreign_guard", [])
assert len(preservation) == 8
assert [event["semantic_sha256"] for event in preservation[:4]] == [event["semantic_sha256"] for event in preservation[4:]]
artifacts = {}
for relative in ["AGENTS.md", "docs/dev/TASKS.md", "docs/dev/TASKS-REVIEW-REPORT.md", "docs/dev/reports/phases/2/2.2.md", "docs/dev/reports/phases/2/PHASE-REPORT.md", "docs/dev/reports/IMPLEMENTATION-REPORT.md"]:
    path = root / relative
    artifacts[relative] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size}
race = prefix / "037-a013-consumer-observations-surviving-race-checkpoint.json"
seal = {
    "kind": "A-013 final reached-state seal", "sealed": time.time(), "completed_published_phase": 2, "stop": True,
    "source": source, "main_merge": merge, "ordered_parents": [target, source], "tree": tree, "remote_refs": refs, "clean": True,
    "integration_acceptance_reported_by_coordinator": acceptance,
    "report_acceptance": "791d494ac22f376a75d7edc7bc09b97045041b82", "milestone_acceptance": "9338f067a575511b6d818a6898a458957f4670a8",
    "pinned_plugin": {"package_pin": "ea515f5624c8a34cc4572731a2590223a5eb27f4", "actual_product_plugin_tree": plugin_tree, "protected_diff_from_resume_empty": True},
    "runtime": {"python": platform.python_version(), "platform": platform.system(), "explicit_B": "-B" in sys.orig_argv, "other_declared_runtimes_platforms": "unverified"},
    "active_owners": 21, "active_checked": 21, "retired_historical_no_checkbox": ["T-010", "T-011", "T-012"], "TODO": "None",
    "merged_checks": {"unit": 37, "integration": 34, "real_extracted_module_cases": 478, "status": 0, "skips_warnings": 0, "fresh_recorded_python_children": 1628, "all_explicit_B_env": True},
    "unchanged_final_docs_campaign": {"fences": 12, "status": 0, "recorded_python_children": 2776, "archive_sha256": "4fcf4a60d08f4a8c2a69a0b2d567de70c5a554e2249eb0f101f18c5340b7349c"},
    "archive": {"path": str(archive), "sha256": archive_sha, "members": members, "checkpoint_note": "ZIP metadata differs after main checkout/merge; member source contents remain exact"},
    "artifacts": artifacts, "accepted_merge_message_sha256": hashlib.sha256(message_path.read_bytes()).hexdigest(),
    "native_write_chronology": native, "closure_command_completions": [{"argv": command["argv"], "status": command["status"], "completed": command["time"]} for command in closures],
    "late_foreign_comparison": {"passed": True, "scope": "late pre-T017 closure/integration through final publication only; no original startup inference", "semantic_hashes": [event["semantic_sha256"] for event in preservation[4:]]},
    "original_observations": {"path": str(observations), "sha256": hashlib.sha256(observations.read_bytes()).hexdigest(), "bytes": observations.stat().st_size, "stable_after_this_seal": True},
    "immutable_child_records": {"directory": str(records_dir), "count": len(record_files), "aggregate_sha256": digest.hexdigest(), "aggregation": "sorted filename UTF-8 + NUL + raw SHA256 digest of exact file bytes"},
    "surviving_race_checkpoint": {"path": str(race), "sha256": hashlib.sha256(race.read_bytes()).hexdigest(), "bytes": race.stat().st_size, "scope": "postrepair surviving captures, not original transient truncated bytes"},
    "limitations": ["Original transient truncated JSON bytes were not snapshotted; overwritten/lost first child channels have unknown count/content and are not reconstructed", "Earlier fifteen missing explicit -B argv gaps inherited bytecode suppression; fresh corrected campaigns alone support explicit-flag claims", "Original fixture-cleanup discrepancy remains; later ownership/hash-guarded unlink and absent-fixture checks establish only the fresh retries", "Some original incidental tool errors lack independent raw-channel prefix records; no universal original command-capture completeness claim", "Original manual-controls preservation proof is independently retained by coordinator; this consumer's late hashes establish only the late boundary"],
    "final_command_record": str(prefix / "037-a013-consumer-final-seal-command.json")
}
assert seal["runtime"]["python"] == "3.12.14" and seal["runtime"]["explicit_B"]
out = prefix / "037-a013-consumer-final-seal.json"
with out.open("x") as stream:
    stream.write(json.dumps(seal, indent=2) + "\n")
print(json.dumps({"seal_path": str(out), "seal_sha256": hashlib.sha256(out.read_bytes()).hexdigest(), "main_merge": merge, "source": source, "stop": True}))
