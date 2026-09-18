> ### REDACTION NOTICE — THIS FILE IS NOT BYTE-IDENTICAL TO THE ARCHIVE
>
> The archived original is `disclosure/results/window_2/code/INVOCATION.md`,
> SHA-256 `a15dc4f16a730319a5795cf1119cb2c971ad36ec40358df86a5908666ae1c00f`, recorded in
> `package/results/window_2/MANIFEST.json`.
>
> Two lines have been replaced. Nothing else has been altered, added or
> reordered. The removed values are the ARNs of the Aurora cluster and of the
> Secrets Manager secret holding that cluster's database credentials. They are
> resource identifiers, not credentials, and confer no access without IAM
> permission — but they name a credential store, so they are withheld.
>
> Every other file in this package IS byte-identical to its archived source.
> See `PROVENANCE.md`.

# Window 2 — invocation record

## Execution environment
- Host: operator workstation (darwin 25.6.0), scratchpad
  `/private/tmp/claude-501/-Users-uikegulu-Desktop-riskloom/bcfd7437-1f90-4db4-a2c9-525c7a102a2a/scratchpad/w2`
- Scripts 01 and 05 ran under the system interpreter: `python3` (3.13.11)
- Scripts 02, 03, 04, 06 ran under:
  `~/Desktop/riskloom/ledger_pipeline/.venv/bin/python` (Python 3.13.2)
  boto3 1.43.89 / botocore 1.43.89 / urllib3 2.7.0 / OpenSSL 3.0.15

## AWS credentials
Read-only access obtained per run as:

    aws sso login --sso-session rl              # profile rl-build, account 587788487647
    aws --profile rl-build sts assume-role \
      --role-arn arn:aws:iam::361964630357:role/OrganizationAccountAccessRole \
      --role-session-name window2-eval

Session credentials exported as AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY /
AWS_SESSION_TOKEN, region eu-west-2, into `assume.sh` and sourced before each
script. Credentials are NOT archived.

## Database handle (script 01 only)
`db.sh` exported, and is NOT archived (contains the secret ARN):

    CL  = [REDACTED — Aurora cluster ARN]
    SEC = [REDACTED — Secrets Manager secret ARN]

Access was read-only via the RDS Data API (`aws rds-data execute-statement`).
Database `riskloom_clone`. No write statement was issued at any point. The
executed Window 2 code contains zero occurrences of INSERT, UPDATE, DELETE,
DROP, ALTER or COPY.

## Order of execution
    01_load_ledger.py          -> ledger_window.json, universe.json
    02_layer1_and_anchors.py   -> layer1.json, episodes.json, baseline.json
    03_build_price_series.py   -> bars.json
    04_layer2_grid.py          -> layer2.json  (+ overall/majors/non_majors tables)
    05_maxstate_split.py       -> max-state split tables (stdout only)
    06_per_symbol.py           -> per-symbol table (stdout only)

Scripts 05 and 06 write no data file; their output is preserved verbatim in
`report/run_log_05.txt` and `report/run_log_06.txt`.

## SCRIPT 03 — SIGSEGV ON FIRST INVOCATION
The first invocation of `03_build_price_series.py` terminated with SIGSEGV
(exit code 139) before producing any output. `report/run_log_03.txt` is
therefore zero bytes and is retained as the record of that failed invocation.

The script was rerun UNMODIFIED, under the same interpreter and the same
environment, and completed successfully (exit code 0). The successful run read
11,661 bodies with 0 missing. Its output is `report/run_log_03_attempt2.txt`.

The fault is a transient failure in the 128-thread TLS read path, not a data
condition: the successful rerun reported zero missing bodies and uniform bar
coverage (10,128 bars for every one of the 69 symbols). Both invocation logs
are retained. No code, parameter or environment was changed between the two
invocations.

## PROVENANCE OF THESE CODE FILES — the Window 1 caveat is closed
Window 1's six scripts executed as inline shell heredocs; its archived `code/`
files were verbatim transcriptions captured after the run, not the file objects
the interpreter opened.

For Window 2 the scripts were written to disk FIRST and executed from those
files. The files archived here ARE the files the interpreter opened. The
SHA-256 values in MANIFEST.json are of those exact files.

## DERIVATION FROM WINDOW 1
Each Window 2 script was derived from the corresponding archived Window 1
script by targeted substitution only:

    01_load_ledger.py         4 changed lines  (scratchpad path; window boundary)
    02..06                    2 changed lines each (scratchpad path only)

Diffed against the Window 1 originals, the count of non-path, non-date
differences is ZERO in all six files. No methodological logic, definition,
threshold, exclusion, horizon, cohort or reporting rule was changed.

## KNOWN COSMETIC ARTEFACTS INHERITED FROM WINDOW 1 CODE (not corrected)
- `02_layer1_and_anchors.py` prints the literal label "market states (of 2016
  rows)". The label is stale for Window 2; the arithmetic correctly divides by
  the actual row count 2014 (e.g. QUIET 1195/2014 = 59.335%). Not edited,
  because editing would break functional identity with Window 1.
- `03_build_price_series.py` reports "symbols with any 1-min gap: 69; total gap
  points: 138". That is exactly 2 per symbol, a direct consequence of the two
  missing ledger slots shifting the 12-slot bar-selection stride. Window 1 had
  no missing slots. Affected anchors fail forward coverage and are excluded by
  the frozen exclusion rule.
