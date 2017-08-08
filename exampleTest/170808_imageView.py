import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        paths = os.getcwd()
        paths = paths.replace("\\", "\\\\")
        # filename = "altools.png"
        filename = "170725_134312_SM-G925S_6.0.1_API_23.jpg"
        open2file = paths + "\\\\" +  filename
        pixmap = QPixmap(filename)
        pixmap4 = pixmap.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap4)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())