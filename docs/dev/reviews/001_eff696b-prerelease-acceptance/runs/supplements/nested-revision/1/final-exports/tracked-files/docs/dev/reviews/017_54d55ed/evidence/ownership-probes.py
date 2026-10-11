"""Review-only counterexamples against the unchanged TextStats ownership helper."""
import importlib.util
import json
from pathlib import Path
import tempfile

SOURCE = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location('reviewed_core', SOURCE / 'acceptance/textstats/scripts/core.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
scenarios = [
    ('supported_duplicate_control', {'TASKS.md': '- [ ] T-001 main\n', 'FEATURE-TASKS.md': '- [ ] T-001 feature\n'}, 'duplicate_task_ownership'),
    ('custom_id_duplicate', {'TASKS.md': '- [ ] T-001 main\n- [ ] F-001 additional\n', 'FEATURE-TASKS.md': '- [ ] F-001 duplicate\n'}, 'duplicate_task_ownership'),
    ('linked_report_is_evidence', {'TASKS.md': '- [x] T-001 implemented\n[Report](report.md)\n', 'report.md': '- [x] T-001 verified result (historical evidence, not executable task)\n'}, 'accepted'),
    ('fenced_example_is_not_owner', {'TASKS.md': '- [ ] T-001 actual\n\n```markdown\n- [ ] T-001 illustrative checklist\n```\n'}, 'accepted'),
]
rows = []
for name, documents, expected in scenarios:
    with tempfile.TemporaryDirectory(prefix='review-ownership-') as tmp:
        root = Path(tmp)
        dev = root / 'docs/dev'
        dev.mkdir(parents=True)
        for path, content in documents.items():
            (dev / path).write_text(content)
        try:
            result = core.ownership(root)
            observed = 'accepted'
            owners = sorted(result['owners'])
        except core.Stop as error:
            observed = error.cause
            owners = None
        rows.append({'scenario': name, 'documents': documents, 'expected': expected, 'observed': observed, 'owners': owners, 'matches_expected': expected == observed})
print(json.dumps({'baseline': '54d55edebd8a7af6499d625bdbb357f864a4db1d', 'kind': 'source helper counterexamples, not agent acceptance', 'results': rows}, indent=2))
