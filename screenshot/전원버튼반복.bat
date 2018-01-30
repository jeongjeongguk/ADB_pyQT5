for /L %%i in (0,1,10) do (
 adb shell input keyevent KEYCODE_POWER
 timeout /t 2
 adb shell input keyevent KEYCODE_POWER
 timeout /t 2
) 