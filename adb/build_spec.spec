# -*- mode: python -*-

block_cipher = None

a = Analysis(['.\\ui.py'],
             pathex=['C:\\Users\\Jeongkuk\\PycharmProjects\\untitled3'],
             hiddenimports=['sys','os','PyQt5','six','re'],
             hookspath=None,
             runtime_hooks=None)

ui_file =  [('adb_test1.ui', 'C:\\Users\\Jeongkuk\\PycharmProjects\\untitled3\\adb_test1.ui', 'DATA')]
pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='AndroidADB.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas + ui_file,
               strip=None,
               upx=True,
               name='AndroidADB')