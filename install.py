import os, time
import subprocess as cmd

class default(object):
    def __init__(self):
        self.filepath = ""
        self.packageName = ""
        self.startActivity = ""

    def check_connect(self):
        os.system("adb devices")

    def install_apk(self, filepath):
        os.chdir("./apks")
        os.system("adb install " + filepath)
        self.run_apk(filepath)

    @classmethod
    def run_info(cls, filepath):
        cls.filepath = filepath
        if os.getcwd() != "C:\\Users\\Jeongkuk\\PycharmProjects\\alsongAndroid\\apks" : os.chdir("./apks")
        test = cmd.check_output("aapt dump badging " + filepath + " | findstr launchable",
                                stderr=cmd.STDOUT, shell=True)
        cls.startActivity = test.decode("utf-8").split(" ")[1].split("'")[1]
        test = cmd.check_output("aapt dump badging " + filepath + " | findstr package",
                                stderr=cmd.STDOUT, shell=True)
        cls.packageName = test.decode("utf-8").split(" ")[1].split("'")[1]

    @classmethod
    def run_apk(cls,filepath):
        cls.run_info(filepath)
        os.system("adb shell am start -n " + cls.packageName +"/"+cls.startActivity)

    @classmethod
    def uninstall_apk(cls,filepath):
        cls.run_info(filepath)
        os.system("adb uninstall " + cls.packageName)

    @classmethod
    def reinstall_apk(cls, filepath):
        cls.run_info(filepath)
        os.system("adb install -r " + filepath)
        cls.run_apk(filepath)

    def adb_kill(self):
        os.system("adb kill-server")
        self.adb_restrat()
        self.check_connect()

    def adb_restrat(self):
        os.system("adb start-server")

if __name__ == "__main__":
    filepath = "alsong_4.0.0.11_7cha.apk"
    test = default()
    #test.run_info(filepath)
    #test.adb_kill()
    #test.install_apk(filepath)
    #test.run_apk(filepath)
    test.reinstall_apk(filepath)