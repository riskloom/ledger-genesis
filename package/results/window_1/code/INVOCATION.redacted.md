> ### REDACTION NOTICE — THIS FILE IS NOT BYTE-IDENTICAL TO THE ARCHIVE
>
> The archived original is `disclosure/results/window_1/code/INVOCATION.md`,
> SHA-256 `dbcee8780c561aa61af7f0ea245a18aeff2be0c8efe6a0f4ba91bb28fe68f077`, recorded in
> `package/results/window_1/MANIFEST.json`.
>
> Two lines have been replaced. Nothing else has been altered, added or
> reordered. The removed values are the ARNs of the Aurora cluster and of the
> Secrets Manager secret holding that cluster's database credentials. They are
> resource identifiers, not credentials, and confer no access without IAM
> permission — but they name a credential store, so they are withheld.
>
> Every other file in this package IS byte-identical to its archived source.
> See `PROVENANCE.md`.

# Window 1 — invocation record

## Execution environment
- Host: operator workstation (darwin 24.6.0), scratchpad
  `/private/tmp/claude-501/-Users-uikegulu/af28e28a-7715-44ff-8b9b-eccaa835c956/scratchpad`
- Scripts 01 and 05 ran under the system interpreter: `python3` (3.13)
- Scripts 02, 03, 04, 06 ran under:
  `~/Desktop/riskloom/ledger_pipeline/.venv/bin/python`
  (boto3 1.43.89 installed into that venv for script 03)

## AWS credentials
Read-only access obtained per run as:

    aws sso login --profile rl-build
    aws sts assume-role \
      --profile rl-build \
      --role-arn arn:aws:iam::361964630357:role/OrganizationAccountAccessRole \
      --role-session-name soak-audit-readonly

Session credentials exported as AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY /
AWS_SESSION_TOKEN, region eu-west-2, into `env-pipeline.sh` and sourced before
each script. Credentials are NOT archived.

## Database handle (script 01 only)
`db.sh` exported, and is NOT archived (contains the secret ARN):

    CL  = [REDACTED — Aurora cluster ARN]
    SEC = [REDACTED — Secrets Manager secret ARN]

Access was read-only via the RDS Data API (`aws rds-data execute-statement`).
Database `riskloom_clone`. No write statement was issued at any point.

## Order of execution
    01_load_ledger.py          -> ledger_window.json, universe.json
    02_layer1_and_anchors.py   -> layer1.json, episodes.json, baseline.json
    03_build_price_series.py   -> bars.json
    04_layer2_grid.py          -> layer2.json  (+ overall/majors/non_majors tables)
    05_maxstate_split.py       -> max-state split tables (stdout only)
    06_per_symbol.py           -> per-symbol table (stdout only)

Scripts 05 and 06 write no data file; their output is preserved verbatim in
`report/run_log_*.txt`.

## PROVENANCE OF THESE CODE FILES — read this
The six scripts executed as inline shell heredocs, not as files on disk. The
files in `code/` are VERBATIM transcriptions of those heredoc bodies, captured
after the run for archival. They were NOT re-executed before archiving, because
the archival instruction forbade rerunning. They are therefore a faithful
record of the source text that ran, but they are not the literal file objects
the interpreter opened — no such file objects existed.

Anyone reproducing this run should expect the same outputs from the same inputs;
that expectation has not been independently re-verified here, and this note
exists so the distinction is not silently lost.
