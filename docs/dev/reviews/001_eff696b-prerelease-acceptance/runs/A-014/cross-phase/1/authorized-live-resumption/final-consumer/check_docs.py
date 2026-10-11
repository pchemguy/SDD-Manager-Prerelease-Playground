import os, re, subprocess, sys
from pathlib import Path
root = Path.cwd()
owned = {"sample.txt": b"alpha beta\r\nbeta\rlast two\n", "bom.txt": b"\xef\xbb\xbf", "-sample": b"alpha beta\n"}
assert all(not (root / name).exists() for name in owned), "Example filename exists; ownership unresolved"
try:
    for document in ["README.md", "docs/public-api.md"]:
        for index, (language, code) in enumerate(re.findall(r"```(bash|python)\n(.*?)\n```", Path(document).read_text(), re.S), 1):
            code = re.sub(r"\bpython(?=\s)", "python -B", code) if language == "bash" else code
            command = ["bash", "-c", "set -e\n" + code] if language == "bash" else [sys.executable, "-B", "-c", code]
            result = subprocess.run(command, cwd=root, env=os.environ.copy(), capture_output=True, text=True)
            print(f"DOCUMENT {document} FENCE {index}\nCOMMAND {command!r}\nSTATUS {result.returncode}\nSTDOUT\n{result.stdout}\nSTDERR\n{result.stderr}", flush=True)
            assert result.returncode == 0
    for document in ["README.md", "docs/public-api.md", "AGENTS.md"]:
        for link in re.findall(r"\]\(([^)]+)\)", Path(document).read_text()):
            if "://" in link or link.startswith("#"):
                continue
            assert (Path(document).parent / link.split("#")[0]).exists(), (document, link)
    print("User-guide local links passed; all runnable fences executed")
finally:
    for name, content in owned.items():
        path = root / name
        if path.exists():
            assert path.read_bytes() == content, ("Unexpected example mutation", name)
            path.unlink()
