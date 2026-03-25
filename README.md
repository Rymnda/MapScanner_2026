<p align="center"><img src="MapScanner_logo (2).png" width="400"></p>
MapScanner 2026 is a desktop file scanner built with Python and PySide6.

It helps you browse folders, scan files, filter through results visually, copy paths or filenames, and export selections to text. The app includes multilingual UI support, custom branding, sortable result columns, and an About dialog with bundled assets.

## Features

- Scan files from a selected folder
- Optional recursive scanning with subfolder depth
- Sort results by columns such as name, folder, type, size, duration, and modified date
- Copy full paths, filenames, or PowerShell-style output
- Export checked results to TXT
- Multilingual interface: Dutch, English, German, Spanish
- Custom icon, about artwork, and bundled display font

## Requirements

- Windows
- Python 3.10 or newer
- `ffprobe` in `PATH` if you want media-duration detection

## Install

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python .\MapScanner_2026_v1.py
```

## Included Runtime Assets

These files should stay next to the Python script when running directly:

- `MapScanner_2026_v1.py`
- `MapScanner_icon.ico`
- `MapScanner_logo (2).png`
- `Ethnocentric Rg.otf`
- `check_white.svg`

## Build Notes

Packaged app and installer artifacts are optional and not required to run the Python version directly.

## Repository

- GitHub: [https://github.com/Rymnda](https://github.com/Rymnda)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
