#!/usr/bin/env python3
"""Cohen kappa per label untuk dua penilai independen. Tidak mengubah label."""
import argparse,json
from pathlib import Path
from analyze import KEYS

def rows(path):
 o=json.loads(Path(path).read_text());rs=o['rows'] if isinstance(o,dict) else o
 out={}
 for r in rs:
  if r.get('source')!='real' or r.get('status')!='ok':continue
  if r['id'] in out:raise ValueError('ID duplikat')
  out[r['id']]=r
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('rater1');p.add_argument('rater2');p.add_argument('--out',default='agreement.json');a=p.parse_args();x=rows(a.rater1);y=rows(a.rater2);out={}
 for k in KEYS:
  pairs=[(x[i]['labels'][k],y[i]['labels'][k]) for i in sorted(x.keys()&y.keys()) if isinstance(x[i].get('labels'),dict) and isinstance(y[i].get('labels'),dict) and type(x[i]['labels'].get(k)) is bool and type(y[i]['labels'].get(k)) is bool];n=len(pairs)
  if n:
   po=sum(v==w for v,w in pairs)/n;px=sum(v for v,w in pairs)/n;py=sum(w for v,w in pairs)/n;pe=px*py+(1-px)*(1-py);out[k]={'n':n,'raw_agreement':po,'kappa':(po-pe)/(1-pe) if pe<1 else None,'matrix':{f'{int(v)}{int(w)}':sum(a==v and b==w for a,b in pairs) for v in [False,True] for w in [False,True]}}
  else:out[k]={'n':0,'raw_agreement':None,'kappa':None}
 Path(a.out).write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
if __name__=='__main__':main()
