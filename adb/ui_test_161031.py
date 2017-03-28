from PyQt5 import QtCore, QtGui, QtWidgets, uic

form_class = uic.loadUiType("adb_test1.ui")[0]  # Load the UI

class Ui_MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.test)    #   to the buttons
        self.pushButton.clicked.connect(self.install) #   to the buttons