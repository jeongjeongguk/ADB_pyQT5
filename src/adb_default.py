'''
ADB를 활용하는 기능들에 대한 함수모음
'''
import ctypes, datetime, time, os, sys
import subprocess as cmd
import win32com.shell.shell as win32shell
from xml.dom.minidom import parse
import win32api
import consts_string
from moviepy.editor import *
import logging
import logging.handlers
from PIL import Image
import re

logger = logging.getLogger('mylogger') # 로거 인스턴스를 만든다
fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s') # 포매터를 만든다
fileHandler = logging.FileHandler('./runtime_ADBGUI.log')# 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
streamHandler = logging.StreamHandler()
fileHandler.setFormatter(fomatter) # 각 핸들러에 포매터를 지정한다.
streamHandler.setFormatter(fomatter)
logger.addHandler(fileHandler) # 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)

class defaultADB(object) :
    def __init__(self):
        self.filepath = ""
        self.packageName = ""
        self.startActivity = ""
        self.ConnectDevices = []
        # self.DisconnectDevices = []
        self.today = ""
        self.currentTime = ""
        self.deviceData = ""
        self.makedir()

    @classmethod
    def check_connect(cls):
        '''
        check & return number of connected android devices.
        If any devices don't connected, '-1' is returned.
        using_place: capture2image, capture2video, install_apk, run_info, update
        :return: len(cls.ConnectDevices)
        '''
        try:
            # \r\n 제거는 윈도우10 x64 Enterprise 1607 기준
            List_misi = cmd.check_output("adb devices | findstr device", stderr=cmd.STDOUT, shell=True) \
                .decode("utf-8") \
                .replace("List of devices attached", "") \
                .replace("\r\n", "") \
                .replace("device", "")
            cls.ConnectDevices = List_misi.split("	")
            cls.ConnectDevices.remove("")
            # print(cls.ConnectDevices) # 여기에, 연결된 기기들 접근 serial이 다 모임

            # TODO: device 제거하지말고, 해당 기기와 같이 묶어서 튜플로 가기, 공백문자는 정규식으로 구분.
            # List_misi = cmd.check_output("adb devices | findstr device", stderr=cmd.STDOUT, shell=True) \
            #     .decode("utf-8") \
            #     .replace("List of devices attached", "")
            # List_misi = re.sub('\s', '', List_misi)  # white space 제거

            return len(cls.ConnectDevices)
        except:
            return -1

    @classmethod
    def install_apk(cls, filepath, option): # def install_apk(self, filepath, option): # option : r, b, ...
        '''
        :param filepath: to install file(.apk)'s path. Must use in English&Number. (because adb doesn't use another language)
        :param option: "" or something
        :return:
        '''
        fileCheck = cls.run_info(filepath)
        try :
            if  fileCheck[0]:
                if option == "" :
                    title = "설치 시작확인"
                    version = cls.getVersion(filepath, "")
                    message = "버전 : {}\n".format(version)
                else :
                    ConnectedDevicesCnt = cls.check_connect()
                    if ConnectedDevicesCnt != 0:
                        title = "덮어쓰기설치 시작확인"
                        OldVersion, NewVersion = cls.getVersion(cls.packageName, filepath)
                        message = "설치된 버전 : {}\n설치할 버전 : {}\n" \
                                  "\n[주의]\n" \
                                  "같거나 높은 버전으로만 덮어쓰기 설치가 가능합니다.\n"\
                                    .format(OldVersion, NewVersion)
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", consts_string.show_flag.foreground.value)
                        return None

                userChoice = ctypes.windll.user32.MessageBoxW \
                            (
                                0,  "패키지명 : {} \n"
                                    "{}"
                                    "\n'확인'을 클릭하시면, 설치를 시작합니다."
                                    "\n기기에따라 최대 20초가량 소요됩니다.".format(cls.packageName, message), title, 1 | consts_string.show_flag.foreground.value
                            )
                # https://msdn.microsoft.com/en-us/library/ms645505(VS.85).aspx

                if userChoice == 1:
                    ConnectedDevicesCnt = cls.check_connect()
                    if ConnectedDevicesCnt != 0:
                        if option == "": cls.uninstall_apk("path", filepath)
                        os.system("adb install " + option + filepath)
                        ctypes.windll.user32.MessageBoxW(0, "기기를 확인해주세요.", "작업완료", consts_string.show_flag.foreground.value)
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", consts_string.show_flag.foreground.value)
                else :
                    ctypes.windll.user32.MessageBoxW(0, "설치가 취소되었습니다.", "설치취소", consts_string.show_flag.foreground.value)
            else :
                ctypes.windll.user32.MessageBoxW(0, "경로나 파일을 확인해주세요", "apk파일확인안됨", consts_string.show_flag.foreground.value)
        except:
            logger.error("{} : Failed to install".format(cls.install_apk.__name__))
        #TODO : adb: error: failed to copy 'teamUP-store-release-v3.5.2.7-122.apk' to '/data/local/tmp/teamUP-store-release-v3.5.2.7-122.apk': no response: Connection reset by peer
        #TODO : 위 내용관련한 처리필요

        #TODO : Failed to install C:/Users/Jeongkuk/PycharmProjects/androidADB/apks/4.0.16.1.apk: Failure [INSTALL_PARSE_FAILED_NO_CERTIFICATES: Failed to collect certificates from /data/app/vmdl490955904.tmp/base.apk using APK Signature Scheme v2: SHA-256 digest of contents did not verify]
        #-----> 최신버전 설치후에 이전버전 덮어쓰기 설치시도해서 설치실패후, 최신버전 재설치할려다가 발생된 메시지 : TODO : 처리필요

        #TODO : Failure [INSTALL_FAILED_UID_CHANGED] ??? 삭제후 설치과정에서, 계속뜸.. 원인확인필요 Gpro 4.4.2 alsong 4.1.1.3 에서 4.1.1.4 갈때 발생.
        # https://byunsooblog.wordpress.com/2013/12/07/install_failed_uid_changed-%EC%97%90%EB%9F%AC/
        # DB삭제가 완전히 안된거. 제대로 삭제가 필요하다.
    @classmethod
    def run_info(cls, filepath):
        ConnectedDevicesCnt = cls.check_connect()
        if ConnectedDevicesCnt > 0:
            if os.path.isfile(filepath) :
                cls.filepath = filepath
            else :
                return False, "Check path or file", "Check path or file"
            # if os.getcwd() != cls.company: os.chdir(cls.company)
            # TODO : 패키지명으로 들어올때, 연결이 중간에 끊어진 상황 처리 필요
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr package",
                                    stderr=cmd.STDOUT, shell=True)
            cls.packageName = test.decode("utf-8").split(" ")[1].split("'")[1]
            try:
                test = cmd.check_output("aapt dump badging " + filepath + " | findstr launchable",
                                        stderr=cmd.STDOUT, shell=True)
                cls.startActivity = test.decode("utf-8").split(" ")[1].split("'")[1]
                return True, cls.packageName, cls.startActivity
            except:
                # TODO:launchable activity가 구해지지 않는 경우 존재. : 추가처리 필요.
                # ?????? 언제 안구해지지? 런쳐액티버티 가렸을때 못찾음 -> 파싱으로 찾기
                # pass
                return False, "None", "None"
        else:
            ctypes.windll.user32.MessageBoxW \
                (0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", consts_string.show_flag.foreground.value)
            # win32api.MessageBox(0, 'hello', 'title', 0x00001000)
            return False, "None", "None"

    @classmethod
    def run_apk(cls,filepath):
        if cls.run_info(filepath)[0] :
            os.system("adb shell am start -n " + cls.packageName +"/"+cls.startActivity)
            ctypes.windll.user32.MessageBoxW(0, "기기를 확인해주세요.", "작업완료", consts_string.show_flag.foreground.value)
        else:
            pass

    @classmethod
    def uninstall_apk(cls, *args):
        try :
            if args[0] == "path" :
                cls.run_info(args[1])
            elif args[0] == "packageName" :
                cls.packageName = args[1]
            os.system("adb uninstall " + cls.packageName)
            ctypes.windll.user32.MessageBoxW(0, "기기를 확인해주세요.", "삭제완료", consts_string.show_flag.foreground.value)
        except :
            ctypes.windll.user32.MessageBoxW(0, "PC와 연결을 확인해주세요.", "연결끊김", consts_string.show_flag.foreground.value)

        # cls.check_install()

    @classmethod
    def reinstall_apk(cls, filepath):
        fileCheck = cls.run_info(filepath)
        # TODO : 버전이 설치된 버전보다 낮을 경우에 대한 처리가 필요함.
        if fileCheck == True:
            ctypes.windll.user32.MessageBoxW \
                (0, "패키지명 : %s \n'확인'을 클릭하시면, 설치를 시작합니다.\n기기에따라 최대 20초가량 소요됩니다." % cls.packageName, "업데이트 설치 시작확인", consts_string.show_flag.foreground.value)
            os.system("adb install -r " + filepath)
            ctypes.windll.user32.MessageBoxW(0, "기기를 확인해주세요.", "작업완료", consts_string.show_flag.foreground.value)
        else:
            ctypes.windll.user32.MessageBoxW(0, "경로나 파일을 확인해주세요", "apk파일확인안됨", consts_string.show_flag.foreground.value)


    @classmethod
    def check_install(cls):
        try:
            test = cmd.check_output("adb shell pm list package -f | findstr " + cls.packageName,
                                    stderr=cmd.STDOUT, shell=True).decode("utf-8").split("=")[1]
            # print(test)
            # print("installed program")
            if test != None :
                ctypes.windll.user32.MessageBoxW \
                    (0, "패키지명 : %s \n설치유무 : 설치됨" % cls.packageName, "설치확인", consts_string.show_flag.foreground.value)
        except:
            # print("Not installed program")
            try:
                ctypes.windll.user32.MessageBoxW \
                    (0, "패키지명 : %s \n설치유무 : 설치안됨" %cls.packageName, "설치확인", consts_string.show_flag.foreground.value)
            except:
                ctypes.windll.user32.MessageBoxW \
                    (0, "선택한 설치파일의 경로 및 파일명을 확인해주세요.\n(영문,숫자만 가능)", "설치확인", consts_string.show_flag.foreground.value)

    @classmethod
    def link2release(cls, *args):
        try :
            if args[0] == "path" :
                cls.run_info(args[1])
            elif args[0] == "packageName" :
                cls.packageName = args[1]

            os.system(
                "adb "
                "shell am start -a android.intent.action.VIEW -d "
                "\"https://play.google.com/store/apps/details?id=\""
                + cls.packageName
            )
        except IndexError:
            ctypes.windll.user32.MessageBoxW(0, "리스트 갱신이 필요합니다.\n리스트갱신버튼을 클릭하세요.", "리스트확인요청", consts_string.show_flag.foreground.value)

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
            ctypes.windll.user32.MessageBoxW(0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", consts_string.show_flag.foreground.value)
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

                ctypes.windll.user32.MessageBoxW(0, "구버전에서 설정할 내용들 설정하세요.", "설정안내", consts_string.show_flag.foreground.value)
                time.sleep(120)
                cls.reinstall_apk(filepath_new)

            except cmd.CalledProcessError :
                ctypes.windll.user32.MessageBoxW(0, "다수의 기기가 연결되어있습니다.", "테스트기기 선택필요", consts_string.show_flag.foreground.value)

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
        userChoice = ctypes.windll.user32.MessageBoxW \
            (0, "[입력하신 명령어] \n"
                "{}\n\n"
                "실행하시겠습니까?".format(command), "명령어 확인", 1|consts_string.show_flag.foreground.value)
        if userChoice == 1:
            if command[0] == "[" : command = command.split("]")[1]
            os.system("start /B start cmd.exe @cmd /k " + command)

    @classmethod
    # staticmethod를 submain01에서 불러다가 쓸려니까 언제 호출되는지 모르겠지만, 응답이 너무 느려서 변경함
    def deleteData(cls, *args):
        if args[0] == "path" :
            cls.run_info(args[1])
        elif args[0] == "packageName" :
            cls.packageName = args[1]

        try:
            os.system("adb shell pm clear " + cls.packageName)
            # test = cmd.check_output("adb shell pm clear " + package_name, stderr=cmd.STDOUT, shell=True)
            ctypes.windll.user32.MessageBoxW(0, cls.packageName + "의 앱데이터가 삭제되었습니다.", cls.packageName, consts_string.show_flag.foreground.value)
        except:
            ctypes.windll.user32.MessageBoxW(0, "패키지명으로 설치된 앱이 확인되지 않습니다.", "패키지명 확인필요", consts_string.show_flag.foreground.value)

    @staticmethod
    def getCurrentActivity(self):
        # "adb shell dumpsys activity | grep -i run"
        test = cmd.check_output("adb shell \"dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'\"",
                                stderr=cmd.STDOUT, shell=True)
        test = test.decode("utf-8")
        ctypes.windll.user32.MessageBoxW(0, test, "현재 화면정보", consts_string.show_flag.foreground.value)

    @staticmethod
    # @accepts(str)
    def getAPKUsingMemmory(self, pakage_name):
        '''
        순간적인 메모리 사용량 확인하는 함수
        :param self:
        :param pakage_name:
        '''
        os.system("start /B start cmd.exe @cmd /k "
                  "adb shell \"dumpsys meminfo {}\"".format(pakage_name))
        # 주석처리된 부분은 QT다이얼로그로 띄우는것. 스페이스간격이 보기 안좋음. 그냥 cmd창 새로 열어서 거기서 보는걸로.
        # string = cmd.check_output("adb shell \"dumpsys meminfo {}\"".format(pakage_name),
        #                         stderr=cmd.STDOUT, shell=True)
        # string = string.decode("utf-8")
        # print(string)
        # from PyQt5 import QtWidgets
        # app = QtWidgets.QApplication([])
        #
        # notifyDialog = QtWidgets.QDialog()
        # notifyDialog.resize(1000, 300)
        # layout = QtWidgets.QVBoxLayout(notifyDialog)
        # scroll = QtWidgets.QScrollArea()
        # scroll.setWidgetResizable(True)
        # layout.addWidget(scroll)
        #
        # scrollContents = QtWidgets.QWidget()
        # layout = QtWidgets.QVBoxLayout(scrollContents)
        # scroll.setWidget(scrollContents)
        #
        # label = QtWidgets.QLabel()
        # label.setText(string)
        #
        # layout.addWidget(label)
        #
        # notifyDialog.show()
        # notifyDialog.raise_()
        # app.exec_()

    @staticmethod
    def getAPKActivityStack(self, pakage_name):
        '''
        :param self:
        :param pakage_name:
        '''

        # '''http://mydevromance.tistory.com/16" 참조'''
        # "adb shell dumpsys activity com.estsoft.alsong"

        os.system("start /B start cmd.exe @cmd /k "
                  "adb shell \"dumpsys activity {}\"".format(pakage_name))

        # adb shell dumpsys activity com.estsoft.alsong > ./Desktop/alsong_activity_data.txt

        # 아래 활성화하면, 다이얼로그로 표시해준다
        # string = cmd.check_output("adb shell \"dumpsys activity {}\"".format(pakage_name),
        #                           stderr=cmd.STDOUT, shell=True)
        # string = string.decode("utf-8")
        # # print(string)
        # from PyQt5 import QtWidgets
        # app = QtWidgets.QApplication([])
        #
        # notifyDialog = QtWidgets.QDialog()
        # notifyDialog.resize(1000, 300)
        # layout = QtWidgets.QVBoxLayout(notifyDialog)
        # scroll = QtWidgets.QScrollArea()
        # scroll.setWidgetResizable(True)
        # layout.addWidget(scroll)
        #
        # scrollContents = QtWidgets.QWidget()
        # layout = QtWidgets.QVBoxLayout(scrollContents)
        # scroll.setWidget(scrollContents)
        #
        # label = QtWidgets.QLabel()
        # label.setText(string)
        #
        # layout.addWidget(label)
        #
        # notifyDialog.show()
        # notifyDialog.raise_()
        # app.exec_()


    @staticmethod
    def goSetLanguagePage(self):
        os.system("adb shell am start -n com.android.settings/.LanguageSettings")

    @staticmethod
    def goSetTimePage(self):
        # 4.4, 7.0 기기에서는 아래커맨드 안된다
        # os.system("adb shell am start -n com.android.settings/.DateTimeSettingsSetupWizard")
        # os.system("adb shell am start -n com.android.settings/.Settings\$DateTimeSettings")
        # os.system("adb shell am start -n com.android.settings/.DateTimeSettings")
        os.system("adb shell am start -n com.android.settings/.Settings\$DateTimeSettingsActivity")
        pass

    @staticmethod
    def goPowerUsageSummaryPage(self):
        # am start -S com.android.settings/.Settings\$PowerUsageSummaryActivity
        # am start -a android.intent.action.POWER_USAGE_SUMMARY
        os.system("adb shell am start -n com.android.settings/.Settings\$PowerUsageSummaryActivity")

    @staticmethod
    def goDevelopPage(self):
        os.system("adb shell am start -S com.android.settings/.Settings\$DevelopmentSettingsActivity")

    @classmethod
    def makedir(cls):
        cls.today = datetime.datetime.now().strftime("%y%m%d")
        check_folder = os.path.exists(cls.today)
        if check_folder == False:
            try :
                cmd.call("mkdir " + cls.today, stderr=None, shell=True)
                # cmd.call("mkdir " + cls.today, stderr=None, shell=False) # except Test
                ctypes.windll.user32.MessageBoxW(0, "[폴더생성 완료]\n폴더명 : " + cls.today, "스크린샷 저장폴더생성", consts_string.show_flag.foreground.value)
            except :
                ctypes.windll.user32.MessageBoxW(0, "폴더생성 불가한 위치에서 프로그램이 실행되었습니다.", "실행파일 경로확인요청", consts_string.show_flag.foreground.value)
                return -1
        else:
            ctypes.windll.user32.MessageBoxW(0, "[스크린샷 저장경로]\n폴더명 : "+ cls.today, "스크린샷 저장경로안내", consts_string.show_flag.foreground.value)

    @classmethod
    def check_time(cls):
        cls.currentTime = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        # print(cls.currentTime)

    @classmethod
    def device_info(cls, select_device): #TODO : 여려기기 연결되어있을때에, 기기를 선택해서 기기별 리스트에 정보저장필요
        '''
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = p.stdout.read()
        retcode = p.wait()
        :param select_device:
        :return:
        '''
        select_device = ""  # TODO : delete this line
        os_ver = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.release",
                                  stderr=cmd.STDOUT, shell=True).decode("utf-8")
        api_level = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.sdk",
                                     stderr=cmd.STDOUT, shell=True).decode("utf-8")
        model = cmd.check_output("adb shell " + select_device + "getprop ro.product.model",
                                 stderr=cmd.STDOUT, shell=True).decode("utf-8")

        cls.deviceData = r"{}_{}_API_{}".format(model, os_ver, api_level)
        cls.deviceData = re.sub('\s','',cls.deviceData) #white space 제거

    @classmethod
    def open_capture_folder(cls):
        chkValue = cls.makedir()
        if chkValue == -1 :
            return None
        cls.check_time()
        # os.system("start " + cls.today)
        # paths = os.getcwd() + "\\" + cls.today
        paths = os.getcwd()
        print(paths)
        cls.show_file_view(None, paths)

    @classmethod
    def capture2image(cls):#TODO : 기기 잠금화면 상태유무 확인후, 잠금해제 메소드 추가 필요
        ConnectedDevicesCnt = cls.check_connect()
        if ConnectedDevicesCnt > 0 :
            cls.makedir()
            # win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + filePath)
            os.system("adb shell rm -r /mnt/sdcard/ScreenCapture")
            # win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + "adb shell rm -r /mnt/sdcard/ScreenCapture")
            os.system("adb shell mkdir /mnt/sdcard/ScreenCapture")

            os.system("adb shell screencap /mnt/sdcard/ScreenCapture/test.png")

            os.system("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png")

            #TODO : textMovingRatio 를 구분해서, 이를 window에 출력하기. -> 중간에 UI그리는 함수로 점프.??
            # movePNG = cmd.Popen("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png",
            #                  stdout=cmd.PIPE, stderr=cmd.STDOUT)
            # textMovingRatio = movePNG.stdout.read().decode("utf-8").split("\r\n")
            # for Cnt in range(len(textMovingRatio)):
            #     print(textMovingRatio[Cnt])

            os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
            cls.check_time()
            time.sleep(1)
            cls.device_info(None)
            changedName = cls.currentTime + "_" + cls.deviceData+".jpg"
            org_image = os.getcwd() + "\\test.png"
            new_image = os.getcwd() + "\\"+ changedName
            cls.capture_down_size(org_image, new_image, 30, 85)
            time.sleep(1)
            os.system("move " + changedName + " " +cls.today)
            os.system("start " + cls.today)
        else :
            ctypes.windll.user32.MessageBoxW \
                (0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", consts_string.show_flag.foreground.value)
            # return  -1

    @classmethod
    def capture_down_size(cls, orgfile, newfile, size_per, jpeg_quaility_per):
        img = Image.open(orgfile)
        downPer = size_per / 100
        resize = (int(img.width * downPer), int(img.height * downPer))
        img = img.resize(resize)
        img.save(newfile, 'jpeg', quality=jpeg_quaility_per)

    @classmethod
    def capture2viedo(cls): # 함수 호출시 try...except pass로 묶을것. 최대 정확히 3분까지만 녹화됨
        ConnectedDevicesCnt = cls.check_connect()
        if ConnectedDevicesCnt > 0 :
            cls.makedir()
            cls.device_info(None)
            # print(ConnectedDevicesCnt)
            # print(cls.deviceData)
            ctypes.windll.user32.MessageBoxW \
                (0, "현재 %i대의 기기가 PC에 연결되어있습니다.\n\n[연결된기기]\n%s" %(ConnectedDevicesCnt, cls.deviceData), "연결된 기기", consts_string.show_flag.foreground.value)
        else :
            ctypes.windll.user32.MessageBoxW \
                (0, "USB연결 및 드라이버설치 \n\n또는 개발자모드활성화를 확인하세요.", "연결된 기기없음", consts_string.show_flag.foreground.value)
            return -1
        # TODO : API 19 이상일때에만 영상녹화하고, 메시지다이얼로그의 '녹화끝','취소'리턴받으면 녹화중지시키고 영상뺴오기
        device_api = cls.deviceData.split("_")[3]
        device_api = device_api.split("I")[0].replace("\r","")
        videoEnableOSver = 19
        # print("연결된 기기의 OS API은 " + device_api)
        if float(device_api) < videoEnableOSver :
            ctypes.windll.user32.MessageBoxW(0, "선택된 기기에서는 녹화가 되지 않습니다.", "녹화지원안됨", consts_string.show_flag.foreground.value)
        else:
            try:
                cmd.check_output("adb shell rm -r /mnt/sdcard/ADB_record", stderr=cmd.STDOUT, shell=True)
                logger.info("Delete Existing Folder : /mnt/sdcard/ADB_record")
            except:
                logger.info("No folder to delete")
            try :
                cmd.check_output("adb shell mkdir /mnt/sdcard/ADB_record", stderr=cmd.STDOUT, shell=True)
                logger.info("Complete Making Folder : /mnt/sdcard/ADB_record")
            except :
                logger.warning("Failed make folder") #TODO : 여기로 들어오면, 녹화가 안되느것.
            # New window cmd : start cmd/k command

            win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' +
                      "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4")
            logger.info("Record Start")
            # os.system("start /B start cmd.exe @cmd /k "
            #           "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4")

            # win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + "adb shell rm -r /mnt/sdcard/ScreenCapture")
            # os.system("start /B start powershell.exe @powershell /k "
            #           "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4")

            path = os.getcwd().replace("\\","/").replace("\r","").replace("\n","")
            time.sleep(1)
            RecordCnt = ctypes.windll.user32.MessageBoxW \
                (0, "영상기록을 시작합니다.\n확인 : 영상기록 PC전송\n취소 : 영상기록삭제", "영상기록중", 1|consts_string.show_flag.foreground.value)
            if RecordCnt == 1: # 확인 : 기기 -> PC 로 영상전송
                # TODO : 확인이나, 취소 누르기전에 연결끊어졌는지 확인할것 -> 이경우, 강제종료됨.
                os.system("TASKKILL /F /IM cmd.exe /T")
                # powershell 기반으로 main.exe가 실행되면 괜찮음?? win7 x86 sp1 ent / win10 x64 ent 에서 g5 7.0으로 확인
                # os.system("TASKKILL /F /FI "
                #           "\"WINDOWTITLE eq C:\WINDOWS\system32\cmd.exe - "
                #           "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4\" /T")
                time.sleep(1)
                cmd.check_output("adb pull /mnt/sdcard/ADB_record/test.mp4 %s/test.mp4" % path, stderr=cmd.STDOUT, shell=True)
                cmd.check_output("adb shell rm /mnt/sdcard/ADB_record/test.mp4", stderr=cmd.STDOUT, shell=True)

                cls.check_time()
                changedName = cls.currentTime + "_" + cls.deviceData + ".mp4"
                os.system("cd %s" % path)
                # print(changedName)
                try :
                    os.system("ren test.mp4 " + changedName)
                except :
                    os.renames("test.mp4", changedName)
                # TODO : 넥서스 6P 8.0 에서 changedName 확인할것. test.mp4를 가져오긴 하는데, 이름변경이 안되고 test.mp4로 머물러있음.
                # 171016_175316_Nexus 6P_8.0.0_API_26.mp4 으로 정상적으로 찍힘.
                os.system("move " + changedName + " " + cls.today)
                os.system("start " + cls.today)

                movie2gif_confirm = ctypes.windll.user32.MessageBoxW \
                    (0, " 녹화된 영상을 업로드가능한 \n gif파일로 변환하시겠습니까?", " 영상파일변환 확인",
                     1 | consts_string.show_flag.foreground.value)
                if movie2gif_confirm == 1:  # 확인 : call mp4_downsize_gif().
                    print("변환시작\n")
                    print(cls.today) # 171012
                    os.chdir(cls.today)
                    # print(os.getcwd()) # C:\Users\Jeongkuk\PycharmProjects\androidADB\src
                    # org_path = os.getcwd() + "\\{}".format(cls.today)
                    # print(org_path) # C:\Users\Jeongkuk\PycharmProjects\androidADB\src\171012
                    print(changedName) # 171012_095106_LG-F700K_7.0_API_24.mp4
                    cls.mp4_downsize_gif(changedName)
                else:
                    print("변환안함\n")

            else : # 취소 : 기기에서 삭제
                os.system("TASKKILL /F /IM cmd.exe /T")
                cmd.check_output("adb shell rm /mnt/sdcard/ADB_record/test.mp4", stderr=cmd.STDOUT, shell=True)

    @classmethod
    def mp4_downsize_gif(cls, org_filename):
        print("hello")
        org_file = org_filename
        clip = VideoFileClip(org_file) 
        org_size = clip.aspect_ratio

        #TODO: 연결기기의 해상도정보가져와서, 그 비율대로 절반크기로 줄이기 
        ch_height = 320
        ch_width = 240

        tmp_height = ch_height * org_size
        tmp_height = int(tmp_height)

        new_filename = org_filename.replace("mp4","gif")
        new_file = new_filename

        # print(tmp_height)
        # os.system("ffmpeg -i movie_360p.mp4 -pix_fmt rgb24 -r 10 -s {}x240 movie_360p_320_tmp.gif".format(tmp_height)) #OK> ffmpeg 폴더를 path에 추가.
        os.system("ffmpeg -i {} -pix_fmt rgb24 -r 10 -s {}x{} {}".format(org_file, tmp_height, ch_width,new_file))
        print("변환완료")

    @classmethod
    def ConnectedDevices(cls):
        pass

    def SelectSetupFile(self):
        '''
        TODO: return으로 선택했던 apk경로, apk이름을 리턴할것. ( 이전에 설치했던 목록화면 표시위해 )
        :param self:
        :return:
        '''
        from PyQt5 import QtWidgets
        self.fileDialog = QtWidgets.QFileDialog()
        select = self.fileDialog.getOpenFileUrl(filter='*.apk')
        # select = self.fileDialog.selectedUrls(filter='*.apk')
        # print(select)
        # (PyQt5.QtCore.QUrl(''), '')
        # (PyQt5.QtCore.QUrl('file:///C:/Users/Jeongkuk/PycharmProjects/androidADB/apks/alsong_1.5.0.0_1cha.apk'), '*.apk')
        path = str(select[0])
        if path == "PyQt5.QtCore.QUrl('')" :
            path = ""
        else :
            path = str(select[0]).replace("PyQt5.QtCore.QUrl('file:///", "")
            path = path.replace("')", "")
            # pass
        # self.lineEdit.setText(path)
        # print(path)

        path = self.regular_path(None, path)

        return  path

    @staticmethod
    def regular_path(self, path):
        # pattern_korean = r"^[가-힣]*$"
        # pattern_network = r"([0-9]{1,3}) \. ([0-9]{1,3}) \. ([0-9]{1,3}) \. ([0-9]{1,3})"
        # prttern_space =  r"[\s]+"
        # hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자
        hangul = r'[ ㄱ-ㅣ가-힣]+'
        network = r"([0-9]{1,3}) \. ([0-9]{1,3}) \. ([0-9]{1,3}) \. ([0-9]{1,3})"
        '''
        한글 코드 범위
        ㄱ ~ ㅎ: 0x3131 ~ 0x314e
        ㅏ ~ ㅣ: 0x314f ~ 0x3163
        가 ~ 힣: 0xac00 ~ 0xd7a3
        출처: http://jokergt.tistory.com/52 [Gun's Knowledge Base]
        '''
        # s = ' 韓子는 싫고, 한글은 nice하다. English 쵝오 -_-ㅋㅑㅋㅑ ./?! '
        # result = hangul.findall(s)
        # print(result)
        result = re.findall(network, path)
        if not result == [] :
            path = "네트워크경로의 파일을 PC로 복사해주세요."
            return path

        result = re.findall(hangul, path)
        if not result == [] :
            path = "한글이나 띄어쓰기가, 경로 및 파일명에 포함됨"
            return path

        return path


    @staticmethod
    def list_ins_program(self):
        # adb shell pm list package
        try :
            string = cmd.check_output("adb shell pm list package", stderr=cmd.STDOUT, shell=True)
            string = string.decode("utf-8")
            string = string.replace("package:", "")
            Installed_app_List = string.split("\r\n")
            test_list = []
            for Cnt in range(len(Installed_app_List)):
                if "estsoft" in Installed_app_List[Cnt]:
                    test_list.append(Installed_app_List[Cnt])
                else:
                    pass
            # 설치된 패키지들 바로 확인하고 싶을때에만 사용
            # print(string) # 설치된 모든 패키지들이 하나의 스트링인 상태
            # from PyQt5 import QtWidgets
            # app = QtWidgets.QApplication([])
            #
            # notifyDialog = QtWidgets.QDialog()
            # notifyDialog.resize(1000, 300)
            # layout = QtWidgets.QVBoxLayout(notifyDialog)
            # scroll = QtWidgets.QScrollArea()
            # scroll.setWidgetResizable(True)
            # layout.addWidget(scroll)
            #
            # scrollContents = QtWidgets.QWidget()
            # layout = QtWidgets.QVBoxLayout(scrollContents)
            # scroll.setWidget(scrollContents)
            #
            # label = QtWidgets.QLabel()
            # label.setText(string)
            #
            # layout.addWidget(label)
            #
            # notifyDialog.show()
            # notifyDialog.raise_()
            # app.exec_()

            # print(Installed_app_List) # 설치된 모든 패키지 리스트
            # print(test_list)

            return test_list
        except :
            return -1

    @classmethod
    def getVersion(cls, *args):
        '''
        adb shell dumpsys package my.package | grep versionName
        >> adb shell dumpsys package my.package | findstr "versionName"
        :param args[0] = packageName_selected
        :param args[1] = packageName_compared

        arg[0]
        > submain01 : 설치된 apk의 버전을 확인
        > submain02 : 설치된 apk의 버전을 확인

        arg[1]
        > submain01 : 설치할(선택된) apk의 버전을 확인

        :return:
        '''
        if (args[0] != "") & (args[0].split(".")[0] == "com"):
            try :
                dumpsys_result = cmd.check_output("adb shell dumpsys package {}".format(args[0])
                                                  , stderr=cmd.STDOUT, shell=True).decode("utf-8").split("\r\n")
                for data in dumpsys_result:
                    if "versionName" in data :
                        version = data
                        version = version.split("=")[1]
                    if "Unable" in data :
                        version = "Not installed"

                if os.path.isfile(args[1]):
                    dumpsys_result = cmd.check_output("aapt d badging {}".format(args[1])
                                                      , stderr=cmd.STDOUT, shell=True).decode("utf-8").split("\r\n")
                    for data in dumpsys_result:
                        if "pack" in data :
                            CmpVersion = data
                            CmpVersion = CmpVersion.split(" ")[3].split("'")[1].split("'")[0]
                    return version, CmpVersion

                return version
            except :
                ctypes.windll.user32.MessageBoxW(0, "리스트갱신버튼을 클릭해주세요.", "확인요청", consts_string.show_flag.foreground.value)
                return None
        elif (args[0] != "") & os.path.isfile(args[0]):
            dumpsys_result = cmd.check_output("aapt d badging {}".format(args[0])
                                              , stderr=cmd.STDOUT, shell=True).decode("utf-8").split("\r\n")
            for data in dumpsys_result:
                if "pack" in data:
                    version = data
                    version = version.split(" ")[3].split("'")[1].split("'")[0]
            return version
        else:
            ctypes.windll.user32.MessageBoxW(0, "패키지가 선택되지 않았습니다.", "도움말", consts_string.show_flag.foreground.value)

        # return args[0], args[1] # ok.
        # return type(args[0]), type(args[1]) # str

    @staticmethod
    def show_help_subform01(self):
        help_text = \
            "def controlDevice(self, command):\n" \
            "   os.system(\"adb \" + command)\n" \
            "출처 : http://www.dreamy.pe.kr/zbxe/CodeClip/163972 \n" \
            "[Usage]\n" \
            "1. https://developer.android.com/studio/run/oem-usb.html?hl=ko 에서 기기별드라이버설치"

        ctypes.windll.user32.MessageBoxW(0, help_text, "도움말", consts_string.show_flag.foreground.value)

    @staticmethod
    def show_help_subform02(self):
         help_text = \
             "[앱삭제/데이터삭제/출시버전]\n" \
             "> 리스트에서, 앱 패키지명을 선택후, 버튼을 클릭하세요.\n\n" \
             "[리스트갱신]\n" \
             "> 앱삭제 이후, 갱신버튼을 누르면 삭제유무확인가능합니다.\n\n" \
             "[참고사항]\n" \
             "> 목록이 없을땐, '리스트갱신'버튼을 클릭하세요.\n" \
             "> 출시버전 버튼은 해당 패키지명으로 구글플레이스토어에서 \n" \
             "  검색한 결과를 보여줍니다."

         ctypes.windll.user32.MessageBoxW(0, help_text, "도움말", consts_string.show_flag.foreground.value)

        # http://pythoncentral.io/pyside-pyqt-tutorial-the-qlistwidget/
        # https://stackoverflow.com/questions/31380457/add-right-click-functionality-to-listwidget-in-pyqt4

    @staticmethod
    def show_file_view(self, path):
        from PyQt5.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QApplication
        from PyQt5 import QtCore
        class MyWindow(QWidget):
            def __init__(self, path, parent=None):
                super(MyWindow, self).__init__(parent)
                self.pathRoot = path
                self.model = QFileSystemModel(self)
                self.model.setRootPath(self.pathRoot)
                self.indexRoot = self.model.index(self.model.rootPath())
                self.treeView = QTreeView(self)
                self.treeView.setModel(self.model)
                self.treeView.setRootIndex(self.indexRoot)
                self.treeView.clicked.connect(self.on_treeView_clicked)
                self.layout = QVBoxLayout(self)
                self.layout.addWidget(self.treeView)

            @QtCore.pyqtSlot(QtCore.QModelIndex)
            def on_treeView_clicked(self, index):
                indexItem = self.model.index(index.row(), 0, index.parent())
                filePath = self.model.filePath(indexItem)
                # os.system(filePath) # main UI 응답없음됨
                win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + filePath)

        print(path)
        app = QApplication([])
        app.setApplicationName('FileView')
        # "C:/Users/Jeongkuk/PycharmProjects/androidADB/"
        # print("hello")
        main = MyWindow(path)
        main.resize(666, 333)
        main.move(app.desktop().screen().rect().center() - main.rect().center())
        main.show()
        app.exec_()

