import ui_test_161031

class A (object)   :
    def test(self):
        self.fileDialog = ui_test_161031.QtWidgets.QFileDialog()
        select = self.fileDialog.getOpenFileUrl()
        path = str(select[0]).replace("PyQt5.QtCore.QUrl('file:///", "")
        path = path.replace("')", "")
        .lineEdit.setText(path)
        print(path)


    def install(self):
        # print(self.lineEdit.text())
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

        # os.system("adb shell am start -n com.estsoft.alsongbeta/com.estsoft.alsong.SplashActivity")
        os.system("adb shell am start -n com.estsoft.teamuptest/com.estsoft.teamup.ui.login.LoginActivity")


