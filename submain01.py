import sys
import adb_default
import adb_command_ui
import main
from PyQt5 import QtWidgets, QtCore


class SubWindow01(QtWidgets.QMainWindow, adb_command_ui.Ui_Form, adb_default.default):
    # def __init__(self):
    #     super(self.__class__, self).__init__()
    #     self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    #     self.setupUi(self)
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect()

    def connect(self):
        self.toolButton.clicked.connect(self.SelectSetupFile)
        self.pushButton_2.clicked.connect(lambda : self.install_apk(self.lineEdit.text()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = SubWindow01()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())