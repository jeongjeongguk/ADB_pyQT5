# https://stackoverflow.com/questions/28080257/how-does-qgraphicsview-receive-mouse-move-events
from PyQt5 import QtCore, QtGui, QtWidgets

class MyGraphicsView(QtWidgets.QGraphicsView):

    def __init__(self, parent):
        QtWidgets.QGraphicsView.__init__(self, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent: pos {}'.format(event.pos()))

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.graphicsView = MyGraphicsView(self)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.graphicsView)

app = QtWidgets.QApplication([])
window = Window()
window.show()
window.resize(200, 100)
app.exec_()