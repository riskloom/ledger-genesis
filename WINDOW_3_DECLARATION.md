# Window 3 — Predeclared Replication Boundary

**Declared:** 2026-09-18, and externally committed to the public Sigstore
transparency log before the boundary below opens. Window 3 is the first
RiskLoom window whose declaration is anchored *before* observation rather than
after. See "External commitment" at the end of this document.

**Status at declaration:** NOT RUN. No Window 3 outcome has been inspected,
computed, or observed by anyone, including the operator declaring it. No part of
the window had occurred when this boundary was fixed.

## Boundary — fixed now

    start (inclusive)  2026-09-20T00:00:00Z
    end   (exclusive)  2026-09-27T00:00:00Z

    first slot         2026-09-20T00:00:00Z
    last  slot         2026-09-26T23:55:00Z
    expected slots     2,016   (7 days x 288 five-minute slots)

Contiguous seven days on the live pipeline's five-minute slot grid, identical in
length and grid alignment to Windows 1 and 2.

For reference, and forming no part of Window 3:

    Window 1   2026-08-30T14:55:00Z to 2026-09-06T14:55:00Z   2,016 slots
    Window 2   2026-09-08T00:00:00Z to 2026-09-15T00:00:00Z   2,016 expected

Window 3 is not adjacent to Window 2. The interval between them
(2026-09-15T00:00:00Z to 2026-09-20T00:00:00Z) is not evaluated and forms no
part of any window.

## Pinned methodology — the exact documents Window 3 commits to

Window 3 is evaluated under these and only these. Each is pinned by SHA-256. If
the document used at evaluation time does not hash to the value below, the
evaluation is void and must be reported as void.

    Protocol v1.0                    9ebf02e41ea4b45f707cf029be68e41f26aba9ec578c4ec52a15bed71d168127
      disclosure/protocol/RiskLoom_Prospective_Evaluation_Protocol_v1.0.pdf
      frozen 2026-09-07T15:19:24Z

    Amendment 1                      f6a8d80c7da1cf1687eae39b7bdd40d8cd7e23197e3982d4643f9c668753b60c
      disclosure/protocol/AMENDMENT_1.md
      archived 2026-09-07T15:57:56Z

Both are published in this repository at `package/protocol/` and can be hashed
directly.

## Pinned configuration — thresholds and pipeline build

    thresholds.json (file)           abaf499d9089fd363dd6fdd6f5b1be59177dccb99520b16f9ed1913de83232d3
      disclosure/thresholds/thresholds.json, published at package/thresholds/

    thresholds_digest                0568f24ceb798001ecffed6d9101c4c863d1e6c0f5718f1d5aedc70151cfb25d
      the production canonicalisation (pipeline.digests.thresholds_digest),
      committed on every in-window ledger row of Windows 1 and 2

    code_digest (pipeline build)     855fe324b44521aef5d6b1dc90c5be4bf115c9c242d92dbddcd5bdae44571dc9
      the observing Lambda bundle, committed on every in-window ledger row of
      Windows 1 and 2

`thresholds_digest` and `code_digest` are values the live pipeline commits onto
each ledger row as it writes it. They are therefore prospective by construction:
they are recorded during the window, not chosen afterwards.

**If either digest differs on any Window 3 in-window row from the value above,
that is a fact about the window and must be reported alongside the results, in
full, with the affected row count. It must not be corrected, back-filled,
excluded, or quietly reconciled.** A changed pipeline build or calibration set
during Window 3 does not invalidate the window; concealing it would.

The 69-symbol universe and the per-symbol thresholds are whatever the pipeline
prospectively commits during Window 3; they are not re-pinned to Window 1's or
Window 2's set. If they differ, that difference is reported, not corrected.

## Pinned evaluation implementation

Window 3 is evaluated by the same six scripts that evaluated Window 2, whose
archived SHA-256 values are:

    01_load_ledger.py                33ff8681bc99cef83f8d23b9b787cdda3d7d4ebca24d8be7d4d1b1f9ef2eaf9e
    02_layer1_and_anchors.py         1176b7465361fdee658e7aa41256034cbda844262096d9b0a9cbb97a0f90fb32
    03_build_price_series.py         1625c1bf48e1c640336d8e15bbb6c30bf00f6878d5e193cee4c1469b740702a5
    04_layer2_grid.py                ad41963494f6251198701321f2d9e49ea2681ecfdf6ee73567a0113cb3103a4b
    05_maxstate_split.py             87370fdd825f810c123646337957e492b5c06dd6bf1a6abd01ae2a901929b253
    06_per_symbol.py                 edd19d758304e30162374a1b105068dcb244bcc725fed681d2790b22f028b505

