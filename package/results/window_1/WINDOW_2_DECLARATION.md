# Window 2 — Predeclared Replication Boundary

**Declared:** 2026-09-07 (see manifest for exact archive timestamp)
**Status at declaration:** NOT RUN. No Window 2 outcome has been inspected,
computed, or observed by anyone, including the operator declaring it.

## Boundary — fixed now

    start (inclusive)  2026-09-08T00:00:00Z
    end   (exclusive)  2026-09-15T00:00:00Z

    first slot         2026-09-08T00:00:00Z
    last  slot         2026-09-14T23:55:00Z
    expected slots     2,016   (7 days x 288 five-minute slots)

Contiguous seven days on the live pipeline's five-minute slot grid. The start is
in the future relative to this declaration, so no part of the window had
occurred when the boundary was fixed.

Window 1 for reference: 2026-08-30T14:55:00Z to 2026-09-06T14:55:00Z, also 2,016
observations. Window 2 is not adjacent to Window 1; the interval between them is
not evaluated and forms no part of either window.

## Terms of the replication

Window 2 is a REPLICATION under identical frozen definitions.

No parameter, threshold, horizon, exclusion or definition may differ from
Window 1. Specifically and without limitation:

- Protocol v1.0 applies unchanged.
  SHA-256 9ebf02e41ea4b45f707cf029be68e41f26aba9ec578c4ec52a15bed71d168127
- Amendment 1 applies unchanged.
  SHA-256 f6a8d80c7da1cf1687eae39b7bdd40d8cd7e23197e3982d4643f9c668753b60c
- Displacement thresholds: 1%, 2%, 3%, 5%. No others, none removed.
- Horizons: 30, 60, 120, 240 minutes. No others, none removed.
- Material price event definition, including C0 per Amendment 1 section 1.
- Warning episode construction: one episode one anchor, first non-NORMAL slot,
  escalation stays one episode, episode ends at first return to NORMAL.
- NORMAL baseline anchors: fixed 240-minute stride, non-overlapping.
- Frozen majors list, eight symbols: BTC, ETH, SOL, XRP, ADA, BNB, LINK, DOGE.
- Exclusions: incomplete forward coverage only, per horizon, applied identically
  to warning and baseline anchors, never counted as a miss or false positive.
- Forward-evidence boundary confined to the Window 2 sealed record, per
  Amendment 1 section 2 applied to Window 2's own start and end.
- Reporting: all sixteen cells, four figures each, three cohort levels plus
  per-symbol detail. No preferred cell. No best horizon.
- Layer 1 and Layer 2 not combined into any single figure.

The 69-symbol universe and the per-symbol thresholds are whatever the pipeline
prospectively commits during Window 2; they are not re-pinned to Window 1's set.
If they differ, that difference is a fact about the window and is reported, not
corrected. Any such difference must be disclosed alongside the Window 2 results.

## Prohibited

No parameter may be tuned against Window 2 outcome data. No cell may be selected
as headline after seeing results. No exclusion may be added after opening. The
majors list may not be changed. If Window 2 results are weak, neutral or
negative, they are reported exactly as they are.

If Window 2 replicates Window 1, that is evidence. If it does not, that is also
evidence, and it is reported with equal prominence.
