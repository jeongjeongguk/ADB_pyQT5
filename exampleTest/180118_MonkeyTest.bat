@echo off
echo remove script file
adb shell rm -f /mnt/sdcard/180118_MonkeyTest.txt
echo move script file
adb push 180118_MonkeyTest.txt /mnt/sdcard/
pause
setlocal
set /p cnt=Enter the number of times to repeat the script:
adb shell monkey -f /mnt/sdcard/180118_MonkeyTest.txt %cnt%
pause