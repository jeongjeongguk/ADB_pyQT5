import adb_default
import os, time, datetime
import subprocess as cmd

class record(adb_default.default):
    def __init__(self):

        self.today = ""
        self.currentTime = ""
        self.makedir()

    @classmethod
    def screenshot(cls): #TODO : 기기 잠금화면 상태유무 확인후, 잠금해제 메소드 추가 필요
        adb_default.default.check_connect()
        os.system("adb shell rm -r /mnt/sdcard/ScreenCapture")
        os.system("adb shell mkdir /mnt/sdcard/ScreenCapture")

        os.system("adb shell screencap /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
        cls.check_time()
        #print(cls.currentTime)
        os.system("ren test.png "+ cls.currentTime +".jpg")

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
    test.screenshot()
    #test.makedir()
    #test.check_time()
    pass