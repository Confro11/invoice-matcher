# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_dynamic_libs

block_cipher = None

# Sbíráme vše co uvicorn potřebuje
uvicorn_datas, uvicorn_binaries, uvicorn_hiddenimports = collect_all('uvicorn')
calamine_datas, calamine_binaries, calamine_hiddenimports = collect_all('python_calamine')

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=uvicorn_binaries + calamine_binaries,
    datas=[
        ('static', 'static'),
        *uvicorn_datas,
        *calamine_datas,
    ],
    hiddenimports=[
        *uvicorn_hiddenimports,
        *calamine_hiddenimports,
        'anyio',
        'anyio._backends._asyncio',
        'anyio._backends._trio',
        'starlette.routing',
        'starlette.staticfiles',
        'starlette.responses',
        'fastapi',
        'lxml',
        'lxml.etree',
        'lxml._elementpath',
        'openpyxl',
        'pandas',
        'h11',
        'click',
        'multipart',
        'python_multipart',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='InvoiceMatcher',
    debug=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    argv_emulation=False,
    target_arch=None,
    icon=None,
)
