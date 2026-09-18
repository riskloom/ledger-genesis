# RiskLoom — Windows 1 and 2 independent verification package

This repository contains the complete evidence for two prospective evaluation
windows of the RiskLoom structural-state pipeline: the frozen protocol, the
amendment, the predeclaration, the calibration set, the exact scripts that ran,
their inputs and outputs, the run logs, the manifests, the evaluation reports
including the Window 1 versus Window 2 comparison, and the archival incident
record.

Everything here is a copy of objects held in a private, versioned,
Object-Lock-protected archive. Every copied file's digest was checked against
the digest recorded for it in that archive's own manifest — manifests written
before this package existed. `PROVENANCE.md` is the file-by-file map: **48 of
50 files are byte-identical to their archived source; 2 are redacted and say
so at the top of the file.**

**You do not need to trust any of the above.** Sections below tell you how to
check it yourself, offline, in under a minute.

---

## Class A and Class B — read this before anything else

**Class A — internally consistent, hash-chained, append-only enforced, but every
guarantee rests on RiskLoom-controlled infrastructure.**
Windows 1 and 2 are Class A. The ledger they were computed from is hash-chained
and signed, each row carries a committed code digest and threshold digest, and
the archive is under S3 Object Lock in COMPLIANCE mode. All of that is real, and
all of it is operated by RiskLoom. An outsider cannot distinguish it from an
equally well-constructed fabrication, because the party making the claim also
controls the infrastructure that attests to it.

**Class B — externally committed to an independently operated transparency log.**
The *package* is Class B. Its root is signed by this repository's GitHub Actions
workload identity and recorded in the public Sigstore transparency log, which
RiskLoom does not operate and cannot rewrite.

These are different claims and this document does not blur them. The Class B
anchor upgrades the *package*, not the *results*. It proves that this exact set
of bytes existed at the moment of the log entry, and that nobody — including
RiskLoom — has altered them since. It proves nothing about when the underlying
evaluation was performed.

## The anchor is retrospective

The transparency-log entry over this package is a **retrospective anchor**. It
establishes that the package existed on the date of the entry. It does **not**
establish that the results predated observation.

Window 1 was computed on **2026-09-07**. Window 2 was computed on
**2026-09-18**. The anchor was created after both. Anyone assessing this
evidence should treat the anchor as fixing the package in time from that date
forward, and nothing earlier.

What *does* speak to ordering, and is Class A:

- Protocol v1.0 was frozen 2026-09-07T15:19:24Z, before any sealed outcome was
  opened. SHA-256 `9ebf02e41ea4b45f707cf029be68e41f26aba9ec578c4ec52a15bed71d168127`.
- Amendment 1, SHA-256 `f6a8d80c7da1cf1687eae39b7bdd40d8cd7e23197e3982d4643f9c668753b60c`.
- Window 2's boundary was declared on 2026-09-07 in
  `package/results/window_1/WINDOW_2_DECLARATION.md`, SHA-256
  `39a9abcf41107d76ad6a30eec5d25a86d43a68fb6f8e0ada2b547c431d6dbb9e`, and
  archived under Object Lock, while the window it named
  (2026-09-08T00:00:00Z to 2026-09-15T00:00:00Z) was still entirely in the
  future. The evaluated boundary matched it exactly.
- Both windows ran on the same pipeline build: code digest
  `855fe324b44521aef5d6b1dc90c5be4bf115c9c242d92dbddcd5bdae44571dc9` and
  thresholds digest `0568f24ceb798001ecffed6d9101c4c863d1e6c0f5718f1d5aedc70151cfb25d`,
  committed on every in-window ledger row of both windows.

Those orderings rest on RiskLoom-controlled timestamps. They are Class A. The
first RiskLoom commitment that a third party can independently date is this one.

---

## Verify it yourself

Nothing below needs RiskLoom credentials. Steps 1 to 3 need no network at all.

```sh
git clone https://github.com/riskloom/ledger-genesis
cd ledger-genesis
```

### 1. Every file matches the commitment manifest, and the manifest matches the tree

```sh
./verify.sh
```

That script does three things, and you can do each by hand instead. Run these
in `bash`, from the repository root.

> `SHA256SUMS` deliberately has **no trailing newline** — the root is the hash of
> exactly those bytes. A naive `while read` loop therefore drops its last line
> and silently skips a file. The `|| [ -n "$line" ]` below is what prevents that.

