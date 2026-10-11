import hashlib, subprocess, re
from pathlib import Path
base="88a5c4b4424f4bba76940e40b1d6523b1f6fe191"
def git(*args):
    return subprocess.check_output(["git", "--no-optional-locks", *args], text=True)
for commit in git("rev-list", "--reverse", f"{base}..HEAD").splitlines():
    subject=git("show", "-s", "--format=%s",commit).strip()
    task=re.match(r"^\[(T-\d{3})\] ",subject).group(1)
    diff=git("diff",f"{commit}^",commit,"--","docs/dev/TASKS.md")
    removed=re.findall(r"^-.*\[ \] (T-\d{3}) —",diff,re.M)
    added=re.findall(r"^\+.*\[x\] (T-\d{3}) —",diff,re.M)
    assert removed==added==[task],(subject,removed,added)
    names=git("diff-tree","--no-commit-id","--name-only","-r",commit).splitlines()
    assert len(names)>1 and "docs/dev/TASKS.md" in names
    print("TASK AUDIT",commit,subject,"initial closure",removed,"paths",names)
for path in [*Path("textstats").glob("*.py"),*Path("tools").glob("*.py"),*Path("tests").rglob("*.py"),*Path("docs/dev").glob("*.md")]:
    print("SHA256",hashlib.sha256(path.read_bytes()).hexdigest(),path)
loaded = [Path("textstats-run-resources/plugin/AGENTS.md")]
for owner in ["sdd-manage","sdd-implement","sdd-orient","sdd-verify","sdd-docs","sdd-tdd","sdd-report"]:
    loaded.append(Path(f"textstats-run-resources/plugin/skills/{owner}/SKILL.md"))
refs={"sdd-manage":["human-document-review","document-qc-gates","tracking-decision","phase-activation","branch-management","git-workflows"],"sdd-implement":["startup-and-continuation","range-selection","task-execution","completion-and-checkpoints"],"sdd-orient":["inspection-and-handoff"],"sdd-verify":["boundary-review","check-selection","execution-and-evidence","failure-assessment"],"sdd-docs":["in-code-documentation","standalone-documentation","review-and-findings"],"sdd-tdd":["test-first-cycle","writing-good-tests"],"sdd-report":["object-drafts","completion-reports"],"sdd-conventions":["development-document-qc","markdown-style"]}
for owner,names in refs.items():
    loaded.extend(Path(f"textstats-run-resources/plugin/skills/{owner}/references/{name}.md") for name in names)
Path("/workspace/scratch/46b31bb4dff6/037-a014-authorized-consumer-artifacts/loaded-skills.sha256").write_text("".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path}\n" for path in loaded))
print("All T001–T008 task result/initial checklist boundaries audited; loaded instruction hashes saved")
