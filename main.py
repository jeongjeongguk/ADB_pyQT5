import sys
from PyQt5 import QtWidgets

import adb_command_ui
import adb_default
import main_ui
import submain01

class MainWindow(QtWidgets.QMdiSubWindow , QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.makedir()
        self.window2 = None # 이 부분이 있어야 클릭시 메인창이 안닫히고, subwinow가 새로 열림
        self.window3 = None

    def connect(self):
        self.Install.clicked.connect(self.show_subform01)
        # self.Uninstall.clicked.connect(self.show_subform01) #TODO : 설치된 앱들 리스트뷰
        self.captureImage.clicked.connect(self.capture2image)
        self.captureVideo.clicked.connect(self.capture2viedo)
        self.ConnectedDevices.clicked.connect(self.open_capture_folder)

    def show_subform01(self):
        if self.window2 is None:
            self.window2 = submain01.SubWindow01(self)
        self.window2.show()

    def show_subform02(self):
        if self.window3 is None:
            self.window3 = submain01.SubWindow01(self)
        self.window3.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())