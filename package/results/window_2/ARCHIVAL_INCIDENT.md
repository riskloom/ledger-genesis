# Window 2 — Archival Incident Record

**Recorded:** 2026-09-18
**Scope:** This document exists solely to record a versioning incident affecting
`disclosure/results/window_2/MANIFEST.json` during archival verification.

It records an operational error made during archival. It does not amend, alter
or qualify the Window 2 evaluation, its method, its inputs or its results.

---

## 1. What happened

After the Window 2 archive was uploaded and read-back verification had passed,
an Object Lock immutability test was performed by attempting to overwrite the
live `MANIFEST.json` key. The test should have been run against a disposable
scratch key. It was not.

The write succeeded. S3 Object Lock in COMPLIANCE mode prevents deletion or
modification of a **retained object version**; it does not prevent an authorised
principal from creating a **new version at the same key** in a versioned bucket.
The result was that a 7-byte file became the current version of the Window 2
manifest.

The condition was detected on the immediately following verification step,
approximately half a minute later, and remediated by re-uploading the correct
manifest as a new current version under the same COMPLIANCE retention as the
rest of the archive.

An attempt was made to delete the accidental version. It was refused, correctly:

    An error occurred (AccessDenied) when calling the DeleteObject operation:
    Access Denied because object protected by object lock.

The accidental version is therefore permanent and will remain in the version
history of this key. That is the intended behaviour of the control, and this
record exists so the history is not silently puzzling to a later reader.

---

## 2. Version history of `disclosure/results/window_2/MANIFEST.json`

All three values below were read back from S3 and hashed locally.

### 2.1 Original correct version

    version id   Gt2td.MBqqXv4Xkf_tbYuA3EYOyDDq0G
    timestamp    2026-09-18T08:30:35Z
    size         12,263 bytes
    sha256       41a4c50162f1cc5398ea5a8711ea3cdead3236cb23f4a26030b4b91cc2ad6ee6
    etag         "b4b210a06a0e907cf41c16dc58fd18c0"
    object lock  COMPLIANCE, retain until 2033-09-18T00:00:00Z
    status       not latest

### 2.2 Accidental version

    version id   kuCkv.UhWZa7YxE2NLCVLgkpRkaJW96j
    timestamp    2026-09-18T08:31:44Z
    size         7 bytes
    content      the ASCII bytes `tamper` followed by a newline (74 61 6d 70 65 72 0a)
    sha256       a37f7924cd97102ce5b8ac87d11c646f2c1cb6203c21cf1c56b1e1dae5a3b0fc
    etag         "57c7f6d939eeda90aa1488b15617b9fa"
    object lock  COMPLIANCE, retain until 2026-09-19T08:31:43.077Z
                 (the bucket DEFAULT retention of 1 day, because the test write
                 did not specify a retention date; the archive's own objects
                 carry an explicit 7-year retention)
    cause        attempted Object Lock immutability test against the live
                 manifest key instead of a scratch key
    status       not latest; deletion refused by object lock; permanent

### 2.3 Restored current version

    version id   syZmUIyr5XJJY4cxJcOkpD6zZcVIqazt
    timestamp    2026-09-18T08:32:22Z
    size         12,263 bytes
    sha256       41a4c50162f1cc5398ea5a8711ea3cdead3236cb23f4a26030b4b91cc2ad6ee6
    etag         "b4b210a06a0e907cf41c16dc58fd18c0"
    object lock  COMPLIANCE, retain until 2033-09-18T00:00:00Z
    status       latest

### 2.4 Original and restored are byte-identical

Confirmed by full-file comparison and by SHA-256:

    Gt2td.MBqqXv4Xkf_tbYuA3EYOyDDq0G  sha256 41a4c501...2ad6ee6   12,263 bytes
    syZmUIyr5XJJY4cxJcOkpD6zZcVIqazt  sha256 41a4c501...2ad6ee6   12,263 bytes

They are the same bytes. The restored manifest is not a reconstruction; it is
the same file re-uploaded.

### 2.5 Duration the accidental version was current

Deterministically established from the S3 `LastModified` timestamps of the
accidental version and the restoring version:

    from 2026-09-18T08:31:44Z
    to   2026-09-18T08:32:22Z
    =    38 seconds

During those 38 seconds, a reader fetching the current version of
`window_2/MANIFEST.json` without specifying a version id would have received the
7-byte file.

---

## 3. Scope of impact — what was NOT changed

Confirmed by inspection after remediation:

- No Window 2 evaluation artefact was changed. All 22 artefacts were read back
  and hash-matched against the manifest with zero mismatches.
- No evaluation result was changed. `layer1.json`, `layer2.json`,
  `episodes.json`, `baseline.json`, `bars.json`, `ledger_window.json` and
  `universe.json` each have exactly one version.
- No executed script was changed. The six scripts under `code/` each have
  exactly one version.
- No run log was changed.
- No production data was modified. All database access throughout was read-only
  SELECT via the RDS Data API against `riskloom_clone`.
- No canon surface was written.
- No protocol artefact was touched. `RiskLoom_Prospective_Evaluation_Protocol_v1.0.pdf`
  and `AMENDMENT_1.md` each have exactly one version.
- No Window 1 artefact was touched. `window_1/MANIFEST.json` has exactly one
  version.
- No frozen methodology, definition, threshold, exclusion, horizon, cohort or
  reporting rule was changed.
- `MANIFEST.json` is the only key in the Window 2 archive with more than one
  version.

## 4. The evaluation was not rerun

The Window 2 evaluation was NOT rerun and NOT recalculated at any point during
archival or during this remediation. Every archived artefact is byte-identical
to the output produced by the six scripts during the single evaluation run. The
remediation consisted only of re-uploading an already-existing file.

## 5. This file is not referenced by MANIFEST.json

`MANIFEST.json` was written before this incident occurred and therefore does not
list `ARCHIVAL_INCIDENT.md` among its artefacts. The manifest has deliberately
NOT been updated to add it. Publishing a further manifest version to describe a
manifest-versioning incident would compound precisely the weakness being
recorded. This file stands on its own.

---

## 6. Control lesson

S3 Object Lock in COMPLIANCE mode protects retained object **versions** from
deletion or alteration. It does not, by itself, prevent an authorised principal
holding `s3:PutObject` from creating a newer version at the same key.

The practical consequence for an evidence archive is this: an auditor who reads
only the current version of an archived object can be misled, while the true
version survives, intact and undeletable, as a non-latest version. Integrity of
the historical record and integrity of what the archive *appears to say today*
are two different properties. COMPLIANCE mode delivers the first. It does not
deliver the second.

In this instance the exposure was 38 seconds, self-inflicted, self-detected and
self-reported. The same mechanism operated deliberately, or operated by accident
and left unreported, would be materially harder to notice: nothing in the
current-version view of the bucket announces that an earlier version existed.

Two mitigations follow from this and are recorded here as observations, not as
changes. Neither has been implemented, and no bucket policy, SCP, IAM policy or
retention setting was altered in producing this record.

1. Verification of an archived object should assert the object's **version id**,
   not only its key. A hash check against the current version proves nothing
   about whether the current version is the intended one.
2. Write access to a completed evidence prefix and the act of completing that
   evidence should not be held by the same principal at the same time.
