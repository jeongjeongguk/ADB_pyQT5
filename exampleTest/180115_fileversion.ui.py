# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileversion.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from win32api import GetFileVersionInfo, LOWORD, HIWORD
import os


x64_programfiles = "C:\\Program Files (x86)\\"
PROGRAMFILES = os.getenv('programfiles') +"\\"
PROGRAMDATA = os.getenv('programdata') +"\\"
APPDATA = os.getenv('appdata') + "\\"
ALUPDATE = "ESTsoft\\ALUpdate\\"
ALAUTH = "ESTsoft\\ALAUTH\\"
ALCM = "ESTsoft\\ALCM\\"
ESTSOFT = "ESTsoft\\"

CONFIRM_LIST_ALUPDATE = [
    ["AZMain.dll",""],
    ["ALUpdate.exe",""],
    ["ALUpdateEx.dll",""],
    ["ALUpExt.exe",""],
    ["ALUpProduct.exe",""],
    ["eausvc.exe",""],
    ["ko-KR.dll",""],
    ["unins000.exe",""],
    ["ezt.exe",""],
    ["ALAd.dll",""]
]

PROGRAMLIST = [
    "ALCapture\\",
    "ALDrive\\",
    "ALKeeper\\",
    "ALPDF\\",
    "ALSee\\",
    "ALSong\\",
    "ALToolBar\\",
    "ALZip\\"
]

CONFIRM_LIST_PROGRAMLIST = [
    ["ALUpdate.dll",""],
    ["ALCMProxy.dll",""],
    ["ALSTS.dll",""]
]
AUTHSERIAL_DLL = [["AuthSerial.dll",""]]
# DLL_LIST = []
# for i in range(0, len(PROGRAMLIST)):
#     DLL_LIST[i] = [PROGRAMLIST[i],CONFIRM_LIST_PROGRAMLIST,AUTHSERIAL_DLL]
DLL_LIST = {PROGRAMNAME: [CONFIRM_LIST_PROGRAMLIST, AUTHSERIAL_DLL] for PROGRAMNAME in PROGRAMLIST}
# print(DLL_LIST)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 686)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 321, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 350, 491, 301))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "AZMain.dll"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "ALUpdate.exe"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "ALUpdateEx.dll"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "ALUpExt.exe"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "ALUpProduct.exe"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "eausvc.exe"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "ko-KR.dll"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "unins000.exe"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "ezt.exe "))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "ALAd.dll"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "참고버전"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "확인버전"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "8.10.13.0"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "18.1.11.0"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "18.1.11.0"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "15.11.27.0"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "18.1.11.0"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "18.1.11.0"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "18.1.12.0"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "18.1.11.0"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Form", "16.7.29.1"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Form", "16.4.28.1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "참고버전"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "ALCapture"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "ALDrive"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "ALKeeper"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "ALPDF"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "ALSee"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("Form", "ALSong"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("Form", "ALToolBar"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("Form", "ALZip"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ALUpdate.dll"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ALCMProxy.dll"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "ALSTS.dll"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "AuthSerial.dll"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Form", "10.12.6.1"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("Form", "11.12.14.2"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("Form", "11.7.15.0"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("Form", "16.12.19.1"))
        # --------------------------------------------------------------------------------------------------------------
        # TODO : Func.
        # for j in range(0, len(CONFIRM_LIST_ALUPDATE)):
        #     # print(CONFIRM_LIST_ALUPDATE[j][1] )
        #     self.tableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(CONFIRM_LIST_ALUPDATE[j][1] ))
        # --------------------------------------------------------------------------------------------------------------
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)