These are the exact file objects the interpreter opened for Window 2. They are
published in this repository at `package/results/window_2/code/` and can be
hashed directly.

The Window 3 scripts will not hash to these values, because two constants must
change. They are permitted to differ from the files above in exactly two ways
and no other:

1. the scratchpad path constant `SP`;
2. in `01_load_ledger.py` only, the two window-boundary timestamp literals,
   which become `2026-09-20T00:00:00Z` and `2026-09-27T00:00:00Z`.

**The count of non-path, non-boundary differences must be ZERO in all six
files**, established by diffing against the published Window 2 originals and
reported as such. This is the same derivation rule, and the same proof
obligation, that produced Window 2 from Window 1.

No methodological logic, definition, threshold, horizon, cohort, exclusion or
reporting rule may be changed. Any edit beyond the two constants above voids the
replication claim and must be disclosed as a new implementation, not as a
replication.

## Terms of the replication

Window 3 is a REPLICATION under identical frozen definitions. No parameter,
threshold, horizon, exclusion or definition may differ from Windows 1 and 2.
Specifically and without limitation:

- Displacement thresholds: 1%, 2%, 3%, 5%. No others, none removed.
- Horizons: 30, 60, 120, 240 minutes. No others, none removed.
- Material price event definition, including C0 per Amendment 1 section 1:
  C0 is the close of the final fully closed 1-minute Binance kline at the anchor
  instant S, that is open_time = S - 60000ms, close_time = S.
- Warning episode construction: one episode one anchor, first non-NORMAL slot,
  escalation stays one episode, episode ends at first return to NORMAL.
- NORMAL baseline anchors: fixed 240-minute stride, non-overlapping.
- Frozen majors list, eight symbols: BTC, ETH, SOL, XRP, ADA, BNB, LINK, DOGE.
- Exclusions: incomplete forward coverage only, per horizon, applied identically
  to warning and baseline anchors, never counted as a miss or false positive.
- Forward-evidence boundary confined to the Window 3 sealed record, per
  Amendment 1 section 2 applied to Window 3's own start and end.
- Reporting: all sixteen cells, four figures each, three cohort levels plus
  max-state split and per-symbol detail. No preferred cell. No best horizon.
- Layer 1 and Layer 2 not combined into any single figure.

## Prohibited

No parameter may be tuned against Window 3 outcome data. No cell may be selected
as headline after seeing results. No exclusion may be added after opening. The
majors list may not be changed. The boundary above may not be moved, extended,
shortened or re-aligned for any reason, including a pipeline outage inside the
window. Missing slots are reported as missing, exactly as Window 2's two missing
slots were.

If Window 3 results are weak, neutral or negative, they are reported exactly as
they are. If Window 3 replicates, that is evidence. If it does not, that is also
evidence, and it is reported with equal prominence.

Windows 1 and 2 found the direction replicating in all 16 overall cells while
the magnitude attenuated in 15 of 16. Window 3 is not being run to rescue the
magnitude. A third attenuation is a result, not a failure of the window.

## Lineage

    Window 2 declaration              39a9abcf41107d76ad6a30eec5d25a86d43a68fb6f8e0ada2b547c431d6dbb9e
      disclosure/results/window_1/WINDOW_2_DECLARATION.md
      published at package/results/window_1/

Window 2's declaration was archived to RiskLoom-controlled immutable storage
before its window opened. That ordering rests on RiskLoom's own timestamps and
is Class A. This declaration is different: it is committed to a transparency log
RiskLoom does not operate.

## External commitment

This file is part of the package committed by `SHA256SUMS`. The package root is
the SHA-256 of `SHA256SUMS`, signed with cosign keyless signing under the
workflow identity

    https://github.com/riskloom/ledger-genesis/.github/workflows/anchor-sha256sums.yml@refs/heads/main
    issuer https://token.actions.githubusercontent.com

and recorded in the public Sigstore transparency log at rekor.sigstore.dev.

The log entry's `integratedTime` is the moment this boundary became externally
witnessed. **That timestamp precedes 2026-09-20T00:00:00Z, and anyone can check
that it does.** The entry is append-only and cannot be withdrawn or backdated by
RiskLoom.

This is what Windows 1 and 2 cannot retroactively become, and it is the whole
purpose of fixing the boundary now rather than later.

Verification instructions are in `README.md`. The specific entry for this
declaration is identified there.
