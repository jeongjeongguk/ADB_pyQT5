import os, time

for item in range(70000):
    os.system("adb shell input swipe 691 1373 691 348")
    time.sleep(1)