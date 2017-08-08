import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 color dialog - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        openColorDialog(self)


def openColorDialog(self):
    color = QColorDialog.getColor()


    if color.isValid():
        print(color.name())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = App()
    main.resize(666, 333)
    main.move(app.desktop().screen().rect().center() - main.rect().center())
    main.show()

    sys.exit(app.exec_())