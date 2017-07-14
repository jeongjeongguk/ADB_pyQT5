# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionSrc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icons/Option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.HelpSarting = QtWidgets.QWidget()
        self.HelpSarting.setObjectName("HelpSarting")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.HelpSarting)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.HelpSarting)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.HelpSarting, "")
        self.HelpUsing = QtWidgets.QWidget()
        self.HelpUsing.setObjectName("HelpUsing")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.HelpUsing)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 481, 461))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.HelpUsing, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Help"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. 다운로드한 zip파일을 압축해제후, 해당 경로를 path에 추가해주세요.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-  <a href=\"https://drive.google.com/open?id=0B2M8w6fAK2lKTm1lX1I1ZDV3Wlk\"><span style=\" text-decoration: underline; color:#0000ff;\">다운로드 링크</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. 연결될 USB 드라이버를 설치해주세요. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\">\n"
"<tr>\n"
"<td colspan=\"2\" style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans,sans-serif\'; font-size:13px;\">USB 설치</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans,sans-serif\'; font-size:13px;\">구글</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://goo.gl/b4uByh\"><span style=\" font-family:\'arial,sans,sans-serif\'; font-size:13px; text-decoration: underline; color:#0000ff;\">https://goo.gl/b4uByh</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans,sans-serif\'; font-size:13px;\">삼성</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://goo.gl/x6Drhh\"><span style=\" text-decoration: underline; color:#0000ff;\">https://goo.gl/x6Drhh</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans,sans-serif\'; font-size:13px;\">LG</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://goo.gl/GKGMxJ\"><span style=\" text-decoration: underline; color:#0000ff;\">https://goo.gl/GKGMxJ</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans,sans-serif\'; font-size:13px;\">OEM</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://goo.gl/eYSTEr\"><span style=\" font-family:\'arial,sans,sans-serif\'; text-decoration: underline; color:#0000ff;\">https://goo.gl/eYSTEr</span></a></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. 기기와 PC를 USB로 연결해주시고, </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">개발자모드에서 USB디버깅사용을 활성화해주세요.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/HelpStarting/icons/developer_option.jpg\" /><img src=\":/HelpStarting/icons/usb_debuging.jpg\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. 유틸을 재실행해주세요.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HelpSarting), _translate("Form", "최초실행시 설정안내"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[선택창에서 연결된 디바이스가 보이지 않을 경우]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt; USB 디버깅 설정이 활성화됐는지 확인해주세요.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt; USB 연결 설정을 미디어(MTP)에서 카메라(PTP)로 변경해봐주세요.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt; USB 케이블을 바꿔서 해봐주세요.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HelpUsing), _translate("Form", "사용방법 안내"))

import helpImages_rc
import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

