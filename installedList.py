import sys

import adb_default
import installedList_ui
from PyQt5 import QtWidgets, QtCore


class SubWindow02(QtWidgets.QMainWindow, installedList_ui.Ui_Form, adb_default.default):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.connect()

    def connect(self):
        _translate = QtCore.QCoreApplication.translate


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = SubWindow02()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())