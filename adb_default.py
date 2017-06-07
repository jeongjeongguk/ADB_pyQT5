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
            # \r\n 제거는 윈도우10 x64 Enterprise 1607 기준
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
        test = cmd.check_output("aapt dump badging " + filepath + " | findstr package",
                                stderr=cmd.STDOUT, shell=True)
        cls.packageName = test.decode("utf-8").split(" ")[1].split("'")[1]
        try:
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr launchable",
                                    stderr=cmd.STDOUT, shell=True)
            cls.startActivity = test.decode("utf-8").split(" ")[1].split("'")[1]
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
            # print(test)
            # print("installed program")
            if test != None :
                ctypes.windll.user32.MessageBoxW \
                    (0, "패키지명 : %s \n설치유무 : 설치됨" % cls.packageName, "설치확인", 0)
        except:
            # print("Not installed program")
            try:
                ctypes.windll.user32.MessageBoxW \
                    (0, "패키지명 : %s \n설치유무 : 설치안됨" %cls.packageName, "설치확인", 0)
            except:
                ctypes.windll.user32.MessageBoxW \
                    (0, "선택한 설치파일의 경로 및 파일명을 확인해주세요.\n(영문,숫자만 가능)", "설치확인", 0)

    @classmethod
    def update(cls, filepath_old, filepath_new): #TODO: devices arg 전달필요
        '''
        :param filepath_old:
        :param filepath_new:
        :return:
        '''
        #TODO : 1. 플레이스토어 -> 셋업 / 2. 구셋업 -> 신셋업
        '''
        adb uninstall com.estsoft.alsong
        ::adb shell am start -a android.intent.action.VIEW -d "https://play.google.com/store/apps/details?id=com.estsoft.alsong"
        adb install  .\Alsong_v3.810_1cha.apk
        adb shell am start -n com.estsoft.alsong/com.estsoft.alsong.ui.AlsongStartActivity
        echo 설정할 것들 설정하세요
        pause
        ::adb uninstall com.estsoft.alsong
        adb install -r .\alsong_4.0.8.0_with_report.apk
        adb shell am start -n com.estsoft.alsong/com.estsoft.alsong.SplashActivity
        pause
        '''

        try:
            cls.run_info(filepath_old)
            cmd.check_output("adb uninstall " + cls.packageName, stderr=cmd.STDOUT, shell=True)
            time.sleep(5)
            cls.run_info(filepath_new)
            cmd.check_output("adb uninstall " + cls.packageName, stderr=cmd.STDOUT, shell=True)
            time.sleep(5)
        except:
            pass
        CHK_ANYDevice = cls.check_connect() #check_any_connect_device
        # print(CHK_ANYDevice)
        if CHK_ANYDevice == 0 :
            ctypes.windll.user32.MessageBoxW(0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", 0)
        else :
            try :
                cls.run_info(filepath_old) #알송기준 : com.estsoft.alsong
                #TODO : 구버전 명시하지 않았고, 출시버전으로 확인시에만 사용. 구버전 apk 사용-> 해당apk설치
                cmd.check_output(
                    "adb shell am start -a android.intent.action.VIEW -d \"https://play.google.com/store/apps/details?id=" \
                    + cls.packageName + "\"", stderr=cmd.STDOUT, shell=True)
                cls.touchByID("com.android.vending:id/buy_button") # 플레이스토어 설치버튼 터치
                try :
                    cls.touchByID("com.android.vending:id/continue_button") # 플레이스토어 팝업뷰>설치버튼 터치 #TODO: 안뜨기도 함
                except:
                    pass
                time.sleep(30)
                CHK_imsi = {}
                CHK_start = \
                cmd.check_output("adb shell pm list package -f " + cls.packageName, stderr=cmd.STDOUT, shell=True) \
                                    .decode("utf-8").split("\r\n")
                CHK_start.remove('')
                for imsi in range(0,len(CHK_start)):
                    CHK_start[imsi] = CHK_start[imsi].split(":")[1]
                    CHK_imsi[CHK_start[imsi].split("=")[1]] = CHK_start[imsi].split("=")[0]

                imsi2 = CHK_imsi.get(cls.packageName)
                command = "adb pull " + imsi2 + " test.apk"
                cmd.check_output(command, stderr=cmd.STDOUT, shell=True)
                time.sleep(10)
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

    @staticmethod
    def deleteData(self, package_name):
        try :
            os.system("adb shell pm clear "+ package_name)
            # test = cmd.check_output("adb shell pm clear " + package_name, stderr=cmd.STDOUT, shell=True)
            ctypes.windll.user32.MessageBoxW(0, package_name + "의 앱데이터가 삭제되었습니다.", package_name, 0)
        except:
            ctypes.windll.user32.MessageBoxW(0, "패키지명으로 설치된 앱이 확인되지 않습니다.", "패키지명 확인필요", 0)

    @staticmethod
    def getCurrentActivity(self):
        test = cmd.check_output("adb shell \"dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'\"",
                                stderr=cmd.STDOUT, shell=True)
        test = test.decode("utf-8")
        ctypes.windll.user32.MessageBoxW(0, test, "현재 화면정보", 0)

    @staticmethod
    def goSetLanguagePage(self):
        os.system("adb shell am start -n com.android.settings/.LanguageSettings")

    @classmethod
    def makedir(cls):
        cls.today = datetime.datetime.now().strftime("%y%m%d")
        check_folder = cmd.call("dir " + cls.today, stderr=cmd.STDOUT, shell=True)
        if check_folder != False:
            os.system("mkdir " + cls.today)
            ctypes.windll.user32.MessageBoxW(0, "[폴더생성 완료]\n폴더명 : " + cls.today, "스크린샷 저장폴더생성", 0)
            # print("make directory " + cls.today)
        else:
            ctypes.windll.user32.MessageBoxW(0, "[스크린샷 저장경로]\n폴더명 : "+ cls.today, "스크린샷 저장경로안내", 0)

    @classmethod
    def check_time(cls):
        cls.currentTime = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        # print(cls.currentTime)

    @classmethod
    def device_info(cls, select_device): #TODO : 여려기기 연결되어있을때에, 기기를 선택해서 기기별 리스트에 정보저장필요
        select_device = ""  # TODO : delete this line
        os_ver = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.release",
                                  stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        api_level = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.sdk",
                                     stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        model = cmd.check_output("adb shell " + select_device + "getprop ro.product.model",
                                 stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        cls.deviceData = model + "_" + os_ver + "_API" + api_level
        # print(cls.deviceData)

    @classmethod
    def capture2image(cls):#TODO : 기기 잠금화면 상태유무 확인후, 잠금해제 메소드 추가 필요
        cls.check_connect()
        os.system("adb shell rm -r /mnt/sdcard/ScreenCapture")
        os.system("adb shell mkdir /mnt/sdcard/ScreenCapture")

        os.system("adb shell screencap /mnt/sdcard/ScreenCapture/test.png")
        os.system("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png")
        os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
        cls.check_time()
        time.sleep(1)
        cls.device_info(None)
        changedName = cls.currentTime + "_" + cls.deviceData+".jpg"
        os.system("ren test.png "+ changedName)
        time.sleep(1)
        os.system("move " + changedName + " " +cls.today) # 이거 안됨

    @classmethod
    def capture2viedo(cls): # 함수 호출시 try...except pass로 묶을것. 최대 정확히 3분까지만 녹화됨
        ConnectedDevicesCnt = cls.check_connect()
        if ConnectedDevicesCnt > 0 :
            cls.device_info(None)
            # print(ConnectedDevicesCnt)
            # print(cls.deviceData)
            ctypes.windll.user32.MessageBoxW \
            (0, "현재 %i대의 기기가 PC에 연결되어있습니다.\n\n[연결된기기]\n%s" %(ConnectedDevicesCnt, cls.deviceData), "연결된 기기", 0)
        else :
            ctypes.windll.user32.MessageBoxW \
                (0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", 0)
        # TODO : 4.4 이상일때에만 영상녹화하고, 메시지다이얼로그의 '녹화끝','취소'리턴받으면 녹화중지시키고 영상뺴오기
        device_api = cls.deviceData.split("_")[1]
        device_api = device_api.split("I")[0].replace("\r","")
        videoEnableOSver = 4.4
        # print("연결된 기기의 OS 버전은 " + device_api)
        if float(device_api) < videoEnableOSver :
            ctypes.windll.user32.MessageBoxW(0, "선택된 기기에서는 녹화가 되지 않습니다.", "녹화지원안됨", 0)
        else:
            try :
                cmd.check_output("adb shell rm -r /mnt/sdcard/ADB_record", stderr=cmd.STDOUT, shell=True)
                cmd.check_output("adb shell mkdir /mnt/sdcard/ADB_record", stderr=cmd.STDOUT, shell=True)
            except :
                pass
            # New window cmd : start cmd/k command
            os.system("start /B start cmd.exe @cmd /k "
                      "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4")
            path = os.getcwd().replace("\\","/").replace("\r","").replace("\n","")
            time.sleep(1)
            RecordCnt = ctypes.windll.user32.MessageBoxW \
                (0, "영상기록을 시작합니다.\n확인 : 영상기록 PC전송\n취소 : 영상기록삭제", "영상기록중", 1)
            if RecordCnt == 1: # 확인 : 기기 -> PC 로 영상전송
                os.system("TASKKILL /F /IM cmd.exe /T")
                # os.system("TASKKILL /F /FI \"WINDOWTITLE eq C:\\WINDOWS\\system32\\cmd.exe - adb shell *\" /T")
                time.sleep(1)
                cmd.check_output("adb pull /mnt/sdcard/ADB_record/test.mp4 %s/test.mp4" % path, stderr=cmd.STDOUT, shell=True)
            else : # 취소 : 기기에서 삭제
                os.system("TASKKILL /F /IM cmd.exe /T")
                cmd.check_output("adb shell rm /mnt/sdcard/ADB_record/test.mp4", stderr=cmd.STDOUT, shell=True)

        cls.check_time()
        changedName = cls.currentTime + "_" + cls.deviceData + ".mp4"
        os.system("cd %s"%path)
        os.system("ren test.mp4 " + changedName)
        os.system("move " + changedName + " " + cls.today)

if __name__ == "__main__":
    # '''
    # filepath = "alsong_4.0.7.3.apk"
    # filepath = "a.apk"
    # filepath = "teamUP-teamup_store-release-v3.6.0.1-133.apk"
    #
    # filepath = "teamUP-teamup_store-release-v3.6.0.2-134.apk"
    # filepath = "teamUP-teamup_test-release-v3.6.0.2-134.apk"
    # filepath = "teamUP-cmc_store-release-v3.6.0.2-134.apk"
    #
    # filepath = "alsong_4.0.8.0_with_report.apk"
    #
    # filepath = "Alsong_v3.810_1cha.apk"
    # filepath = "AlsongAndroid-4.0.8.2_2cha.apk"
    #
    # filepath ="AlzipAndroid-release-v1.3.7_2.apk"
    #
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
    # filepath_new = "teamUP-teamup_store-release.apk"
    # filepath_old = "teamUP-teamup_store-release-v3.6.0.0-132.apk"
    # test.update(filepath_old,filepath_new)

    # TODO : 데이터 삭제
    # test.deleteData(None, "com.estsoft.alzip")

    # TODO : 언어 변경 화면으로 이동
    # test.controlDevice(None, "adb shell am start -n com.android.settings/.LanguageSettings")
    test.goSetLanguagePage(None)

    #TODO : 현재화면 구하기 ( 커맨드창에서만 확인가능 )
    # test.getCurrentActivity(None)

    # test.controlDevice(None,"adb shell am satrt -n com.android.settings/1000")
    #
    # filepath_new = "alsong_1.5.0.0_1cha.apk"
    # filepath_old = "alsong_4.0.8.0_with_report.apk"
    # filepath_old = "alsong_1.5.0.0_1cha.apk"
    # filepath_new = "AlsongAndroid-4.0.8.2_2cha.apk"
    # test.update(filepath_old, filepath_new)
    #
    # text = "controlDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicec" \
    #        "ontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDeviceco" \
    #        "ntrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecon" \
    #        "trolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecont" \
    #        "rolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontr" \
    #        "olDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontro" \
    #        "lDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrol" \
    #        "DevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolD" \
    #        "evicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDe" \
    #        "vicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDev" \
    #        "icecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevi" \
    #        "cecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevice" \
    #        "controlDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicec" \
    #        "ontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDeviceco" \
    #        "ntrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevicecontrolDevice"
    # text = "https://docs.google.com/spreadsheets/d/1SeoAONbApwsWDIhGgFnJgeqoTHmZMO4WOfiQO34_y7s/edit#gid=1535606058"
    # text = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222"
    #
    # text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012"
    # test.controlDevice(None,"adb shell input text " + text)
    #
    #
    # time.sleep(30)
    # filepath = "alsong_4.0.7.3.apk"
    # test.run_info(filepath)
    # test.install_apk(filepath)
    # test.capture2image()
    # try :
    #     test.capture2viedo()
    # except :
    #     pass
    # from cProfile import Profile
    # from pstats import Stats
    # profiler = Profile()
    # profiler.runcall(test.capture2viedo)
    # stats = Stats()
    # stats.strip_dirs()
    # stats.sort_stats('cumulative')
    # stats.print_stats()
