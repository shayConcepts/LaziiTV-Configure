# -*- mode: python -*-
a = Analysis(['laziitv_configure_gtk.py'],
             pathex=['./'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='laziitv_configure_gtk.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False
        )
coll = COLLECT(exe,
               a.binaries,
                   [('icudt.dll', 'icudt.dll', 'BINARY')],
                     [('libEGL.dll', 'libEGL.dll', 'BINARY')],
                     [('d3dcompiler_43.dll', 'd3dcompiler_43.dll', 'BINARY')],
                     [('libGLESv2.dll', 'libGLESv2.dll', 'BINARY')],
                     [('locales\\en-US.pak', 'locales\\en-US.pak', 'DATA')],
                     [('cef.pak', 'cef.pak', 'DATA')],
                     [('cefclient.exe', 'cefclient.exe', 'DATA')],
                     [('devtools_resources.pak', 'devtools_resources.pak', 'DATA')],
                     [('subprocess.exe', 'subprocess.exe', 'DATA')],
					 [('cefpython-BSD-3-License.txt','cefpython-BSD-3-License.txt', 'DATA')],
					 [('file_extensions.json','file_extensions.json','DATA')],
					 [('key_bindings.json','key_bindings.json','DATA')],
					 [('icon.ico','icon.ico','DATA')],
					 [('icon_big.ico','icon_big.ico','DATA')],
					 [('LICENSE.txt','LICENSE.txt','DATA')],
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='laziitv_configure_gtk')
