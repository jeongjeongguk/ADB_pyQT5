import adb_default
import os, time, datetime
import subprocess as cmd

class record(adb_default.default):
    def __init__(self):
        self.today = ""
        self.currentTime = ""
        self.deviceData = {}
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
        cls.device_info(None)
        os.system("ren test.png "+ cls.currentTime + "_" + cls.deviceData+".jpg")

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
        cls.currentTime = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        print(cls.currentTime)

    @classmethod
    def device_info(cls, *devices):
        for arg in devices :
            select_device = []
            select_device.append(arg)
        # select_device = "" #TODO : delete this line
            os_ver = cmd.check_output("adb shell "+ select_device[arg] +"getprop ro.build.version.release",
                             stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n","")
            api_level = cmd.check_output("adb shell "+ select_device[arg]+"getprop ro.build.version.sdk",
                             stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n","")
            model = cmd.check_output("adb shell "+ select_device[arg]+"getprop ro.product.model",
                             stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n","")
            cls.deviceData = model + "_" + os_ver +"_API"+ api_level
        print(cls.deviceData)

    @classmethod
    def check_connect(cls):
        try:
            # \r\n 제거는 윈도우기준
            List_misi = cmd.check_output("adb devices | findstr device", stderr=cmd.STDOUT, shell=True) \
                .decode("utf-8") \
                .replace("List of devices attached", "") \
                .replace("\r\n", "") \
                .replace("device", "") #TODO : 제거가 아니라, 이것도 따로 뽑아서 속성으로 묶어야됨. wifi인 경우 확인필요
            cls.ConnectDevices = List_misi.split("	")
            cls.ConnectDevices.remove("")
            # return len(cls.ConnectDevices)
            return cls.ConnectDevices
        except:
            return 0


if __name__ == "__main__":

    test = record()
    # test.screenshot()
    # test.makedir()
    # test.check_time()
    # test.device_info(None)
    print(test.check_connect())