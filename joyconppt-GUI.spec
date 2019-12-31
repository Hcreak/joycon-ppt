# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['joyconppt-GUI.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\joycon-ppt'],
             binaries=[],
             datas=[
                 ('joyconppt.ico', '.'),
                 ('jc_right.png', '.'),
                 ('jc_right_on.png', '.')
             ],
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
          name='joyconppt-GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='joyconppt.ico')
