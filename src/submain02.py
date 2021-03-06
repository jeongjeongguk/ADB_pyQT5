import sys, ctypes, os
currentPaths = os.getcwd()
currentPathsSet = currentPaths.replace("src","ui_py")
sys.path.insert(0, currentPathsSet)
import installedList_ui
import adb_default
from PyQt5 import QtWidgets
import consts_string
import subprocess as cmd

class SubWindow02(QtWidgets.QMainWindow, installedList_ui.Ui_Form, adb_default.defaultADB):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect()
        self.listup()

    def connect(self):
        #TODO : 연결이 중간에 끊어진 상황과, 해당 패키지명이 설치되지 않은상황 처리필요
        '''
        : button과 기능함수을 연결해주는 함수
        '''
        # 앱 삭제, listWidget.selectedItems()의 반환값은 선택된 항목들 리스트.
        self.pushButton.clicked.connect(
            lambda :
            self.uninstall_apk("packageName", self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )

        # 데이터 삭제
        self.pushButton_2.clicked.connect(
            # lambda : self.deleteData("packageName", self.listWidget.selectedItems()[0].text()) # it's ok. old_ver.
            lambda :
            self.deleteData("packageName", self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
            # lambda : print(self.listWidget.selectedItems()) # it returns []
        )

        # 출시버전
        self.pushButton_3.clicked.connect(
            lambda :
            self.link2release("packageName", self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )
        '''
       Traceback (most recent call last):
          File "C:/Users/Jeongkuk/PycharmProjects/androidADB/submain02.py", line 29, in <lambda>
        lambda : self.link2release("packageName", self.listWidget.selectedItems()[0].text())
            IndexError: list index out of range
 
        '''
        # 리스트 갱신
        self.pushButton_4.clicked.connect(self.listup)
        # 도움말
        self.pushButton_5.clicked.connect(lambda : self.show_help_subform02(None))

        self.pushButton_6.clicked.connect(
            lambda:
            ctypes.windll.user32.MessageBoxW(0,
                                             "선택된 앱 : {}\n확인된 버전 : {}"
                                             .format(self.listWidget.selectedItems()[0].text(),self.getVersion(self.listWidget.selectedItems()[0].text(), ""))
                                             , "버전확인", consts_string.show_flag.foreground.value)

            # print(self.getVersion(self.listWidget.selectedItems()[0].text(), ""))
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )

        # Monkey Test
        self.MonkeyTest.clicked.connect(
            lambda:
            # print(self.listWidget.selectedItems()[0].text())
            self.controlDevice(None, "adb shell monkey -p {} -v --throttle 100 1200".format(self.listWidget.selectedItems()[0].text()))
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )

        # DeveloperPage
        self.DeveloperPage.clicked.connect(
            lambda:
            self.goDevelopPage(None)
        )

        # StartApp
        # 패키지를 PC로 가지고와서, aapt로 시작화면 구해서 실행시키는거
        # self.StartApp.clicked.connect(
        #     lambda:
        #         self.getappinfo(None, self.listWidget.selectedItems()[0].text())
        #     if self.listWidget.selectedItems() != []
        #     else self.exceptionMessage()
        # )
        self.StartApp.clicked.connect(
            lambda:
                self.startAppCmd(self.listWidget.selectedItems()[0].text())
                # print(self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )

    def startAppCmd(self, packageName):
        '''
        adb shell monkey -p $packageName -c android.intent.category.LAUNCHER 1
        :param packageName:
        :return:
        '''
        try:
            CMD = "adb shell monkey -p ${} -c android.intent.category.LAUNCHER 1".format(packageName)
            print(CMD)
            cmd.call(CMD, stderr=None, shell=True)
        except:
            ctypes.windll.user32.MessageBoxW(0,
                                             "선택된 앱 : {}\n위 앱이 설치되지 않은 상태입니다.\n리스트갱신 버튼을 클릭하세요."
                                             .format(self.listWidget.selectedItems()[0].text())
                                             , "설치확인", consts_string.show_flag.foreground.value)

    def getappinfo(self, *args):
        getAPP = self.getAPK(args[1])
        print(getAPP)
        if getAPP :
            # self.check_connect()[1] : connected devices's list
            self.run_apk(getAPP, self.check_connect()[1])
            os.remove(getAPP)
        else:
            ctypes.windll.user32.MessageBoxW(0, "선택된 앱이 설치되지 않았습니다.\n리스트갱신합니다.", "리스트확인요청",
                                             consts_string.show_flag.foreground.value)
            self.listup()

    def listup(self):
        self.listWidget.clear() # clear list
        InstProgramInfo = self.list_ins_program(None)
        if InstProgramInfo != -1 :
            for index in range(len(InstProgramInfo)):
                self.listWidget.addItem(InstProgramInfo[index])
        else :
            ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", consts_string.show_flag.foreground.value)

    def exceptionMessage(self):
        ctypes.windll.user32.MessageBoxW(0, "선택된 앱이 없습니다.\n리스트에서 앱을 선택하세요.", "리스트확인요청",
                                         consts_string.show_flag.foreground.value | consts_string.show_flag.ICON_STOP.value)
        


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # Main = QtWidgets.QMainWindow()
    # ui = SubWindow02()
    # ui.setupUi(Main)
    # ui.connect()
    # Main.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = SubWindow02()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())