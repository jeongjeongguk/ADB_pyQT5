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
            return -1

    @classmethod
    def install_apk(cls, filepath): # def install_apk(self, filepath, option): # option : r, b, ...
        cls.run_info(filepath)

        cls.uninstall_apk("path",filepath)
        # if os.getcwd() != cls.company: os.chdir(cls.company)
        # TODO : error: more than one device/emulator 예외처리필요
        os.system("adb install -r " + filepath) #TODO: 인스톨 여기에요~~~~~~~~~~~~~~~~~~~~~~

        #print(filepath)
        time.sleep(10)
        cls.run_apk(filepath)
        #TODO : adb: error: failed to copy 'teamUP-store-release-v3.5.2.7-122.apk' to '/data/local/tmp/teamUP-store-release-v3.5.2.7-122.apk': no response: Connection reset by peer
        #TODO : 위 내용관련한 처리필요

    @classmethod
    def run_info(cls, filepath):
        cls.filepath = filepath
        # if os.getcwd() != cls.company: os.chdir(cls.company)
        test = cmd.check_output("aapt dump badging " + filepath + " | findstr package",
                                stderr=cmd.STDOUT, shell=True)
        cls.packageName = test.decode("utf-8").split(" ")[1].split("'")[1]
        try:
            test = cmd.check_output("aapt dump badging " + filepath + " | findstr launchable",
                                    stderr=cmd.STDOUT, shell=True)
            cls.startActivity = test.decode("utf-8").split(" ")[1].split("'")[1]
            return cls.packageName, cls.startActivity
        except:
            # TODO:launchable activity가 구해지지 않는 경우 존재. : 추가처리 필요.
            # ?????? 언제 안구해지지? 런쳐액티버티 가렸을때 못찾음 -> 파싱으로 찾기
            pass

    @classmethod
    def run_apk(cls,filepath):
        cls.run_info(filepath)
        os.system("adb shell am start -n " + cls.packageName +"/"+cls.startActivity)

    @classmethod
    def uninstall_apk(cls, *args):
        if args[0] == "path" :
            cls.run_info(args[1])
        elif args[0] == "packageName" :
            cls.packageName = args[1]
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
    def link2release(cls, *args):
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
        os.system("adb " + command)

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
            ctypes.windll.user32.MessageBoxW(0, cls.packageName + "의 앱데이터가 삭제되었습니다.", cls.packageName, 0)
        except:
            ctypes.windll.user32.MessageBoxW(0, "패키지명으로 설치된 앱이 확인되지 않습니다.", "패키지명 확인필요", 0)

    @staticmethod
    def getCurrentActivity(self):
        # "adb shell dumpsys activity | grep -i run"
        test = cmd.check_output("adb shell \"dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'\"",
                                stderr=cmd.STDOUT, shell=True)
        test = test.decode("utf-8")
        ctypes.windll.user32.MessageBoxW(0, test, "현재 화면정보", 0)


    @staticmethod
    def getAPKVersion(self, pakage_name):
        '''
        This function is to get selected package's version.
        :param self:
        :param pakage_name:
        '''
        test = cmd.check_output("adb shell \"dumpsys package {} | grep 'versionName'\"".format(pakage_name),
                                stderr=cmd.STDOUT, shell=True)
        test = test.decode("utf-8")
        ctypes.windll.user32.MessageBoxW(0, "버전 : {}".format(test), pakage_name, 0)

    @staticmethod
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
        # os.system("start /B start cmd.exe @cmd /k "
        # "adb shell \"dumpsys activity {}\"".format(pakage_name))
        string = cmd.check_output("adb shell \"dumpsys activity {}\"".format(pakage_name),
                                  stderr=cmd.STDOUT, shell=True)
        string = string.decode("utf-8")
        print(string)
        from PyQt5 import QtWidgets
        app = QtWidgets.QApplication([])

        notifyDialog = QtWidgets.QDialog()
        notifyDialog.resize(1000, 300)
        layout = QtWidgets.QVBoxLayout(notifyDialog)
        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)

        scrollContents = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(scrollContents)
        scroll.setWidget(scrollContents)

        label = QtWidgets.QLabel()
        label.setText(string)

        layout.addWidget(label)

        notifyDialog.show()
        notifyDialog.raise_()
        app.exec_()


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
        '''
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = p.stdout.read()
        retcode = p.wait()
        :param select_device:
        :return:
        '''
        select_device = ""  # TODO : delete this line
        os_ver = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.release",
                                  stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        api_level = cmd.check_output("adb shell " + select_device + "getprop ro.build.version.sdk",
                                     stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        model = cmd.check_output("adb shell " + select_device + "getprop ro.product.model",
                                 stderr=cmd.STDOUT, shell=True).decode("utf-8").replace("\r\n", "")
        cls.deviceData = model + "_" + os_ver + "_API_" + api_level

        # print(cls.deviceData)

    @classmethod
    def open_capture_folder(cls):
        cls.makedir()
        cls.check_time()
        os.system("start " + cls.today)

    @classmethod
    def capture2image(cls):#TODO : 기기 잠금화면 상태유무 확인후, 잠금해제 메소드 추가 필요
        cls.makedir()
        ConnectedDevicesCnt = cls.check_connect()
        if ConnectedDevicesCnt != 0 :
            os.system("adb shell rm -r /mnt/sdcard/ScreenCapture")
            os.system("adb shell mkdir /mnt/sdcard/ScreenCapture")

            os.system("adb shell screencap /mnt/sdcard/ScreenCapture/test.png")

            # os.system("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png")
            #TODO : textMovingRatio 를 구분해서, 이를 window에 출력하기. -> 중간에 UI그리는 함수로 점프.??
            movePNG = cmd.Popen("adb pull /mnt/sdcard/ScreenCapture/test.png ./test.png",
                             stdout=cmd.PIPE, stderr=cmd.STDOUT)
            textMovingRatio = movePNG.stdout.read().decode("utf-8").split("\r\n")
            for Cnt in range(len(textMovingRatio)):
                print(textMovingRatio[Cnt])

            os.system("adb shell rm /mnt/sdcard/ScreenCapture/test.png")
            cls.check_time()
            time.sleep(1)
            cls.device_info(None)
            changedName = cls.currentTime + "_" + cls.deviceData+".jpg"
            os.system("ren test.png "+ changedName)
            time.sleep(1)
            os.system("move " + changedName + " " +cls.today) # 이거 안됨????
            os.system("start " + cls.today)
        else :
            ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", 0)
            # return  -1

    @classmethod
    def capture2viedo(cls): # 함수 호출시 try...except pass로 묶을것. 최대 정확히 3분까지만 녹화됨
        cls.makedir()
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
            return -1
        # TODO : API 19 이상일때에만 영상녹화하고, 메시지다이얼로그의 '녹화끝','취소'리턴받으면 녹화중지시키고 영상뺴오기
        device_api = cls.deviceData.split("_")[3]
        device_api = device_api.split("I")[0].replace("\r","")
        videoEnableOSver = 19
        # print("연결된 기기의 OS API은 " + device_api)
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

            # os.system("start /B start powershell.exe @powershell /k "
            #           "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4")

            path = os.getcwd().replace("\\","/").replace("\r","").replace("\n","")
            time.sleep(1)
            RecordCnt = ctypes.windll.user32.MessageBoxW \
                (0, "영상기록을 시작합니다.\n확인 : 영상기록 PC전송\n취소 : 영상기록삭제", "영상기록중", 1)
            if RecordCnt == 1: # 확인 : 기기 -> PC 로 영상전송
                os.system("TASKKILL /F /IM cmd.exe /T")
                # powershell 기반으로 main.exe가 실행되면 괜찮음?? win7 x86 sp1 ent / win10 x64 ent 에서 g5 7.0으로 확인
                # os.system("TASKKILL /F /FI "
                #           "\"WINDOWTITLE eq C:\WINDOWS\system32\cmd.exe - "
                #           "adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4\" /T")
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
        os.system("start " + cls.today)

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
        print(select)
        # (PyQt5.QtCore.QUrl(''), '')
        # (PyQt5.QtCore.QUrl('file:///C:/Users/Jeongkuk/PycharmProjects/androidADB/apks/alsong_1.5.0.0_1cha.apk'), '*.apk')
        path = str(select[0])
        if path == "PyQt5.QtCore.QUrl('')" :
            path = ""
        else :
            path = str(select[0]).replace("PyQt5.QtCore.QUrl('file:///", "")
            path = path.replace("')", "")
        # self.lineEdit.setText(path)
        # print(path)
        return  path

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
        :param args:
        :return:
        '''

    @staticmethod
    def show_help_subform01(self):
        help_text = \
            "def controlDevice(self, command):\n" \
            "   os.system(\"adb \" + command)\n" \
            "출처 : http://www.dreamy.pe.kr/zbxe/CodeClip/163972 \n" \
            "[Usage]\n" \
            "1. https://developer.android.com/studio/run/oem-usb.html?hl=ko 에서 기기별드라이버설치"

        ctypes.windll.user32.MessageBoxW(0, help_text, "도움말", 0)

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

         ctypes.windll.user32.MessageBoxW(0, help_text, "도움말", 0)

        # http://pythoncentral.io/pyside-pyqt-tutorial-the-qlistwidget/
        # https://stackoverflow.com/questions/31380457/add-right-click-functionality-to-listwidget-in-pyqt4

if __name__ == "__main__":
    from PyQt5 import QtWidgets
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

    # filepath = "Picnic-0.0.0.0-debug.apk"
    # filepath = "picnic-0.0.0.0-release.apk"
    # filepath = "picnic-0.0.0.1-release.apk"
    filepath = "app-debug.apk"
    #
    test = default()
    # test.run_info(filepath)
    # test.uninstall_apk(filepath)
    # test.adb_kill()
    # os.system("timeout 5")
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
    # test.show_help_subform01(None)
    # test.list_ins_program(None)
    # test.goDevelopPage(None)

    # TODO : 데이터 삭제
    # test.deleteData(None, "com.estsoft.alzip")
    # test.deleteData(None, "com.estsoft.picnic")

    # TODO : 언어 변경 화면으로 이동
    # test.controlDevice(None, "adb shell am start -n com.android.settings/.LanguageSettings")
    # test.goSetLanguagePage(None)

    # TODO : 재부팅
    # os.system("adb reboot")

    #TODO : 현재화면 구하기
    # test.getCurrentActivity(None)

    #TODO : 패키지 버전 확인
    # packageName = "com.estsoft.picnic"
    # test.getAPKVersion(None,packageName) #TODO : 처음연결시에, 반환되는 문자열이 연결정보임. 이거 필터링필요.

    #TODO : 패키지의 activity 호출 스택 확인
    # packageName = "com.android.settings"
    # test.getAPKActivityStack(None,packageName)


    #TODO : 메모리상태 확인packageName
    # packageName = "com.estsoft.alsong"
    # test.getAPKUsingMemmory(None, packageName)

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
    test.capture2image()
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