class functions(object):
    @classmethod
    def get_version_number(cls,filename):
        try:
            info = GetFileVersionInfo(filename, "\\")
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)
        except:
            return "None"

    @classmethod
    def confirm_version(cls):
        # ==================================================================================================================
        print("=" * 5 + "[ {} ]".format(PROGRAMFILES + ALUPDATE) + "=" * 5)
        print("{}".format(PROGRAMFILES + ALUPDATE + CONFIRM_LIST_ALUPDATE[1][0]))
        for j in range(0, len(CONFIRM_LIST_ALUPDATE)):
            try:
                CONFIRM_LIST_ALUPDATE[j][1] = ".".join([str(i) for i in cls.get_version_number(
                    "{}".format(PROGRAMFILES + ALUPDATE + CONFIRM_LIST_ALUPDATE[j][0]))])

            except:
                CONFIRM_LIST_ALUPDATE[j][1] = "None"
            print("{} : ".format(CONFIRM_LIST_ALUPDATE[j][0]) + CONFIRM_LIST_ALUPDATE[j][1])
        # ==================================================================================================================
        print("=" * 5 + "[ {} ]".format(APPDATA + ALAUTH) + "=" * 5)
        try:
            AuthReg_exe = ".".join([str(i) for i in cls.get_version_number(
                "{}".format(APPDATA + ALAUTH + "AuthReg.exe"))])
        except:
            AuthReg_exe = "None"
        print("AuthReg.exe : " + AuthReg_exe)
        # ==================================================================================================================
        print("=" * 5 + "[ {} ]".format(PROGRAMDATA + ALCM) + "=" * 5)
        try:
            ALCMUpdate_exe = ".".join([str(i) for i in cls.get_version_number(
                "{}".format(PROGRAMDATA + ALCM + "ALCMUpdate.exe"))])
        except:
            ALCMUpdate_exe = "None"
        print("{} :   {}".format("ALCMUpdate.exe", ALCMUpdate_exe))
        # ==================================================================================================================
        for i in range(0, len(PROGRAMLIST)):
            if os.path.isdir("{}".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i])):
                print("=" * 5 + "[ {} ]".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
                for j in range(0, len(CONFIRM_LIST_PROGRAMLIST)):
                    try:
                        DLL_LIST[PROGRAMLIST[i]][0][j][1] = ".".join([str(i) for i in cls.get_version_number(
                            "{}".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i] + CONFIRM_LIST_PROGRAMLIST[j][0]))])
                        # print("test : " + str(DLL_LIST[PROGRAMLIST[i]][0][i][1]))
                        # print(DLL_LIST[PROGRAMLIST[i]][0])
                    except:
                        pass
                    if CONFIRM_LIST_PROGRAMLIST[j][1] != "N.o.n.e":
                        print("{} :   {}".format(CONFIRM_LIST_PROGRAMLIST[j][0], CONFIRM_LIST_PROGRAMLIST[j][1]))
            else:
                print("=" * 5 + "[ {} ]".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
                print(PROGRAMLIST[i] + "'s foleder isn't Exist")


class refresh(Ui_Form):
    functions.confirm_version()
    def confirmedVersion(self):
        # --------------------------------------------------------------------------------------------------------------
        for j in range(0, len(CONFIRM_LIST_ALUPDATE)):
            # print(CONFIRM_LIST_ALUPDATE[j][1] )
            self.tableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(CONFIRM_LIST_ALUPDATE[j][1] ))
        # --------------------------------------------------------------------------------------------------------------
        for i in range(1, len(PROGRAMLIST)+1):
            print(PROGRAMLIST[i-1] + " : " + str(DLL_LIST[PROGRAMLIST[i-1]]))
            # ALCapture\ : [[['ALUpdate.dll', 'None'], ['ALCMProxy.dll', 'None'], ['ALSTS.dll', 'None']], [['AuthSerial.dll', '']]]
            for j in range(0, len(CONFIRM_LIST_PROGRAMLIST)):
                self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(DLL_LIST[PROGRAMLIST[i-1]][0][j][1]  ))

if __name__ == "__main__":
    import sys
    # functions.confirm_version()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    # setText Func.
    refresh.confirmedVersion(ui)


    Form.show()
    sys.exit(app.exec_())


    # ==================================================================================================================
    # for i in range(0, len(PROGRAMLIST)):
    #     if os.path.isdir("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i])) :
    #         print("=" * 5 + "[ {} ]".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #         for i in range(0, len(PROGRAMLIST)):
    #             # print("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i] + AUTHSERIAL_DLL[i][0]))
    #             if os.path.isfile("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i] + AUTHSERIAL_DLL[i][0])) :
    #                 print("=" * 5 + "[ {} ]".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #             else :
    #                 print("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #             try:
    #                 # AUTHSERIAL_DLL[i][1] = ".".join([str(i) for i in get_version_number(
    #                 #     "{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i] + AUTHSERIAL_DLL[i][0]))])
    #                 pass
    #             except:
    #                 pass
    #             # if AUTHSERIAL_DLL[i][1] != "N.o.n.e":
    #             #     print("{} :   {}".format(AUTHSERIAL_DLL[i][0],AUTHSERIAL_DLL[i][1]))
    #     else :
    #         print("=" * 5 + "[ {} ]".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #         print(PROGRAMLIST[i] + "'s foleder isn't Exist")
    # ==================================================================================================================

    # os.system("pause")
