# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 101)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(342, 101))
        MainWindow.setMaximumSize(QtCore.QSize(342, 101))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icons/Main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Install = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Install.setFont(font)
        self.Install.setStyleSheet("")
        self.Install.setIcon(icon)
        self.Install.setIconSize(QtCore.QSize(30, 30))
        self.Install.setCheckable(False)
        self.Install.setAutoRepeat(False)
        self.Install.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Install.setAutoRaise(True)
        self.Install.setObjectName("Install")
        self.horizontalLayout.addWidget(self.Install)
        self.Uninstall = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icons/1494232917_icon-trash-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Uninstall.setIcon(icon1)
        self.Uninstall.setIconSize(QtCore.QSize(30, 30))
        self.Uninstall.setCheckable(False)
        self.Uninstall.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Uninstall.setAutoRaise(True)
        self.Uninstall.setObjectName("Uninstall")
        self.horizontalLayout.addWidget(self.Uninstall)
        self.captureImage = QtWidgets.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/icons/Capture_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.captureImage.setIcon(icon2)
        self.captureImage.setIconSize(QtCore.QSize(30, 30))
        self.captureImage.setCheckable(False)
        self.captureImage.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.captureImage.setAutoRaise(True)
        self.captureImage.setObjectName("captureImage")
        self.horizontalLayout.addWidget(self.captureImage)
        self.captureVideo = QtWidgets.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/icons/Capture_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.captureVideo.setIcon(icon3)
        self.captureVideo.setIconSize(QtCore.QSize(30, 30))
        self.captureVideo.setCheckable(False)
        self.captureVideo.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.captureVideo.setAutoRaise(True)
        self.captureVideo.setObjectName("captureVideo")
        self.horizontalLayout.addWidget(self.captureVideo)
        self.ConnectedDevices = QtWidgets.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/icons/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConnectedDevices.setIcon(icon4)
        self.ConnectedDevices.setIconSize(QtCore.QSize(30, 30))
        self.ConnectedDevices.setCheckable(False)
        self.ConnectedDevices.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ConnectedDevices.setAutoRaise(True)
        self.ConnectedDevices.setObjectName("ConnectedDevices")
        self.horizontalLayout.addWidget(self.ConnectedDevices)
        self.option = QtWidgets.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/menu/icons/Option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.option.setIcon(icon5)
        self.option.setIconSize(QtCore.QSize(30, 30))
        self.option.setCheckable(False)
        self.option.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.option.setAutoRaise(True)
        self.option.setObjectName("option")
        self.horizontalLayout.addWidget(self.option)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB GUI"))
        self.Install.setToolTip(_translate("MainWindow", "설치,실행,날짜/언어"))
        self.Install.setText(_translate("MainWindow", "Cmd"))
        self.Uninstall.setToolTip(_translate("MainWindow", "앱리스트/삭제,데이터삭제,버전"))
        self.Uninstall.setText(_translate("MainWindow", "AppList"))
        self.captureImage.setToolTip(_translate("MainWindow", "현재 화면캡처"))
        self.captureImage.setText(_translate("MainWindow", "Capture"))
        self.captureVideo.setToolTip(_translate("MainWindow", "화면동작 녹화"))
        self.captureVideo.setText(_translate("MainWindow", "Record"))
        self.ConnectedDevices.setToolTip(_translate("MainWindow", "캡처/녹화 파일확인"))
        self.ConnectedDevices.setText(_translate("MainWindow", "Capture"))
        self.option.setToolTip(_translate("MainWindow", "도움말"))
        self.option.setText(_translate("MainWindow", "Help"))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
