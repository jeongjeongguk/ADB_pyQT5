from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QGraphicsView, QApplication, QGraphicsScene, QPushButton, QVBoxLayout, QGraphicsLineItem

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.view = View(self)
        self.button = QPushButton('Clear View', self)
        self.button.clicked.connect(self.handleClearView)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.button)

    def handleClearView(self):
        self.view.scene().clear()

class View(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setScene(QGraphicsScene(self))
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))

    def mousePressEvent(self, event):
        self._start = event.pos()
        print("왼쪽버튼 누르고 : " + str(self._start))

    def mouseReleaseEvent(self, event):
        self._end = event.pos()
        print("왼쪽버튼 뗍니다 : " + str(self._end))
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(self._end))
        self.scene().addItem(
            QGraphicsLineItem(QtCore.QLineF(start, end)))
        # for point in (start, end):
        #     text = self.scene().addSimpleText(
        #         '(%d, %d)' % (point.x(), point.y()))
        #     text.setBrush(QtCore.Qt.blue)
        #     text.setPos(point)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())