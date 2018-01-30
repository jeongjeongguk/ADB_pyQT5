setlocal
set date2=%date:-=%
set time2=%time: =0%
set time3=%date2:~4,4%_%time2:~0,2%%time2:~3,2%_%time2:~6,2%

FOR /F "tokens=* USEBACKQ" %%F IN (`adb shell getprop ro.build.version.release`) DO ( SET osver=%%F )
FOR /F "tokens=* USEBACKQ" %%F IN (`adb shell getprop ro.build.version.sdk`) DO ( SET apilevel=API%%F )
FOR /F "tokens=* USEBACKQ" %%F IN (`adb shell getprop ro.product.model`) DO ( SET model=%%F )

set osver=%osver: =%
set apilevel=%apilevel: =%
set model=%model: =%

ren screenshot.png %time3%_%model%_%osver%_%apilevel%.jpg