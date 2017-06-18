import sys
import adb_default
import main_ui
import adb_command_ui
import submain01
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMdiSubWindow , QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()
        # self.connect()
        self.makedir()
        self.window2 = None # 이 부분이 있어야 클릭시 메인창이 안닫히고, subwinow가 새로 열림

    def connect(self):
        # filepath = "alsong_4.0.7.3.apk"
        # self.Install.clicked.connect(lambda: self.install_apk(filepath))
        self.captureImage.clicked.connect(self.capture2image)
        self.captureVideo.clicked.connect(self.capture2viedo)
        self.ConnectedDevices.clicked.connect(self.showSubForm01)

    # def showSubForm01(self):
    #     '''
    #     https://www.google.co.kr/search?q=how+to+show+sub+form+in+main+window+button+at+python3+pyqt5&oq=how+to+show+sub+form+in+main+window+button+at+python3+pyqt5&aqs=chrome..69i57.30079j0j7&sourceid=chrome&ie=UTF-8
    #     https://stackoverflow.com/questions/27567208/how-do-i-open-sub-window-after-i-click-on-button-on-main-screen-in-pyqt4
    #     :return:
    #     '''
    #     subForm = submain01.SubWindow01(self)
    #     subForm.show()

    def showSubForm01(self):
        if self.window2 is None:
            self.window2 = submain01.SubWindow01(self)
        self.window2.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    # ui_sub =
    Main.show()
    sys.exit(app.exec_())