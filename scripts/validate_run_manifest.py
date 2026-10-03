#!/usr/bin/env python3
import argparse,csv,sys

REQUIRED=["run_id","case_id","source_type","product_or_model","timestamp"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_file")
    a=ap.parse_args()
    with open(a.csv_file,encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        rows=list(reader)
        fields=reader.fieldnames or []
    missing=[x for x in REQUIRED if x not in fields]
    if missing:
        print("missing_columns="+",".join(missing))
        sys.exit(2)
    ids=[r.get("run_id","") for r in rows]
    seen=set(); dup=set()
    for x in ids:
        if not x:
            continue
        if x in seen:
            dup.add(x)
        seen.add(x)
    blank=[i+2 for i,x in enumerate(ids) if not x]
    print(f"rows={len(rows)} duplicate_run_ids={len(dup)} blank_run_ids={len(blank)}")
    if dup:
        print("duplicates="+",".join(sorted(dup)))
    if blank:
        print("blank_rows="+",".join(map(str,blank)))
    sys.exit(1 if dup or blank else 0)

if __name__=="__main__":
    main()
