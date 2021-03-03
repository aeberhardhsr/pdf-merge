# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Your Main App Name.py'],
             pathex=['<Your Working Dir Path'],
             binaries=[],
             datas=[('<Your Data File Path>', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='<You Exe App Name (No need to include .exe)>',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='<Icon path to use as program icon>')
