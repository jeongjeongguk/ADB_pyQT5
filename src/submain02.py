import sys, ctypes
src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
sys.path.insert(0, src_path_company)
# src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
# sys.path.insert(0, src_path_home)
import installedList_ui
import adb_default
from PyQt5 import QtWidgets

class SubWindow02(QtWidgets.QMainWindow, installedList_ui.Ui_Form, adb_default.default):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect()
        self.listup()

    def connect(self):
        #TODO : 연결이 중간에 끊어진 상황과, 해당 패키지명이 설치되지 않은상황 처리필요
        '''
        : button과 기능함수을 연결해주는 함수
        '''
        # 앱 삭제, listWidget.selectedItems()의 반환값은 선택된 항목들 리스트.
        self.pushButton.clicked.connect(
            lambda :
            self.uninstall_apk("packageName", self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )

        # 데이터 삭제
        self.pushButton_2.clicked.connect(
            # lambda : self.deleteData("packageName", self.listWidget.selectedItems()[0].text()) # it's ok. old_ver.
            lambda :
            self.deleteData("packageName", self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
            # lambda : print(self.listWidget.selectedItems()) # it returns []
        )

        # 출시버전
        self.pushButton_3.clicked.connect(
            lambda :
            self.link2release("packageName", self.listWidget.selectedItems()[0].text())
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )
        '''
       Traceback (most recent call last):
          File "C:/Users/Jeongkuk/PycharmProjects/androidADB/submain02.py", line 29, in <lambda>
        lambda : self.link2release("packageName", self.listWidget.selectedItems()[0].text())
            IndexError: list index out of range
 
        '''
        # 리스트 갱신
        self.pushButton_4.clicked.connect(self.listup)
        # 도움말
        self.pushButton_5.clicked.connect(lambda : self.show_help_subform02(None))

        self.pushButton_6.clicked.connect(
            lambda:
            ctypes.windll.user32.MessageBoxW(0,
                                             "선택된 앱 : {}\n확인된 버전 : {}"
                                             .format(self.listWidget.selectedItems()[0].text(),self.getVersion(self.listWidget.selectedItems()[0].text(), ""))
                                             , "버전확인", 0)

            # print(self.getVersion(self.listWidget.selectedItems()[0].text(), ""))
            if self.listWidget.selectedItems() != []
            else self.exceptionMessage()
        )

    def listup(self):
        self.listWidget.clear() # clear list
        InstProgramInfo = self.list_ins_program(None)
        if InstProgramInfo != -1 :
            for index in range(len(InstProgramInfo)):
                self.listWidget.addItem(InstProgramInfo[index])
        else :
            ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", 0)

    def exceptionMessage(self):
        ctypes.windll.user32.MessageBoxW(0, "선택된 앱이 없습니다.\n리스트에서 앱을 선택하세요.", "리스트확인요청", 0)


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # Main = QtWidgets.QMainWindow()
    # ui = SubWindow02()
    # ui.setupUi(Main)
    # ui.connect()
    # Main.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = SubWindow02()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())