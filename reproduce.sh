#!/usr/bin/env sh
# Re-run the evaluation stages that need no RiskLoom access, and compare the
# output byte-for-byte against the archived output shipped in this package.
#
#   ./reproduce.sh          both windows
#   ./reproduce.sh 1        Window 1 only
#
# Needs python3 only. No network, no credentials.
#
# Stages 01 (ledger read) and 03 (raw bar read) are NOT re-run: they read
# RiskLoom-private infrastructure. Their outputs are shipped as inputs here.
# See LIMITATIONS.md.

set -eu
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

fail=0
for N in ${1:-1 2}; do
  SRC="package/results/window_$N"
  T="$WORK/w$N"; mkdir -p "$T"
  cp "$SRC"/data/*.json "$T"/

  # The archived scripts hard-code the absolute scratchpad path they ran under.
  # Repoint that one constant; nothing else is touched.
  for s in 02_layer1_and_anchors 04_layer2_grid 05_maxstate_split 06_per_symbol; do
    sed -E "s|^SP=\".*\"|SP=\"$T\"|" "$SRC/code/$s.py" > "$T/$s.py"
    sed -E "s|^SP=\".*\"|SP=X|" "$SRC/code/$s.py" > "$T/.a"
    sed -E "s|^SP=\".*\"|SP=X|" "$T/$s.py"          > "$T/.b"
    if ! cmp -s "$T/.a" "$T/.b"; then
      echo "window $N: $s changed by more than the SP constant - aborting"; exit 1
    fi
    rm -f "$T/.a" "$T/.b"
  done

  echo "== window $N: re-running stages 02, 04, 05, 06 from packaged data only"
  ( cd "$T"
    for s in 02_layer1_and_anchors 04_layer2_grid 05_maxstate_split 06_per_symbol; do
      "$PY" "$s.py" > "out_$s.txt" 2>&1 || { echo "   $s FAILED"; tail -5 "out_$s.txt"; exit 1; }
    done )

  for f in layer1.json episodes.json baseline.json layer2.json; do
    if cmp -s "$T/$f" "$SRC/data/$f"; then echo "   IDENTICAL  data/$f"
    else echo "   DIFFERS    data/$f"; fail=1; fi
  done

  # stdout of 04/05/06 is archived verbatim; filenames differ between windows
  for s in 04 05 06; do
    log=$(ls "$SRC"/report/run_log_${s}*.txt 2>/dev/null | head -1) || continue
    out=$(ls "$T"/out_${s}_*.txt | head -1)
    if cmp -s "$out" "$log"; then echo "   IDENTICAL  report/$(basename "$log")"
    else echo "   DIFFERS    report/$(basename "$log")"; fail=1; fi
  done
  echo ""
done

if [ "$fail" -eq 0 ]; then
  echo "RESULT: PASS - every independently reproducible stage reproduced byte-for-byte"
else
  echo "RESULT: FAIL"; exit 1
fi
