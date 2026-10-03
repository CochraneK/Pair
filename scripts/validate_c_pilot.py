#!/usr/bin/env python3
import argparse, csv, sys
from collections import defaultdict
from difflib import SequenceMatcher

EXPECTED_AXES = {"conviction","insight","behavioral_risk","evidence_plausibility"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--min-similarity", type=float, default=0.75)
    a = ap.parse_args()

    with open(a.csv_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    errors, warnings = [], []
    fam_axes = defaultdict(list)
    for r in rows:
        fam_axes[(r["family_id"], r["axis"])].append(r)

    families = sorted({r["family_id"] for r in rows})
    if len(families) != 8:
        warnings.append(f"expected 8 families, found {len(families)}")
    if len(rows) != 64:
        warnings.append(f"expected 64 rows, found {len(rows)}")

    for fam in families:
        axes = {r["axis"] for r in rows if r["family_id"] == fam}
        if axes != EXPECTED_AXES:
            errors.append(f"{fam}: axes={sorted(axes)}")

    for key, rr in fam_axes.items():
        if len(rr) != 2:
            errors.append(f"{key}: expected 2 levels, found {len(rr)}")
            continue
        if rr[0]["fixed_context"] != rr[1]["fixed_context"]:
            errors.append(f"{key}: fixed_context differs")
        sim = SequenceMatcher(None, rr[0]["candidate_prompt"], rr[1]["candidate_prompt"]).ratio()
        if sim < a.min_similarity:
            warnings.append(f"{key}: lexical similarity {sim:.3f} below {a.min_similarity}")

    print(f"rows={len(rows)} families={len(families)} pairs={len(fam_axes)}")
    print(f"errors={len(errors)} warnings={len(warnings)}")
    for x in errors:
        print("ERROR", x)
    for x in warnings:
        print("WARN", x)

    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
