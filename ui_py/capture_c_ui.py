# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture_c.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/icons/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"  background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget::title {\n"
" height: 24px;\n"
" font-weight: bold;\n"
" color: #000000;\n"
" background: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.treeView = QtWidgets.QTreeView(self.tab)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_5.addWidget(self.treeView)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.treeView_2 = QtWidgets.QTreeView(self.tab_2)
        self.treeView_2.setObjectName("treeView_2")
        self.horizontalLayout_6.addWidget(self.treeView_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.treeView_3 = QtWidgets.QTreeView(self.tab_3)
        self.treeView_3.setObjectName("treeView_3")
        self.horizontalLayout_7.addWidget(self.treeView_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.treeView_4 = QtWidgets.QTreeView(self.tab_4)
        self.treeView_4.setStyleSheet("QTreeView::branch {\n"
"        background: palette(base);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"        background: cyan;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"        background: red;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"        background: blue;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        background: pink;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"        background: gray;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"        background: magenta;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"        background: green;\n"
"}\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(branch-more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(branch-end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image: url(branch-closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"        border-image: none;\n"
"        image: url(branch-open.png);\n"
"}")
        self.treeView_4.setObjectName("treeView_4")
        self.horizontalLayout_8.addWidget(self.treeView_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newCapture = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/icons/Capture_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newCapture.setIcon(icon1)
        self.newCapture.setIconSize(QtCore.QSize(25, 25))
        self.newCapture.setAutoRepeat(False)
        self.newCapture.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.newCapture.setAutoRaise(True)
        self.newCapture.setObjectName("newCapture")
        self.horizontalLayout.addWidget(self.newCapture)
        self.link2mspaint = QtWidgets.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/icons/mspaint_0001.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.link2mspaint.setIcon(icon2)
        self.link2mspaint.setIconSize(QtCore.QSize(25, 25))
        self.link2mspaint.setAutoRepeat(False)
        self.link2mspaint.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.link2mspaint.setAutoRaise(True)
        self.link2mspaint.setObjectName("link2mspaint")
        self.horizontalLayout.addWidget(self.link2mspaint)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_5)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setWhatsThis("")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.axWidget = QAxContainer.QAxWidget(self.tab_6)
        self.axWidget.setObjectName("axWidget")
        self.verticalLayout_5.addWidget(self.axWidget)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.action1pt.setCheckable(True)
        self.action1pt.setChecked(True)
        self.action1pt.setObjectName("action1pt")
        self.action2pt = QtWidgets.QAction(MainWindow)
        self.action2pt.setCheckable(True)
        self.action2pt.setObjectName("action2pt")
        self.action3pt = QtWidgets.QAction(MainWindow)
        self.action3pt.setCheckable(True)
        self.action3pt.setObjectName("action3pt")
        self.action4pt = QtWidgets.QAction(MainWindow)
        self.action4pt.setCheckable(True)
        self.action4pt.setObjectName("action4pt")
        self.action5pt = QtWidgets.QAction(MainWindow)
        self.action5pt.setCheckable(True)
        self.action5pt.setObjectName("action5pt")
        self.action6pt = QtWidgets.QAction(MainWindow)
        self.action6pt.setCheckable(True)
        self.action6pt.setObjectName("action6pt")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CaptureEdit"))
        self.label.setText(_translate("MainWindow", "파일경로"))
        self.label_2.setText(_translate("MainWindow", "파일이름"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "gif"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "etc"))
        self.newCapture.setText(_translate("MainWindow", "새 캡쳐"))
        self.link2mspaint.setText(_translate("MainWindow", "그림판"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "image"))
        self.axWidget.setProperty("control", _translate("MainWindow", "{6bf52a52-394a-11d3-b153-00c04f79faa6}"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "video"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "gif"))
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

from PyQt5 import QAxContainer
import capture_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

