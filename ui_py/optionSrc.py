import sys
import optionSrc_ui
from PyQt5 import QtWidgets, QtCore


class windowForm(QtWidgets.QMainWindow, optionSrc_ui.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect()

    def connect(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = windowForm()
    ui.setupUi(Main)
    ui.connect()
    Main.show()
    sys.exit(app.exec_())