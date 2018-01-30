::cd %USERPROFILE%\Desktop\screenshot

adb shell rm -r /mnt/sdcard/ScreenCapture
adb shell mkdir /mnt/sdcard/ScreenCapture

adb shell screencap /mnt/sdcard/ScreenCapture/test.png

::for /L %%i in (0,1,100) do (
::  adb shell screencap /mnt/sdcard/ScreenCapture/%%i.raw
::  adb pull screencap /mnt/sdcard/ScreenCapture/%%i.raw
::) 
pause

