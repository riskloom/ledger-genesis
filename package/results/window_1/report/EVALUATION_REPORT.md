# Prospective Evaluation — Window 1 — Completed Report

Protocol v1.0 + Amendment 1 implemented literally. Nothing tuned after results were visible.

Evidence base: 2,016 ledger rows, 69 symbols, universe consistent on every row.
Price: 10,136 contiguous 1-minute bars per symbol from retained klines,
2026-08-30T13:55Z to 2026-09-06T14:50Z, zero gaps in any symbol, so all exclusions
below are tail-coverage only.

## 1. Layer 1 — structural state (descriptive)

Per-symbol bands — 139,104 symbol-slot observations:

| Band | Slots | Share | Runs | Mean | Median |
|---|---|---|---|---|---|
| NORMAL | 136,690 | 98.265% | 801 | 853.2 min | 255 min |
| ELEVATED | 2,328 | 1.674% | 738 | 15.8 min | 15 min |
| CASCADE_PRESSURE | 86 | 0.062% | 35 | 12.3 min | 15 min |

Market state — 2,016 slots:

| State | Slots | Share | Runs | Mean | Median |
|---|---|---|---|---|---|
| QUIET | 1,014 | 50.298% | 186 | 27.3 min | 20 min |
| BUILDING | 624 | 30.952% | 244 | 12.8 min | 10 min |
| ELEVATED | 249 | 12.351% | 118 | 10.6 min | 10 min |
| STRESSED | 129 | 6.399% | 48 | 13.4 min | 15 min |
| UNKNOWN | 0 | 0.000% | 0 | - | - |

Descriptive only. Not a performance measure.

## 2-4. Layer 2 — full grid

Denominators: 733 warning episodes (700 max-ELEVATED, 33 max-CASCADE_PRESSURE);
2,898 NORMAL baseline anchors (69 x 42).

Full numeric grids for OVERALL, MAJORS, NON-MAJORS are in
`report/run_log_04_grid.txt` and machine-readable in `data/layer2.json`.
Max-state split is in `report/run_log_05_maxstate.txt`.

Headline structure, reported without selection:

- OVERALL: direction of effect positive in all 16 cells. Absolute lift ranges
  +8.30pp (5%/30m) to +40.90pp (1%/30m). Relative incidence 1.122 to 9.299.
- MAJORS: substantially weaker. 5%/30m and 5%/60m warning incidence 0.00%.
  3%/60m lift +1.59pp. Relative incidence undefined in four cells because
  NORMAL incidence is exactly zero (3%/30m, 5%/30m, 5%/60m, 5%/120m).
  The largest ratio in the grid, majors 2%/30m at 45.303x, rests on a baseline
  of 1 hit in 336 anchors and is an artefact of a near-zero denominator.
- NON-MAJORS: supplies 639 of 733 episodes and carries the overall result.
- max-CASCADE_PRESSURE (n=33): largest lifts at every cell, on a small
  denominator. Stated as measured, not as a claim.

## 5 & 7. Per-symbol detail and denominators

Full table at the 2%/60m reference cell in `report/run_log_06_per_symbol.txt`.
Structure, not claims:

- Top 5 symbols hold 33.0% of all 733 episodes. MAGMAUSDT (67) and ARBUSDT (65)
  alone account for 132.
- 4 symbols produced zero episodes (ALLO, SKYAI, STG, TON).
- Only 18 of 69 symbols ever reached CASCADE_PRESSURE.
- Several symbols show warning incidence at or below their own baseline at this
  cell: BNBUSDT 0.0% vs 4.8%; TRXUSDT 0.0% vs 0.0%; XAUUSDT 0.0% vs 0.0%;
  LTCUSDT 0.0% vs 2.4%; BTCUSDT 0.0% vs 0.0%.
- Symbols showing 100% warning incidence (CLO, PORTAL, RIF, VELVET, BEAT, SENT)
  have 1-8 episodes each.

Per-symbol counts are single and double digit and are shown so concentration
cannot be hidden. No claim rests on them.

## 6. Exclusions — incomplete forward coverage

Tail-coverage only; no gaps existed mid-series. Never counted as a miss or a
false positive.

| Horizon | Warning excluded | Baseline excluded |
|---|---|---|
| 30 min | 13 of 733 | 0 of 2,898 |
| 60 min | 13 of 733 | 0 of 2,898 |
| 120 min | 14 of 733 | 0 of 2,898 |
| 240 min | 18 of 733 | 69 of 2,898 |

Baseline exclusions appear only at 240 min because the fixed 240-minute stride
puts exactly one terminal anchor per symbol (69) beyond full coverage.

## Summary — what the frozen test demonstrated, and what it did not

DEMONSTRATED. Across the sealed seven days, states RiskLoom precommitted to the
ledger preceded larger absolute price displacement than fixed-stride NORMAL
anchors on the same symbols, same grid, same definitions. The direction of the
effect is positive in all 16 overall cells, on both absolute lift (+8.30 to
+40.90 pp) and relative incidence (1.12x to 9.30x). The result holds in the
non-majors cohort, which supplies 639 of 733 episodes.

ALSO DEMONSTRATED, AND UNFAVOURABLE. The effect is substantially weaker in
majors. At 5%/30m and 5%/60m, majors warning incidence is 0.00% - no episode
reached a 5% move - and at 3%/60m the lift is +1.59pp. Four majors-cohort
symbols show warning incidence at or below their own baseline at the reference
cell. The single largest relative figure in the whole grid, majors 2%/30m at
45.3x, rests on a baseline of 1 hit in 336 anchors; that ratio is an artefact of
a near-zero denominator, not a strong result, which is why the protocol requires
the absolute lift (+13.19pp) beside it.

NOT DEMONSTRATED. No directional claim - displacement is absolute, and RiskLoom
publishes no side. No causal claim; the test measures precedence, not mechanism.
No claim about tradeable edge: no costs, slippage, execution or position sizing
enter this. Nothing about liquidation-cascade prediction, which was deliberately
excluded from Layer 2 as tautological. No statistical significance: no test or
confidence interval was predeclared, so none is computed or implied - every
figure is a raw incidence on the stated denominator. No claim of stability: this
is one seven-day window in one regime, and 33% of episodes come from five
symbols. Layer 1 and Layer 2 are not combined, and no cell is selected as
headline.

Nothing was tuned, excluded, or adjusted after results were visible.
