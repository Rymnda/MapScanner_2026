#define MyAppName "MapScanner 2026"
#define MyAppVersion "v1.0.0"
#define MyAppPublisher "Rymnda"
#define MyAppExeName "MapScanner_2026_portable.exe"
#define MySetupName "MapScanner_2026_setup"

[Setup]
AppId={{E6B07E89-9704-4ADF-B92F-0B560B13AB8B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\MapScanner 2026
DefaultGroupName={#MyAppName}
OutputDir=installer_output
OutputBaseFilename={#MySetupName}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
SetupIconFile=Assets\MapScanner_icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
LicenseFile=Assets\LICENSE

[Languages]
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"

[Tasks]
Name: "desktopicon"; Description: "Snelkoppeling op bureaublad"; Flags: unchecked
Name: "context_dir"; Description: "Context menu: right-click on a folder"; Flags: unchecked
Name: "context_bg"; Description: "Context menu: right-click in the background of an open folder"; Flags: unchecked

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Registry]
Root: HKCR; Subkey: "Directory\shell\MapScannerHere"; ValueType: string; ValueName: ""; ValueData: "MapScanner hier openen"; Flags: uninsdeletekey; Tasks: context_dir
Root: HKCR; Subkey: "Directory\shell\MapScannerHere"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName}"; Tasks: context_dir
Root: HKCR; Subkey: "Directory\shell\MapScannerHere\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Tasks: context_dir
Root: HKCR; Subkey: "Directory\Background\shell\MapScannerHere"; ValueType: string; ValueName: ""; ValueData: "MapScanner hier openen"; Flags: uninsdeletekey; Tasks: context_bg
Root: HKCR; Subkey: "Directory\Background\shell\MapScannerHere"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName}"; Tasks: context_bg
Root: HKCR; Subkey: "Directory\Background\shell\MapScannerHere\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%V"""; Tasks: context_bg
