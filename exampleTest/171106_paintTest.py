
from PyQt5 import QtGui, QtCore
from win32api import

class test():
    def paint(self):
        # convert image  file into pixmap
        self.pixmap_image = QtGui.QPixmap(self.filename)

        # create painter instance with pixmap
        self.painterInstance = QtGui.QPainter(self.pixmap_image)

        # set rectangle color and thickness
        self.penRectangle = QtGui.QPen(QtCore.Qt.red)
        self.penRedBorder.setWidth(3)

        # draw rectangle on painter
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(xPos,yPos,xLen,yLen)

        # set pixmap onto the label widget
        self.ui.label_imageDisplay.setPixmap(self.pixmap_image)
        self.ui.label_imageDisplay.show()