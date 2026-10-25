import sys, pathlib, unittest, json, tempfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import runner
class RunnerTests(unittest.TestCase):
 def setUp(self):
  self.c=json.loads((runner.ROOT/'config.example.json').read_text()); self.s=json.loads((runner.ROOT/'data/scenarios.json').read_text())
 def test_design(self):
  runner.validate_config(self.c);batch=runner.jobs(self.c,self.s)
  self.assertEqual(len(batch),600);self.assertEqual(len({r['id'] for _,r in batch}),600)
  for m in self.c['models']:
   for c in ['jelas','ambigu']:
    for l in [0,2,4]:self.assertEqual(len({r['scenario_id'] for _,r in batch if r['model']==m['name'] and r['condition']==c and r['autonomy']==l}),50)
  self.assertEqual(batch,runner.jobs(self.c,self.s))
 def test_reject_same_model(self):
  self.c['models'][1]['model']=self.c['models'][0]['model']
  with self.assertRaises(AssertionError):runner.validate_config(self.c)
 def test_resume_hash_tracks_prompts(self):
  a=runner.jobs(self.c,self.s)[0][1]['protocol_hash'];self.s[0]['clear']+=' Test'
  self.assertNotEqual(a,runner.jobs(self.c,self.s)[0][1]['protocol_hash'])
 def test_atomic_json(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'test.json';runner.write_atomic(p,[{'status':'ok'}]);self.assertEqual(json.loads(p.read_text()),[{'status':'ok'}])
if __name__=='__main__':unittest.main()
