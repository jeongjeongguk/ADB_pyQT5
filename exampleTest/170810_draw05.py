from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PIL import Image, ImageQt
from PyQt5.QtGui import QPixmap
class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.scene)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
        img = Image.open('altools.png')
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        self.pixMap = QPixmap.fromImage(self.imgQ)
        self.pixmap_item = QtWidgets.QGraphicsPixmapItem(self.pixMap)
        # self.scene.addPixmap(self.pixMap)
        self.graphicsView.fitInView(0, 0, w, h, 1)
        self.scene.update()

        self.pixMap.mousePressEvent = self.pixelSelect
        self.click_positions = []

    def pixelSelect(self, event):
        self.click_positions.append(event.pos())
        if len(self.click_positions) < 4:
            return
        pen = QtGui.QPen(QtCore.Qt.red)
        self.scene.addPolygon(QtGui.QPolygonF(self.click_positions), pen)
        for point in self.click_positions:
            self.scene.addEllipse(point.x(), point.y(), 2, 2, pen)
        self.click_positions = []


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.resize(640, 480)
    widget.show()
    sys.exit(app.exec_())