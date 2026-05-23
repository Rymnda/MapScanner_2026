# build_setup.ps1
# Run 1-liner: & C:\Users\ansem\Documents\GitHub\_venvs\venv_cuda_py311_np2\Scripts\Activate.ps1; .\build_setup.ps1
# pip install pyinstaller PySide6
# Advies venv: venv_cuda_py311_np2
$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$PortableBuilder = Join-Path $ProjectRoot "build_portable.ps1"
$IsccCandidates = @(
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
    "C:\Program Files\Inno Setup 6\ISCC.exe"
)

& $PortableBuilder

$IsccPath = $IsccCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
if (-not $IsccPath) {
    throw "ISCC.exe niet gevonden. Installeer Inno Setup 6 of pas het pad aan in build_setup.ps1."
}

& $IsccPath (Join-Path $ProjectRoot "MapScanner2026.iss")
