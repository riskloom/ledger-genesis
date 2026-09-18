import json
SP="/private/tmp/claude-501/-Users-uikegulu/af28e28a-7715-44ff-8b9b-eccaa835c956/scratchpad"
res=json.load(open(SP+"/layer2.json"))
HOR=[30,60,120,240]; THR=[1,2,3,5]
for g in ("max_ELEVATED","max_CASCADE_PRESSURE"):
    r=res[g]
    print(f"\n===== {g} (episodes {r['warn_total']}, baseline {r['base_total']}) =====")
    print(f"{'cell':>10} | {'warn n':>6} {'excl':>4} | {'warn%':>7} {'norm%':>7} {'lift pp':>8} {'rel':>6}")
    for t in THR:
        for H in HOR:
            c=r["cells"][f"{t}%_{H}m"]
            print(f"{t}%/{H:>3}m | {c['warn_n']:6d} {c['warn_excl']:4d} | {c['warn_inc_pct']:7.2f} {c['base_inc_pct']:7.2f} {c['abs_lift_pp']:8.2f} {str(c['rel_inc']):>6}")
