# build_portable.ps1
# Run 1-liner: & C:\Users\ansem\Documents\GitHub\_venvs\venv_cuda_py311_np2\Scripts\Activate.ps1; .\build_portable.ps1
# pip install pyinstaller PySide6
# Advies venv: venv_cuda_py311_np2
$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonExe = "C:\Users\ansem\Documents\Github\_venvs\venv_cuda_py311_np2\Scripts\python.exe"
$MainScript = Join-Path $ProjectRoot "MapScanner_2026_v1.py"
$OutputName = "MapScanner_2026_portable"
$AssetDir = Join-Path $ProjectRoot "Assets"
$IconFile = Join-Path $AssetDir "MapScanner_icon.ico"

$dataFiles = @(
    "check_white.svg",
    "Ethnocentric Rg.otf",
    "MapScanner_icon.ico",
    "MapScanner_logo (2).png"
)

$pyiArgs = @(
    "-m", "PyInstaller",
    "--noconfirm",
    "--clean",
    "--onefile",
    "--windowed",
    "--name", $OutputName,
    "--distpath", (Join-Path $ProjectRoot "dist"),
    "--workpath", (Join-Path $ProjectRoot "build"),
    "--specpath", (Join-Path $ProjectRoot "build")
)

if (Test-Path -LiteralPath $IconFile) {
    $pyiArgs += @("--icon", $IconFile)
}

foreach ($fileName in $dataFiles) {
    $sourceFile = Join-Path $AssetDir $fileName
    if (Test-Path -LiteralPath $sourceFile) {
        $pyiArgs += @("--add-data", "$sourceFile;.")
    }
}

$pyiArgs += $MainScript

& $PythonExe @pyiArgs
