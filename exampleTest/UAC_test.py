import ctypes
import os
import sys

this = os.path.abspath(sys.argv[0])


class UAC:
    def __init__(self):
        try:
            self.UACStatus = ctypes.windll.shell32.IsUserAnAdmin()
        except Exception as error:
            print("Unable to retrieve UAC Elevation level: %s" % error)
            self.UACStatus = 0

    def get(self):
        print("UAC Level: %s" % self.UACStatus)
        return bool(self.UACStatus)

    def set(self):
        if not self.get():
            try:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", this, "", None, 1)
            except Exception as error:
                print("Unable to request UAC Elevation: %s" % error)


if __name__ == "__main__":
    print(this)
    Elevation = UAC()
    Elevation.set()