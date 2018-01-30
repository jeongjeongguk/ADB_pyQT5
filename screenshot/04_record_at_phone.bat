@echo off
setlocal

echo adb shell screenrecord 명령어로 녹화를 시작합니다. 녹화중지는 Ctrl+C 입력후 y를 입력하세요.
echo.
echo 현재 날짜: %date%
echo 현재 시각: %time%
echo.
echo --------------------------
echo.


adb shell rm -r /mnt/sdcard/alyac_sample
adb shell mkdir /mnt/sdcard/alyac_sample

adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/alyac_sample/test.mp4

pause
:: 4.2에서 screenrecord 없다고한다.