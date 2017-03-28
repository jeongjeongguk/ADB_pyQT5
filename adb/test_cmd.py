import ui, os

class myADB(object):
    def test(self):
        ui.Ui_MainWindow.fileDialog = ui.QtWidgets.QFileDialog()
        select = ui.Ui_MainWindow.fileDialog.getOpenFileUrl()
        path = str(select[0]).replace("PyQt5.QtCore.QUrl('file:///", "")
        path = path.replace("')", "")

        ui.Ui_MainWindow.setupUi.lineEdit = ui.QtWidgets.QLineEdit() #되긴하지만, 레퍼런스가 ui랑 다름
        ui.Ui_MainWindow.setupUi.lineEdit.setText(path)
        print(ui.Ui_MainWindow.setupUi.lineEdit.text())

        #ui.Ui_MainWindow.setupUi.lineEdit.text()
        #ui.Ui_MainWindow.test(path)

    def install(self):
        print(ui.Ui_MainWindow.setupUi.lineEdit.text())
        #ui.Ui_MainWindow.label.setText("설치중")
        path = ui.Ui_MainWindow.setupUi.lineEdit.text()
        adb_command_install = "adb install -r " + path

        os.system(adb_command_install)
        #ui.Ui_MainWindow.label.setText("설치완료")

        get_start_activity = "aapt dump badging " + path + " | FINDSTR launchable-activity"
        get_package_name = "aapt dump badging " + path + " | FINDSTR package"

        os.system(get_start_activity)
        os.system(get_package_name)

        # del_index = imsi_text.find("=")
        # print(del_index)
        # imsi_text = imsi_text[del_index:]

        # os.system("adb shell am start -n com.estsoft.alsongbeta/com.estsoft.alsong.SplashActivity")
        os.system("adb shell am start -n com.estsoft.teamuptest/com.estsoft.teamup.ui.login.LoginActivity")


if __name__ == "__main__":
    import sys
    app = ui.QtWidgets.QApplication(sys.argv)
    MainWindow = ui.QtWidgets.QMainWindow()
    UI = ui.Ui_MainWindow()
    UI.setupUi(MainWindow)
    ui.QtCore.QMetaObject.connectSlotsByName(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())