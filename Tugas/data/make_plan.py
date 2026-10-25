#!/usr/bin/env python3
"""Generate a plan with empty responses. Never calls any model."""
import argparse,json,csv,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'aplikasi'));import runner
p=argparse.ArgumentParser();p.add_argument('--config',default=str(ROOT/'aplikasi/config.example.json'));a=p.parse_args();c=runner.validate_config(json.loads(Path(a.config).read_text()));s=json.loads((ROOT/'aplikasi/data/scenarios.json').read_text());rows=[]
for _,r in runner.jobs(c,s):r.update(source='planned',status='planned');rows.append(r)
(ROOT/'data/rencana_600.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (ROOT/'data/prompt_600.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['id','scenario_id','model','model_identity','condition','autonomy','system_prompt','prompt','intent','rubric','protocol_hash']);w.writeheader();w.writerows([{k:r[k] for k in w.fieldnames} for r in rows])
print('600 pekerjaan direncanakan. Nol panggilan API. Tidak ada respons model.')
