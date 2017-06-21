import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess

import main_ui, adb_command_ui, installedList_ui
import submain01, submain02
import adb_default

import subprocess

'''
기본 : QtWidgets.QMainWindow
UI   : main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, installedList_ui.Ui_Form
기능 : adb_default.default
'''
class MainWindow(QtWidgets.QMainWindow,
                  main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, installedList_ui.Ui_Form,
                  adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.makedir()
        self.window2 = None # 설치창
        self.window3 = None # 설치된 앱리스트창
        # QTimer.singleShot(5000, self.show_subform01)

    def connect(self):
        self.Install.clicked.connect(self.show_subform01)
        self.Uninstall.clicked.connect(self.show_subform02) #TODO : 설치된 앱들 리스트뷰
        self.captureImage.clicked.connect(self.capture2image)
        self.captureVideo.clicked.connect(self.capture2viedo)
        self.ConnectedDevices.clicked.connect(self.open_capture_folder)

    def show_subform01(self):
        if self.window2 is None:
            self.window2 = submain01.SubWindow01(self)
        self.window2.show() # run ok.
        # self.window2.StartQT5()

        # process = QProcess(self)
        # process.start(self.window2.show()) # 되긴하는데, 동작할때 메인창도 같이 응답없음상태임. 음..??

        # subprocess.call(self.window2.show(), stderr=subprocess.STDOUT, shell=True) # crash

    def show_subform02(self):
        if self.window3 is None:
            self.window3 = submain02.SubWindow02(self)
        self.window3.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())