if __name__ == "__main__":
    from PyQt5 import QtWidgets
    # '''
    filepath = "alsong_4.0.7.3.apk"
    # print(os.path.isfile(filepath))
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

    # filepath = "Picnic-0.0.0.0-debug.apk"
    # filepath = "picnic-0.0.0.0-release.apk"
    # filepath = "picnic-0.0.0.1-release.apk"
    # filepath = "app-debug.apk"
    # filepath = ""
    # filepath2 = "C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\apks\\" + "Picnic-test-release-v0.0.0.5-1.apk"
    # print(os.path.isfile(filepath))
    test = defaultADB()

    # print(test.getVersion(filepath,filepath2))
    # test.run_info(filepath)
    # test.uninstall_apk(filepath)
    # test.adb_kill()
    # os.system("timeout 5")
    # test.install_apk(filepath2,"")
    # test.run_apk(filepath)
    # test.reinstall_apk(filepath)
    # test.check_install()
    # test.uninstall_apk(filepath)
    # test.check_connect()
    # print(test.check_connect())
    # test.update(None,None)
    # filepath_new = "teamUP-teamup_store-release.apk"
    # filepath_old = "teamUP-teamup_store-release-v3.6.0.0-132.apk"
    # test.update(filepath_old,filepath_new)
    # test.show_help_subform01(None)
    # test.list_ins_program(None)
    # test.goDevelopPage(None)
    # test.regular_path(None,None)


    # TODO : 프로파일링
    # import cProfile
    # cProfile.run('test.show_help_subform02(None)')
    # import doctest
    # doctest.testmod()


    # 데이터 삭제
    # test.deleteData(None, "com.estsoft.alzip")
    # test.deleteData(None, "com.estsoft.picnic")

    # 언어 변경 화면으로 이동
    # test.controlDevice(None, "adb shell am start -n com.android.settings/.LanguageSettings")
    # test.goSetLanguagePage(None)

    # 재부팅
    # os.system("adb reboot")

    # 현재화면 구하기
    # test.getCurrentActivity(None)

    # 패키지 버전 확인
    # packageName = "com.estsoft.picnic"
    # test.getAPKVersion(None,packageName) #TODO : 처음연결시에, 반환되는 문자열이 연결정보임. 이거 필터링필요.

    # TODO : 패키지의 activity 호출 스택 확인
    # packageName = "com.estsoft.picnic.test"
    # packageName = "com.estsoft.alsong"
    # test.getAPKActivityStack(None,packageName)


    # TODO : 메모리상태 확인packageName
    # packageName = "com.estsoft.alsong"
    # # packageName = 4
    # test.getAPKUsingMemmory(None,packageName)

    #TODO : 타켓/최소 sdk버전 확인
    # apkFileName = "C:\\Users\Jeongkuk\Desktop\Plain-test-release-v1.0.0.1-1.apk"
    # # os.system("aapt list -a {} | findstr \"SdkVersion\"".format(apkFileName)) #minSdkVersion, targetSdkVersion
    # os.system("aapt list -a {} | findstr \"minSdkVersion\"".format(apkFileName))
    # os.system("adb shell getprop ro.build.version.sdk")
    # api_level = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.sdk",
    #                              stderr=cmd.STDOUT, shell=True).decode("utf-8")\
    apkFileName = "C:\\Users\Jeongkuk\Desktop\Plain-test-release-v1.0.0.1-1.apk"
    ApkAPI = cmd.check_output("aapt list -a {} | findstr \"minSdkVersion\"".format(apkFileName), stderr=cmd.STDOUT, shell=True).decode("utf-8")
    DeviceAPI = cmd.check_output("adb shell getprop ro.build.version.sdk", stderr=cmd.STDOUT, shell=True).decode("utf-8")
    ApkAPI = re.sub('\s', '', ApkAPI)[-4:]
    DeviceAPI = re.sub('\s', '', DeviceAPI)

    print("[APK] : {}".format(ApkAPI))
    print("[Devices] : {}".format(DeviceAPI))


    '''
    aapt list -a .\4.0.16.1.apk | findstr "SdkVersion"
    A: android:minSdkVersion(0x0101020c)=(type 0x10)0xe
    A: android:targetSdkVersion(0x01010270)=(type 0x10)0x19
    '''
    '''
    https://developer.xamarin.com/guides/android/application_fundamentals/understanding_android_api_levels/
    '''

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

    # test.show_file_view(None, "C:\\Users\Jeongkuk\PycharmProjects\\androidADB\src")
