@echo off
REM build_windows.bat
REM Windows build script for KokoroTTSGenerator using uv and pyinstaller

REM Exit on error
setlocal enabledelayedexpansion
set ERRLEV=0

REM Check for cmake
where cmake >nul 2>nul
if errorlevel 1 (
    echo Error: cmake is not installed. Please install it (e.g., choco install cmake) and try again.
    exit /b 1
)

REM Ensure we're in the script's directory
cd /d "%~dp0"

REM Clean previous build artifacts
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist KokoroTTSGenerator.spec del /q KokoroTTSGenerator.spec

REM Build UPX from source if not already built
if not exist external\upx\src\upx.exe (
    echo Building UPX from source...
    if not exist external\upx (
        git clone https://github.com/upx/upx.git external\upx
        if errorlevel 1 (
            echo Error: Failed to clone UPX repository.
            exit /b 1
        )
    )
    pushd external\upx
    git submodule update --init
    REM On Windows, building UPX requires MSYS2/MinGW or MSVC. You may need to build manually.
    echo Please build UPX manually for Windows if not already built. Press any key to continue...
    pause
    popd
) else (
    echo UPX already built, skipping build.
)

REM Run PyInstaller with UPX for compression
REM Note: --strip is ignored on Windows, but kept for parity.
uv run pyinstaller app.py ^
    -n KokoroTTSGenerator ^
    --noconfirm ^
    --clean ^
    --collect-all "en_core_web_sm" ^
    --add-data "src;src" ^
    --add-data ".venv/Lib/site-packages/nicegui;nicegui" ^
    --add-data ".venv/Lib/site-packages/language_data;language_data" ^
    --add-data ".venv/Lib/site-packages/language_tags;language_tags" ^
    --add-data ".venv/Lib/site-packages/espeakng_loader;espeakng_loader" ^
    --add-data ".venv/Lib/site-packages/en_core_web_sm;en_core_web_sm" ^
    --add-data ".venv/Lib/site-packages/espeakng_loader-0.2.4.dist-info;espeakng_loader-0.2.4.dist-info" ^
    --add-data ".venv/Lib/site-packages/misaki;misaki" ^
    --icon=icon.ico ^
    --upx-dir=external\upx\src

if errorlevel 1 (
    echo Build failed.
    exit /b 1
)

echo Build complete. Executable is in the dist\ directory.
exit /b 0
