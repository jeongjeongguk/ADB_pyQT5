import sys, ctypes

import installedList_ui
import adb_default
from PyQt5 import QtWidgets, QtCore

class SubWindow02(QtWidgets.QMainWindow, installedList_ui.Ui_Form, adb_default.default):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect()
        try :
            self.listup()
        except :
            ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", 0)
            pass
            # raise Exception('연결된 기기가 없습니다. ') #TODO : Exception 에 대한 Main에서 처리.

    def connect(self):
        '''
        : button과 기능함수을 연결해주는 함수
        '''
        # 앱 삭제, listWidget.selectedItems()의 반환값은 선택된 항목들 리스트.
        self.pushButton.clicked.connect(
            lambda : self.uninstall_apk("packageName", self.listWidget.selectedItems()[0].text())
        )

        # 데이터 삭제
        self.pushButton_2.clicked.connect(
            lambda : self.deleteData("packageName", self.listWidget.selectedItems()[0].text())
        )
        # 출시버전

        self.pushButton_3.clicked.connect(
            lambda : self.link2release("packageName", self.listWidget.selectedItems()[0].text())
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

    def listup(self):
        self.listWidget.clear() # clear list
        InstProgramInfo = self.list_ins_program(None)
        for index in range(len(InstProgramInfo)):
            self.listWidget.addItem(InstProgramInfo[index])
        # print(InstProgramInfo)


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