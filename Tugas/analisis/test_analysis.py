import unittest,math
from analyze import exact,wilson,holm,analyze
class Test(unittest.TestCase):
 def test_binomial(self):
  self.assertEqual(exact(0,0),1);self.assertAlmostEqual(exact(5,0),.0625);self.assertEqual(exact(3,3),1)
 def test_wilson(self):
  self.assertIsNone(wilson(0,0));self.assertAlmostEqual(wilson(0,50)[1],.0713476,places=6)
 def test_holm(self):
  r=holm([{'p':.04},{'p':.01},{'p':.03}]);self.assertEqual([x['p_holm'] for x in r],[.06,.03,.06])
 def test_synthetic_excluded(self):
  self.assertEqual(analyze([{'source':'demo','status':'ok'}])['n_rated'],0)
 def test_empty(self):self.assertEqual(analyze([])['status'],'NOT_EXECUTED')
 def test_duplicate(self):
  r={'source':'real','status':'error','model':'A','condition':'jelas','autonomy':0,'scenario_id':'S001','protocol_hash':'a','model_identity':'m'}
  with self.assertRaises(ValueError):analyze([r,r])
if __name__=='__main__':unittest.main()

class FullDesignTest(unittest.TestCase):
 def test_all_contrasts_and_denominators(self):
  # Synthetic unit-test fixture only, never written as research output.
  rows=[]
  for m in ['A','B']:
   for c in ['jelas','ambigu']:
    for l in [0,2,4]:
     for i in range(1,51):
      rows.append({'source':'real','status':'ok','id':f'{m}-{c}-{l}-{i}','protocol_hash':'UNIT_TEST_ONLY','model':m,'model_identity':m,'returned_model':m,'condition':c,'autonomy':l,'scenario_id':f'S{i:03}','labels':{'alignment':True,'gaming':c=='ambigu' and i<=10,'clarification':False,'unsafe':l==4 and i<=5,'approval':True}})
  r=analyze(rows);self.assertEqual(r['status'],'COMPLETE');self.assertEqual(len(r['tests']),16);self.assertEqual(len(r['groups']),12)
  self.assertTrue(all(t['n_pairs']==50 for t in r['tests']));self.assertTrue(all(t['p_holm']>=t['p'] for t in r['tests']))
  self.assertAlmostEqual(r['tests'][0]['difference_right_minus_left'],.2)
