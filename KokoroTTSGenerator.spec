# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('src', 'src'), ('.venv/lib/python3.12/site-packages/nicegui', 'nicegui'), ('.venv/lib/python3.12/site-packages/language_data', 'language_data'), ('.venv/lib/python3.12/site-packages/language_tags', 'language_tags'), ('.venv/lib/python3.12/site-packages/espeakng_loader', 'espeakng_loader'), ('.venv/lib/python3.12/site-packages/en_core_web_sm', 'en_core_web_sm'), ('.venv/lib/python3.12/site-packages/espeakng_loader-0.2.4.dist-info', 'espeakng_loader-0.2.4.dist-info'), ('.venv/lib/python3.12/site-packages/misaki', 'misaki')]
binaries = []
hiddenimports = []
tmp_ret = collect_all('en_core_web_sm')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KokoroTTSGenerator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='KokoroTTSGenerator',
)
