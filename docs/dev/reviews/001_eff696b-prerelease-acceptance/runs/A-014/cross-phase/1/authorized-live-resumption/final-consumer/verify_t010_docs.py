import os, shutil, subprocess, sys, tempfile
from pathlib import Path
root=Path.cwd()
artifact=Path('/workspace/scratch/46b31bb4dff6/037-a014-authorized-consumer-artifacts')
with tempfile.TemporaryDirectory(dir=artifact, prefix='t010-docs-') as directory:
    target=Path(directory)
    paths=subprocess.check_output(['git','--no-optional-locks','ls-files'], text=True).splitlines()
    for name in paths:
        if name.startswith(('textstats-run-resources/', '.github/', 'docs/testing/')):
            continue
        source=root/name
        if not source.is_file():
            continue
        destination=target/name
        destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(source,destination)
    (target/'textstats-run-resources').symlink_to(root/'textstats-run-resources', target_is_directory=True)
    result=subprocess.run([sys.executable,'-B',str(artifact/'check_docs.py')],cwd=target,env=os.environ.copy())
    raise SystemExit(result.returncode)
