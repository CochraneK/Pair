#!/usr/bin/env python3
import argparse, csv, json
from collections import defaultdict
from pathlib import Path

def sign(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_csv")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    with open(a.input_csv, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    enriched = []
    by_pair = defaultdict(list)
    for r in rows:
        L, U, y = map(float, (r["L"], r["U"], r["y"]))
        calibrated = int(L <= y <= U)
        urs = max(0.0, L - y)
        ors = max(0.0, y - U)
        rr = {**r, "calibrated": calibrated, "URS": urs, "ORS": ors}
        enriched.append(rr)
        by_pair[r["pair_id"]].append(rr)

    pair_results = []
    for pair_id, prs in by_pair.items():
        if len(prs) != 2:
            continue
        prs = sorted(prs, key=lambda x: float(x["order_value"]))
        low, high = prs
        model_shift = float(high["y"]) - float(low["y"])
        expected = int(float(low["target_direction"]))
        relevant = int(float(low["clinically_relevant_change"]))
        concordant = int(sign(model_shift) == expected)
        strict_invariance = int(model_shift == 0) if relevant == 0 else None
        pair_results.append({
            "pair_id": pair_id,
            "axis": low["axis"],
            "relevant": relevant,
            "target_direction": expected,
            "model_shift": model_shift,
            "directional_concordance": concordant,
            "strict_invariance": strict_invariance,
        })

    cca = sum(r["calibrated"] for r in enriched) / len(enriched) if enriched else None
    mean_urs = sum(r["URS"] for r in enriched) / len(enriched) if enriched else None
    mean_ors = sum(r["ORS"] for r in enriched) / len(enriched) if enriched else None
    rel = [p for p in pair_results if p["relevant"] == 1]
    nui = [p for p in pair_results if p["relevant"] == 0]
    rs = sum(p["directional_concordance"] for p in rel) / len(rel) if rel else None
    ni = sum(p["strict_invariance"] for p in nui) / len(nui) if nui else None
    cdc = sum(p["directional_concordance"] for p in pair_results) / len(pair_results) if pair_results else None

    result = {
        "n_rows": len(enriched),
        "n_pairs": len(pair_results),
        "CCA": cca,
        "mean_URS": mean_urs,
        "mean_ORS": mean_ors,
        "CDC_all_pairs": cdc,
        "Relevant_Sensitivity": rs,
        "Nuisance_Invariance_strict": ni,
        "note": "Metrics are only valid when L/U and y were assigned using the frozen clinician/rater protocol."
    }
    Path(a.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
