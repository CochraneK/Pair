#!/usr/bin/env python3
import argparse, csv, random
from collections import defaultdict
from pathlib import Path

A_PRODUCTS = ["deepseek_app","doubao_app","kimi_app","qwen_app","yuanbao_app"]
B_PRODUCTS = ["deepseek_app","doubao_app","qwen_app"]
C_CONFIGS = ["C-DS-V41F-20260910","C-QWEN38MAX-0902","C-DOUBAO21PRO-260915"]

SEED_A_REPEAT = 202610031
SEED_A_ORDER = 202610100
SEED_B_ORDER = 202610200
SEED_C_ORDER = 202610300


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)


def load_a(repo):
    rows=[]
    for fp in sorted((repo/"benchmark/A_CASES_v0.1").glob("A_CASES_P*_32_v0.1.csv")):
        rows.extend(read_csv(fp))
    if len(rows) != 160:
        raise SystemExit(f"Expected 160 Plan-A rows, got {len(rows)}")
    return rows


def build_a(rows):
    psych=[r for r in rows if r["condition"]=="psychotic"]
    bydom=defaultdict(list)
    for r in psych: bydom[r["sips_domain"]].append(r)
    alloc={"P1":4,"P2":3,"P3":3,"P4":3,"P5":3}
    rng=random.Random(SEED_A_REPEAT)
    repeat=[]
    for dom,n in alloc.items():
        vals=sorted(bydom[dom], key=lambda x:x["case_id"])
        repeat += [x["case_id"] for x in rng.sample(vals,n)]
    repeat=set(repeat)

    out=[]
    for pi,prod in enumerate(A_PRODUCTS):
        primary=rows.copy(); seed=SEED_A_ORDER+pi; random.Random(seed).shuffle(primary)
        seq=1
        for r in primary:
            out.append({"sequence":seq,"product_id":prod,"phase":"primary","replicate":1,"case_id":r["case_id"],"pair_id":r["pair_id"],"sips_domain":r["sips_domain"],"condition":r["condition"],"prompt_text":r["prompt_text"],"randomization_seed":seed}); seq+=1
        reps=[r for r in rows if r["case_id"] in repeat]
        for rep in (2,3):
            rr=reps.copy(); rseed=SEED_A_ORDER+1000*rep+pi; random.Random(rseed).shuffle(rr)
            for r in rr:
                out.append({"sequence":seq,"product_id":prod,"phase":"stability_repeat","replicate":rep,"case_id":r["case_id"],"pair_id":r["pair_id"],"sips_domain":r["sips_domain"],"condition":r["condition"],"prompt_text":r["prompt_text"],"randomization_seed":rseed}); seq+=1
    return out, sorted(repeat)


def build_b(rows):
    out=[]
    for pi,prod in enumerate(B_PRODUCTS):
        seq=1
        for rep in (1,2,3):
            rr=rows.copy(); seed=SEED_B_ORDER+pi*100+rep; random.Random(seed).shuffle(rr)
            for r in rr:
                out.append({"sequence":seq,"product_id":prod,"replicate":rep,"case_id":r["case_id"],"family_id":r["family_id"],"sips_domain":r["sips_domain"],"axis":r["axis"],"level":r["level"],"prompt_text":r["prompt_text"],"randomization_seed":seed}); seq+=1
    return out


def build_c(rows):
    out=[]
    for mi,cfg in enumerate(C_CONFIGS):
        seq=1
        for rep in (1,2,3):
            rr=rows.copy(); seed=SEED_C_ORDER+mi*100+rep; random.Random(seed).shuffle(rr)
            for r in rr:
                case_id=r.get("case_id") or f"{r['family_id']}-{r['axis']}-{r['level']}"
                out.append({"sequence":seq,"config_id":cfg,"replicate":rep,"case_id":case_id,"family_id":r["family_id"],"domain":r["domain"],"axis":r["axis"],"level":r["level"],"prompt_text":r["candidate_prompt"],"randomization_seed":seed}); seq+=1
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--outdir", default="execution/generated")
    a=ap.parse_args()
    repo=Path(a.repo); outdir=repo/a.outdir

    A=load_a(repo)
    B=read_csv(repo/"benchmark/B_PILOT_v0.1/B_PILOT_36_v0.1.csv")
    C=read_csv(repo/"routes/C/PILOT_BLUEPRINTS_64.csv")

    a_sched, repeat=build_a(A); b_sched=build_b(B); c_sched=build_c(C)
    write_csv(outdir/"A_COLLECTION_SCHEDULE_v0.1.csv", a_sched)
    write_csv(outdir/"B_COLLECTION_SCHEDULE_v0.1.csv", b_sched)
    write_csv(outdir/"C_API_PILOT_SCHEDULE_v0.1.csv", c_sched)
    write_csv(outdir/"A_REPEAT_SUBSET_v0.1.csv", [{"case_id":x} for x in repeat])

    print(f"A={len(a_sched)} B={len(b_sched)} C={len(c_sched)} total={len(a_sched)+len(b_sched)+len(c_sched)}")

if __name__ == "__main__":
    main()
