#!/usr/bin/env python3
"""Build a blinded rating pack from collected responses.

Input CSV must contain run_id, case_id, product_id/config_id and response_text.
This script does NOT silently rewrite substantive response text. It flags potential
brand leakage for manual review and assigns blinded response IDs.
"""
import argparse, csv, hashlib, random, re
from pathlib import Path

BRAND_PATTERNS = [
    r"\bChatGPT\b", r"\bOpenAI\b", r"\bDeepSeek\b", r"\bKimi\b",
    r"豆包", r"通义千问", r"千问", r"腾讯元宝", r"元宝", r"Qwen",
]


def has_brand(text):
    return [p for p in BRAND_PATTERNS if re.search(p, text or "", flags=re.I)]


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input_csv")
    ap.add_argument("--outdir",required=True)
    ap.add_argument("--seed",type=int,default=202610400)
    a=ap.parse_args()

    with open(a.input_csv,encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    req={"run_id","case_id","response_text"}
    miss=req-set(rows[0]) if rows else req
    if miss: raise SystemExit(f"Missing columns: {sorted(miss)}")

    rng=random.Random(a.seed)
    shuffled=rows.copy(); rng.shuffle(shuffled)
    outdir=Path(a.outdir); outdir.mkdir(parents=True,exist_ok=True)

    pack=[]; mapping=[]; leakage=[]
    for i,r in enumerate(shuffled,1):
        blind_id=f"RSP-{i:05d}-{h(r['run_id'])}"
        brands=has_brand(r.get("response_text",""))
        pack.append({
            "blind_response_id":blind_id,
            "case_id":r["case_id"],
            "response_text":r.get("response_text",""),
            "appropriateness_0_2":"",
            "recognition":"",
            "non_reinforcement":"",
            "urgency":"",
            "resources":"",
            "policy_level_0_5":"",
            "over_refusal":"",
            "over_pathologization":"",
            "comments":"",
        })
        mapping.append({"blind_response_id":blind_id,"run_id":r["run_id"],"product_or_config":r.get("product_id") or r.get("config_id") or ""})
        if brands:
            leakage.append({"blind_response_id":blind_id,"run_id":r["run_id"],"patterns":";".join(brands)})

    def write(name, data):
        path=outdir/name
        with path.open("w",encoding="utf-8-sig",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(data[0].keys()) if data else ["empty"]);w.writeheader();
            if data:w.writerows(data)
        return path

    p1=write("rating_pack.csv",pack)
    p2=write("blind_mapping_PRIVATE.csv",mapping)
    p3=write("brand_leakage_review.csv",leakage)
    print(f"pack={p1} mapping={p2} leakage={len(leakage)}")

if __name__=="__main__":
    main()
