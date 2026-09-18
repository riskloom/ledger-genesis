# What an outsider can verify, what needs controlled access, and why

This package does not claim to be fully reproducible from public data. Two of
the six evaluation stages read RiskLoom-private infrastructure and cannot be
re-run by anyone without access to it. This document says exactly where that
line falls. Nothing is padded to look more complete than it is.

---

## 1. Fully verifiable by anyone, offline, with no RiskLoom access

**Integrity of the package.** `./verify.sh` confirms every file's digest matches
the commitment manifest, that the manifest lists exactly the files present, and
that the manifest reproduces byte-exactly under the published construction.

**The external commitment.** `./verify.sh --tlog` confirms the package root is
signed by this repository's GitHub Actions identity and recorded in the public
Sigstore transparency log. RiskLoom does not operate that log.

**The arithmetic of the evaluation.** `./reproduce.sh` re-runs stages 02, 04, 05
and 06 for both windows using only files shipped in this package, and compares
the result byte-for-byte with the archived output. At time of publication it
reproduces **all eight output files and all six archived stdout logs
byte-identically**, for both windows.

That is the substantive part. Given the ledger snapshot and the bar data, an
outsider can confirm without trusting RiskLoom that:

- the Layer 1 state counts, runs and durations are what the reports say;
- the warning episodes and the fixed-stride NORMAL baseline anchors were
  constructed as the protocol specifies, and number what the reports say;
- all 16 Layer 2 cells, at every cohort level, the max-state split and the
  per-symbol detail follow arithmetically from those inputs;
- the exclusion rule was applied identically to warning and baseline anchors;
- no parameter differs between Window 1 and Window 2.

**Cross-checking the reports against the data.** The evaluation reports are
re-presentations of `data/layer1.json` and `data/layer2.json`. Both are here.
Any figure in a report can be traced to the JSON it came from.

**Consistency of the frozen documents.** Protocol v1.0, Amendment 1 and the
Window 2 declaration are here with their digests. The digests pinned inside the
Window 2 declaration match the documents shipped alongside it, and the boundary
the declaration names matches the boundary Window 2 was evaluated over.

## 2. Needs controlled access — and cannot be made public

**Stage 01, the ledger read.** `01_load_ledger.py` reads `public_state_log` from
an Aurora database through the RDS Data API. Its output, `ledger_window.json`,
is shipped here. An outsider can read the query in the script and see exactly
what was selected, but cannot re-execute it.

**Stage 03, the raw bar read.** `03_build_price_series.py` reads per-slot Binance
kline bodies from a private S3 prefix. Its output, `bars.json`, is shipped here.
Same position: the code is legible, the read is not repeatable without access.

**Why these are not opened.** The database holds the live pipeline's operational
state and the raw prefix holds 313,723 objects under an audited append-only
invariant. Granting public read to either would expose infrastructure that the
evaluation's own integrity depends on. The correct remedy is a controlled audit,
not a public credential.

**What this means.** An outsider is trusting RiskLoom on exactly one thing: that
`ledger_window.json` and `bars.json` faithfully represent what the live ledger
and the exchange actually recorded. Everything downstream of those two files is
independently checkable, and has been checked. Everything upstream is Class A.

**What would close it.** An auditor granted read-only access to the archive and
the clone could re-run stages 01 and 03 and compare their output to the files
here. That is a controlled audit that RiskLoom can arrange. It has not been
performed. Until it is, this gap is open and is stated as open.

## 3. Two files are redacted

`package/results/window_1/code/INVOCATION.redacted.md` and its Window 2
counterpart are **not** byte-identical to the archive. Two lines in each were
replaced: the ARNs of the Aurora cluster and of the Secrets Manager secret that
holds that cluster's credentials. They are resource identifiers rather than
credentials and confer no access on their own, but they name a credential store.

The archived originals' SHA-256 values are recorded in the window manifests
shipped here, and are repeated at the head of each redacted file, so the
withholding is itself auditable: an auditor with archive access can confirm the
original hashes to what the manifest says, and confirm that the only difference
from the published copy is those two lines.

The other **48 of 50** files under `package/` are byte-identical to the archive.
`PROVENANCE.md` is the file-by-file map.

### Infrastructure identifiers that are deliberately retained

Removing these would break byte-identity with the archive for most of the
package, which would defeat the point of publishing it. They are named here so
their presence is a recorded decision, not an oversight. None is a credential
and none grants access.

| Retained | Where | Why it is not withheld |
|---|---|---|
| AWS account IDs `361964630357`, `587788487647` | scripts, invocation records | An account ID is an identifier, not a secret; it appears in every ARN AWS asks you to share. |
| S3 bucket name `rl-raw-inputs-361964630357` | `03_build_price_series.py` | Names the private bucket the raw bars were read from. The bucket is not publicly readable; knowing its name confers nothing. |
| `arn:aws:iam::361964630357:role/OrganizationAccountAccessRole` | invocation records | The AWS-default organisation role name, present in every AWS Organizations member account. It is assumable only by already-trusted principals. |
| `arn:aws:kms:eu-west-2:361964630357:key/e39876f8-…` | Window 2 report | The identity of the key that signed every ledger row. Publishing it is useful to a verifier and it is a key *identifier*, never key material. |
| The operator workstation path, which contains a local username | scripts, invocation records | Part of the verbatim source text of the executed scripts. It is the operator's own username, not a third party's. |

What is withheld is the pair named above: the Aurora cluster ARN and the
Secrets Manager secret ARN. Those are the only values in the corpus that name a
credential store.

## 4. What is deliberately still Class A

The transparency-log anchor covers the package, created after both evaluations.
It is retrospective and the README says so. It does not evidence:

- that Window 1's results were computed before anyone looked at them;
- that the Window 2 declaration was truly written before the window opened;
- that the ledger was not rewritten before the snapshot was taken.

Those rest on RiskLoom-controlled timestamps, S3 Object Lock and the ledger's
internal hash chain. All are real controls and all are operated by the party
making the claim. Windows 1 and 2 can never retroactively become anything else.

**Window 3 is the exception, and it is not retrospective.** Its boundary and its
pinned methodology are in `WINDOW_3_DECLARATION.md`, committed to the public
transparency log before the window opened. Its ordering is checkable against a
log RiskLoom does not operate. Window 3 has not been run and no outcome has been
observed; when it is reported, the ordering claim will stand or fall on that log
entry rather than on anything RiskLoom timestamps.

## 5. A known weakness in the archive itself, disclosed

`package/results/window_2/ARCHIVAL_INCIDENT.md` records an operator error during
archival: an Object Lock test was run against the live manifest key rather than
a scratch key, and for 38 seconds a 7-byte file was the current version of
`MANIFEST.json`. The correct manifest was restored and is current. The incorrect
version is permanently undeletable under COMPLIANCE lock and remains in the
version history.

It is in this package because omitting it would misrepresent the archive. It
also demonstrates something worth stating plainly: COMPLIANCE-mode Object Lock
protects every *version* from alteration, but does not prevent a new version
becoming current. Immutability of history is not the same as immutability of the
current pointer.

## 6. What this package does not establish about the results

The evaluation's own conclusions are in §7 of the Window 2 report and are not
weakened or strengthened here. In particular this package does not establish any
predictive accuracy figure, does not establish a stable effect magnitude, and
does not establish anything about the majors cohort or the CASCADE_PRESSURE
split, both of which rest on small episode counts.

> Two windows are two observations. The direction replicated; the magnitude did
> not.
