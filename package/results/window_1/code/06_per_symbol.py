import json
SP="/private/tmp/claude-501/-Users-uikegulu/af28e28a-7715-44ff-8b9b-eccaa835c956/scratchpad"
bars={s:{int(k):v for k,v in d.items()} for s,d in json.load(open(SP+"/bars.json")).items()}
eps=json.load(open(SP+"/episodes.json")); base=json.load(open(SP+"/baseline.json"))
L1=json.load(open(SP+"/layer1.json"))
MAJ={"BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","ADAUSDT","BNBUSDT","LINKUSDT","DOGEUSDT"}
MAXT=max(max(d) for d in bars.values())
def disp(sym,S,H):
    d=bars[sym]; c0=d.get(S-60000)
    if c0 is None: return None
    C0=c0[2]; need=[S+i*60000 for i in range(H)]
    if need[-1]>MAXT: return None
    hi=[];lo=[]
    for t in need:
        b=d.get(t)
        if b is None: return None
        hi.append(b[0]); lo.append(b[1])
    return max((max(hi)-C0)/C0,(C0-min(lo))/C0)
# per-symbol: 2% / 60m reference cell only, plus episode/anchor counts
by={}
for s in sorted(bars):
    we=[e for e in eps if e["symbol"]==s]; ba=[b for b in base if b["symbol"]==s]
    wv=[disp(s,e["anchor"],60) for e in we]; bv=[disp(s,b["anchor"],60) for b in ba]
    wv2=[v for v in wv if v is not None]; bv2=[v for v in bv if v is not None]
    by[s]={"maj":s in MAJ,"eps":len(we),"anch":len(ba),
      "w_n":len(wv2),"w_hit":sum(1 for v in wv2 if v>=0.02),
      "b_n":len(bv2),"b_hit":sum(1 for v in bv2 if v>=0.02),
      "cp_slots":L1["per_symbol"][s]["CASCADE_PRESSURE"],"el_slots":L1["per_symbol"][s]["ELEVATED"]}
print("PER-SYMBOL DETAIL — reference cell 2% / 60 min (visible, not used for claims)")
print(f"{'symbol':<16}{'maj':>4}{'eps':>5}{'w_n':>5}{'w_hit':>6}{'warn%':>8}{'anch':>6}{'b_hit':>6}{'norm%':>8}{'ELEV':>6}{'CASC':>6}")
for s,v in sorted(by.items(), key=lambda kv:(-kv[1]["eps"],kv[0])):
    wp=100*v["w_hit"]/v["w_n"] if v["w_n"] else float('nan')
    bp=100*v["b_hit"]/v["b_n"] if v["b_n"] else float('nan')
    print(f"{s:<16}{'Y' if v['maj'] else '':>4}{v['eps']:5d}{v['w_n']:5d}{v['w_hit']:6d}{wp:8.1f}{v['anch']:6d}{v['b_hit']:6d}{bp:8.1f}{v['el_slots']:6d}{v['cp_slots']:6d}")
print()
print("episodes concentration: top 5 symbols hold",
      round(100*sum(sorted([v['eps'] for v in by.values()],reverse=True)[:5])/sum(v['eps'] for v in by.values()),1),"% of all episodes")
print("symbols with 0 episodes:",sum(1 for v in by.values() if v['eps']==0))
print("symbols with >=1 CASCADE_PRESSURE slot:",sum(1 for v in by.values() if v['cp_slots']>0))
