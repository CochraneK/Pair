#!/usr/bin/env python3
"""Run PAIR-C fixed API pilot using OpenAI-compatible providers.

Requires: pip install openai
Never stores API keys. Writes one JSON object per run plus a CSV manifest.
"""
import argparse, csv, hashlib, json, os, time
from pathlib import Path
from openai import OpenAI


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def safe_request_record(cfg, prompt, row):
    return {
        "config_id": row["config_id"],
        "model": cfg["model"],
        "reasoning_effort": cfg.get("reasoning_effort"),
        "extra_body": cfg.get("extra_body", {}),
        "messages": [{"role":"user","content":prompt}],
        "tools": None,
        "web": False,
        "prompt_sha256": sha256_text(prompt),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("schedule_csv")
    ap.add_argument("--config", default="configs/C_API_PILOT_REQUESTS_v0.1.json")
    ap.add_argument("--outdir", default="data/raw_api")
    ap.add_argument("--limit", type=int, default=None, help="Smoke-test only first N scheduled rows")
    ap.add_argument("--sleep", type=float, default=0.0)
    args=ap.parse_args()

    cfgdoc=load_json(args.config)
    common=cfgdoc["common"]
    configs=cfgdoc["configs"]
    with open(args.schedule_csv, encoding="utf-8-sig", newline="") as f:
        schedule=list(csv.DictReader(f))
    if args.limit is not None:
        schedule=schedule[:args.limit]

    outdir=Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)
    manifest=[]
    clients={}

    for idx,row in enumerate(schedule,1):
        cid=row["config_id"]
        cfg=configs[cid]
        key=os.environ.get(cfg["api_key_env"])
        if not key:
            raise SystemExit(f"Missing environment variable {cfg['api_key_env']}")
        base_url=cfg.get("base_url") or os.environ.get(cfg.get("base_url_env", ""))
        if not base_url:
            raise SystemExit(f"Missing base URL for {cid}")
        ckey=(cid,base_url)
        if ckey not in clients:
            clients[ckey]=OpenAI(api_key=key, base_url=base_url)
        client=clients[ckey]

        prompt=row["prompt_text"]
        run_id=f"{cid}__{row['case_id']}__r{row['replicate']}"
        request_record=safe_request_record(cfg,prompt,row)
        request_hash=sha256_text(json.dumps(request_record,ensure_ascii=False,sort_keys=True))
        t0=time.time(); error=None; response_text=""; response_meta={}
        try:
            kwargs={
                "model": cfg["model"],
                "messages": [{"role":"user","content":prompt}],
                "reasoning_effort": cfg.get("reasoning_effort", common.get("reasoning_effort")),
                "extra_body": cfg.get("extra_body", {}),
            }
            # Do not set temperature/top_p in thinking mode unless frozen later.
            completion=client.chat.completions.create(**kwargs)
            response_text=completion.choices[0].message.content or ""
            usage=getattr(completion,"usage",None)
            response_meta={
                "provider_response_id": getattr(completion,"id",None),
                "provider_model": getattr(completion,"model",None),
                "finish_reason": completion.choices[0].finish_reason,
                "usage": usage.model_dump() if hasattr(usage,"model_dump") else None,
            }
        except Exception as e:
            error=type(e).__name__+": "+str(e)
        latency=time.time()-t0

        record={
            "run_id":run_id,
            "schedule":row,
            "request":request_record,
            "request_sha256":request_hash,
            "response_text":response_text,
            "response_meta":response_meta,
            "latency_seconds":latency,
            "error":error,
            "timestamp_unix":time.time(),
        }
        outpath=outdir/f"{run_id}.json"
        outpath.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding="utf-8")
        manifest.append({
            "run_id":run_id,
            "case_id":row["case_id"],
            "config_id":cid,
            "replicate":row["replicate"],
            "request_sha256":request_hash,
            "raw_json_path":str(outpath),
            "response_chars":len(response_text),
            "latency_seconds":f"{latency:.3f}",
            "error":error or "",
        })
        print(f"[{idx}/{len(schedule)}] {run_id} {'ERROR' if error else 'OK'}")
        if args.sleep: time.sleep(args.sleep)

    mpath=outdir/"run_manifest.csv"
    with mpath.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(manifest[0].keys()));w.writeheader();w.writerows(manifest)
    print(f"manifest={mpath} runs={len(manifest)}")

if __name__=="__main__":
    main()
