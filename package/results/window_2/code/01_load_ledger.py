import json,subprocess,os
SP="/private/tmp/claude-501/-Users-uikegulu-Desktop-riskloom/bcfd7437-1f90-4db4-a2c9-525c7a102a2a/scratchpad/w2"
CL=os.popen("source %s/db.sh; echo $CL"%SP).read().strip()
SEC=os.popen("source %s/db.sh; echo $SEC"%SP).read().strip()
rows=[];off=0
while True:
    sql=("select to_char(observed_at,'YYYY-MM-DD\"T\"HH24:MI:SS\"Z\"'), market_state, symbol_bands::text "
         "from public_state_log "
         "where observed_at >= timestamptz '2026-09-08T00:00:00Z' and observed_at < timestamptz '2026-09-15T00:00:00Z' "
         "order by observed_at limit 200 offset %d"%off)
    r=subprocess.run(["aws","rds-data","execute-statement","--resource-arn",CL,"--secret-arn",SEC,
                      "--database","riskloom_clone","--sql",sql,"--output","json"],capture_output=True,text=True)
    recs=json.loads(r.stdout)["records"]
    if not recs: break
    for rec in recs:
        rows.append([rec[0]["stringValue"],rec[1]["stringValue"],json.loads(rec[2]["stringValue"])])
    off+=200
    if len(recs)<200: break
json.dump(rows,open(SP+"/ledger_window.json","w"))
print("in-window rows:",len(rows))
print("first:",rows[0][0]," last:",rows[-1][0])
print("symbols per row:",len(rows[0][2]))
syms=sorted(rows[0][2].keys())
print("universe consistent across all rows:", all(sorted(r[2].keys())==syms for r in rows))
json.dump(syms,open(SP+"/universe.json","w"))
