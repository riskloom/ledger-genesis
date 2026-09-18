import json,statistics,datetime as dt
SP="/private/tmp/claude-501/-Users-uikegulu-Desktop-riskloom/bcfd7437-1f90-4db4-a2c9-525c7a102a2a/scratchpad/w2"
rows=json.load(open(SP+"/ledger_window.json")); syms=json.load(open(SP+"/universe.json"))
def ms(s): return int(dt.datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp()*1000)
slots=[ms(r[0]) for r in rows]
SLOT=300000
# ---------- LAYER 1 ----------
band_counts={b:0 for b in ("NORMAL","ELEVATED","CASCADE_PRESSURE")}
per_sym_bands={s:{b:0 for b in band_counts} for s in syms}
for r in rows:
    for s,b in r[2].items():
        band_counts[b]+=1; per_sym_bands[s][b]+=1
mkt_counts={}
for r in rows: mkt_counts[r[1]]=mkt_counts.get(r[1],0)+1

def runs_of(seq, target):
    """contiguous runs where value==target; returns list of run lengths in slots"""
    out=[];cur=0
    for v in seq:
        if v==target: cur+=1
        else:
            if cur: out.append(cur); cur=0
    if cur: out.append(cur)
    return out

band_runs={b:[] for b in band_counts}
for s in syms:
    seq=[r[2][s] for r in rows]
    for b in band_counts: band_runs[b]+=runs_of(seq,b)
mkt_seq=[r[1] for r in rows]
mkt_runs={st:runs_of(mkt_seq,st) for st in set(mkt_seq)}

def dur(rl):
    if not rl: return (0,None,None)
    m=[x*5 for x in rl]
    return (len(m), round(statistics.mean(m),1), round(statistics.median(m),1))

L1={"total_rows":len(rows),"symbol_slot_observations":len(rows)*len(syms),
    "bands":{b:{"slots":band_counts[b],"share_pct":round(100*band_counts[b]/(len(rows)*len(syms)),3),
                "runs":dur(band_runs[b])[0],"mean_min":dur(band_runs[b])[1],"median_min":dur(band_runs[b])[2]}
             for b in band_counts},
    "market_states":{st:{"slots":mkt_counts.get(st,0),"share_pct":round(100*mkt_counts.get(st,0)/len(rows),3),
                "runs":dur(mkt_runs.get(st,[]))[0],"mean_min":dur(mkt_runs.get(st,[]))[1],"median_min":dur(mkt_runs.get(st,[]))[2]}
             for st in ("QUIET","BUILDING","ELEVATED","STRESSED","UNKNOWN")},
    "per_symbol":{s:{b:per_sym_bands[s][b] for b in band_counts} for s in syms}}
json.dump(L1,open(SP+"/layer1.json","w"),indent=1)

# ---------- ANCHORS ----------
episodes=[]   # symbol, anchor_ms, max_state, length_slots
for s in syms:
    seq=[r[2][s] for r in rows]
    i=0
    while i<len(seq):
        if seq[i]!="NORMAL":
            j=i; mx="ELEVATED"
            while j<len(seq) and seq[j]!="NORMAL":
                if seq[j]=="CASCADE_PRESSURE": mx="CASCADE_PRESSURE"
                j+=1
            episodes.append({"symbol":s,"anchor":slots[i],"max_state":mx,"len_slots":j-i})
            i=j
        else: i+=1
# NORMAL baseline anchors: walk NORMAL slots, take first, then skip forward 240 min
STRIDE=240*60*1000
baseline=[]
for s in syms:
    seq=[r[2][s] for r in rows]
    last=None
    for i,v in enumerate(seq):
        if v!="NORMAL": continue
        t=slots[i]
        if last is None or t>=last+STRIDE:
            baseline.append({"symbol":s,"anchor":t}); last=t
json.dump(episodes,open(SP+"/episodes.json","w"))
json.dump(baseline,open(SP+"/baseline.json","w"))
print("=== LAYER 1 ===")
print("symbol-slot observations:",L1["symbol_slot_observations"])
for b,v in L1["bands"].items(): print(f"  {b:18s} slots={v['slots']:7d} share={v['share_pct']:7.3f}%  runs={v['runs']:5d} mean={v['mean_min']} median={v['median_min']}")
print("market states (of 2016 rows):")
for st,v in L1["market_states"].items(): print(f"  {st:10s} slots={v['slots']:5d} share={v['share_pct']:7.3f}%  runs={v['runs']:4d} mean={v['mean_min']} median={v['median_min']}")
print()
print("warning episodes :",len(episodes), " (ELEVATED-max:",sum(1 for e in episodes if e['max_state']=='ELEVATED'),
      " CASCADE_PRESSURE-max:",sum(1 for e in episodes if e['max_state']=='CASCADE_PRESSURE'),")")
print("baseline anchors :",len(baseline))
