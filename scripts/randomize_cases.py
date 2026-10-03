#!/usr/bin/env python3
import argparse,csv,random
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input_csv")
    ap.add_argument("--out",required=True)
    ap.add_argument("--seed",type=int,default=20261003)
    a=ap.parse_args()
    with open(a.input_csv,encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f)); fields=f.fieldnames or []
    rng=random.Random(a.seed); rng.shuffle(rows)
    for i,r in enumerate(rows,1):
        r["presentation_order"]=i
    outf=fields+([] if "presentation_order" in fields else ["presentation_order"])
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    with open(a.out,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=outf); w.writeheader(); w.writerows(rows)
    print(f"rows={len(rows)} seed={a.seed}")

if __name__=="__main__":
    main()