```bash
# (a) every listed file has the digest recorded for it
bad=0
while IFS= read -r line || [ -n "$line" ]; do
  [ -n "$line" ] || continue
  f=${line% *}; want=${line##* }
  got=$(sha256sum "$f" | cut -d' ' -f1)
  [ "$got" = "$want" ] || { echo "MISMATCH $f"; bad=$((bad+1)); }
done < SHA256SUMS
echo "checked $(( $(wc -l < SHA256SUMS) + 1 )) files, $bad bad"

# (b) SHA256SUMS lists exactly the files present, no more and no fewer
diff <(find . -type f ! -path './.git/*' ! -name SHA256SUMS | sed 's|^\./||' | LC_ALL=C sort) \
     <(cut -d' ' -f1 SHA256SUMS | LC_ALL=C sort) && echo "inventory is exact"

# (c) SHA256SUMS is byte-exact under the published construction
./sha256sums.sh | cmp - SHA256SUMS && echo "canonical bytes reproduce"
```

### 2. Compute the package root

```sh
sha256sum SHA256SUMS
```

The root is the SHA-256 of `SHA256SUMS` itself. There is no Merkle tree and no
domain separation. The construction is in `CLASS_B_SPECIFICATION.md` §1.

### 3. Check the root against the public transparency log

```sh
gh release download --repo riskloom/ledger-genesis --pattern cosign.bundle

cosign verify-blob \
  --bundle cosign.bundle \
  --certificate-identity "https://github.com/riskloom/ledger-genesis/.github/workflows/anchor-sha256sums.yml@refs/heads/main" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  SHA256SUMS
```

Both pinned values matter. `--certificate-identity` binds the signature to this
repository's workflow on `main`; `--certificate-oidc-issuer` binds it to GitHub's
OIDC provider. Without both pins a valid-looking signature from any Sigstore
identity would pass.

Or query the log directly, without cosign:

```sh
rekor-cli search --sha $(sha256sum SHA256SUMS | cut -d' ' -f1)
rekor-cli get --uuid <uuid-from-above>
```

### 4. Check the results against the evidence

```sh
less package/results/window_2/report/EVALUATION_REPORT.md   # §6 is W1 vs W2
less package/results/window_1/report/EVALUATION_REPORT.md
less package/results/window_2/ARCHIVAL_INCIDENT.md
```

The reports are re-presentations of `data/layer1.json` and `data/layer2.json`,
which are in this package. The scripts that produced them are in `code/`. Re-run them yourself:

```sh
./reproduce.sh
```

That re-executes stages 02, 04, 05 and 06 for both windows from the packaged
data alone and diffs the result against the archived output. It currently
reproduces all eight output files and all six archived stdout logs
byte-identically. Stages 01 and 03 read RiskLoom-private infrastructure and are
not re-runnable — `LIMITATIONS.md` says exactly where that line falls.

---

## What is in the package

```
package/MANIFEST.json                       archive manifest for protocol + thresholds
package/protocol/                           Protocol v1.0 (PDF), Amendment 1
package/thresholds/thresholds.json          the 69-symbol calibration set in force
package/results/window_1/                   Window 1: manifest, Window 2 declaration,
                                            code, data, report, run logs
package/results/window_2/                   Window 2: manifest, archival incident,
                                            code, data, report, run logs
```

Window 1 evaluated 2026-08-30T14:55:00Z to 2026-09-06T14:55:00Z, 2,016 slots.
Window 2 evaluated 2026-09-08T00:00:00Z to 2026-09-15T00:00:00Z, 2,014 of 2,016
slots present; the two absent slots are identified in the Window 2 manifest and
report and were handled by the frozen exclusion rule, not by a correction.

## What the two windows show

The full statement is §7 of `package/results/window_2/report/EVALUATION_REPORT.md`
and is not summarised away here. In short: across both windows, under an
identical frozen protocol and an identical pipeline build, structural-state
warnings preceded larger absolute price displacement than fixed-stride NORMAL
anchors in all 16 predeclared cells of the overall grid. The measured lift fell
in 15 of 16 overall cells in Window 2, in several by more than half, while
NORMAL-anchor incidence was nearly unchanged — so the attenuation sits in the
warning arm, not in a shifted baseline. Majors disagree in direction across 6 of
16 cells on 88 to 94 episodes. Nothing here establishes a predictive accuracy
figure.

> Two windows are two observations. The direction replicated; the magnitude did
> not.

## Limitations

`LIMITATIONS.md` states what an outsider can verify unaided, what requires
controlled access, and why. Read it before drawing conclusions from this
package.

## Files

| File | What it is |
|---|---|
| `CLASS_B_SPECIFICATION.md` | the frozen commitment and anchoring design |
| `PROVENANCE.md` | every published file mapped to its archived source and digest |
| `LIMITATIONS.md` | what is and is not independently checkable |
| `SHA256SUMS` | the commitment manifest; the root is its own SHA-256 |
| `sha256sums.sh` | regenerates `SHA256SUMS` under the published construction |
| `verify.sh` | runs the integrity and transparency-log checks above |
| `reproduce.sh` | re-runs every evaluation stage that needs no RiskLoom access and diffs it against the archived output |
| `.github/workflows/anchor-sha256sums.yml` | the workflow whose identity signs the root |
