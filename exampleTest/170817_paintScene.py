import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class myView(QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def drawBackground(self, painter, rect):
        # background_brush = QtGui.QBrush( QtGui.QColor(255,170,255), QtCore.Qt.SolidPattern)
        # painter.fillRect(rect, background_brush)
        # pen = QtGui.QPen(QtGui.QColor(46, 84, 255))
        pen = QtGui.QPen(QtCore.Qt.red)
        pen.setWidth(5)
        painter.setPen(pen)

        line1 = QtCore.QLineF(0,0,0,100)
        # line2 = QtCore.QLineF(0,100,100,100)
        # line3 = QtCore.QLineF(100,100,100,0)
        # line4 = QtCore.QLineF(100,0,0,0)
        # painter.drawLines([line1, line2, line3, line4])
        painter.drawLines([line1])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    scene = QtWidgets.QGraphicsScene()
    scene.addEllipse(0,0,100,100)

    view = myView(scene)
    view.show()
    view.centerOn(50,50)

    app.exec_()