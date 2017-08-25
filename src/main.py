import sys, ctypes, os, datetime
currentPaths = os.getcwd()
currentPathsSet = currentPaths.replace("src","ui_py")
sys.path.insert(0, currentPathsSet)

from PyQt5 import QtWidgets, QtCore

import main_ui
import submain01, submain02, submain03, optionSrc
import adb_default
import consts_string

import subprocess

'''
기본 : QtWidgets.QMainWindow
UI   : main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, installedList_ui.Ui_Form
기능 : adb_default.default
'''
#TODO : UI 중력뭉개질떄 추가할것
'''
self.widget = QtWidgets.QWidget(Form)
self.widget.setGeometry(QtCore.QRect(10, 10, 322, 157)) # 이부분이 필요한거다
self.widget.setObjectName("widget")
'''
class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_default.defaultADB):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.window2 = None # 설치창
        self.window3 = None # 설치된 앱리스트창
        self.window4 = None # 캡쳐한 파일들 편집창
        self.opitonForm = None # 설정안내창
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def connect(self):
        self.Install.clicked.connect(self.show_subform01)
        self.Uninstall.clicked.connect(self.show_subform02)
        self.captureImage.clicked.connect(self.call_capture2image)
        self.captureVideo.clicked.connect(self.call_capture2viedo)
        # self.ConnectedDevices.clicked.connect(self.open_capture_folder)
        self.ConnectedDevices.clicked.connect(self.show_subform03)
        self.option.clicked.connect(self.show_optionform)

    def show_subform01(self):
        if self.window2 is None:
            self.window2 = submain01.SubWindow01(self)
        self.window2.show()

    def show_subform02(self):
        # QT Designer에서, ui파일작성시 잘못작성하면, ui.py에 geometry가 빠지고, 그러면 다른 py에서 해당 ui불러내면
        # UI가 뭉개져서(각 요소들 중력값이 무시된채로) 표시됨. -> 해결방법 못찾음 ( 기존 ui파일의 요소들만 지우고
        # 거기다가 새로그림)
        if self.window3 is None:
            self.window3 = submain02.SubWindow02(self)
        self.window3.show()

    def show_subform03(self):
        today = datetime.datetime.now().strftime("%y%m%d")
        path = os.getcwd() + "\\{}".format(today)
        if self.window4 is None:
            self.window4 = submain03.SubWindow03(path)
        self.window4.show()

    def show_optionform(self):
        if self.opitonForm is None:
            self.opitonForm = optionSrc.windowForm(self)
        self.opitonForm.show()

    def call_capture2image(self):
        self.captureImage.setEnabled(False)
        self.capture2image()
        self.captureImage.setEnabled(True)

    def call_capture2viedo(self):
        self.captureVideo.setEnabled(False)
        self.capture2viedo()
        self.captureVideo.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())
