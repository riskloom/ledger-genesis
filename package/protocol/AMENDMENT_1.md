# Prospective Evaluation Protocol v1.0 — Amendment 1

**Dated:** 2026-09-07
**Status:** Recorded before any prospective outcome was opened or calculated.
**Parent document:** RiskLoom_Prospective_Evaluation_Protocol_v1.0.pdf
**Parent SHA-256:** 9ebf02e41ea4b45f707cf029be68e41f26aba9ec578c4ec52a15bed71d168127
**Parent freeze time:** 2026-09-07T15:19:24Z

This amendment resolves implementation ambiguity only. It does not change any
price threshold, horizon, warning definition, baseline construction, episode
rule, majors classification, exclusion principle or performance metric in the
frozen protocol.

Issued under the protocol's own rule: "If a defect is found later it is
disclosed as an amendment with its date, never applied silently."

---

## 1. C0 — ANCHOR PRICE

C0 is the close of the final fully closed one-minute Binance kline available at
the anchor instant S:

    open_time  = S - 60,000 ms
    close_time = S

Do not use the one-minute bar opening at S, because its close occurs after the
anchor and would introduce post-anchor information.

## 2. FORWARD-EVIDENCE BOUNDARY

Layer 2 forward price evidence is confined to the sealed 2,016-observation soak
window:

    2026-08-30T14:55:00Z through 2026-09-06T14:55:00Z

Do not use retained bodies from observations after the sealed window to extend
forward coverage.

If an anchor lacks complete forward coverage within the sealed window for a
given horizon, exclude it from that horizon only, exactly as specified in
Protocol v1.0, and report the excluded count.

## 3. LAYER 1 DESCRIPTIVE REPORTING

For incidence, report slot count and share.

For duration, report:
  - number of continuous runs
  - mean run duration in minutes
  - median run duration in minutes

These are descriptive statistics only and must not be used as predictive
performance measures.

---

## Origin

Both ambiguities were identified by inspection of the frozen protocol text and
the retained evidence structure, and reported to the owner BEFORE any outcome
was inspected or calculated. The owner issued the resolutions above. No outcome
data informed either resolution.
