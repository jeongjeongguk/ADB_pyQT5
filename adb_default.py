import ctypes
import datetime
import os
import subprocess as cmd
import time
from xml.dom.minidom import parse


class default(object):
    company = "C:\\Users\\Jeongkuk\\PycharmProjects\\androidADB\\apks"
    home = "C:\\Users\\Administrator\\PycharmProjects\\androidADB\\apks"

    def __init__(self):
        self.filepath = ""
        self.packageName = ""
        self.startActivity = ""
        self.ConnectDevices = []
        #self.DisconnectDevices = []
        self.today = ""
        self.currentTime = ""
        self.deviceData = ""
        self.makedir()

    @classmethod
    def check_connect(cls):
        try:
            # \r\n 제거는 윈도우기준
            List_misi = cmd.check_output("adb devices | findstr device", stderr=cmd.STDOUT, shell=True) \
                                            .decode("utf-8") \
                                            .replace("List of devices attached", "") \
                                            .replace("\r\n", "") \
                                            .replace("device", "")
            cls.ConnectDevices = List_misi.split("	")
            cls.ConnectDevices.remove("")
            return len(cls.ConnectDevices)
        except:
            return 0

    @classmethod
    def install_apk(cls, filepath): # def install_apk(self, filepath, option): # option : r, b, ...
        if os.getcwd() != cls.company: os.chdir(cls.company)
        # TODO : error: more than one device/emulator 예외처리필요
        os.system("adb install -r " + filepath) #TODO: 인스톨 여기에요~~~~~~~~~~~~~~~~~~~~~~
        time.sleep(10)
        cls.run_apk(filepath)
        #TODO : adb: error: failed to copy 'teamUP-store-release-v3.5.2.7-122.apk' to '/data/local/tmp/teamUP-store-release-v3.5.2.7-122.apk': no response: Connection reset by peer
        #TODO : 위 내용관련한 처리필요

    @classmethod
    def run_info(cls, filepath):
        cls.filepath = filepath
        if os.getcwd() != cls.company: os.chdir(cls.company)
        try:
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr launchable",
                                    stderr=cmd.STDOUT, shell=True)
            cls.startActivity = test.decode("utf-8").split(" ")[1].split("'")[1]
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr package",
                                    stderr=cmd.STDOUT, shell=True)
            cls.packageName = test.decode("utf-8").split(" ")[1].split("'")[1]
        except:
            # TODO:launchable activity가 구해지지 않는 경우 존재. : 추가처리 필요.
            # ?????? 언제 안구해지지? 런쳐액티버티 가렸을때 못찾음 -> 파싱으로 찾기
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

    '''
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
    @classmethod
    def update(cls, filepath_old, filepath_new): #TODO: devices arg 전달필요
        try:
            cls.run_info(filepath_old)
            os.system("adb uninstall " + cls.packageName)
            time.sleep(5)
            cls.run_info(filepath_new)
            os.system("adb uninstall " + cls.packageName)
            time.sleep(5)
        except:
            pass
        CHK_ANYDevice = cls.check_connect() #check_any_connect_device
        print(CHK_ANYDevice)
        if CHK_ANYDevice == 0 :
            #TODO : HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            test = ctypes.windll.user32.MessageBoxW(0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", 0)
            print(test)
        else :
            try :
                cls.run_info(filepath_old) #알송기준 : com.estsoft.alsong
                #TODO : 구버전 명시하지 않았고, 출시버전으로 확인시에만 사용. 구버전 apk 사용-> 해당apk설치
                cmd.check_output(
                    "adb shell am start -a android.intent.action.VIEW -d \"https://play.google.com/store/apps/details?id=" \
                    + cls.packageName + "\"", stderr=cmd.STDOUT, shell=True)
                cls.touchByID("com.android.vending:id/buy_button") # 플레이스토어 설치버튼 터치
                cls.touchByID("com.android.vending:id/continue_button") # 플레이스토어 팝업뷰>설치버튼 터치
                time.sleep(30)

                CHK_start = \
                cmd.check_output("adb shell pm list package -f " + cls.packageName, stderr=cmd.STDOUT, shell=True) \
                                    .decode("utf-8").split(":")[1].split("=")[0]
                cmd.check_output("adb pull " + CHK_start + " test.apk", stderr=cmd.STDOUT, shell=True)
                cls.run_apk("test.apk")
                # cls.run_apk(filepath_old) #TODO : 출시버전의 apk 추출해서 packagename, startactivity 구하기

                ctypes.windll.user32.MessageBoxW(0, "구버전에서 설정할 내용들 설정하세요.", "설정안내", 0)
                time.sleep(120)
                cls.reinstall_apk(filepath_new)

            except cmd.CalledProcessError :
                ctypes.windll.user32.MessageBoxW(0, "다수의 기기가 연결되어있습니다.", "테스트기기 선택필요", 0)

    @staticmethod
    def exportXML():
        cmd.call("adb shell uiautomator dump /mnt/sdcard/test.xml", stderr=cmd.STDOUT, shell=True)
        cmd.call("adb pull /mnt/sdcard/test.xml ./test_me.xml", stderr=cmd.STDOUT, shell=True)

    @classmethod
    def touchByID(cls, ID):
        cls.exportXML()
        directory = '%s/' % os.getcwd()
        dom = parse(directory + ".\\test_me.xml")
        for node in dom.getElementsByTagName('node'):
            if node.getAttribute('resource-id') == ID:
                position = node.getAttribute('bounds')
                positionL = position.split('][')[0].split('[')[1]
                positionLX = positionL.split(',')[0]
                positionLY = positionL.split(',')[1]

                positionR = position.split('][')[1].split(']')[0]
                positionRX = positionR.split(',')[0]
                positionRY = positionR.split(',')[1]

                positionCX = (int(positionLX) + int(positionRX)) / 2
                positionCY = (int(positionLY) + int(positionRY)) / 2
        cmd.check_output("adb shell input tap %s %s" % (positionCX, positionCY), stderr=cmd.STDOUT, shell=True)

    # command set : "adb reboot", "adb start-server", "adb kill-server", ... etc
    @staticmethod
    def controlDevice(self, command):
        os.system(command)

    @classmethod
    def makedir(cls):
        cls.today = datetime.datetime.now().strftime("%y%m%d")
        check_folder = cmd.call("dir " + cls.today, stderr=cmd.STDOUT, shell=True)
        if check_folder != False:
            os.system("mkdir " + cls.today)
            print("make directory " + cls.today)  # TODO: Need to change method to "pop-up message"
        else:
            print("생성된 폴더내에 파일이 저장됩니다.")  # TODO: Need to change method to "pop-up message"

    @classmethod
    def check_time(cls):
        cls.currentTime = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        print(cls.currentTime)

    @classmethod
    def device_info(cls, select_device):
        select_device = ""  # TODO : delete this line
        os_ver = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.release",
                                  stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        api_level = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.sdk",
                                     stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        model = cmd.check_output("adb shell " + select_device + "getprop ro.product.model",
                                 stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        cls.deviceData = model + "_" + os_ver + "_API" + api_level
        print(cls.deviceData)

    @classmethod
    def capture2image(cls):#TODO : 기기 잠금화면 상태유무 확인후, 잠금해제 메소드 추가 필요
        cls.check_connect()
        os.system("adb shell rm -r /mnt/sdcard/ScreenCapture")
        os.system("adb shell mkdir /mnt/sdcard/ScreenCapture")

        os.system("adb shell screencap /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
        cls.check_time()
        cls.device_info(None)
        changedName = cls.currentTime + "_" + cls.deviceData+".jpg"
        os.system("ren test.png "+ changedName)
        os.system("move " + changedName + " " +cls.today)

    @classmethod
    def capture2viedo(cls):
        cls.check_connect()
        cls.device_info(None)
        # TODO : 4.4 이상일때에만 영상녹화하고, 메시지다이얼로그의 '녹화끝','취소'리턴받으면 녹화중지시키고 영상뺴오기
        cls.check_time()
        changedName = cls.currentTime + "_" + cls.deviceData + ".mp4"
        os.system("ren test.mp4 " + changedName)
        os.system("move " + changedName + " " + cls.today)
        pass

if __name__ == "__main__":
    #'''
    filepath = "alsong_4.0.7.3.apk"
    # filepath = "Alsong_v3.810_1cha.apk"
    test = default()
    # test.run_info(filepath)
    # test.uninstall_apk(filepath)
    # test.adb_kill()
    # test.install_apk(filepath)
    # test.run_apk(filepath)
    # test.reinstall_apk(filepath)
    # test.check_install()
    # test.uninstall_apk(filepath)
    # test.check_connect()
    # test.update(None,None)
    # filepath_new = "alsong_4.0.7.3.apk"
    # filepath_old = "Alsong_v3.810_1cha.apk"
    # test.update(filepath_old,filepath_new)
    # time.sleep(30)
    # filepath = "alsong_4.0.7.3.apk"
    # test.run_info(filepath)
    # test.install_apk(filepath)
    # test.capture2image()