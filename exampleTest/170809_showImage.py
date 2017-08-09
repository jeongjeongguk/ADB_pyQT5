import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt,ImageEnhance
# import ImageQt
# import ImageEnhance
import time

class TestWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.button = QtWidgets.QPushButton("Do test")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.button.clicked.connect(self.do_test)

    def do_test(self):
        # img = Image.open('altools.png')
        img = Image.open('170725_134312_SM-G925S_6.0.1_API_23.png')
        # 아래코드는 뭐 밝기 조절하는거 같다 삭제
        # enhancer = ImageEnhance.Brightness(img)
        # for i in range(1, 8):
        #     img = enhancer.enhance(i)
        #     self.display_image(img)
        #     QtCore.QCoreApplication.processEvents()  # let Qt do his work
        #     time.sleep(0.5)
        self.display_image(img)

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.view.fitInView(0,0,w,h,1)
        self.scene.update()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = TestWidget()
    widget.resize(640, 480)
    widget.show()

    sys.exit(app.exec_())