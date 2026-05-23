# MapScanner_2026_v1.py
# Run 1-liner: & C:\Users\ansem\Documents\GitHub\_venvs\venv_cuda_py311_np2\Scripts\Activate.ps1; python .\MapScanner_2026_v1.py
# pip install PySide6
# Advies venv: venv_cuda_py311_np2
from __future__ import annotations
import sys
import os

# ---------------------

# MapScanner 2026 | Zoek. Vind. Klaar.
# v1.0.0

import shutil
import subprocess
import datetime as dt
from dataclasses import dataclass
from typing import List, Iterable, Optional, Dict

from PySide6 import QtCore, QtGui, QtWidgets


# ---------------- Config ----------------
APP_NAME = "MapScanner 2026"
TAGLINE = "Zoek. Vind. Klaar."
VERSION = "v1.0.0"
APP_ID = "MapScanner2026"
SETTINGS_ORG = "MapScanner"
REPO_URL = "https://github.com/Rymnda"
APP_ICON_FILE = "MapScanner_icon.ico"
ABOUT_IMAGE_FILE = "MapScanner_logo (2).png"
HEADER_FONT_FILE = "Ethnocentric Rg.otf"
ADVISED_VENV = "venv_cuda_py311_np2"

VIDEO_EXTS = {".mp4", ".mkv", ".mov", ".avi", ".webm", ".m4v", ".ts", ".flv"}

# ---------------- i18n ----------------
STRINGS: Dict[str, Dict[str, str]] = {
    "en": {
        "file": "File", "settings": "Settings", "info_menu": "Info", "help": "Help", "exit": "Exit",
        "language": "Language", "include_sub": "Include subfolders",
        "tagline": "Search. Find. Done.",
        "scan": "Scan files", "copy_sel": "Copy paths", "copy_names": "Copy filenames", "copy_ps": "Copy (PS Format)",
        "header_title": f"{APP_NAME}", "input_folder": "Selected folder",
        "browse": "Browse", "ready": "Ready", "help_dlg_title": "Help",
        "help_text": f"Repo: {REPO_URL}",
        "about_title": "About", "about_text": f"{APP_NAME}\n{TAGLINE}\nVersion {VERSION}",
        "ps_view": "Show PS output", "invalid_folder": "Invalid folder",
        "found": "Found {n} files", "copied_n": "Copied {n} items",
        "copied_one": "Copied: {p}", "scanning": "Scanning: {p}",
        "no_ffprobe": "ffmpeg missing",
        "select_all": "Check all", "deselect_all": "Uncheck all",
        "fit_cols": "Auto-fit columns", "checked_stat": "Checked: {n} / Total: {t}",
        "export_txt": "Export to TXT",
        "selected_folders": "{n} folders selected",
        # Context menu
        "ctx_open_file": "▶ Open file", "ctx_open_folder": "📂 Open containing folder",
        "ctx_copy_path": "📋 Copy full path", "ctx_check": "✓ Check selected", "ctx_uncheck": "✗ Uncheck selected",
        # Settings
        "set_media_info": "Scan Media Duration (Slower)",
        "set_hidden_files": "Show Hidden Files",
        "set_separator": "Copy Separator",
        "sep_newline": "New Line",
        "sep_comma": "Comma",
        "set_default_dir": "Set Current as Default Folder",
        "clear_default_dir": "Clear Default Folder",
        "default_set": "Default folder set to: {p}",
        "default_cleared": "Default folder cleared."
    },
    "nl": {
        "file": "Bestand", "settings": "Instellingen", "info_menu": "Info", "help": "Help", "exit": "Afsluiten",
        "language": "Taal", "include_sub": "Submappen meenemen",
        "tagline": "Zoek. Vind. Klaar.",
        "scan": "Bestanden scannen", "copy_sel": "Kopieer paden", "copy_names": "Kopieer bestandsnamen", "copy_ps": "Kopieer (PS Formaat)",
        "header_title": f"{APP_NAME}", "input_folder": "Geselecteerde map",
        "browse": "Bladeren", "ready": "Gereed", "help_dlg_title": "Help",
        "help_text": f"Repo: {REPO_URL}",
        "about_title": "Over", "about_text": f"{APP_NAME}\n{TAGLINE}\nVersie {VERSION}",
        "ps_view": "Toon als PowerShell lijst", "invalid_folder": "Ongeldige map",
        "found": "{n} bestanden gevonden", "copied_n": "{n} items gekopieerd",
        "copied_one": "Gekopieerd: {p}", "scanning": "Bezig met scannen: {p}",
        "no_ffprobe": "ffmpeg niet gevonden (geen media info)",
        "select_all": "Alles aanvinken", "deselect_all": "Alles uitvinken",
        "fit_cols": "Kolommen passend maken", "checked_stat": "Aangevinkt: {n} / Totaal: {t}",
        "export_txt": "Exporteer naar TXT",
        "selected_folders": "{n} mappen geselecteerd",
        # Context menu
        "ctx_open_file": "▶ Bestand openen", "ctx_open_folder": "📂 Map openen",
        "ctx_copy_path": "📋 Pad kopiëren", "ctx_check": "✓ Selectie aanvinken", "ctx_uncheck": "✗ Selectie uitvinken",
        # Settings
        "set_media_info": "Media-duur scannen (langzamer)",
        "set_hidden_files": "Verborgen bestanden tonen",
        "set_separator": "Kopieer scheidingsteken",
        "sep_newline": "Nieuwe regel",
        "sep_comma": "Komma",
        "set_default_dir": "Huidige map als standaard instellen",
        "clear_default_dir": "Standaard map wissen",
        "default_set": "Standaard map ingesteld op: {p}",
        "default_cleared": "Standaard map gewist. Laatst gebruikte map wordt nu gebruikt."
    },
    "de": {
        "file": "Datei", "settings": "Einstellungen", "info_menu": "Info", "help": "Hilfe", "exit": "Beenden",
        "language": "Sprache", "include_sub": "Unterordner einbeziehen",
        "tagline": "Suchen. Finden. Fertig.",
        "scan": "Dateien scannen", "copy_sel": "Pfade kopieren", "copy_names": "Dateinamen kopieren", "copy_ps": "Kopieren (PS-Format)",
        "header_title": f"{APP_NAME}", "input_folder": "Ausgewählter Ordner",
        "browse": "Durchsuchen", "ready": "Bereit", "help_dlg_title": "Hilfe",
        "help_text": f"Repo: {REPO_URL}",
        "about_title": "Info", "about_text": f"{APP_NAME}\nSuchen. Finden. Fertig.\nVersion {VERSION}",
        "ps_view": "Als PowerShell-Liste anzeigen", "invalid_folder": "Ungültiger Ordner",
        "found": "{n} Dateien gefunden", "copied_n": "{n} Elemente kopiert",
        "copied_one": "Kopiert: {p}", "scanning": "Scanne: {p}",
        "no_ffprobe": "ffmpeg nicht gefunden (keine Medieninfo)",
        "select_all": "Alles auswählen", "deselect_all": "Alles abwählen",
        "fit_cols": "Spalten anpassen", "checked_stat": "Ausgewählt: {n} / Gesamt: {t}",
        "export_txt": "Nach TXT exportieren",
        "selected_folders": "{n} Ordner ausgewählt",
        "ctx_open_file": "▶ Datei öffnen", "ctx_open_folder": "📂 Ordner öffnen",
        "ctx_copy_path": "📋 Vollständigen Pfad kopieren", "ctx_check": "✓ Auswahl markieren", "ctx_uncheck": "✗ Auswahl aufheben",
        "set_media_info": "Mediendauer scannen (langsamer)",
        "set_hidden_files": "Versteckte Dateien anzeigen",
        "set_separator": "Kopier-Trennzeichen",
        "sep_newline": "Neue Zeile",
        "sep_comma": "Komma",
        "set_default_dir": "Aktuellen Ordner als Standard festlegen",
        "clear_default_dir": "Standardordner löschen",
        "default_set": "Standardordner gesetzt auf: {p}",
        "default_cleared": "Standardordner gelöscht."
    },
    "es": {
        "file": "Archivo", "settings": "Configuración", "info_menu": "Info", "help": "Ayuda", "exit": "Salir",
        "language": "Idioma", "include_sub": "Incluir subcarpetas",
        "tagline": "Busca. Encuentra. Listo.",
        "scan": "Escanear archivos", "copy_sel": "Copiar rutas", "copy_names": "Copiar nombres", "copy_ps": "Copiar (Formato PS)",
        "header_title": f"{APP_NAME}", "input_folder": "Carpeta seleccionada",
        "browse": "Examinar", "ready": "Listo", "help_dlg_title": "Ayuda",
        "help_text": f"Repo: {REPO_URL}",
        "about_title": "Acerca de", "about_text": f"{APP_NAME}\nBusca. Encuentra. Listo.\nVersión {VERSION}",
        "ps_view": "Mostrar como lista de PowerShell", "invalid_folder": "Carpeta no válida",
        "found": "{n} archivos encontrados", "copied_n": "{n} elementos copiados",
        "copied_one": "Copiado: {p}", "scanning": "Escaneando: {p}",
        "no_ffprobe": "ffmpeg no encontrado",
        "select_all": "Marcar todo", "deselect_all": "Desmarcar todo",
        "fit_cols": "Ajustar columnas", "checked_stat": "Marcados: {n} / Total: {t}",
        "export_txt": "Exportar a TXT",
        "selected_folders": "{n} carpetas seleccionadas",
        "ctx_open_file": "▶ Abrir archivo", "ctx_open_folder": "📂 Abrir carpeta",
        "ctx_copy_path": "📋 Copiar ruta completa", "ctx_check": "✓ Marcar selección", "ctx_uncheck": "✗ Desmarcar selección",
        "set_media_info": "Escanear duración multimedia (más lento)",
        "set_hidden_files": "Mostrar archivos ocultos",
        "set_separator": "Separador de copia",
        "sep_newline": "Nueva línea",
        "sep_comma": "Coma",
        "set_default_dir": "Establecer carpeta actual como predeterminada",
        "clear_default_dir": "Borrar carpeta predeterminada",
        "default_set": "Carpeta predeterminada establecida en: {p}",
        "default_cleared": "Carpeta predeterminada borrada."
    },
}


