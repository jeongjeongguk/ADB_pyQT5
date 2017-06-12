import sys
import adb_default
import adb_command_ui
from PyQt5 import QtWidgets


class SubWindow01(QtWidgets.QMainWindow, adb_command_ui.Ui_Form, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()

    def connect(self):
        pass

    def showSubWindow01(self):
        app = QtWidgets.QApplication(sys.argv)
        Sub01 = QtWidgets.QMainWindow()
        ui = SubWindow01()
        ui.setupUi(Sub01)
        ui.connect()
        Sub01.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    SubWindow01.showSubWindow01(None)