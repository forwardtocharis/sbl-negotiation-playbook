# check.ps1 - the whole build, checked, in one command (build_plan.md section 6 WP9, section 9).
#
#   powershell -ExecutionPolicy Bypass -File check.ps1
#
# Three stages, in order:
#   1. sbl validate   - the library loads and every cross-reference resolves
#   2. pytest -q      - every test, including the golden-deal snapshots
#   3. sbl run        - each deal in deals/, one invocation each, into runs/
#
# Stage 3 checks the exit code against the code that deal is supposed to
# produce, not against zero. An escalating deal exits 2 by design
# (build_plan.md section 2.4), so for D02, D04, D05 and D06 an exit of 2 is a pass and
# an exit of 0 is a failure: it would mean an escalation went missing. Any
# other code (1 = the file did not load, anything else = a crash) fails.
#
# Deliberately ASCII-only: Windows PowerShell 5.1 reads a UTF-8 file without a
# byte order mark as ANSI, which mangles anything outside ASCII.

$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

# -- interpreter ------------------------------------------------------------
# The project venv if it is there, otherwise whatever 'python' is on PATH, so a
# fresh clone that has run 'pip install -e .' into its own environment works.
$venvPython = Join-Path $root '.venv\Scripts\python.exe'
if (Test-Path $venvPython) {
    $py = $venvPython
    $pyLabel = '.venv\Scripts\python'
} else {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($null -eq $cmd) {
        Write-Host 'FAIL: no .venv and no python on PATH.' -ForegroundColor Red
        exit 1
    }
    $py = $cmd.Source
    $pyLabel = 'python'
}

Write-Host ''
Write-Host '=== SBL Negotiation Playbook Demonstrator: check ===' -ForegroundColor Cyan
Write-Host ("interpreter: {0}" -f $pyLabel)
Write-Host ''

# -- expected exit code per deal -------------------------------------------
# Keyed by the deal file's base name. 2 means "this deal must escalate".
$expected = [ordered]@{
    'D01_plain_vanilla'          = 0
    'D02_trust_concentrated_pdmr' = 2
    'D03_swiss_corporate_purpose' = 0
    'D04_third_party_pledge_lux'  = 2
    'D05_real_estate_hard_stop'   = 2
    'D06_below_floor_request'     = 2
}

$rows = New-Object System.Collections.ArrayList
$failed = 0

function Add-Row($stage, $expectedText, $actualText, $ok) {
    if ($ok) { $verdict = 'PASS' } else { $verdict = 'FAIL' }
    [void]$rows.Add([pscustomobject]@{
        Stage    = $stage
        Expected = $expectedText
        Actual   = $actualText
        Result   = $verdict
    })
}

# -- 1. validate ------------------------------------------------------------
Write-Host '--- 1/3  sbl validate ---' -ForegroundColor Yellow
& $py -m sbl validate
$code = $LASTEXITCODE
$ok = ($code -eq 0)
Add-Row 'sbl validate' 'exit 0' ("exit {0}" -f $code) $ok
if (-not $ok) { $failed++ }
Write-Host ''

# -- 2. pytest --------------------------------------------------------------
Write-Host '--- 2/3  pytest -q ---' -ForegroundColor Yellow
& $py -m pytest -q
$code = $LASTEXITCODE
$ok = ($code -eq 0)
Add-Row 'pytest -q' 'exit 0' ("exit {0}" -f $code) $ok
if (-not $ok) { $failed++ }
Write-Host ''

# -- 3. run every deal ------------------------------------------------------
Write-Host '--- 3/3  sbl run (each deal into runs/) ---' -ForegroundColor Yellow
$dealFiles = Get-ChildItem -Path (Join-Path $root 'deals') -Filter '*.yaml' | Sort-Object Name
if ($dealFiles.Count -eq 0) {
    Write-Host 'FAIL: deals/ holds no .yaml files.' -ForegroundColor Red
    Add-Row 'deals/' 'six deal files' 'none found' $false
    $failed++
}

foreach ($deal in $dealFiles) {
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($deal.Name)
    & $py -m sbl run $deal.FullName --out (Join-Path $root 'runs')
    $code = $LASTEXITCODE
    if ($expected.Contains($stem)) {
        $want = $expected[$stem]
        $ok = ($code -eq $want)
        $wantText = "exit $want"
        if ($want -eq 2) { $wantText = 'exit 2 (escalates)' }
    } else {
        # A deal the script does not know about: no expectation to check it
        # against, so treat only a clean run as a pass and say why.
        $want = 0
        $ok = ($code -eq 0)
        $wantText = 'exit 0 (not in the expected table)'
    }
    Add-Row $stem $wantText ("exit {0}" -f $code) $ok
    if (-not $ok) { $failed++ }
}
Write-Host ''

# -- summary ----------------------------------------------------------------
Write-Host '=== summary ===' -ForegroundColor Cyan
$rows | Format-Table -AutoSize | Out-String -Width 200 | Write-Host

if ($failed -eq 0) {
    Write-Host ("OK: {0} checks passed." -f $rows.Count) -ForegroundColor Green
    Write-Host 'Demonstrator built from public sources. Synthetic deals. Not legal advice.'
    exit 0
} else {
    Write-Host ("FAILED: {0} of {1} checks failed." -f $failed, $rows.Count) -ForegroundColor Red
    exit 1
}
