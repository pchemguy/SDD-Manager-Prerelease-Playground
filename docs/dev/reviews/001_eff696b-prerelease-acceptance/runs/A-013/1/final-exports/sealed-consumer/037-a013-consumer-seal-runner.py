import hashlib, json, os, subprocess, sys, time
from pathlib import Path

root = "/workspace/scratch/46b31bb4dff6/037-textstats-product"
out = Path("/workspace/scratch/46b31bb4dff6/037-a013-consumer-final-seal-command.json")
assert not out.exists(), "Preserve existing final command record"
started = time.time()
environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", GIT_ASKPASS="/workspace/scratch/46b31bb4dff6/playground-askpass.sh", GIT_TERMINAL_PROMPT="0")
process = subprocess.run(sys.argv[1:], cwd=root, env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
record = {"wrapper_orig_argv": sys.orig_argv, "argv": sys.argv[1:], "cwd": root, "stdout": process.stdout.decode("utf-8", "replace"), "stderr": process.stderr.decode("utf-8", "replace"), "status": process.returncode, "input_hex": None, "input_sha256": None, "started": started, "completed": time.time(), "environment": {k: v for k, v in environment.items() if k in {"PYTHONDONTWRITEBYTECODE", "LANG", "LC_ALL"}}}
with out.open("x") as stream:
    stream.write(json.dumps(record, indent=2) + "\n")
print(json.dumps({"record_path": str(out), "record_sha256": hashlib.sha256(out.read_bytes()).hexdigest(), "status": process.returncode, "stdout": record["stdout"], "stderr": record["stderr"]}))
sys.exit(process.returncode)