def which_lang() -> str:
    return QtCore.QSettings(SETTINGS_ORG, APP_ID).value("language", "nl")


def set_lang(lang: str) -> None:
    QtCore.QSettings(SETTINGS_ORG, APP_ID).setValue("language", lang)


def T(key: str) -> str:
    lang = which_lang()
    table = STRINGS.get(lang, STRINGS.get("en", {}))
    return table.get(key, STRINGS.get("en", {}).get(key, key))


def app_base_dir() -> str:
    if getattr(sys, "frozen", False):
        return getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def detect_active_venv_name() -> str:
    exe_dir = os.path.dirname(sys.executable)
    if os.path.basename(exe_dir).lower() == "scripts":
        venv_name = os.path.basename(os.path.dirname(exe_dir))
        if venv_name:
            return venv_name
    return ADVISED_VENV


def build_window_title() -> str:
    return f"{APP_NAME} - {VERSION} - {detect_active_venv_name()}"


def resource_path(filename: str) -> str:
    candidates = [
        os.path.join(app_base_dir(), filename),
        os.path.join(app_base_dir(), "Assets", filename),
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate
    return candidates[0]


def load_app_icon() -> QtGui.QIcon:
    icon_path = resource_path(APP_ICON_FILE)
    if os.path.exists(icon_path):
        return QtGui.QIcon(icon_path)
    return QtGui.QIcon()


def load_header_font_family() -> str:
    font_path = resource_path(HEADER_FONT_FILE)
    if not os.path.exists(font_path):
        return "Ethnocentric"

    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        return "Ethnocentric"

    families = QtGui.QFontDatabase.applicationFontFamilies(font_id)
    return families[0] if families else "Ethnocentric"


def section_title_style() -> str:
    return (
        "color: #ffffff; "
        "font-weight: 900; "
        "font-size: 11pt; "
        "letter-spacing: 0.2px; "
        "padding: 6px 10px; "
        "background-color: #0c1627; "
        "border: 1px solid #263d58; "
        "border-radius: 10px;"
    )


# -------------- utils --------------

def human_size(n: int) -> str:
    step = 1024.0
    for u in ["B", "KB", "MB", "GB", "TB"]:
        if n < step:
            return f"{n:.0f} {u}"
        n /= step
    return f"{n:.0f} PB"


def dur_to_str(s: float) -> str:
    if not s or s <= 0:
        return ""
    m, sec = divmod(int(s + 0.5), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def unique_existing_dirs(paths: Iterable[str]) -> List[str]:
    unique: List[str] = []
    seen = set()
    for raw_path in paths:
        cleaned = os.path.normpath(str(raw_path).strip().strip('"'))
        if not cleaned or not os.path.isdir(cleaned):
            continue
        key = os.path.normcase(cleaned)
        if key in seen:
            continue
        seen.add(key)
        unique.append(cleaned)
    return unique


def compact_scan_roots(paths: Iterable[str], recurse: bool) -> List[str]:
    roots = unique_existing_dirs(paths)
    if not recurse:
        return roots

    compacted: List[str] = []
    compacted_keys: List[str] = []
    for root in sorted(roots, key=lambda item: (len(item), item.lower())):
        root_key = os.path.normcase(root)
        is_nested = False
        for key in compacted_keys:
            try:
                if os.path.commonpath([root_key, key]) == key:
                    is_nested = True
                    break
            except ValueError:
                continue
        if is_nested:
            continue
        compacted.append(root)
        compacted_keys.append(root_key)
    return compacted


def parse_scan_roots_text(text: str) -> List[str]:
    chunks = text.replace("\r", "\n").replace(";", "\n").split("\n")
    return unique_existing_dirs(chunks)


FFPROBE = shutil.which("ffprobe")


def probe_duration(path: str) -> float:
    if not FFPROBE:
        return 0.0
    try:
        creation_flags = 0x08000000 if os.name == "nt" else 0
        out = subprocess.check_output(
            [
                FFPROBE,
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=nk=1:nw=1",
                path,
            ],
            stderr=subprocess.STDOUT,
            creationflags=creation_flags,
        ).decode("utf-8", "ignore").strip()
        return float(out) if out else 0.0
    except Exception:
        return 0.0


def open_file_or_folder(path: str, open_folder: bool = False):
    p = QtCore.QDir.toNativeSeparators(path)
    if open_folder:
        p = os.path.dirname(p)

    try:
        if sys.platform == "win32":
            os.startfile(p)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", p])
        else:
            subprocess.Popen(["xdg-open", p])
    except Exception:
        pass


# -------------- data --------------


@dataclass
class FileInfo:
    name: str
    full_path: str
    size: int
    mtime: float
    ext: str
    root_path: str
    depth: int
    duration: float = 0.0
    checked: bool = False

    @property
    def last_modified_str(self) -> str:
        return dt.datetime.fromtimestamp(self.mtime).strftime("%Y-%m-%d %H:%M:%S")

    @property
    def type_str(self) -> str:
        return (self.ext or "").lstrip(".").upper()

    @property
    def duration_str(self) -> str:
        return dur_to_str(self.duration)


# -------------- model --------------


class FileTableModel(QtCore.QAbstractTableModel):
    COLS = ["✓", "Name", "Depth", "Map", "Type", "Full Path", "Size", "Duration", "Modified"]

    def __init__(self, items: Optional[List[FileInfo]] = None):
        super().__init__()
        self._items: List[FileInfo] = items or []

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self._items)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.COLS)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.COLS[section]
        return None

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        if index.column() == 0:
            return (
                QtCore.Qt.ItemIsEnabled
                | QtCore.Qt.ItemIsSelectable
                | QtCore.Qt.ItemIsUserCheckable
            )
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index: QtCore.QModelIndex, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        fi = self._items[index.row()]
        c = index.column()

        if role == QtCore.Qt.CheckStateRole and c == 0:
            return QtCore.Qt.Checked if fi.checked else QtCore.Qt.Unchecked

        if role == QtCore.Qt.DisplayRole:
            if c == 0: return ""
            if c == 1: return fi.name
            if c == 2: return fi.depth
            if c == 3: return os.path.basename(os.path.dirname(fi.full_path))
            if c == 4: return fi.type_str
            if c == 5: return fi.full_path
            if c == 6: return human_size(fi.size)
            if c == 7: return fi.duration_str
            if c == 8: return fi.last_modified_str

        if role == QtCore.Qt.TextAlignmentRole and c in (2, 6, 7):
            return QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
        if role == QtCore.Qt.ToolTipRole and c == 5:
            return fi.full_path
        return None

    def setData(self, index, value, role):
        if (
            index.isValid()
            and role == QtCore.Qt.CheckStateRole
            and index.column() == 0
        ):
            self._items[index.row()].checked = value == QtCore.Qt.Checked
            self.dataChanged.emit(index, index, [QtCore.Qt.CheckStateRole])
            return True
        return False

    def setItems(self, items: List[FileInfo]) -> None:
        self.beginResetModel()
        self._items = items
        self.endResetModel()

    def itemAt(self, row: int) -> FileInfo:
        return self._items[row]

    def setAllChecked(self, state: bool):
        if not self._items:
            return
        self.beginResetModel()
        for fi in self._items:
            fi.checked = state
        self.endResetModel()


