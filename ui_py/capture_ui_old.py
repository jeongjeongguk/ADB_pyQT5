# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 618)
        MainWindow.setMinimumSize(QtCore.QSize(751, 618))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/icons/Capture_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0021.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0019.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0007.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setWhatsThis("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/icons/TeamUP_0000.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0012.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setBaseSize(QtCore.QSize(0, 0))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setIconSize(QtCore.QSize(30, 30))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(False)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0016.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0015.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(":/button/icons/ALCapture_0013.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/button/icons/mspaint_0001.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, "")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # [수정한 부분] ================================================================================================
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.scene)
        # ==============================================================================================================
        self.graphicsView.setWhatsThis("")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_T = QtWidgets.QMenu(self.menubar)
        self.menu_T.setObjectName("menu_T")
        self.menu_F_2 = QtWidgets.QMenu(self.menu_T)
        self.menu_F_2.setObjectName("menu_F_2")
        self.menu_L = QtWidgets.QMenu(self.menu_T)
        self.menu_L.setObjectName("menu_L")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_I = QtWidgets.QAction(MainWindow)
        self.action_I.setObjectName("action_I")
        self.action_R = QtWidgets.QAction(MainWindow)
        self.action_R.setObjectName("action_R")
        self.action_Q = QtWidgets.QAction(MainWindow)
        self.action_Q.setObjectName("action_Q")
        self.action_G = QtWidgets.QAction(MainWindow)
        self.action_G.setObjectName("action_G")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setObjectName("action_14")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_16 = QtWidgets.QAction(MainWindow)
        self.action_16.setObjectName("action_16")
        self.action1pt = QtWidgets.QAction(MainWindow)
        self.action1pt.setObjectName("action1pt")
        self.action2pt = QtWidgets.QAction(MainWindow)
        self.action2pt.setObjectName("action2pt")
        self.action3pt = QtWidgets.QAction(MainWindow)
        self.action3pt.setObjectName("action3pt")
        self.action4pt = QtWidgets.QAction(MainWindow)
        self.action4pt.setObjectName("action4pt")
        self.action5pt = QtWidgets.QAction(MainWindow)
        self.action5pt.setObjectName("action5pt")
        self.action6pt = QtWidgets.QAction(MainWindow)
        self.action6pt.setObjectName("action6pt")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu_F.addAction(self.action)
        self.menu_F.addAction(self.action_2)
        self.menu_F.addAction(self.action_3)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_5)
        self.menu_E.addAction(self.action_7)
        self.menu_E.addAction(self.action_8)
        self.menu_E.addAction(self.action_9)
        self.menu_F_2.addAction(self.action_13)
        self.menu_F_2.addAction(self.action_14)
        self.menu_F_2.addAction(self.action_15)
        self.menu_F_2.addAction(self.action_16)
        self.menu_L.addAction(self.action1pt)
        self.menu_L.addAction(self.action2pt)
        self.menu_L.addAction(self.action3pt)
        self.menu_L.addAction(self.action4pt)
        self.menu_L.addAction(self.action5pt)
        self.menu_L.addAction(self.action6pt)
        self.menu_T.addAction(self.menu_L.menuAction())
        self.menu_T.addAction(self.menu_F_2.menuAction())
        self.menu_T.addSeparator()
        self.menu_T.addAction(self.action_I)
        self.menu_T.addSeparator()
        self.menu_T.addAction(self.action_R)
        self.menu_T.addAction(self.action_Q)
        self.menu_T.addSeparator()
        self.menu_T.addAction(self.action_G)
        self.menu_S.addAction(self.action_6)
        self.menu_S.addAction(self.action_17)
        self.menu_H.addAction(self.action_4)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_T.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "파일경로"))
        self.label_2.setText(_translate("MainWindow", "파일이름"))
        self.pushButton.setText(_translate("MainWindow", "새 캡쳐"))
        self.pushButton_2.setText(_translate("MainWindow", "저장"))
        self.pushButton_3.setText(_translate("MainWindow", "복사"))
        self.pushButton_4.setText(_translate("MainWindow", "공유하기"))
        self.pushButton_5.setText(_translate("MainWindow", "지우개"))
        self.comboBox.setItemText(0, _translate("MainWindow", "펜"))
        self.comboBox.setItemText(1, _translate("MainWindow", "도형"))
        self.comboBox.setItemText(2, _translate("MainWindow", "잉크색"))
        self.menu_F.setTitle(_translate("MainWindow", "파일(F)"))
        self.menu_E.setTitle(_translate("MainWindow", "편집(E)"))
        self.menu_T.setTitle(_translate("MainWindow", "도구(T)"))
        self.menu_F_2.setTitle(_translate("MainWindow", "도형(F)"))
        self.menu_L.setTitle(_translate("MainWindow", "펜(L)"))
        self.menu_S.setTitle(_translate("MainWindow", "공유하기(S)"))
        self.menu_H.setTitle(_translate("MainWindow", "도움말(H)"))
        self.action.setText(_translate("MainWindow", "새 캡처"))
        self.action_2.setText(_translate("MainWindow", "저장"))
        self.action_3.setText(_translate("MainWindow", "다른 이름으로 저장"))
        self.action_5.setText(_translate("MainWindow", "종료"))
        self.action_6.setText(_translate("MainWindow", "팀업 대화방선택"))
        self.action_7.setText(_translate("MainWindow", "실행취소"))
        self.action_8.setText(_translate("MainWindow", "다시실행"))
        self.action_9.setText(_translate("MainWindow", "복사"))
        self.action_I.setText(_translate("MainWindow", "잉크 색(I)"))
        self.action_R.setText(_translate("MainWindow", "지우개(R)"))
        self.action_Q.setText(_translate("MainWindow", "모든 잉크 지우기(Q)"))
        self.action_G.setText(_translate("MainWindow", "그림판으로 내보내기(G)"))
        self.action_13.setText(_translate("MainWindow", "선"))
        self.action_14.setText(_translate("MainWindow", "화살표"))
        self.action_15.setText(_translate("MainWindow", "사각형"))
        self.action_16.setText(_translate("MainWindow", "원"))
        self.action1pt.setText(_translate("MainWindow", "1pt"))
        self.action2pt.setText(_translate("MainWindow", "2pt"))
        self.action3pt.setText(_translate("MainWindow", "3pt"))
        self.action4pt.setText(_translate("MainWindow", "4pt"))
        self.action5pt.setText(_translate("MainWindow", "5pt"))
        self.action6pt.setText(_translate("MainWindow", "6pt"))
        self.action_17.setText(_translate("MainWindow", "팀업 로그인"))
        self.action_4.setText(_translate("MainWindow", "읽어보세요"))

import capture_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
