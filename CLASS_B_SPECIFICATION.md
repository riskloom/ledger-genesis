# Class B Specification

Status: frozen. Recorded 2026-09-18 from the originating design discussion.
This document is a transcription of a design that was worked out in conversation
and not previously written to a file. It is not a redesign.

## 1. Commitment construction

For every file in the package, compute SHA-256.

Build one line per file:

    <relative-path><single space><hex-sha256>

Sort the lines bytewise ascending by the full line. Join with LF (0x0A). No
trailing LF.

`SHA256SUMS` contains exactly that canonical joined byte sequence: UTF-8, lines
separated by LF, no trailing LF.

The package root is SHA-256 over the exact bytes of `SHA256SUMS`, so
`sha256sum SHA256SUMS` literally produces the root.

`SHA256SUMS` is the commitment manifest and is excluded from its own file
inventory. Any signature, certificate or bundle generated from `SHA256SUMS` is
also outside the committed package root.

No Merkle tree. No domain separation. Plain and checkable.

## 2. Rekor entry

`cosign` with keyless signing over the `SHA256SUMS` file. Standard `hashedrekord`
entry via the public instance at `rekor.sigstore.dev`. Nothing custom.

## 3. Signing identity

GitHub Actions workload identity from the public repository
`riskloom/ledger-genesis`.

    Certificate identity (SAN URI):
      https://github.com/riskloom/ledger-genesis/.github/workflows/<WORKFLOW>@refs/heads/main
    OIDC issuer:
      https://token.actions.githubusercontent.com

Verifiers pin both.

## 4. Class A versus Class B

**Class A** — internally consistent, hash-chained, append-only enforced, but
every guarantee rests on RiskLoom-controlled infrastructure. Windows 1 and 2 are
Class A.

**Class B** — externally committed to an independently operated transparency log.

This distinction must be stated plainly in the README and must not be blurred.
