import sys, os

import adb_command_ui
import adb_default
from PyQt5 import QtWidgets, QtCore


class SubWindow01(QtWidgets.QMainWindow, adb_command_ui.Ui_Form, adb_default.default):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.connect()

    def connect(self):
        _translate = QtCore.QCoreApplication.translate
        self.toolButton.clicked.connect(self.SelectSetupFile)
        self.pushButton.clicked.connect(
            lambda : self.label_3.setText(_translate("Form", self.run_info(self.lineEdit.text())[0])))
        self.pushButton.clicked.connect(
            lambda: self.label_4.setText(_translate("Form", self.run_info(self.lineEdit.text())[1])))
        self.pushButton_2.clicked.connect(lambda: self.install_apk(self.lineEdit.text()))
        self.pushButton_3.clicked.connect(lambda: self.deleteData(self.lineEdit.text()))
        self.pushButton_4.clicked.connect(lambda: self.run_apk(self.lineEdit.text()))
        self.pushButton_5.clicked.connect(lambda: self.controlDevice(None, "reboot"))
        self.pushButton_6.clicked.connect(lambda: self.goSetLanguagePage(None))
        self.pushButton_7.clicked.connect(lambda: self.goSetTimePage(None))
        self.pushButton_8.clicked.connect(lambda: self.show_help_subform01(None)) # 도움말 ㅋㅋ
        self.pushButton_9.clicked.connect(lambda: self.controlDevice(self.lineEdit_2.text()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = SubWindow01()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())