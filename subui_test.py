#--------------------------------------------------------
'''
현재 윈도우에 다른 윈도우를 그리는거
'pyqt5 python3 sub window' 으로 구글링 검색결과 참조
https://stackoverflow.com/questions/13517568/how-to-create-new-pyqt4-windows-from-an-existing-window
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import main_ui
import adb_command_ui


class Form1(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        # QtWidgets.__init__(self, parent)
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.ConnectedDevices.clicked.connect(self.handleButton)
        self.window2 = None

    def handleButton(self):
        if self.window2 is None:
            self.window2 = Form2(self)
        self.window2.show()

class Form2(QtWidgets.QWidget, adb_command_ui.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())

#--------------------------------------------------------
