import sys, os, ctypes
src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
sys.path.insert(0, src_path_company)
# src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
# sys.path.insert(0, src_path_home)
import adb_command_ui
import adb_default
from PyQt5 import QtWidgets, QtCore


class SubWindow01(QtWidgets.QMainWindow, adb_command_ui.Ui_Form, adb_default.default):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.connect()
        self.commandListup()

    def connect(self):
        #TODO : staticmethod는 기능함수에서 -1로 리턴하고, -1일때 예외처리. UI값읽어오는것은, UI값 비정상인 상태를 lambda 삼항연산으로 처리.
        _translate = QtCore.QCoreApplication.translate
        self.toolButton.clicked.connect(self.setAPKpath) #TODO : 파일익스플로러에서 취소클릭시, 제거할 스트링 넘기지않도록 처리.
        self.pushButton.clicked.connect(
            lambda :
            self.label_3.setText(_translate("Form", self.run_info(self.lineEdit.text())[1]))
            if self.lineEdit.text() != "" else self.exceptionMessage()
        )
        self.pushButton.clicked.connect(
            lambda:
            self.label_4.setText(_translate("Form", self.run_info(self.lineEdit.text())[2]))
            if self.lineEdit.text() != ""
            else self.label_3.setText(_translate("Form", "None"))
        )
        self.pushButton_2.clicked.connect(
            lambda:
            self.install_apk(self.lineEdit.text(),"")
            if self.lineEdit.text() != ""
            else self.exceptionMessage()
        )
        # self.pushButton_3.clicked.connect(
        #     lambda: self.reinstall_apk(self.lineEdit.text()) if self.lineEdit.text() != "" else self.exceptionMessage()
        # )
        self.pushButton_3.clicked.connect(
            lambda:
            self.install_apk(self.lineEdit.text(), "-r ")
            if self.lineEdit.text() != ""
            else self.exceptionMessage()
        )

        self.pushButton_4.clicked.connect(
            lambda: self.run_apk(self.lineEdit.text()) if self.lineEdit.text() != "" else self.exceptionMessage()
        )
        self.pushButton_5.clicked.connect(lambda: self.controlDevice(None, "adb reboot"))
        self.pushButton_6.clicked.connect(lambda: self.goSetLanguagePage(None))
        self.pushButton_7.clicked.connect(lambda: self.goSetTimePage(None))
        self.pushButton_8.clicked.connect(lambda: self.show_help_subform01(None)) # 도움말 ㅋㅋ
        # lineEdit : self.lineEdit.text()
        # comboBox : self.comboBox.currentText()
        self.pushButton_9.clicked.connect(
            lambda: self.controlDevice(None, self.comboBox.currentText()) if self.comboBox.currentText() != ""
            else ctypes.windll.user32.MessageBoxW(0, "명령어를 입력해주세요", "명령어없음", 0)
        )
        # lineEdit : self.lineEdit.returnPressed.connect(self.pushButton_9)
        # comboBox : self.comboBox.lineEdit().returnPressed.connect()
        # comboBox 에서 엔터입력시 포커스 이동 : self.comboBox.lineEdit().returnPressed.connect(self.pushButton_9.setFocus)
        self.comboBox.lineEdit().returnPressed.connect(
            lambda: self.controlDevice(None, self.comboBox.currentText()) if self.comboBox.currentText() != ""
            else ctypes.windll.user32.MessageBoxW(0, "명령어를 입력해주세요", "명령어없음", 0)
        ) # 엔터키입력시에도, 버튼을 클릭했을때와 동일한 함수를 연결.



    def setAPKpath(self):
        path = self.SelectSetupFile()
        # print(path)
        self.lineEdit.setText(path)

    def exceptionMessage(self):
        ctypes.windll.user32.MessageBoxW(0, "선택된 앱이 없습니다.\n...을 클릭해서 apk파일을 선택하세요.", "파일확인요청", 0)

    def check_command(self):
        command = None #TODO : check command
        return command

    def commandListup(self):
        List = [
            "[쉘]adb shell",
            "[PC ADB kill]adb kill-server",
            "[PC ADB start]adb start-server",
            "[재부팅]adb reboot",
            "[홈버튼]adb shell input keyevent KEYCODE_HOME",
            "[back버튼]adb shell input keyevent KEYCODE_BACK",
            "[메뉴버튼]adb shell input keyevent KEYCODE_MENU",
            "[전원버튼]adb shell input keyevent KEYCODE_POWER"
        ]

        for command in range(0,len(List)):
            self.comboBox.addItem(List[command])
        return List

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = SubWindow01()
    ui.setupUi(Main)
    ui.connect()
    # ui.commandListup() #submain01만 확인할때는 주석제거, main에서 submain01호출할때는 정상적으로 리스트추가됨
    Main.show()
    sys.exit(app.exec_())

    # print(SubWindow01.commandListup(None))
    # print(type(SubWindow01.commandListup(None)[0][1]))
    # print(SubWindow01.commandListup(None)[0][0])
    # print(SubWindow01.commandListup(None)[0][1])