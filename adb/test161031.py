import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

form_class = uic.loadUiType("adb_test1.ui")[0]

class MyWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUi.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.btn_clicked)

    def btn_clicked(self):
        text = self.lineEdit.text()
        self.label.setText(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()