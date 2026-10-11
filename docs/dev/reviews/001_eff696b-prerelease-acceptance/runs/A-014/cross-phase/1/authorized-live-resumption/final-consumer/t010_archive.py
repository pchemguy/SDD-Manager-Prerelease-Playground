import hashlib, zipfile
from pathlib import Path
from tools.package_source import FILES, build_archive
from tools.check_distribution import verify_archive
root=Path.cwd()
output=Path('/workspace/scratch/46b31bb4dff6/037-a014-authorized-consumer-artifacts/t010-current-source.zip')
archive=build_archive(root,output)
print('ARCHIVE',archive,'SHA256',hashlib.sha256(archive.read_bytes()).hexdigest(),flush=True)
with zipfile.ZipFile(archive) as bundle:
    assert len(bundle.namelist())==11
    assert set(bundle.namelist())=={'textstats-source/'+name for name in FILES}
    for name in FILES:
        data=bundle.read('textstats-source/'+name)
        assert data==(root/name).read_bytes()
        print('MEMBER SHA256',hashlib.sha256(data).hexdigest(),'textstats-source/'+name,flush=True)
print('RETAINED TEXT CHECKS',verify_archive(archive),flush=True)
legacy=root/'dist/textstats-source.zip'
print('PRODUCT IGNORED ARCHIVE',legacy,'SHA256',hashlib.sha256(legacy.read_bytes()).hexdigest(),flush=True)
with zipfile.ZipFile(legacy) as bundle:
    matches=all(bundle.read('textstats-source/'+name)==(root/name).read_bytes() for name in FILES)
    print('PRODUCT ARCHIVE MEMBERS CURRENT',matches,flush=True)
