from pathlib import Path
import json,hashlib,sys,time
base=Path('/workspace/scratch/46b31bb4dff6/037-a012-consumer-observations');p=Path(str(base)+'.json');x=json.loads(p.read_text())
proof=json.loads(Path(str(base)+'.integration-proof.json').read_text());assert proof['clean'] and proof['source_tree_equal'];assert len(json.loads(Path(str(base)+'.hosted-results.json').read_text()))==19
x['status']='COMPLETE: accepted JSON withdrawal integrated into actual paused Phase2, immediately published/exactly read back; STOP. No stdin/main/fullphase/release execution.'
x['conclusion'].update(accepted=True,acceptance_commit='c908c19a5828a32d46f97a269820445d9f41faf9',product_commit='160c0a980286c68f62d0d13b3238dad0748885e9',remote_exact_readback='160c0a980286c68f62d0d13b3238dad0748885e9')
x['integration']=proof
x['integration']['root_authorization']='Exact five conclusion acceptance and explicit two-parent paused integration authorization at coordinator c908c19a5828a32d46f97a269820445d9f41faf9; source publication precedes target consumption.'
x['boundaries']['commits']=[{'sha':c,'kind':k,'push':'origin '+b,'exact_remote_tip':c,'immediately_pushed_before_other_work':True} for c,k,b in [('636b46d8daf1455c940c98f4d535c9936c0f1733','non-task accepted preparation/opening','revision/003_795f3a3-remove-json'),('1dc6851aef7fdcc9581b00aaffc8c4661ff67d3f','non-task accepted implementation','revision/003_795f3a3-remove-json'),('160c0a980286c68f62d0d13b3238dad0748885e9','non-task accepted conclusion/QC/tracking checkpoint','revision/003_795f3a3-remove-json'),('77e7106e3134cc7053a2b1a045cf1a76cf0361ea','explicit ordered two-parent paused-phase integration','phase/2-json-and-stdin')]]
x['commands']['original_failures'] += ['Initial two focused RED tests: two assertion failures and three mock-serialization errors; realistic doubles corrected without production change; rerun same two tests yielded five intended behavioral failures/no errors.','Root rejected original19 hosted plan before mutation: DOTALL title suffix capture/empty body content; exact original plan preserved, bounded corrected plan accepted.','Issue15 successful PATCH followed by proxy tunnel403 transport failure on GET; all writes stopped, original traceback/exit1 retained; authorized same-endpoint GET-only recovery independently verified exact payload before remaining14 writes, no PATCH replay.','Continuation auxiliary rg docs/dev/*QC* used nonexistent glob, exit2; actual adjacent *-REVIEW-REPORT.md paths then read. No product change resulted.']
x['commands']['capture_limits']='Primary implementation/verification/publication/hosted commands are captured with actual argv/cwd/exit and separate stdout/stderr in commands.jsonl. First orientation and later auxiliary shell reads/script creation used direct tools, whose returned channels are merged; their tool records/script provenance are retained but are not falsely characterized as complete separate-channel captures. Original known limitations above remain.'
x['hosted']['original_failure_preserved']=True;x['hosted']['completed_operations']=19;x['hosted']['exact_fields_and_history_verified']=True;x['hosted']['unmanaged_preserved']=True
x['independent_root_proofs']={}
for name in ['037-a012-final-hosted-readback.json','037-a012-root-hosted-checks.json']:
 f=base.parent/name;assert f.exists();x['independent_root_proofs'][str(f)]=hashlib.sha256(f.read_bytes()).hexdigest()
x['stopped']=True;x['remaining_work']='Only separately authorized future stdin/final T-013–T-017.21 active checklist tasks16 checked5 pending;3 JSON identities retired historically. Main, whole-phase completion and release unchanged.'
x['final_seal_time']=time.time()
output='External final seal completed; product and hosted writes stopped.\n'
with Path(str(base)+'.commands.jsonl').open('a') as f:f.write(json.dumps({'command':['python','-B',str(Path(__file__))],'cwd':'/workspace/scratch/46b31bb4dff6/037-textstats-product','bytecode_disabled':True,'exit_code':0,'stdout':output,'stderr':'','timestamp':time.time(),'capture':'final standalone serialization with fixed output; hashing occurs after this final command event'})+'\n')
x['sidecars']={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(base.parent.glob('037-a012-consumer-observations.*')) if f.is_file() and f!=p}
x['frozen_candidate_trees']={}
for name in ['first-preparation','first-implementation']:
 d=Path(str(base)+'.'+name);assert d.is_dir();x['frozen_candidate_trees'][str(d)]={str(f.relative_to(d)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(d.rglob('*')) if f.is_file()}
p.write_text(json.dumps(x,indent=2)+'\n')
print(output,end='')
