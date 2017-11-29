# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installedList.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(342, 280))
        Form.setMaximumSize(QtCore.QSize(342, 280))
        Form.setBaseSize(QtCore.QSize(342, 204))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icons/1494232917_icon-trash-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 341, 265))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.StartApp = QtWidgets.QPushButton(self.layoutWidget)
        self.StartApp.setObjectName("StartApp")
        self.verticalLayout.addWidget(self.StartApp)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.MonkeyTest = QtWidgets.QPushButton(self.layoutWidget)
        self.MonkeyTest.setObjectName("MonkeyTest")
        self.verticalLayout.addWidget(self.MonkeyTest)
        self.DeveloperPage = QtWidgets.QPushButton(self.layoutWidget)
        self.DeveloperPage.setObjectName("DeveloperPage")
        self.verticalLayout.addWidget(self.DeveloperPage)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Application"))
        self.listWidget.setSortingEnabled(True)
        self.pushButton.setText(_translate("Form", "앱 삭제"))
        self.pushButton_2.setText(_translate("Form", "데이터삭제"))
        self.pushButton_3.setText(_translate("Form", "출시버전"))
        self.StartApp.setText(_translate("Form", "앱 시작"))
        self.pushButton_4.setText(_translate("Form", "리스트갱신"))
        self.pushButton_6.setText(_translate("Form", "버전확인"))
        self.MonkeyTest.setText(_translate("Form", "Monkey Test"))
        self.DeveloperPage.setText(_translate("Form", "개발자페이지"))
        self.pushButton_5.setText(_translate("Form", "도움말"))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

