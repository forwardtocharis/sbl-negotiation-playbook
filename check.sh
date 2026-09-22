#!/usr/bin/env sh
# check.sh - POSIX twin of check.ps1 (build_plan.md section 6 WP9, section 9).
#
#   sh check.sh
#
# Same three stages, same expectations, same exit code:
#   1. sbl validate   - the library loads and every cross-reference resolves
#   2. pytest -q      - every test, including the golden-deal snapshots
#   3. sbl run        - each deal in deals/, one invocation each, into runs/
#
# Stage 3 checks each deal's exit code against the code that deal is supposed
# to produce, not against zero. An escalating deal exits 2 by design
# (build_plan.md section 2.4), so for D02, D04, D05 and D06 exit 2 is a pass
# and exit 0 is a failure: it would mean an escalation went missing. Any other
# code (1 = the file did not load, anything else = a crash) fails.
#
# Kept in sync with check.ps1 by hand. If you change the expected table in one,
# change it in the other; tests/test_golden_deals.py is the thing that actually
# pins the behaviour, and these two only decide what "pass" prints.

set -u

root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$root" || exit 1

# -- interpreter ------------------------------------------------------------
# The project venv if it is there, otherwise whatever 'python' is on PATH.
# .venv/Scripts/python is the Windows layout, .venv/bin/python the POSIX one;
# this script runs under Git Bash and WSL alike, so try both.
if [ -x ".venv/Scripts/python.exe" ]; then
    PY=".venv/Scripts/python.exe"
    PY_LABEL=".venv/Scripts/python"
elif [ -x ".venv/bin/python" ]; then
    PY=".venv/bin/python"
    PY_LABEL=".venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PY="python3"
    PY_LABEL="python3"
elif command -v python >/dev/null 2>&1; then
    PY="python"
    PY_LABEL="python"
else
    echo "FAIL: no .venv and no python on PATH."
    exit 1
fi

echo ""
echo "=== SBL Negotiation Playbook Demonstrator: check ==="
echo "interpreter: $PY_LABEL"
echo ""

# -- expected exit code per deal -------------------------------------------
# Keyed by the deal file's base name; 2 means "this deal must escalate".
# Written as a case statement rather than an associative array, because those
# are a bashism and this script is POSIX sh.
expected_code() {
    case "$1" in
        D01_plain_vanilla)           echo 0 ;;
        D02_trust_concentrated_pdmr) echo 2 ;;
        D03_swiss_corporate_purpose) echo 0 ;;
        D04_third_party_pledge_lux)  echo 2 ;;
        D05_real_estate_hard_stop)   echo 2 ;;
        D06_below_floor_request)     echo 2 ;;
        *)                           echo 0 ;;
    esac
}

known_deal() {
    case "$1" in
        D01_plain_vanilla|D02_trust_concentrated_pdmr|D03_swiss_corporate_purpose|\
        D04_third_party_pledge_lux|D05_real_estate_hard_stop|D06_below_floor_request)
            return 0 ;;
        *) return 1 ;;
    esac
}

rows=""
failed=0
checks=0

add_row() {  # stage, expected, actual, ok(0|1)
    if [ "$4" -eq 0 ]; then verdict="PASS"; else verdict="FAIL"; failed=$((failed + 1)); fi
    checks=$((checks + 1))
    rows=$(printf '%s\n%-32s %-32s %-10s %s' "$rows" "$1" "$2" "$3" "$verdict")
}

# -- 1. validate ------------------------------------------------------------
echo "--- 1/3  sbl validate ---"
"$PY" -m sbl validate
code=$?
if [ "$code" -eq 0 ]; then ok=0; else ok=1; fi
add_row "sbl validate" "exit 0" "exit $code" "$ok"
echo ""

# -- 2. pytest --------------------------------------------------------------
echo "--- 2/3  pytest -q ---"
"$PY" -m pytest -q
code=$?
if [ "$code" -eq 0 ]; then ok=0; else ok=1; fi
add_row "pytest -q" "exit 0" "exit $code" "$ok"
echo ""

# -- 3. run every deal ------------------------------------------------------
echo "--- 3/3  sbl run (each deal into runs/) ---"
found=0
for deal in deals/*.yaml; do
    [ -e "$deal" ] || continue
    found=$((found + 1))
    stem=$(basename "$deal" .yaml)
    "$PY" -m sbl run "$deal" --out runs
    code=$?
    want=$(expected_code "$stem")
    if [ "$code" -eq "$want" ]; then ok=0; else ok=1; fi
    if known_deal "$stem"; then
        if [ "$want" -eq 2 ]; then want_text="exit 2 (escalates)"; else want_text="exit $want"; fi
    else
        want_text="exit 0 (not in the expected table)"
    fi
    add_row "$stem" "$want_text" "exit $code" "$ok"
done

if [ "$found" -eq 0 ]; then
    echo "FAIL: deals/ holds no .yaml files."
    add_row "deals/" "six deal files" "none found" 1
fi
echo ""

# -- summary ----------------------------------------------------------------
echo "=== summary ==="
printf '%-32s %-32s %-10s %s\n' "Stage" "Expected" "Actual" "Result"
printf '%s\n' "--------------------------------------------------------------------------------"
printf '%s\n' "$rows" | sed '/^$/d'
echo ""

if [ "$failed" -eq 0 ]; then
    echo "OK: $checks checks passed."
    echo "Demonstrator built from public sources. Synthetic deals. Not legal advice."
    exit 0
fi
echo "FAILED: $failed of $checks checks failed."
exit 1
