import sys
import adb_default
import main_ui
from PyQt5 import QtWidgets


class MainWindow(main_ui.Ui_MainWindow, adb_default.default):
    def __init__(self):
        super(self.__class__, self).__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())