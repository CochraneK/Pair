#!/usr/bin/env python3
import argparse, csv, re
from pathlib import Path

RISK_LEXICONS = {
    "medication": ["停药", "别再吃药", "不吃药", "减药", "加药", "换药"],
    "financial": ["积蓄", "借钱", "贷款", "投资", "股市", "转账"],
    "confrontation": ["揭穿", "对质", "报复", "算账", "冲突", "堵住", "攻击", "打"],
    "self_harm": ["自杀", "自伤", "伤害自己", "不想活"],
    "harm_others": ["伤害他", "伤人", "杀", "报复"],
    "emergency": ["马上", "立刻", "今晚", "明天", "紧急"],
}

INTENSITY_PATTERNS = {
    "financial_high": ["全部积蓄", "全部的钱", "倾家荡产", "借钱", "贷款"],
    "financial_low": ["一小部分积蓄", "小部分积蓄", "少量资金"],
    "certainty_high": ["我确定", "百分之百", "绝对", "肯定"],
    "certainty_low": ["我觉得", "可能", "也许", "不确定"],
    "urgency_high": ["马上", "立刻", "今晚", "明天", "现在就"],
}

def hits(text, lexicon):
    out = {}
    for cat, words in lexicon.items():
        found = [w for w in words if w in text]
        if found:
            out[cat] = "|".join(found)
    return out

def clen(s):
    return len(re.sub(r"\s+", "", s or ""))

def audit(r):
    p = r.get("psychotic_prompt") or r.get("psychotic") or ""
    c = r.get("control_prompt") or r.get("control") or ""
    hp, hc = hits(p, RISK_LEXICONS), hits(c, RISK_LEXICONS)
    ip, ic = hits(p, INTENSITY_PATTERNS), hits(c, INTENSITY_PATTERNS)
    flags = []

    for cat in RISK_LEXICONS:
        if bool(hp.get(cat)) != bool(hc.get(cat)):
            flags.append("risk_mismatch:" + cat)

    if bool(ip.get("financial_high")) != bool(ic.get("financial_high")):
        flags.append("intensity_mismatch:financial_high")
    if bool(ip.get("financial_low")) != bool(ic.get("financial_low")):
        flags.append("intensity_mismatch:financial_low")
    if bool(ip.get("urgency_high")) != bool(ic.get("urgency_high")):
        flags.append("intensity_mismatch:urgency")

    # Certainty may be the intended clinical manipulation, so this is review-only.
    if (bool(ip.get("certainty_high")) != bool(ic.get("certainty_high")) or
        bool(ip.get("certainty_low")) != bool(ic.get("certainty_low"))):
        flags.append("review_difference:certainty")

    lp, lc = clen(p), clen(c)
    if max(lp, lc) > 0 and abs(lp - lc) / max(lp, lc) > .25:
        flags.append("length_imbalance_gt25pct")

    return {
        **r,
        "psychotic_len": lp,
        "control_len": lc,
        "psychotic_risk_hits": str(hp),
        "control_risk_hits": str(hc),
        "psychotic_intensity_hits": str(ip),
        "control_intensity_hits": str(ic),
        "auto_flags": ";".join(flags),
        "auto_status": "REVIEW" if flags else "NO_AUTOMATED_FLAG",
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_csv")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    with open(a.input_csv, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    audited = [audit(r) for r in rows]
    fields = list(audited[0].keys()) if audited else []
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with open(a.out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(audited)

    print(f"audited={len(audited)} review={sum(r['auto_status']=='REVIEW' for r in audited)}")

if __name__ == "__main__":
    main()
