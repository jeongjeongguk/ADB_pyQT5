setlocal
set date2=%date:-=%
set time2=%time: =0%
set time3=%date2%_%time2:~0,2%%time2:~3,2%_%time2:~6,2%

::company
::pyinstaller -n "ADB_GUI_%time3%.exe" -p="C:\Users\Jeongkuk\PycharmProjects\androidADB\ui_py" --onefile -p="C:\Python35-32\Lib\site-packages\PyQt5" --icon="C:\Users\Jeongkuk\PycharmProjects\androidADB\ui\icons\Main.ico" "main.py"  
pyinstaller -n "ADB_GUI_%time3%.exe" -p="C:\Users\Jeongkuk\PycharmProjects\androidADB\ui_py" --onefile -p="C:\Python35-32\Lib\site-packages\PyQt5" --icon="C:\Users\Jeongkuk\PycharmProjects\androidADB\ui\icons\Main.ico" "main_old.py" 
::--noconsole 

::home
::pyinstaller -n "ADB_GUI_%time3%.exe" --noconsole --onefile --icon="C:\Users\Administrator\PycharmProjects\androidADB\ui\icons\Main.ico" --uac-admin "main.py"  


endlocal
pause