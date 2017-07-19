import sys
# src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
# sys.path.insert(0, src_path_company)
src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
sys.path.insert(0, src_path_home)

from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess

import main_ui, adb_command_ui, installedList_ui, optionSrc_ui
import submain01, submain02, optionSrc
import adb_default

import subprocess

'''
기본 : QtWidgets.QMainWindow
UI   : main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, installedList_ui.Ui_Form
기능 : adb_default.default
'''
#TODO : UI 중력뭉개질떄 추가할것
'''
self.widget = QtWidgets.QWidget(Form)
self.widget.setGeometry(QtCore.QRect(10, 10, 322, 157))
self.widget.setObjectName("widget")
'''
class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.window2 = None # 설치창
        self.window3 = None # 설치된 앱리스트창
        self.opitonForm = None # 설정안내창

    def connect(self):
        self.Install.clicked.connect(self.show_subform01)
        self.Uninstall.clicked.connect(self.show_subform02) #TODO : 설치된 앱들 리스트뷰
        self.captureImage.clicked.connect(self.capture2image)
        self.captureVideo.clicked.connect(self.capture2viedo)
        self.ConnectedDevices.clicked.connect(self.open_capture_folder)
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

    def show_optionform(self):
        if self.opitonForm is None:
            self.opitonForm = optionSrc.windowForm(self)
        self.opitonForm.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())
