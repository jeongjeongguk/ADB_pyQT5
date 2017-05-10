import sys
import adb_default
import main_ui
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()
        # self.connect()
        self.makedir()

    def connect(self):
        # filepath = "alsong_4.0.7.3.apk"
        # self.Install.clicked.connect(lambda: self.install_apk(filepath))
        self.captureImage.clicked.connect(self.capture2image)
        self.captureVideo.clicked.connect(self.capture2viedo)
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())