class SortProxy(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.setDynamicSortFilter(True)
        self.setSortRole(QtCore.Qt.DisplayRole)

    def lessThan(self, left, right):
        model = self.sourceModel()
        if not model:
            return super().lessThan(left, right)

        left_item = model.itemAt(left.row())
        right_item = model.itemAt(right.row())
        column = left.column()

        if column == 1:
            return left_item.name.lower() < right_item.name.lower()
        if column == 2:
            return left_item.depth < right_item.depth
        if column == 3:
            left_folder = os.path.basename(os.path.dirname(left_item.full_path)).lower()
            right_folder = os.path.basename(os.path.dirname(right_item.full_path)).lower()
            return left_folder < right_folder
        if column == 4:
            return left_item.type_str.lower() < right_item.type_str.lower()
        if column == 5:
            return left_item.full_path.lower() < right_item.full_path.lower()
        if column == 6:
            return left_item.size < right_item.size
        if column == 7:
            return left_item.duration < right_item.duration
        if column == 8:
            return left_item.mtime < right_item.mtime

        return super().lessThan(left, right)


# -------------- workers --------------


class ScannerWorker(QtCore.QObject):
    finished = QtCore.Signal(list)
    progress = QtCore.Signal(str)

    def __init__(self, roots: List[str], recurse: bool, max_depth: int, want_duration: bool, show_hidden: bool):
        super().__init__()
        self.roots = roots
        self.recurse = recurse
        self.want_duration = want_duration
        self.show_hidden = show_hidden
        self._abort = False
        self.max_depth = max_depth

    @QtCore.Slot()
    def run(self) -> None:
        try:
            items: List[FileInfo] = []
            vid_exts = VIDEO_EXTS
            seen_paths = set()
            for root in self.roots:
                self.progress.emit(T("scanning").format(p=root))
                for fi in self._iter_files(root, self.recurse, self.max_depth):
                    if self._abort:
                        break
                    path_key = os.path.normcase(fi.full_path)
                    if path_key in seen_paths:
                        continue
                    seen_paths.add(path_key)
                    if self.want_duration and fi.ext in vid_exts:
                        fi.duration = probe_duration(fi.full_path)
                    items.append(fi)
                if self._abort:
                    break
            items.sort(key=lambda x: x.mtime, reverse=True)
            self.finished.emit(items)
        except Exception as e:
            self.progress.emit(f"Error: {e}")
            self.finished.emit([])

    def abort(self) -> None:
        self._abort = True

    def _iter_files(self, root: str, recurse: bool, max_depth: int) -> Iterable[FileInfo]:
        stack = [(root, 0)]

        while stack:
            current, depth = stack.pop()

            try:
                with os.scandir(current) as it:
                    for entry in it:

                        # hidden files
                        if not self.show_hidden and entry.name.startswith("."):
                            continue

                        if entry.is_dir(follow_symlinks=False):
                            try:
                                stat = entry.stat()
                                yield FileInfo(
                                    name=entry.name,
                                    full_path=entry.path,
                                    size=0,
                                    mtime=stat.st_mtime,
                                    ext=".MAP",
                                    root_path=root,
                                    depth=depth + 1,
                                    checked=False,
                                )
                            except OSError:
                                pass

                            # 🔥 DEPTH LOGICA
                            if recurse and (max_depth < 0 or depth < max_depth):
                                stack.append((entry.path, depth + 1))

                            continue

                        if entry.is_file(follow_symlinks=False):
                            try:
                                ext = os.path.splitext(entry.name)[1].lower()
                                is_checked = ext in VIDEO_EXTS
                                stat = entry.stat()

                                yield FileInfo(
                                    entry.name,
                                    entry.path,
                                    stat.st_size,
                                    stat.st_mtime,
                                    ext,
                                    root,
                                    depth + 1,
                                    checked=is_checked,
                                )
                            except OSError:
                                continue

            except PermissionError:
                continue


# -------------- UI helpers --------------
class DarkPalette:
    @staticmethod
    def stylesheet() -> str:
        check_svg_path = resource_path("check_white.svg")

        # SVG content for the checkbox
        CHECK_SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2d7bff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>"""

        if not os.path.exists(check_svg_path):
            try:
                with open(check_svg_path, "w", encoding="utf-8") as f:
                    f.write(CHECK_SVG_CONTENT.strip() + "\n")
            except OSError:
                # Als we het bestand niet kunnen schrijven, gaan we verder zonder custom image
                pass

        check_svg_url = check_svg_path.replace("\\", "/")

        return f"""
        QMainWindow, QWidget {{
            background-color: #050812;
            color: #eef5ff;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 10pt;
        }}
        QMenuBar {{
            background: #070d18;
            color: #d8e8fb;
            border-bottom: 1px solid #1d3552;
            padding: 4px 8px;
            font-weight: 700;
        }}
        QMenuBar::item {{
            padding: 7px 12px;
            border-radius: 8px;
            background: transparent;
        }}
        QMenuBar::item:selected {{ background: #13243a; color: #ffffff; }}
        QMenu {{
            background: #0a1220;
            color: #edf6ff;
            border: 1px solid #284765;
            padding: 8px;
        }}
        QMenu::item {{
            padding: 8px 28px;
            border-radius: 7px;
        }}
        QMenu::item:selected {{ background: #1f6feb; color: #ffffff; }}

        QLineEdit {{
            background: #060d18;
            border: 1px solid #263d58;
            padding: 10px 12px;
            border-radius: 12px;
            color: #edf6ff;
            font-weight: 700;
        }}
        QLineEdit:focus {{ border: 1px solid #4aa7e8; }}

        QPushButton {{
            background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #19304d, stop:1 #0f2035);
            border: 1px solid #376797;
            padding: 11px 14px;
            border-radius: 10px;
            color: #f8fbff;
            font-weight: 800;
        }}
        QPushButton:hover {{ background: #1c426c; border-color: #67d4ff; }}
        QPushButton:checked {{ background: #16395e; border-color: #4aa7e8; }}
        QPushButton:pressed {{ background: #0c1a2c; }}
        QPushButton:disabled {{ color: #60758c; background: #0b1523; border-color: #1d3148; }}
        QPushButton#PrimaryButton {{ background: #36bffa; border-color: #8ee4ff; color: #03111f; }}
        QPushButton#PrimaryButton:hover {{ background: #67d4ff; border-color: #8ee4ff; }}

        QCheckBox {{ spacing: 8px; }}
        
        /* CHECKBOX STYLING */
        QCheckBox::indicator, QTableView::indicator {{
            width: 20px; height: 20px;
            border-radius: 6px;
            border: 2px solid #4aa7e8;
            background: #060d18;
        }}
        QCheckBox::indicator:hover, QTableView::indicator:hover {{
            border-color: #67d4ff;
        }}
        QCheckBox::indicator:checked, QTableView::indicator:checked {{
            background-color: transparent;
            border-color: #4aa7e8;
            image: url("{check_svg_url}");
        }}

        QHeaderView::section {{
            background: #13233a;
            color: #dcecff;
            padding: 10px;
            border: none;
            border-right: 1px solid #203752;
            font-weight: 900;
        }}
        QTableView, QPlainTextEdit {{
            background: #060d18;
            alternate-background-color: #091321;
            border: 1px solid #263d58;
            border-radius: 12px;
            color: #edf6ff;
            gridline-color: transparent;
            selection-background-color: #1769aa;
            selection-color: #ffffff;
        }}
        QTreeView, QListView {{
            background: #060d18;
            border: 1px solid #263d58;
            border-radius: 12px;
            color: #edf6ff;
            outline: 0;
        }}
        QTreeView::item:hover, QListView::item:hover {{ background: #13243a; }}
        QTreeView::item:selected, QListView::item:selected {{ background: #1769aa; color: white; }}
        QFrame.card {{
            background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #0b1220, stop:0.52 #101d30, stop:1 #07111f);
            border-radius: 18px;
            border: 1px solid #263d58;
        }}
        QFrame.card:hover {{ border-color: #4aa7e8; }}
        QSplitter::handle {{ background: #1d2a3e; }}
        QScrollBar:vertical {{ background: #07101d; width: 13px; margin: 0; }}
        QScrollBar::handle:vertical {{ background: #294866; min-height: 32px; border-radius: 6px; }}
        QScrollBar::handle:vertical:hover {{ background: #3b6a93; }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
        """


class PSResultDialog(QtWidgets.QDialog):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PowerShell Output")
        self.resize(800, 500)
        lay = QtWidgets.QVBoxLayout(self)
        self.te = QtWidgets.QPlainTextEdit(self)
        self.te.setPlainText(text)
        self.te.setStyleSheet(
            "font-family: Consolas, monospace; background: #0d121c; color: #E6EEF8;"
        )
        lay.addWidget(self.te)
        btns = QtWidgets.QHBoxLayout()
        copy = QtWidgets.QPushButton(T("copy_sel"))
        copy.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton))
        copy.clicked.connect(
            lambda: QtWidgets.QApplication.clipboard().setText(
                self.te.toPlainText()
            )
        )
        btns.addStretch(1)
        btns.addWidget(copy)
        lay.addLayout(btns)


# -------------- main window --------------


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, startup_dir: str = ""):
        super().__init__()
        self.setWindowTitle(build_window_title())
        self.resize(1500, 950)
        
        # Load Settings
        self.settings = QtCore.QSettings(SETTINGS_ORG, APP_ID)
        
        # Check media info setting
        self.want_duration = self.settings.value("scan_media_info", True, type=bool) and bool(FFPROBE)
        self.show_hidden = self.settings.value("show_hidden", False, type=bool)
        
        app_icon = load_app_icon()
        if not app_icon.isNull():
            self.setWindowIcon(app_icon)
        else:
            self.setWindowIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_DirOpenIcon)
            )

        self.setStyleSheet(DarkPalette.stylesheet())
        self._thread, self._worker = None, None
        self._selected_scan_paths: List[str] = []

        self._build_menubar()

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        main_layout = QtWidgets.QVBoxLayout(central)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        header = QtWidgets.QFrame()
        header.setObjectName("HeroCard")
        header.setFixedHeight(60)
        self.header_frame = header
        self._set_header_bg()
        hl = QtWidgets.QHBoxLayout(header)
        hl.setContentsMargins(12, 0, 12, 0)
        hl.setSpacing(14)
        header_font_family = load_header_font_family()
        self.app_name_label = QtWidgets.QLabel(APP_NAME)
        self.app_name_label.setStyleSheet(
            f"color: white; font-family: '{header_font_family}'; font-size: 22px; border: none; background: transparent;"
        )
        separator_label = QtWidgets.QLabel("|")
        separator_label.setStyleSheet(
            "color: white; font-weight: 700; font-size: 20px; border: none; background: transparent;"
        )
        self.tagline_label = QtWidgets.QLabel(T("tagline"))
        self.tagline_label.setStyleSheet(
            f"color: white; font-family: '{header_font_family}'; font-size: 17px; border: none; background: transparent;"
        )
        hl.addWidget(self.app_name_label)
        hl.addWidget(separator_label)
        hl.addWidget(self.tagline_label)
        hl.addStretch(1)

        content_layout = QtWidgets.QHBoxLayout()

        left_card = QtWidgets.QFrame()
        left_card.setProperty("class", "card")
        left_card.setObjectName("Card")
        left_layout = QtWidgets.QVBoxLayout(left_card)
        left_layout.setContentsMargins(12, 12, 12, 12)

        self.fs_model = QtWidgets.QFileSystemModel()
        self.fs_model.setRootPath("")
        self.fs_model.setFilter(
            QtCore.QDir.AllDirs
            | QtCore.QDir.NoDotAndDotDot
            | QtCore.QDir.Drives
        )

        self.lib_model = QtWidgets.QFileSystemModel()
        self.lib_model.setRootPath(QtCore.QDir.homePath())
        self.lib_model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
        self.lib_model.setNameFilters(
            [
                "Desktop",
                "Documents",
                "Music",
                "Pictures",
                "Videos",
                "Downloads",
                "Camera Roll",
                "CameraRoll",
            ]
        )
        self.lib_model.setNameFilterDisables(False)

        lbl_user = QtWidgets.QLabel("Bibliotheken")
        lbl_user.setStyleSheet(section_title_style())
        left_layout.addWidget(lbl_user)

        self.user_list = QtWidgets.QListView()
        self.user_list.setModel(self.lib_model)
        self.user_list.setRootIndex(
            self.lib_model.index(QtCore.QDir.homePath())
        )
        self.user_list.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.user_list.setSpacing(4)
        self.user_list.selectionModel().selectionChanged.connect(
            self._on_tree_selection_changed
        )
        self.user_list.activated.connect(self._on_tree_double_clicked)
        self.user_list.doubleClicked.connect(self._on_tree_double_clicked)
        left_layout.addWidget(self.user_list, 1)

        lbl_drives = QtWidgets.QLabel("Deze PC / Schijven")
        lbl_drives.setStyleSheet(section_title_style())
        left_layout.addWidget(lbl_drives)

        self.folder_tree = QtWidgets.QTreeView()
        self.folder_tree.setModel(self.fs_model)
        self.folder_tree.setHeaderHidden(True)
        self.folder_tree.setRootIndex(self.fs_model.index(""))
        self.folder_tree.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        for c in range(1, 4):
            self.folder_tree.hideColumn(c)
        self.folder_tree.selectionModel().selectionChanged.connect(
            self._on_tree_selection_changed
        )
        self.folder_tree.activated.connect(self._on_tree_double_clicked)
        self.folder_tree.doubleClicked.connect(self._on_tree_double_clicked)
        left_layout.addWidget(self.folder_tree, 2)

        folder_row = QtWidgets.QHBoxLayout()
        folder_row.setSpacing(8)

        self.folder_line = QtWidgets.QLineEdit()
        self.folder_line.setPlaceholderText(T("input_folder"))
        self.folder_line.setClearButtonEnabled(True)
        self.folder_line.returnPressed.connect(self.start_scan)
        folder_row.addWidget(self.folder_line, 1)

        self.browse_btn = QtWidgets.QPushButton(T("browse"))
        self.browse_btn.clicked.connect(self._browse_for_folder)
        folder_row.addWidget(self.browse_btn)
        left_layout.addLayout(folder_row)

        self.recurse_cb = QtWidgets.QCheckBox(T("include_sub"))
        self.recurse_cb.setChecked(True)
        left_layout.addWidget(self.recurse_cb)

        # --- NIEUW: Zoekdiepte combobox ---
        self.depth_combo = QtWidgets.QComboBox()
        self.depth_combo.addItems([
            "1 niveau diep",
            "2 niveaus diep",
            "3 niveaus diep",
            "Onbeperkt"
        ])
        self.depth_combo.setCurrentIndex(3)  # standaard = onbeperkt
        left_layout.addWidget(self.depth_combo)

        # Enable/disable afhankelijk van checkbox
        self.depth_combo.setEnabled(self.recurse_cb.isChecked())
        self.recurse_cb.toggled.connect(self.depth_combo.setEnabled)

        self.scan_btn = QtWidgets.QPushButton(T("scan"))
        self.scan_btn.setObjectName("PrimaryButton")
        self.scan_btn.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_BrowserReload)
        )
        left_layout.addWidget(self.scan_btn)

        right_card = QtWidgets.QFrame()
        right_card.setProperty("class", "card")
        right_card.setObjectName("Card")
        right_layout = QtWidgets.QVBoxLayout(right_card)
        right_layout.setContentsMargins(12, 12, 12, 12)

        lbl_res = QtWidgets.QLabel("Resultaten")
        lbl_res.setStyleSheet(section_title_style())

        res_toolbar = QtWidgets.QHBoxLayout()
        self.sel_all_btn = QtWidgets.QPushButton(T("select_all"))
        self.desel_all_btn = QtWidgets.QPushButton(T("deselect_all"))
        res_toolbar.addWidget(lbl_res)
        res_toolbar.addStretch()
        res_toolbar.addWidget(self.sel_all_btn)
        res_toolbar.addWidget(self.desel_all_btn)

        self.table = QtWidgets.QTableView()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows
        )
        self.table.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.table.setShowGrid(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
            self.show_table_context_menu
        )
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().sectionClicked.connect(
            self._sort_results_by_column
        )

        self.model = FileTableModel([])
        self.proxy = SortProxy()
        self.proxy.setSourceModel(self.model)
        self.table.setModel(self.proxy)
        self._sort_orders = {}
        # --- v2.3 default column widths (from v2.0 Wider) ---
        try:
            widths = [40, 240, 80, 190, 90, 500, 90, 90, 160]
            for i, w in enumerate(widths):
                self.table.setColumnWidth(i, w)
        except Exception:
            pass


        self.table.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Fixed
        )
        self.table.setColumnWidth(0, 40)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Interactive
        )

        action_bar = QtWidgets.QHBoxLayout()
        self.copy_btn = QtWidgets.QPushButton(T("copy_sel"))
        self.copy_btn.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton)
        )

        self.copy_names_btn = QtWidgets.QPushButton(T("copy_names"))
        self.copy_names_btn.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon)
        )

        self.copy_ps_btn = QtWidgets.QPushButton(T("copy_ps"))
        self.copy_ps_btn.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_CommandLink)
        )
        self.export_txt_btn = QtWidgets.QPushButton(T("export_txt"))
        self.export_txt_btn.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon)
        )
        self.fit_cols_btn = QtWidgets.QPushButton(T("fit_cols"))
        self.ps_view_btn = QtWidgets.QPushButton(T("ps_view"))

        action_bar.addWidget(self.copy_btn)
        action_bar.addWidget(self.copy_names_btn)
        action_bar.addWidget(self.copy_ps_btn)
        action_bar.addWidget(self.export_txt_btn)
        action_bar.addWidget(self.fit_cols_btn)
        action_bar.addStretch()
        action_bar.addWidget(self.ps_view_btn)

        right_layout.addLayout(res_toolbar)
        right_layout.addWidget(self.table)
        right_layout.addLayout(action_bar)

        content_layout.addWidget(left_card, 4)
        content_layout.addWidget(right_card, 6)

        footer = QtWidgets.QFrame()
        footer.setFixedHeight(30)
        footer.setStyleSheet("background: transparent; border: none;")
        fl = QtWidgets.QHBoxLayout(footer)
        fl.setContentsMargins(4, 0, 4, 0)
        self.status_lbl = QtWidgets.QLabel(T("ready"))
        self.status_lbl.setStyleSheet("color: #7FAED6;")
        self.footer_lbl = QtWidgets.QLabel("")
        self.footer_lbl.setStyleSheet("color: #4b5770;")
        fl.addWidget(self.status_lbl)
        fl.addStretch()
        fl.addWidget(self.footer_lbl)

        main_layout.addWidget(header)
        main_layout.addLayout(content_layout)
        main_layout.addWidget(footer)

        self.scan_btn.clicked.connect(self.start_scan)
        self.copy_btn.clicked.connect(self.copy_checked)
        self.copy_names_btn.clicked.connect(self.copy_checked_filenames)
        self.copy_ps_btn.clicked.connect(self.copy_checked_ps)
        self.fit_cols_btn.clicked.connect(
            self.table.resizeColumnsToContents
        )
        self.ps_view_btn.clicked.connect(self.show_ps_results)
        self.export_txt_btn.clicked.connect(self.export_checked_txt)
        self.table.activated.connect(self.open_row_file)
        self.table.doubleClicked.connect(self.open_row_file)

        self.sel_all_btn.clicked.connect(
            lambda: self.model.setAllChecked(True)
        )
        self.desel_all_btn.clicked.connect(
            lambda: self.model.setAllChecked(False)
        )
        self.model.dataChanged.connect(self._update_checked_status)
        self.model.modelReset.connect(self._update_checked_status)

        QtGui.QShortcut(
            QtGui.QKeySequence("Ctrl+A"),
            self.table,
            activated=self.table.selectAll,
        )
        QtGui.QShortcut(
            QtGui.QKeySequence("Ctrl+Return"),
            self,
            activated=self.start_scan,
        )
        QtGui.QShortcut(
            QtGui.QKeySequence("Ctrl+Shift+C"),
            self,
            activated=self.copy_checked,
        )
        QtGui.QShortcut(
            QtGui.QKeySequence("Ctrl+Shift+N"),
            self,
            activated=self.copy_checked_filenames,
        )
        QtGui.QShortcut(
            QtGui.QKeySequence("Ctrl+Shift+P"),
            self,
            activated=self.copy_checked_ps,
        )

        # Logic for Default Folder vs Last Folder
        default_folder = self.settings.value("default_start_folder", "")
        last_folder = self.settings.value("last_folder", "")
        
        start_dir = ""
        if default_folder and os.path.isdir(str(default_folder)):
            start_dir = str(default_folder)
        elif last_folder and os.path.isdir(str(last_folder)):
            start_dir = str(last_folder)
            
        if startup_dir and os.path.isdir(startup_dir):
            start_dir = startup_dir

        if start_dir:
            self._set_scan_roots([start_dir])

    def _build_menubar(self):
        mb = self.menuBar()
        m_file = mb.addMenu(T("file"))
        act_exit = QtGui.QAction(T("exit"), self)
        act_exit.setShortcut("Ctrl+Q")
        act_exit.triggered.connect(self.close)
        m_file.addAction(act_exit)

        # --- SETTINGS MENU ---
        m_set = mb.addMenu(T("settings"))
        
        # 1. Media Info Toggle
        act_media = QtGui.QAction(T("set_media_info"), self, checkable=True)
        act_media.setChecked(self.want_duration)
        if not FFPROBE:
             act_media.setEnabled(False)
             act_media.setText(act_media.text() + " (ffprobe missing)")
        act_media.triggered.connect(self._toggle_media_info)
        m_set.addAction(act_media)
        
        # 2. Hidden Files Toggle
        act_hidden = QtGui.QAction(T("set_hidden_files"), self, checkable=True)
        act_hidden.setChecked(self.show_hidden)
        act_hidden.triggered.connect(self._toggle_hidden_files)
        m_set.addAction(act_hidden)
        
        m_set.addSeparator()
        
        # 3. Copy Separator Submenu
        m_sep = m_set.addMenu(T("set_separator"))
        sep_grp = QtGui.QActionGroup(self)
        current_sep = self.settings.value("copy_separator", "newline")
        
        for val, lbl in [("newline", "sep_newline"), ("comma", "sep_comma")]:
            a = QtGui.QAction(T(lbl), self, checkable=True)
            if current_sep == val:
                a.setChecked(True)
            a.triggered.connect(lambda c, v=val: self._set_separator(v))
            sep_grp.addAction(a)
            m_sep.addAction(a)

        m_set.addSeparator()

        # 4. Default Start Folder
        m_def_dir = m_set.addMenu("Standaard Startmap") # Keeping label simple in code, relying on translation
        act_set_def = QtGui.QAction(T("set_default_dir"), self)
        act_set_def.triggered.connect(self._set_default_folder)
        m_def_dir.addAction(act_set_def)
        
        act_clr_def = QtGui.QAction(T("clear_default_dir"), self)
        act_clr_def.triggered.connect(self._clear_default_folder)
        m_def_dir.addAction(act_clr_def)

        m_set.addSeparator()
        
        # Language
        lang = m_set.addMenu(T("language"))
        grp = QtGui.QActionGroup(self)
        for c, l in [
            ("en", "English"),
            ("nl", "Nederlands"),
            ("de", "Deutsch"),
            ("es", "Español"),
        ]:
            a = QtGui.QAction(l, self, checkable=True)
            if which_lang() == c:
                a.setChecked(True)
            a.triggered.connect(lambda checked, x=c: self._change_lang(x))
            grp.addAction(a)
            lang.addAction(a)

        m_info = mb.addMenu(T("info_menu"))
        m_info.addAction(T("help"), self._show_help)
        m_info.addAction(T("about_title"), self._show_about)

    # --- Settings Logic ---
    
    def _toggle_media_info(self, checked):
        self.want_duration = checked
        self.settings.setValue("scan_media_info", checked)
        
    def _toggle_hidden_files(self, checked):
        self.show_hidden = checked
        self.settings.setValue("show_hidden", checked)

    def _set_separator(self, val):
        self.settings.setValue("copy_separator", val)

    def _set_default_folder(self):
        roots = parse_scan_roots_text(self.folder_line.text())
        curr = roots[0] if roots else self.folder_line.text().strip()
        if curr and os.path.isdir(curr):
            self.settings.setValue("default_start_folder", curr)
            self.setStatus(T("default_set").format(p=curr))
        else:
            self.setStatus(T("invalid_folder"))

    def _clear_default_folder(self):
        self.settings.remove("default_start_folder")
        self.setStatus(T("default_cleared"))
        
    def _get_separator_char(self):
        val = self.settings.value("copy_separator", "newline")
        if val == "comma":
            return ", "
        return "\n"

    def _sort_results_by_column(self, column: int):
        if column == 0:
            return
        current_order = self._sort_orders.get(column, QtCore.Qt.DescendingOrder)
        next_order = (
            QtCore.Qt.AscendingOrder
            if current_order == QtCore.Qt.DescendingOrder
            else QtCore.Qt.DescendingOrder
        )
        self._sort_orders[column] = next_order
        self.proxy.sort(column, next_order)
        self.table.horizontalHeader().setSortIndicator(column, next_order)

    # ----------------------

    def _change_lang(self, code):
        set_lang(code)
        self.status_lbl.setText("Language changed. Restart recommended.")
        self.setWindowTitle(build_window_title())
        self.app_name_label.setText(APP_NAME)
        self.tagline_label.setText(T("tagline"))
        self.folder_line.setPlaceholderText(T("input_folder"))
        self.browse_btn.setText(T("browse"))
        self.scan_btn.setText(T("scan"))
        self.copy_btn.setText(T("copy_sel"))
        self.copy_names_btn.setText(T("copy_names"))
        self.copy_ps_btn.setText(T("copy_ps"))
        self.fit_cols_btn.setText(T("fit_cols"))
        self.export_txt_btn.setText(T("export_txt"))
        self.sel_all_btn.setText(T("select_all"))
        self.desel_all_btn.setText(T("deselect_all"))
        self.recurse_cb.setText(T("include_sub"))
        self._update_checked_status()


    def _show_help(self):
        QtWidgets.QMessageBox.information(
            self, T("help_dlg_title"), T("help_text")
        )

    def _show_about(self):
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle(T("about_title"))
        dlg.setModal(True)
        dlg.resize(760, 620)

        app_icon = load_app_icon()
        if not app_icon.isNull():
            dlg.setWindowIcon(app_icon)

        lay = QtWidgets.QVBoxLayout(dlg)
        lay.setContentsMargins(20, 20, 20, 20)
        lay.setSpacing(14)

        title_lbl = QtWidgets.QLabel(APP_NAME)
        title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        title_lbl.setStyleSheet(
            "color: #eaf7ff; font-size: 22px; font-weight: 700;"
        )
        lay.addWidget(title_lbl)

        subtitle_lbl = QtWidgets.QLabel(T("tagline"))
        subtitle_lbl.setAlignment(QtCore.Qt.AlignCenter)
        subtitle_lbl.setStyleSheet(
            "color: #9edfff; font-size: 13px; font-weight: 600;"
        )
        lay.addWidget(subtitle_lbl)

        info_lbl = QtWidgets.QLabel(f"Version {VERSION}\nRepo: {REPO_URL}")
        info_lbl.setAlignment(QtCore.Qt.AlignCenter)
        info_lbl.setTextFormat(QtCore.Qt.PlainText)
        info_lbl.setStyleSheet(
            "color: #d7e7f6; font-size: 12px;"
        )
        lay.addWidget(info_lbl)

        about_image_path = resource_path(ABOUT_IMAGE_FILE)
        if os.path.exists(about_image_path):
            pixmap = QtGui.QPixmap(about_image_path)
            if not pixmap.isNull():
                image_lbl = QtWidgets.QLabel()
                image_lbl.setAlignment(QtCore.Qt.AlignCenter)
                image_lbl.setPixmap(
                    pixmap.scaled(
                        680,
                        380,
                        QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation,
                    )
                )
                lay.addWidget(image_lbl)

        btn_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        btn_box.accepted.connect(dlg.accept)
        lay.addWidget(btn_box)

        dlg.exec()

    def _set_header_bg(self):
        style = """
            background: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #09243f, stop:0.36 #0b3a5f, stop:0.68 #17243f, stop:1 #101725);
            border-radius: 20px;
            border: 1px solid #2f80bd;
        """
        self.header_frame.setStyleSheet(style)

    def _set_scan_roots(self, paths: Iterable[str]) -> None:
        roots = unique_existing_dirs(paths)
        self._selected_scan_paths = roots
        self.folder_line.setText("; ".join(roots))
        if roots:
            self.setStatus(T("selected_folders").format(n=len(roots)))

    def _collect_selected_scan_paths(self) -> List[str]:
        paths: List[str] = []
        for view in (self.user_list, self.folder_tree):
            selection_model = view.selectionModel()
            if not selection_model:
                continue
            for index in selection_model.selectedRows():
                path = index.model().filePath(index)
                if os.path.isdir(path):
                    paths.append(path)
        return unique_existing_dirs(paths)

    def _on_tree_selection_changed(self, sel, desel):
        paths = self._collect_selected_scan_paths()
        if paths:
            self._set_scan_roots(paths)

    def _browse_for_folder(self):
        roots = parse_scan_roots_text(self.folder_line.text())
        current = roots[0] if roots else self.folder_line.text().strip()
        base_dir = current if os.path.isdir(current) else QtCore.QDir.homePath()
        selected = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            T("input_folder"),
            base_dir,
        )
        if selected:
            self._set_scan_roots([selected])

    def _on_tree_double_clicked(self, idx):
        source_model = idx.model()
        path = source_model.filePath(idx)

        # Synchroniseer de onderste TreeView en klap deze open
        if os.path.isdir(path):
            tree_idx = self.fs_model.index(path)
            if tree_idx.isValid():
                self.folder_tree.setCurrentIndex(tree_idx)
                self.folder_tree.scrollTo(tree_idx)
                self.folder_tree.expand(tree_idx)
            self._set_scan_roots(self._collect_selected_scan_paths() or [path])

    def start_scan(self):
        roots = parse_scan_roots_text(self.folder_line.text())
        roots = compact_scan_roots(roots, self.recurse_cb.isChecked())
        if not roots:
            self.setStatus(T("invalid_folder"))
            return

        self._set_scan_roots(roots)
        QtCore.QSettings(SETTINGS_ORG, APP_ID).setValue("last_folder", roots[0])

        if self._thread:
            self._worker.abort()
        self.model.setItems([])
        self.setStatus(T("scanning").format(p="; ".join(roots)))

        self._thread = QtCore.QThread()
        # Pass show_hidden and want_duration correctly
        if not self.recurse_cb.isChecked():
            max_depth = 0
        else:
            idx = self.depth_combo.currentIndex()
            if idx == 0:
                max_depth = 1
            elif idx == 1:
                max_depth = 2
            elif idx == 2:
                max_depth = 3
            else:
                max_depth = -1  # onbeperkt

        self._worker = ScannerWorker(
            roots,
            self.recurse_cb.isChecked(),
            max_depth,
            self.want_duration,
            self.show_hidden
        )
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.progress.connect(self.setStatus)
        self._worker.finished.connect(self.on_scan_finished)
        self._worker.finished.connect(self._thread.quit)
        self._worker.finished.connect(self._worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()

    def on_scan_finished(self, items):
        self.model.setItems(items)
        self.proxy.invalidate()
        
        self.model.setAllChecked(True)
        
        self.setStatus(T("found").format(n=len(items)))
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(0, 40)

    def show_table_context_menu(self, pos: QtCore.QPoint):
        menu = QtWidgets.QMenu(self.table)

        act_open_file = menu.addAction(
            self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon),
            T("ctx_open_file"),
        )
        act_open_folder = menu.addAction(
            self.style().standardIcon(QtWidgets.QStyle.SP_DirOpenIcon),
            T("ctx_open_folder"),
        )
        act_copy_path = menu.addAction(
            self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton),
            T("ctx_copy_path"),
        )
        menu.addSeparator()
        act_check = menu.addAction(T("ctx_check"))
        act_uncheck = menu.addAction(T("ctx_uncheck"))

        idx = self.table.indexAt(pos)
        has_row = idx.isValid()
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows and has_row:
            selected_rows = [idx]

        action = menu.exec(self.table.viewport().mapToGlobal(pos))
        if not action:
            return

        if action == act_open_file and has_row:
            self.open_row_file(idx)
        elif action == act_open_folder and has_row:
            fi = self.model.itemAt(self.proxy.mapToSource(idx).row())
            open_file_or_folder(fi.full_path, open_folder=True)
        elif action == act_copy_path and has_row:
            fi = self.model.itemAt(self.proxy.mapToSource(idx).row())
            QtWidgets.QApplication.clipboard().setText(fi.full_path)
            self.setStatus(T("copied_one").format(p=fi.full_path))
        elif action == act_check and selected_rows:
            self._set_rows_checked(selected_rows, True)
        elif action == act_uncheck and selected_rows:
            self._set_rows_checked(selected_rows, False)

    def _set_rows_checked(self, proxy_indexes, state):
        for idx in proxy_indexes:
            src_idx = self.proxy.mapToSource(idx)
            check_idx = self.model.index(src_idx.row(), 0)
            self.model.setData(
                check_idx,
                QtCore.Qt.Checked if state else QtCore.Qt.Unchecked,
                QtCore.Qt.CheckStateRole,
            )

    def open_row_file(self, idx):
        if idx.isValid():
            fi = self.model.itemAt(self.proxy.mapToSource(idx).row())
            open_file_or_folder(fi.full_path)

    def _get_checked_files(self) -> List[FileInfo]:
        return [fi for fi in self.model._items if fi.checked]

    def copy_checked(self):
        files = self._get_checked_files()
        sep = self._get_separator_char()
        if files:
            QtWidgets.QApplication.clipboard().setText(
                sep.join([f.full_path for f in files])
            )
            self.setStatus(T("copied_n").format(n=len(files)))
        else:
            self.setStatus("Niets aangevinkt")

    def copy_checked_filenames(self):
        files = self._get_checked_files()
        sep = self._get_separator_char()
        if files:
            QtWidgets.QApplication.clipboard().setText(
                sep.join([f.name for f in files])
            )
            self.setStatus(T("copied_n").format(n=len(files)))
        else:
            self.setStatus("Niets aangevinkt")

    def copy_checked_ps(self):
        files = self._get_checked_files()
        if files:
            lines = [f"{f.full_path}\t{f.size}" for f in files]
            QtWidgets.QApplication.clipboard().setText("\n".join(lines))
            self.setStatus(T("copied_n").format(n=len(files)))
        else:
            self.setStatus("Niets aangevinkt")

    def export_checked_txt(self):
        files = self._get_checked_files()
        if not files:
            self.setStatus("Niets aangevinkt")
            return
        lines = ["FullName\tLength\tLastWriteTime"] + [
            f"{f.full_path}\t{f.size}\t{f.last_modified_str}" for f in files
        ]
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save TXT", "", "Text (*.txt)"
        )
        if fn:
            with open(fn, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            self.setStatus(f"Exported to {fn}")

    def show_ps_results(self):
        lines = ["FullName\tLength\tLastWriteTime"]
        for r in range(self.model.rowCount()):
            fi = self.model.itemAt(r)
            lines.append(
                f"{fi.full_path}\t{fi.size}\t{fi.last_modified_str}"
            )
        PSResultDialog("\n".join(lines), self).exec()

    def setStatus(self, t):
        self.status_lbl.setText(t)

    def _update_checked_status(self, *a):
        checked = len(self._get_checked_files())
        total = self.model.rowCount()
        self.footer_lbl.setText(
            T("checked_stat").format(n=checked, t=total) if total > 0 else ""
        )


def main():
    QtCore.QCoreApplication.setOrganizationName(SETTINGS_ORG)
    QtCore.QCoreApplication.setApplicationName(APP_ID)
    QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(
        QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QtWidgets.QApplication(sys.argv)
    app_icon = load_app_icon()
    if not app_icon.isNull():
        app.setWindowIcon(app_icon)
    startup_dir = ""
    if len(sys.argv) > 1:
        candidate = os.path.normpath(sys.argv[1].strip('"'))
        if os.path.isfile(candidate):
            candidate = os.path.dirname(candidate)
        if os.path.isdir(candidate):
            startup_dir = candidate

    w = MainWindow(startup_dir=startup_dir)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
