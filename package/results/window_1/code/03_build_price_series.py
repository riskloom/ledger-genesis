import boto3,json,datetime as dt,time,collections
from concurrent.futures import ThreadPoolExecutor
from botocore.config import Config
SP="/private/tmp/claude-501/-Users-uikegulu/af28e28a-7715-44ff-8b9b-eccaa835c956/scratchpad"
s3=boto3.client("s3",config=Config(max_pool_connections=200,retries={'max_attempts':5}))
B="rl-raw-inputs-361964630357"
rows=json.load(open(SP+"/ledger_window.json")); syms=json.load(open(SP+"/universe.json"))
slot_str=[r[0] for r in rows]
# every 12th slot (60-min spacing => contiguous 61-bar coverage) plus the final slot
idx=list(range(0,len(rows),12))
if len(rows)-1 not in idx: idx.append(len(rows)-1)
sel=[slot_str[i] for i in idx]
print("bodies to read:",len(sel),"slots x",len(syms),"symbols =",len(sel)*len(syms))
jobs=[(s,sym) for s in sel for sym in syms]
bars=collections.defaultdict(dict)   # sym -> {open_ms: (high,low,close)}
def get(j):
    slot,sym=j
    try:
        b=s3.get_object(Bucket=B,Key=f"raw/{slot}/binance__{sym}.json")["Body"].read()
    except Exception:
        return sym,None
    return sym,json.loads(b)
t=time.time(); done=0; missing=0
with ThreadPoolExecutor(max_workers=128) as ex:
    for sym,doc in ex.map(get,jobs):
        done+=1
        if doc is None: missing+=1; continue
        d=bars[sym]
        for k in doc:
            d[int(k[0])]=(float(k[2]),float(k[3]),float(k[4]))
        if done%2000==0: print(f"  {done}/{len(jobs)}  {time.time()-t:.0f}s",flush=True)
print(f"read {done} bodies in {time.time()-t:.0f}s, missing bodies: {missing}")
out={s:{str(k):v for k,v in sorted(d.items())} for s,d in bars.items()}
json.dump(out,open(SP+"/bars.json","w"))
cnt={s:len(d) for s,d in bars.items()}
mn=min(cnt.values()); mx=max(cnt.values())
print("bars per symbol: min",mn,"max",mx)
allt=sorted(bars[syms[0]].keys())
f=lambda m: dt.datetime.fromtimestamp(m/1000,dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
print("bar span:",f(allt[0]),"->",f(allt[-1]))
# contiguity check per symbol
gaps={s:sum(1 for a,b in zip(sorted(d),sorted(d)[1:]) if b-a!=60000) for s,d in bars.items()}
print("symbols with any 1-min gap:",sum(1 for v in gaps.values() if v),"; total gap points:",sum(gaps.values()))
