# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUI_working2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
#TODO : setContentsMargins(0,0,0,0) -> (10, 10, 10, 10)
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 574)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.device = QtWidgets.QDockWidget(MainWindow)
        self.device.setMinimumSize(QtCore.QSize(151, 212))
        self.device.setMaximumSize(QtCore.QSize(200, 600))
        self.device.setStyleSheet("")
        self.device.setObjectName("device")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.TBRefresh_2 = QtWidgets.QToolButton(self.dockWidgetContents)
        self.TBRefresh_2.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh_2.setAutoRepeat(False)
        self.TBRefresh_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh_2.setAutoRaise(True)
        self.TBRefresh_2.setObjectName("TBRefresh_2")
        self.horizontalLayout_6.addWidget(self.TBRefresh_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.usb = QtWidgets.QWidget()
        self.usb.setObjectName("usb")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.usb)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TWUSB = QtWidgets.QTableWidget(self.usb)
        self.TWUSB.setObjectName("TWUSB")
        self.TWUSB.setColumnCount(0)
        self.TWUSB.setRowCount(0)
        self.TWUSB.horizontalHeader().setCascadingSectionResizes(True)
        self.TWUSB.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.TWUSB, 0, 0, 1, 1)
        self.tabWidget.addTab(self.usb, "")
        self.wifi = QtWidgets.QWidget()
        self.wifi.setObjectName("wifi")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.wifi)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TWWIFI = QtWidgets.QTableWidget(self.wifi)
        self.TWWIFI.setObjectName("TWWIFI")
        self.TWWIFI.setColumnCount(0)
        self.TWWIFI.setRowCount(0)
        self.TWWIFI.horizontalHeader().setCascadingSectionResizes(True)
        self.TWWIFI.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.TWWIFI, 0, 0, 1, 1)
        self.tabWidget.addTab(self.wifi, "")
        self.all = QtWidgets.QWidget()
        self.all.setObjectName("all")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.all)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TWALL = QtWidgets.QTableWidget(self.all)
        self.TWALL.setObjectName("TWALL")
        self.TWALL.setColumnCount(0)
        self.TWALL.setRowCount(0)
        self.TWALL.horizontalHeader().setCascadingSectionResizes(True)
        self.TWALL.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.TWALL, 0, 0, 1, 1)
        self.tabWidget.addTab(self.all, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.device.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.device)
        self.control = QtWidgets.QDockWidget(MainWindow)
        self.control.setMinimumSize(QtCore.QSize(587, 513))
        self.control.setObjectName("control")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_2.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.command = QtWidgets.QWidget()
        self.command.setObjectName("command")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.command)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.command)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TBRefresh = QtWidgets.QToolButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icons/icons8-restart-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBRefresh.setIcon(icon)
        self.TBRefresh.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh.setAutoRepeat(False)
        self.TBRefresh.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh.setAutoRaise(True)
        self.TBRefresh.setObjectName("TBRefresh")
        self.horizontalLayout_2.addWidget(self.TBRefresh)
        self.TBStart = QtWidgets.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icons/icons8-play-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBStart.setIcon(icon1)
        self.TBStart.setIconSize(QtCore.QSize(20, 20))
        self.TBStart.setAutoRepeat(False)
        self.TBStart.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart.setAutoRaise(True)
        self.TBStart.setObjectName("TBStart")
        self.horizontalLayout_2.addWidget(self.TBStart)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TBStart_2 = QtWidgets.QToolButton(self.frame)
        self.TBStart_2.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_2.setAutoRepeat(False)
        self.TBStart_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_2.setAutoRaise(True)
        self.TBStart_2.setObjectName("TBStart_2")
        self.horizontalLayout.addWidget(self.TBStart_2)
        self.TBStart_3 = QtWidgets.QToolButton(self.frame)
        self.TBStart_3.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_3.setAutoRepeat(False)
        self.TBStart_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_3.setAutoRaise(True)
        self.TBStart_3.setObjectName("TBStart_3")
        self.horizontalLayout.addWidget(self.TBStart_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.LDelete = QtWidgets.QLabel(self.frame)
        self.LDelete.setInputMethodHints(QtCore.Qt.ImhNone)
        self.LDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.LDelete.setObjectName("LDelete")
        self.verticalLayout.addWidget(self.LDelete)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.TBStart_4 = QtWidgets.QToolButton(self.frame)
        self.TBStart_4.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_4.setAutoRepeat(False)
        self.TBStart_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_4.setAutoRaise(True)
        self.TBStart_4.setObjectName("TBStart_4")
        self.gridLayout_9.addWidget(self.TBStart_4, 0, 0, 1, 1)
        self.CBactivity = QtWidgets.QComboBox(self.frame)
        self.CBactivity.setObjectName("CBactivity")
        self.CBactivity.addItem("")
        self.CBactivity.addItem("")
        self.gridLayout_9.addWidget(self.CBactivity, 0, 1, 1, 1)
        self.LActivity = QtWidgets.QLabel(self.frame)
        self.LActivity.setObjectName("LActivity")
        self.gridLayout_9.addWidget(self.LActivity, 1, 0, 1, 1)
        self.CBcheck = QtWidgets.QComboBox(self.frame)
        self.CBcheck.setObjectName("CBcheck")
        self.CBcheck.addItem("")
        self.CBcheck.addItem("")
        self.gridLayout_9.addWidget(self.CBcheck, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_9)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TBScreen = QtWidgets.QToolButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/icons/Capture_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBScreen.setIcon(icon2)
        self.TBScreen.setIconSize(QtCore.QSize(20, 20))
        self.TBScreen.setAutoRepeat(False)
        self.TBScreen.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBScreen.setAutoRaise(True)
        self.TBScreen.setObjectName("TBScreen")
        self.horizontalLayout_3.addWidget(self.TBScreen)
        self.TBRecord = QtWidgets.QToolButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/icons/Capture_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBRecord.setIcon(icon3)
        self.TBRecord.setIconSize(QtCore.QSize(20, 20))
        self.TBRecord.setAutoRepeat(False)
        self.TBRecord.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRecord.setAutoRaise(True)
        self.TBRecord.setObjectName("TBRecord")
        self.horizontalLayout_3.addWidget(self.TBRecord)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.TWApplist = QtWidgets.QTableWidget(self.command)
        self.TWApplist.setObjectName("TWApplist")
        self.TWApplist.setColumnCount(0)
        self.TWApplist.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.TWApplist)
        self.TWApplist_2 = QtWidgets.QTreeView(self.command)
        self.TWApplist_2.setObjectName("TWApplist_2")
        self.horizontalLayout_5.addWidget(self.TWApplist_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget_2.addTab(self.command, "")
        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.test)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.TBRefresh_3 = QtWidgets.QToolButton(self.test)
        self.TBRefresh_3.setIcon(icon)
        self.TBRefresh_3.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh_3.setAutoRepeat(False)
        self.TBRefresh_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh_3.setAutoRaise(True)
        self.TBRefresh_3.setObjectName("TBRefresh_3")
        self.horizontalLayout_7.addWidget(self.TBRefresh_3)
        self.TBStart_5 = QtWidgets.QToolButton(self.test)
        self.TBStart_5.setIcon(icon1)
        self.TBStart_5.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_5.setAutoRepeat(False)
        self.TBStart_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_5.setAutoRaise(True)
        self.TBStart_5.setObjectName("TBStart_5")
        self.horizontalLayout_7.addWidget(self.TBStart_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.label = QtWidgets.QLabel(self.test)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.line_4 = QtWidgets.QFrame(self.test)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_10.addWidget(self.line_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.TBRefresh_4 = QtWidgets.QToolButton(self.test)
        self.TBRefresh_4.setIcon(icon)
        self.TBRefresh_4.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh_4.setAutoRepeat(False)
        self.TBRefresh_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh_4.setAutoRaise(True)
        self.TBRefresh_4.setObjectName("TBRefresh_4")
        self.horizontalLayout_8.addWidget(self.TBRefresh_4)
        self.TBRefresh_5 = QtWidgets.QToolButton(self.test)
        self.TBRefresh_5.setIcon(icon)
        self.TBRefresh_5.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh_5.setAutoRepeat(False)
        self.TBRefresh_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh_5.setAutoRaise(True)
        self.TBRefresh_5.setObjectName("TBRefresh_5")
        self.horizontalLayout_8.addWidget(self.TBRefresh_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_2 = QtWidgets.QLabel(self.test)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.line_5 = QtWidgets.QFrame(self.test)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_10.addWidget(self.line_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.TBRefresh_7 = QtWidgets.QToolButton(self.test)
        self.TBRefresh_7.setIcon(icon)
        self.TBRefresh_7.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh_7.setAutoRepeat(False)
        self.TBRefresh_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh_7.setAutoRaise(True)
        self.TBRefresh_7.setObjectName("TBRefresh_7")
        self.horizontalLayout_9.addWidget(self.TBRefresh_7)
        self.TBRefresh_6 = QtWidgets.QToolButton(self.test)
        self.TBRefresh_6.setIcon(icon)
        self.TBRefresh_6.setIconSize(QtCore.QSize(20, 20))
        self.TBRefresh_6.setAutoRepeat(False)
        self.TBRefresh_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBRefresh_6.setAutoRaise(True)
        self.TBRefresh_6.setObjectName("TBRefresh_6")
        self.horizontalLayout_9.addWidget(self.TBRefresh_6)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.stackedWidget = QtWidgets.QStackedWidget(self.test)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page_Batch = QtWidgets.QWidget()
        self.Page_Batch.setObjectName("Page_Batch")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Page_Batch)
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.TBStart_6 = QtWidgets.QToolButton(self.Page_Batch)
        self.TBStart_6.setIcon(icon1)
        self.TBStart_6.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_6.setAutoRepeat(False)
        self.TBStart_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_6.setAutoRaise(True)
        self.TBStart_6.setObjectName("TBStart_6")
        self.verticalLayout_8.addWidget(self.TBStart_6)
        self.TBStart_7 = QtWidgets.QToolButton(self.Page_Batch)
        self.TBStart_7.setIcon(icon1)
        self.TBStart_7.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_7.setAutoRepeat(False)
        self.TBStart_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_7.setAutoRaise(True)
        self.TBStart_7.setObjectName("TBStart_7")
        self.verticalLayout_8.addWidget(self.TBStart_7)
        self.TBStart_8 = QtWidgets.QToolButton(self.Page_Batch)
        self.TBStart_8.setIcon(icon1)
        self.TBStart_8.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_8.setAutoRepeat(False)
        self.TBStart_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_8.setAutoRaise(True)
        self.TBStart_8.setObjectName("TBStart_8")
        self.verticalLayout_8.addWidget(self.TBStart_8)
        self.TBStart_9 = QtWidgets.QToolButton(self.Page_Batch)
        self.TBStart_9.setIcon(icon1)
        self.TBStart_9.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_9.setAutoRepeat(False)
        self.TBStart_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_9.setAutoRaise(True)
        self.TBStart_9.setObjectName("TBStart_9")
        self.verticalLayout_8.addWidget(self.TBStart_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        self.listView = QtWidgets.QListView(self.Page_Batch)
        self.listView.setObjectName("listView")
        self.horizontalLayout_11.addWidget(self.listView)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.stackedWidget.addWidget(self.Page_Batch)
        self.Page_Transfer = QtWidgets.QWidget()
        self.Page_Transfer.setObjectName("Page_Transfer")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.Page_Transfer)
        self.horizontalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.treeView = QtWidgets.QTreeView(self.Page_Transfer)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_10.addWidget(self.treeView)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.TBStart_11 = QtWidgets.QToolButton(self.Page_Transfer)
        self.TBStart_11.setIcon(icon1)
        self.TBStart_11.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_11.setAutoRepeat(False)
        self.TBStart_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_11.setAutoRaise(True)
        self.TBStart_11.setObjectName("TBStart_11")
        self.horizontalLayout_12.addWidget(self.TBStart_11)
        self.TBStart_10 = QtWidgets.QToolButton(self.Page_Transfer)
        self.TBStart_10.setIcon(icon1)
        self.TBStart_10.setIconSize(QtCore.QSize(20, 20))
        self.TBStart_10.setAutoRepeat(False)
        self.TBStart_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.TBStart_10.setAutoRaise(True)
        self.TBStart_10.setObjectName("TBStart_10")
        self.horizontalLayout_12.addWidget(self.TBStart_10)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.treeView_2 = QtWidgets.QTreeView(self.Page_Transfer)
        self.treeView_2.setObjectName("treeView_2")
        self.verticalLayout_10.addWidget(self.treeView_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_10)
        self.stackedWidget.addWidget(self.Page_Transfer)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget_2.addTab(self.test, "")
        self.option = QtWidgets.QWidget()
        self.option.setObjectName("option")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.option)
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.option)
        self.tabWidget_3.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_3.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_30.addWidget(self.label_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_15.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_15.addWidget(self.toolButton)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_15)
        self.verticalLayout_17.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMinimumSize(QtCore.QSize(30, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_31.addWidget(self.label_4)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_12.addWidget(self.radioButton)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setAutoExclusive(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_14.addWidget(self.radioButton_2)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_14.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_31.addLayout(self.verticalLayout_12)
        self.verticalLayout_17.addLayout(self.horizontalLayout_31)
        spacerItem2 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem2)
        self.horizontalLayout_32.addLayout(self.verticalLayout_17)
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_18.addWidget(self.label_6)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_16.addWidget(self.lineEdit_2)
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_16.addWidget(self.toolButton_2)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_16)
        self.verticalLayout_20.addLayout(self.horizontalLayout_18)
        spacerItem3 = QtWidgets.QSpacerItem(519, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem3)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_15.addWidget(self.label_7)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_19.addWidget(self.label_5)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setAutoExclusive(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_13.addWidget(self.radioButton_3)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setAutoExclusive(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_17.addWidget(self.radioButton_4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_17.addWidget(self.spinBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19.addLayout(self.verticalLayout_13)
        self.verticalLayout_15.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_22.addLayout(self.verticalLayout_15)
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_22.addWidget(self.line_6)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setMinimumSize(QtCore.QSize(50, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_20.addWidget(self.label_8)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setAutoExclusive(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_14.addWidget(self.radioButton_5)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_6.setAutoExclusive(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_21.addWidget(self.radioButton_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_21.addWidget(self.spinBox_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem5)
        self.verticalLayout_14.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20.addLayout(self.verticalLayout_14)
        self.verticalLayout_16.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_22.addLayout(self.verticalLayout_16)
        self.verticalLayout_20.addLayout(self.horizontalLayout_22)
        spacerItem6 = QtWidgets.QSpacerItem(519, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem6)
        self.horizontalLayout_34.addLayout(self.verticalLayout_20)
        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_7 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_7.setGeometry(QtCore.QRect(20, 90, 210, 60))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_29.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_7)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/if_Rounded-06_2024632.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_29.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_7)
        self.pushButton_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/Option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_29.addWidget(self.pushButton_3)
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 307, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMaximumSize(QtCore.QSize(18, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_26.addWidget(self.label_11)
        self.comboBox_inputID = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_inputID.setMinimumSize(QtCore.QSize(150, 20))
        self.comboBox_inputID.setEditable(True)
        self.comboBox_inputID.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_inputID.setObjectName("comboBox_inputID")
        self.horizontalLayout_26.addWidget(self.comboBox_inputID)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.radioButton_real = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_real.setObjectName("radioButton_real")
        self.horizontalLayout_25.addWidget(self.radioButton_real)
        self.radioButton_test = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_test.setChecked(True)
        self.radioButton_test.setObjectName("radioButton_test")
        self.horizontalLayout_25.addWidget(self.radioButton_test)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem7)
        self.verticalLayout_18.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_28.addWidget(self.label_12)
        self.lineEdit_inputPW = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_inputPW.sizePolicy().hasHeightForWidth())
        self.lineEdit_inputPW.setSizePolicy(sizePolicy)
        self.lineEdit_inputPW.setMinimumSize(QtCore.QSize(150, 20))
        self.lineEdit_inputPW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_inputPW.setObjectName("lineEdit_inputPW")
        self.horizontalLayout_28.addWidget(self.lineEdit_inputPW)
        self.horizontalLayout_27.addLayout(self.horizontalLayout_28)
        self.pushButton_login = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_27.addWidget(self.pushButton_login)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem8)
        self.verticalLayout_18.addLayout(self.horizontalLayout_27)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.verticalLayout_11.addWidget(self.tabWidget_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 207, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem9)
        self.tabWidget_2.addTab(self.option, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.log)
        self.horizontalLayout_33.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_10 = QtWidgets.QLabel(self.log)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_23.addWidget(self.label_10)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.log)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_24.addWidget(self.lineEdit_3)
        self.toolButton_3 = QtWidgets.QToolButton(self.log)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_24.addWidget(self.toolButton_3)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)
        self.verticalLayout_19.addLayout(self.horizontalLayout_23)
        self.textBrowser = QtWidgets.QTextBrowser(self.log)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_19.addWidget(self.textBrowser)
        self.horizontalLayout_33.addLayout(self.verticalLayout_19)
        self.tabWidget_2.addTab(self.log, "")
        self.gridLayout_8.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.control.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.control)
        self.actionDevice = QtWidgets.QAction(MainWindow)
        self.actionDevice.setObjectName("actionDevice")
        self.actionControl_ADB = QtWidgets.QAction(MainWindow)
        self.actionControl_ADB.setObjectName("actionControl_ADB")
        self.actionRead_Me = QtWidgets.QAction(MainWindow)
        self.actionRead_Me.setObjectName("actionRead_Me")
        self.menuView.addAction(self.actionDevice)
        self.menuView.addAction(self.actionControl_ADB)
        self.menuHelp.addAction(self.actionRead_Me)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.device.setWindowTitle(_translate("MainWindow", "  Device"))
        self.TBRefresh_2.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usb), _translate("MainWindow", "USB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wifi), _translate("MainWindow", "WiFi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all), _translate("MainWindow", "ALL"))
        self.control.setWindowTitle(_translate("MainWindow", "  Control ADB"))
        self.TBRefresh.setText(_translate("MainWindow", "Refresh"))
        self.TBStart.setText(_translate("MainWindow", "Start"))
        self.TBStart_2.setText(_translate("MainWindow", "APP"))
        self.TBStart_3.setText(_translate("MainWindow", "Data"))
        self.LDelete.setText(_translate("MainWindow", "Delete"))
        self.TBStart_4.setText(_translate("MainWindow", "GO"))
        self.CBactivity.setItemText(0, _translate("MainWindow", "Developer"))
        self.CBactivity.setItemText(1, _translate("MainWindow", "Permission"))
        self.LActivity.setText(_translate("MainWindow", "Activity"))
        self.CBcheck.setItemText(0, _translate("MainWindow", "Now"))
        self.CBcheck.setItemText(1, _translate("MainWindow", "App\'s "))
        self.TBScreen.setText(_translate("MainWindow", "Screen"))
        self.TBRecord.setText(_translate("MainWindow", "Record"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.command), _translate("MainWindow", "Command"))
        self.TBRefresh_3.setText(_translate("MainWindow", "New"))
        self.TBStart_5.setText(_translate("MainWindow", "Update"))
        self.label.setText(_translate("MainWindow", "Install"))
        self.TBRefresh_4.setText(_translate("MainWindow", "Appium"))
        self.TBRefresh_5.setText(_translate("MainWindow", "UIAuto..."))
        self.label_2.setText(_translate("MainWindow", "Another"))
        self.TBRefresh_7.setText(_translate("MainWindow", "Batch"))
        self.TBRefresh_6.setText(_translate("MainWindow", "Transfer"))
        self.TBStart_6.setText(_translate("MainWindow", "+ Add"))
        self.TBStart_7.setText(_translate("MainWindow", "- Del"))
        self.TBStart_8.setText(_translate("MainWindow", "~ Run"))
        self.TBStart_9.setText(_translate("MainWindow", "path"))
        self.TBStart_11.setText(_translate("MainWindow", "Down"))
        self.TBStart_10.setText(_translate("MainWindow", "UP"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.test), _translate("MainWindow", "Test"))
        self.label_3.setText(_translate("MainWindow", "Paths"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Size"))
        self.radioButton.setText(_translate("MainWindow", "Real [100%]"))
        self.radioButton_2.setText(_translate("MainWindow", "Custom [%]"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "Screen Capture"))
        self.label_6.setText(_translate("MainWindow", "Paths"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_7.setText(_translate("MainWindow", "[ MP4 ]"))
        self.label_5.setText(_translate("MainWindow", "Size"))
        self.radioButton_3.setText(_translate("MainWindow", "Real [100%]"))
        self.radioButton_4.setText(_translate("MainWindow", "Custom [%]"))
        self.label_9.setText(_translate("MainWindow", "[ Convert : MP4 -> GIF ]"))
        self.label_8.setText(_translate("MainWindow", "Size"))
        self.radioButton_5.setText(_translate("MainWindow", "Real [100%]"))
        self.radioButton_6.setText(_translate("MainWindow", "Custom [%]"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("MainWindow", "Record"))
        self.pushButton_2.setText(_translate("MainWindow", "Confirm"))
        self.label_11.setText(_translate("MainWindow", "ID  "))
        self.radioButton_real.setText(_translate("MainWindow", "R"))
        self.radioButton_test.setText(_translate("MainWindow", "T"))
        self.label_12.setText(_translate("MainWindow", "PW"))
        self.pushButton_login.setText(_translate("MainWindow", "로그인"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Teamup"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.option), _translate("MainWindow", "Option"))
        self.label_10.setText(_translate("MainWindow", "Paths"))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.log), _translate("MainWindow", "Log"))
        self.actionDevice.setText(_translate("MainWindow", "Device"))
        self.actionControl_ADB.setText(_translate("MainWindow", "Control ADB"))
        self.actionRead_Me.setText(_translate("MainWindow", "Read Me"))

import capture_rc
import icon_rc
import teamup_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

