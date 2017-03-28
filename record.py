import adb_default
import os, time, datetime
import subprocess as cmd

class record(adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.today = ""
        self.currentTime = ""
        self.makedir()

    """

    adb shell rm -r /mnt/sdcard/ScreenCapture
    adb shell mkdir /mnt/sdcard/ScreenCapture

    adb shell screencap /mnt/sdcard/ScreenCapture/test.png

    adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png

    adb shell rm /mnt/sdcard/ScreenCapture/test.png

    adb shell rm /mnt/sdcard/ScreenCapture/test.png

    FOR /F "tokens=* USEBACKQ" %%F IN (`adb shell getprop ro.build.version.release`) DO ( SET osver=%%F )
    FOR /F "tokens=* USEBACKQ" %%F IN (`adb shell getprop ro.build.version.sdk`) DO ( SET apilevel=API%%F )
    FOR /F "tokens=* USEBACKQ" %%F IN (`adb shell getprop ro.product.model`) DO ( SET model=%%F )

    set osver=%osver: =%
    set apilevel=%apilevel: =%
    set model=%model: =%

    setlocal
    set date2=%date:-=%
    set time2=%time: =0%
    set time3=%date2:~4,4%_%time2:~0,2%%time2:~3,2%_%time2:~6,2%

    ren test.png %time3%_%model%_%osver%_%apilevel%.jpg
    """
    @classmethod
    def screenshot(cls): #TODO : 기기 잠금화면 상태유무 확인후, 잠금해제 메소드 추가 필요
        #TODO: 부모클래스의 클래스 메소드 Call ???
        os.system("adb shell rm -r /mnt/sdcard/ScreenCapture")
        os.system("adb shell mkdir /mnt/sdcard/ScreenCapture")

        os.system("adb shell screencap /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")

        os.systme("ren test.png "+ cls.currentTime +".jpg")


    @classmethod
    def makedir(cls):
        cls.today = datetime.datetime.now().strftime("%y%m%d")
        check_folder = cmd.call("dir "+ cls.today, stderr=cmd.STDOUT, shell=True)
        if check_folder != False:
            os.system("mkdir " + cls.today)
            print("make directory " + cls.today) #TODO: Need to change method to "pop-up message"
        else :
            print("hello") #TODO: Need to change method to "pop-up message"

    @classmethod
    def check_time(cls):
        cls.currentTime = datetime.datetime.now().strftime("%H%M%S")
        print(cls.currentTime)


if __name__ == "__main__":

    test = record()
    #test.screenshot()
    #test.makedir()
    test.check_time()
    pass