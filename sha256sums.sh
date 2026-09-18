#!/usr/bin/env sh
# Class B commitment construction, section 1.
#
#   For every file in the package, compute SHA-256.
#   Build lines: <relative-path><single space><hex-sha256>
#   Sort bytewise ascending by the full line.
#   Join with LF (0x0A), no trailing LF.
#
# The package is every file in this repository except .git/, SHA256SUMS itself,
# and the signature material. Per the specification: SHA256SUMS is the
# commitment manifest and is excluded from its own file inventory, and "any
# signature, certificate or bundle generated from SHA256SUMS is also outside the
# committed package root". So cosign.bundle / cosign.sig / cosign.pem /
# cosign.crt are excluded too, and downloading them into a checkout does not
# change the root.
#
#   ./sha256sums.sh          print the canonical bytes to stdout
#   ./sha256sums.sh --write  write them to ./SHA256SUMS
#
# The package root is SHA-256 over the exact bytes of SHA256SUMS, so
# `sha256sum SHA256SUMS` literally produces the root.

set -eu
cd "$(dirname "$0")"

if command -v sha256sum >/dev/null 2>&1; then
  _d() { sha256sum "$1" | cut -d' ' -f1; }
elif command -v shasum >/dev/null 2>&1; then
  _d() { shasum -a 256 "$1" | cut -d' ' -f1; }
else
  echo "need sha256sum or shasum" >&2; exit 1
fi

_lines() {
  find . -type f \
       ! -path './.git/*' \
       ! -name 'SHA256SUMS' \
       ! -name 'cosign.bundle' ! -name 'cosign.sig' \
       ! -name 'cosign.pem' ! -name 'cosign.crt' \
  | sed 's|^\./||' \
  | while IFS= read -r f; do
      printf '%s %s\n' "$f" "$(_d "$f")"
    done \
  | LC_ALL=C sort
}

# $(...) strips trailing newlines; printf '%s' adds none.
OUT=$(_lines)

if [ "${1:-}" = "--write" ]; then
  printf '%s' "$OUT" > SHA256SUMS
  echo "wrote SHA256SUMS: $(printf '%s' "$OUT" | wc -l | tr -d ' ') LF separators, $(_d SHA256SUMS) root" >&2
else
  printf '%s' "$OUT"
fi
