import sys
import adb_default
import main_ui
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())