import sys, ctypes, os, datetime
currentPaths = os.getcwd()
currentPathsSet = currentPaths.replace("src","ui_py")
sys.path.insert(0, currentPathsSet)

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot

import main_ui
import submain01, submain02, submain03, optionSrc
import adb_default
import consts_string

import subprocess

__author__ = "JeongKuk <wjdrnr6176@gmail.com>"


'''
기본 : QtWidgets.QMainWindow
UI   : main_ui.Ui_MainWindow, adb_command_ui.Ui_Form, installedList_ui.Ui_Form
기능 : adb_default.default
'''
#TODO : UI 중력뭉개질떄 추가할것
'''
self.widget = QtWidgets.QWidget(Form)
self.widget.setGeometry(QtCore.QRect(10, 10, 322, 157)) # 이부분이 필요한거다
self.widget.setObjectName("widget")
'''
class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow, adb_default.defaultADB):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.window2 = None # 설치창
        self.window3 = None # 설치된 앱리스트창
        self.window4 = None # 캡쳐한 파일들 편집창
        self.opitonForm = None # 설정안내창
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def connect(self):
        self.TBScreen.clicked.connect(self.call_capture2image)
        self.TBRecord.clicked.connect(self.call_capture2viedo)
        self.listup_devices()
        # print(self.check_connect()[1])
        # self.ConnectedDevices.clicked.connect(self.open_capture_folder)

    # def show_subform01(self):
    #     if self.window2 is None:
    #         self.window2 = submain01.SubWindow01(self)
    #     self.window2.show()
    #
    # def show_subform02(self):
    #     # QT Designer에서, ui파일작성시 잘못작성하면, ui.py에 geometry가 빠지고, 그러면 다른 py에서 해당 ui불러내면
    #     # UI가 뭉개져서(각 요소들 중력값이 무시된채로) 표시됨. -> 해결방법 못찾음 ( 기존 ui파일의 요소들만 지우고
    #     # 거기다가 새로그림)
    #     if self.window3 is None:
    #         self.window3 = submain02.SubWindow02(self)
    #     self.window3.show()
    #
    # def show_subform03(self):
    #     today = datetime.datetime.now().strftime("%y%m%d")
    #     path = os.getcwd() + "\\{}".format(today)
    #     if self.window4 is None:
    #         self.window4 = submain03.SubWindow03(path)
    #     self.window4.show()
    #
    # def show_optionform(self):
    #     if self.opitonForm is None:
    #         self.opitonForm = optionSrc.windowForm(self)
    #     self.opitonForm.show()

    def listup_devices(self):
        '''
        self.check_connect()[1] : 연결된 기기 리스트 전체 ( 현재 U
        '''
        self.LWUSB.clear() # clear list
        ConnectedDevicesCnt = self.check_connect()[0]
        if ConnectedDevicesCnt != 0:
            for index in range(0,ConnectedDevicesCnt):
                self.LWUSB.addItem(self.check_connect()[1][index])
                self.LWALL.addItem(self.check_connect()[1][index])
        else :
            ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", consts_string.show_flag.foreground.value)

    #
    # def listup(self):
    #     self.listWidget.clear() # clear list
    #     InstProgramInfo = self.list_ins_program(None)
    #     if InstProgramInfo != -1 :
    #         for index in range(len(InstProgramInfo)):
    #             self.listWidget.addItem(InstProgramInfo[index])
    #     else :
    #         ctypes.windll.user32.MessageBoxW(0, "연결된 기기가 없습니다.", "USB연결 확인요청", consts_string.show_flag.foreground.value)


    def call_capture2image(self):
        '''
        TBScreen : image capture
        '''
        self.TBScreen.setEnabled(False)
        self.capture2image()
        self.TBScreen.setEnabled(True)

    def call_capture2viedo(self):
        '''
        TBRecord : record screen
        '''
        self.TBRecord.setEnabled(False)
        self.capture2viedo()
        self.TBRecord.setEnabled(True)
# '''
    @pyqtSlot()
    def error(self):
        raise RuntimeError

def exception_hook(t, val, tb):
    '''
    :param t: Exception type
    :param val: Exception message
    :param tb: where happen
    :return:
    '''
    # QMessageBox.critical(None, "An exception was raised", "Exception type: {}".format(t), consts_string.show_flag.foreground.value)
    # 표시안됨. flag 값 확인?
    # QMessageBox.critical(None, "An exception was raised", "Exception type: {}".format(t))
    ctypes.windll.user32.MessageBoxW(0, "Exception type: {}".format(t)
                                     , "An exception was raised", consts_string.show_flag.foreground.value)
    adb_default.logger.error("Exception type: {}".format(t))
    adb_default.logger.error("Exception message: {}".format(val))
    # adb_default.logger.error("Exception type: {}".format(tb))
    old_exception_hook(t, val, tb)

if __name__ == "__main__":
    # '''
    # 예외 훅을 재설정.
    old_exception_hook = sys.excepthook
    sys.excepthook = exception_hook
    # '''
    os.system("adb devices") #https://github.com/jeongjeongguk/androidADB/issues/2
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())
