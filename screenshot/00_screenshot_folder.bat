::@echo off
::cd %USERPROFIL%\Desktop
setlocal
set date2=%date:-=%
set time2=%time: =0%
set time3=%time2:~0,2%
mkdir %date2%
endlocal
::pause
