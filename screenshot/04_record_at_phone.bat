@echo off
setlocal

echo adb shell screenrecord ��ɾ�� ��ȭ�� �����մϴ�. ��ȭ������ Ctrl+C �Է��� y�� �Է��ϼ���.
echo.
echo ���� ��¥: %date%
echo ���� �ð�: %time%
echo.
echo --------------------------
echo.


adb shell rm -r /mnt/sdcard/alyac_sample
adb shell mkdir /mnt/sdcard/alyac_sample

adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/alyac_sample/test.mp4

pause
:: 4.2���� screenrecord ���ٰ��Ѵ�.