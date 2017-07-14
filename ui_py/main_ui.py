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
        MainWindow.resize(299, 101)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(299, 101))
        MainWindow.setMaximumSize(QtCore.QSize(299, 101))
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
        self.Install = QtWidgets.QPushButton(self.centralwidget)
        self.Install.setText("")
        self.Install.setIcon(icon)
        self.Install.setIconSize(QtCore.QSize(30, 30))
        self.Install.setFlat(True)
        self.Install.setObjectName("Install")
        self.horizontalLayout.addWidget(self.Install)
        self.Uninstall = QtWidgets.QPushButton(self.centralwidget)
        self.Uninstall.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icons/1494232917_icon-trash-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Uninstall.setIcon(icon1)
        self.Uninstall.setIconSize(QtCore.QSize(30, 30))
        self.Uninstall.setFlat(True)
        self.Uninstall.setObjectName("Uninstall")
        self.horizontalLayout.addWidget(self.Uninstall)
        self.captureImage = QtWidgets.QPushButton(self.centralwidget)
        self.captureImage.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/icons/Capture_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.captureImage.setIcon(icon2)
        self.captureImage.setIconSize(QtCore.QSize(30, 30))
        self.captureImage.setFlat(True)
        self.captureImage.setObjectName("captureImage")
        self.horizontalLayout.addWidget(self.captureImage)
        self.captureVideo = QtWidgets.QPushButton(self.centralwidget)
        self.captureVideo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/icons/Capture_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.captureVideo.setIcon(icon3)
        self.captureVideo.setIconSize(QtCore.QSize(25, 25))
        self.captureVideo.setFlat(True)
        self.captureVideo.setObjectName("captureVideo")
        self.horizontalLayout.addWidget(self.captureVideo)
        self.ConnectedDevices = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectedDevices.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/icons/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConnectedDevices.setIcon(icon4)
        self.ConnectedDevices.setIconSize(QtCore.QSize(30, 30))
        self.ConnectedDevices.setFlat(True)
        self.ConnectedDevices.setObjectName("ConnectedDevices")
        self.horizontalLayout.addWidget(self.ConnectedDevices)
        self.option = QtWidgets.QPushButton(self.centralwidget)
        self.option.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/menu/icons/Option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.option.setIcon(icon5)
        self.option.setIconSize(QtCore.QSize(30, 30))
        self.option.setFlat(True)
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

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

