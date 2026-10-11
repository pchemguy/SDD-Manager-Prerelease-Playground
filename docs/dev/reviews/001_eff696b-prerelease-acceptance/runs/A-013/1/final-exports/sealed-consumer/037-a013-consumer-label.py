import importlib.util
spec=importlib.util.spec_from_file_location("api","/workspace/scratch/46b31bb4dff6/037-a013-consumer-api.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
name="sdd-phase-2-Ranges-and-stdin";endpoint="/labels/"+name
before=m.api(endpoint)
assert before["id"]==12626943170 and before["name"]==name
payload={"description":"Named-file ranges and strict UTF-8 stdin; exact text output."}
m.append("hosted_candidates",{"identity":12626943170,"endpoint":m.base+endpoint,"method":"PATCH","payload":payload,"actual_before":before,"scope":"Root delegated T016 gate bounded maintenance, description only, after published T016 exact readback"})
if before["description"]!=payload["description"]:m.api(endpoint,"PATCH",payload)
after=m.api(endpoint)
assert after["description"]==payload["description"]
for k,v in before.items():
 if k!="description":assert after[k]==v,k
print("managed phase label description corrected/read back; ID/name/color and all other fields preserved")
