
for %%i in (*.qrc) do pyrcc5  %%i -o %%i.py
ren *.qrc.py *_rc.py
pause