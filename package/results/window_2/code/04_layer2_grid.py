import json
SP="/private/tmp/claude-501/-Users-uikegulu-Desktop-riskloom/bcfd7437-1f90-4db4-a2c9-525c7a102a2a/scratchpad/w2"
bars={s:{int(k):v for k,v in d.items()} for s,d in json.load(open(SP+"/bars.json")).items()}
eps=json.load(open(SP+"/episodes.json")); base=json.load(open(SP+"/baseline.json"))
MAJ={"BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","ADAUSDT","BNBUSDT","LINKUSDT","DOGEUSDT"}
HOR=[30,60,120,240]; THR=[0.01,0.02,0.03,0.05]
MAXT=max(max(d) for d in bars.values())

def disp(sym,S,H):
    d=bars[sym]
    c0=d.get(S-60000)
    if c0 is None: return None,"no_c0"
    C0=c0[2]
    need=[S+i*60000 for i in range(H)]
    if need[-1]>MAXT: return None,"incomplete"
    hi=[];lo=[]
    for t in need:
        b=d.get(t)
        if b is None: return None,"incomplete"
        hi.append(b[0]); lo.append(b[1])
    return max((max(hi)-C0)/C0,(C0-min(lo))/C0),None

def evaluate(anchors):
    """-> {H: {'n':n_eval,'excl':n_excluded,'disp':[...]}} """
    out={}
    for H in HOR:
        vals=[];ex=0
        for a in anchors:
            v,err=disp(a["symbol"],a["anchor"],H)
            if v is None: ex+=1
            else: vals.append(v)
        out[H]={"n":len(vals),"excl":ex,"disp":vals}
    return out

def subset(lst,pred): return [a for a in lst if pred(a)]
groups={
 "overall":   (eps, base),
 "majors":    (subset(eps,lambda a:a["symbol"] in MAJ), subset(base,lambda a:a["symbol"] in MAJ)),
 "non_majors":(subset(eps,lambda a:a["symbol"] not in MAJ), subset(base,lambda a:a["symbol"] not in MAJ)),
 "max_ELEVATED":(subset(eps,lambda a:a["max_state"]=="ELEVATED"), base),
 "max_CASCADE_PRESSURE":(subset(eps,lambda a:a["max_state"]=="CASCADE_PRESSURE"), base),
}
res={}
for g,(w,b) in groups.items():
    W=evaluate(w); B=evaluate(b)
    res[g]={"warn_total":len(w),"base_total":len(b),"cells":{}}
    for H in HOR:
        for t in THR:
            wn=W[H]["n"]; bn=B[H]["n"]
            wi=100*sum(1 for v in W[H]["disp"] if v>=t)/wn if wn else None
            bi=100*sum(1 for v in B[H]["disp"] if v>=t)/bn if bn else None
            res[g]["cells"][f"{int(t*100)}%_{H}m"]={
              "warn_n":wn,"warn_excl":W[H]["excl"],"warn_hits":sum(1 for v in W[H]["disp"] if v>=t),
              "base_n":bn,"base_excl":B[H]["excl"],"base_hits":sum(1 for v in B[H]["disp"] if v>=t),
              "warn_inc_pct":None if wi is None else round(wi,2),
              "base_inc_pct":None if bi is None else round(bi,2),
              "abs_lift_pp":None if (wi is None or bi is None) else round(wi-bi,2),
              "rel_inc":None if (wi is None or bi is None or bi==0) else round(wi/bi,3)}
json.dump(res,open(SP+"/layer2.json","w"),indent=1)

for g in ("overall","majors","non_majors"):
    r=res[g]
    print(f"\n===== {g.upper()}  (warning episodes {r['warn_total']}, baseline anchors {r['base_total']}) =====")
    print(f"{'cell':>10} | {'warn n':>6} {'excl':>5} | {'base n':>6} {'excl':>5} | {'warn%':>7} {'norm%':>7} {'lift pp':>8} {'rel':>6}")
    for t in THR:
        for H in HOR:
            c=r["cells"][f"{int(t*100)}%_{H}m"]
            print(f"{int(t*100)}%/{H:>3}m | {c['warn_n']:6d} {c['warn_excl']:5d} | {c['base_n']:6d} {c['base_excl']:5d} | "
                  f"{c['warn_inc_pct']:7.2f} {c['base_inc_pct']:7.2f} {c['abs_lift_pp']:8.2f} {str(c['rel_inc']):>6}")
