# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adb_test1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, os

form_class = uic.loadUiType("ui.ui")[0]  # Load the UI

class Ui_MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.test)    #   to the buttons
        self.pushButton.clicked.connect(self.install) #   to the buttons

    def test(self):
        self.fileDialog = QtWidgets.QFileDialog()
        select = self.fileDialog.getOpenFileUrl()
        path = str(select[0]).replace("PyQt5.QtCore.QUrl('file:///", "")
        path = path.replace("')", "")
        self.lineEdit.setText(path)
        print(path)

    def install(self):
        imsi = 10
        '''
        while imsi < 10:
            os.system("adb shell screencap /mnt/sdcard/ScreenCapture/{}.png".format(imsi))
            imsi += 1
            print(imsi)
'''
 #       '''
        #print(self.lineEdit.text())
        self.label.setText("실행중")
        path = self.lineEdit.text()
        adb_command_install = "adb install -r " + path

        os.system(adb_command_install)
        self.label.setText("설치완료")

        get_start_activity = "aapt dump badging " + path + " | FINDSTR launchable-activity"
        get_package_name = "aapt dump badging " + path + " | FINDSTR package"

        os.system(get_start_activity)
        os.system(get_package_name)

        # del_index = imsi_text.find("=")
        # print(del_index)
        # imsi_text = imsi_text[del_index:]

        #os.system("adb shell am start -n com.estsoft.alsongbeta/com.estsoft.alsong.SplashActivity")
        os.system("adb shell am start -n com.estsoft.teamuptest/com.estsoft.teamup.ui.login.LoginActivity")

    # Define function to import external files when using PyInstaller.
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
#'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = Ui_MainWindow()
    myWindow.show()
    app.exec_()



'''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 112)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "           "))

        self.connect(MainWindow)

    def connect(self, MainWindow):
        self.toolButton.clicked.connect(test_cmd.myADB.test)
        self.pushButton.clicked.connect(test_cmd.myADB.install)
'''