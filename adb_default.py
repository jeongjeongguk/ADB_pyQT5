import os, time
import subprocess as cmd

class default(object):
    def __init__(self):
        self.filepath = ""
        self.packageName = ""
        self.startActivity = ""
        #self.ConnectDevices = []
        #self.DisconnectDevices = []

    @classmethod
    def check_connect(cls):
        os.system("adb devices")
        '''
        devicesList = cmd.check_output("adb devices | findstr device", stderr=cmd.STDOUT, shell=True).decode("utf-8")
        devicesList = devicesList.replace("List of devices attached","")
        devicesList = devicesList.replace("\r\n","")
        #b'List of devices attached\r\nLGF700K525fbc3\tdevice\r\n'
        #TODO : devicesList를 self.ConnectDevices 에 추가하고, self.ConnectDevices 프린트
        print(devicesList)
        '''

    def install_apk(self, filepath):
        #os.chdir("./apks")
        company = "C:\\Users\\Jeongkuk\\PycharmProjects\\androidADB\\apks"
        home = "C:\\Users\\Administrator\\PycharmProjects\\androidADB\\apks"
        if os.getcwd() != company: os.chdir(company)
        # TODO : error: more than one device/emulator 예외처리필요
        os.system("adb install -r " + filepath) #TODO: 인스톨 여기에요~~~~~~~~~~~~~~~~~~~~~~
        time.sleep(10)
        self.run_apk(filepath)
        #TODO : adb: error: failed to copy 'teamUP-store-release-v3.5.2.7-122.apk' to '/data/local/tmp/teamUP-store-release-v3.5.2.7-122.apk': no response: Connection reset by peer
        #TODO : 위 내용관련한 처리필요


    @classmethod
    def run_info(cls, filepath):
        cls.filepath = filepath
        company = "C:\\Users\\Jeongkuk\\PycharmProjects\\androidADB\\apks"
        home = "C:\\Users\\Administrator\\PycharmProjects\\androidADB\\apks"
        if os.getcwd() != company: os.chdir(company)
        try:
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr launchable",
                                    stderr=cmd.STDOUT, shell=True)
            cls.startActivity = test.decode("utf-8").split(" ")[1].split("'")[1]
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr package",
                                    stderr=cmd.STDOUT, shell=True)
            cls.packageName = test.decode("utf-8").split(" ")[1].split("'")[1]
        except:
            # TODO:launchable activity가 구해지지 않는 경우 존재. : 추가처리 필요.
            pass

    @classmethod
    def run_apk(cls,filepath):
        cls.run_info(filepath)
        os.system("adb shell am start -n " + cls.packageName +"/"+cls.startActivity)

    @classmethod
    def uninstall_apk(cls,filepath):
        cls.run_info(filepath)
        os.system("adb uninstall " + cls.packageName)
        cls.check_install()

    @classmethod
    def reinstall_apk(cls, filepath):
        cls.run_info(filepath)
        os.system("adb install -r " + filepath)
        cls.run_apk(filepath)

    @classmethod
    def check_install(cls):
        try:
            test = cmd.check_output("adb shell pm list package -f | findstr " + cls.packageName,
                                    stderr=cmd.STDOUT, shell=True).decode("utf-8").split("=")[1]
            print(test)
            print("installed program")
        except:
            print("Not installed program")

    @staticmethod
    def adb_kill(self):
        os.system("adb kill-server")
        self.adb_restrat()
        self.check_connect()

    @staticmethod
    def adb_restart(self):
        os.system("adb start-server")

    @staticmethod
    def adb_device_reboot(self):
        os.system("adb reboot")

'''
adb uninstall com.estsoft.alsong
adb shell am start -a android.intent.action.VIEW -d "https://play.google.com/store/apps/details?id=com.estsoft.alsong"
::adb install  .\alsong_release.apk
@echo off
adb shell am start -n com.estsoft.alsong/com.estsoft.alsong.ui.AlsongStartActivity
echo 설정할 것들 설정하세요
pause
::adb uninstall com.estsoft.alsong
adb install -r .\alsong_4.0.0.11_7cha.apk
::adb install -r .\alsong_4.0.0.10_7cha.apk
::adb shell am start -n com.estsoft.alsong/com.estsoft.alsong.ui.AlsongStartActivity
adb shell am start -n com.estsoft.alsong/com.estsoft.alsong.SplashActivity
pause
'''

if __name__ == "__main__":
    filepath = "alsong_4.0.7.3.apk"
    #filepath = "Alsong_v3.810_1cha.apk"
    test = default()
    test.run_info(filepath)
    test.uninstall_apk(filepath)
    #test.adb_kill()
    test.install_apk(filepath)
    #test.run_apk(filepath)
    #test.reinstall_apk(filepath)
    #test.check_install()
    #test.uninstall_apk(filepath)
    #test.check_connect()
    '''
    time.sleep(30)
    filepath = "alsong_4.0.7.3.apk"
    test.run_info(filepath)
    test.install_apk(filepath)
    '''
