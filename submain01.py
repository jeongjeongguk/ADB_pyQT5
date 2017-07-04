import sys, os, ctypes

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
        #TODO : staticmethod는 기능함수에서 -1로 리턴하고, -1일때 예외처리. UI값읽어오는것은, UI값 비정상인 상태를 lambda 삼항연산으로 처리.
        _translate = QtCore.QCoreApplication.translate
        self.toolButton.clicked.connect(self.setAPKpath) #TODO : 파일익스플로러에서 취소클릭시, 제거할 스트링 넘기지않도록 처리.
        self.pushButton.clicked.connect(
            lambda :
            self.label_3.setText(_translate("Form", self.run_info(self.lineEdit.text())[0]))
            if self.lineEdit.text() != "" else self.exceptionMessage()
        )
        self.pushButton.clicked.connect(
            lambda:
            self.label_4.setText(_translate("Form", self.run_info(self.lineEdit.text())[1]))
            if self.lineEdit.text() != ""
            else self.label_3.setText(_translate("Form", "None"))
        )
        self.pushButton_2.clicked.connect(
            lambda: self.install_apk(self.lineEdit.text()) if self.lineEdit.text() != "" else self.exceptionMessage()
        )
        self.pushButton_3.clicked.connect(
            lambda: self.reinstall_apk(self.lineEdit.text()) if self.lineEdit.text() != "" else self.exceptionMessage()
        )
        self.pushButton_4.clicked.connect(
            lambda: self.run_apk(self.lineEdit.text()) if self.lineEdit.text() != "" else self.exceptionMessage()
        )
        self.pushButton_5.clicked.connect(lambda: self.controlDevice(None, "reboot"))
        self.pushButton_6.clicked.connect(lambda: self.goSetLanguagePage(None))
        self.pushButton_7.clicked.connect(lambda: self.goSetTimePage(None))
        self.pushButton_8.clicked.connect(lambda: self.show_help_subform01(None)) # 도움말 ㅋㅋ
        self.pushButton_9.clicked.connect(
            lambda: self.controlDevice(self.lineEdit_2.text()) if self.lineEdit_2.text() != ""
            else ctypes.windll.user32.MessageBoxW(0, "명령어를 입력해주세요", "명령어없음", 0)
        )

    def setAPKpath(self):
        path = self.SelectSetupFile()
        print(path)
        self.lineEdit.setText(path)

    def exceptionMessage(self):
        ctypes.windll.user32.MessageBoxW(0, "선택된 앱이 없습니다.\n...을 클릭해서 apk파일을 선택하세요.", "파일확인요청", 0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = SubWindow01()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())