import sys, ctypes, os
src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
src_path = src_path_company if os.path.exists(src_path_company) else src_path_home
sys.path.insert(0, src_path)

import capture_ui_working
import adb_default
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QApplication, QLabel, QLineEdit, QGridLayout, QGraphicsScene, QGraphicsLineItem,QGraphicsView
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint, QRect
from PIL import Image, ImageQt
import win32com.shell.shell as win32shell
import paint
import logging

set_foreground_flag = 0x00001000
class SubWindow03(QtWidgets.QMainWindow, capture_ui_working.Ui_MainWindow, adb_default.defaultADB):
    def __init__(self, path, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.pathRoot = path
        self.setupUi(self)
        self.model = QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)
        self.indexRoot = self.model.index(self.model.rootPath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.connect()

        self.myPenWidth = 5
        self.myPenColor = Qt.blue
        # self.image = QImage()
        self.lastPoint = QPoint()
        self.scribbling = False

        self.click_positions = []

    def connect(self):
        self.treeView.doubleClicked.connect(self.on_treeView_clicked)

    def mousePressEvent(self, event):
        # https://doc.qt.io/qt-5/qmouseevent.html#QMouseEvent-3 참고할것.
        # import win32api
        # mouseX, mouseY = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

        if event.button() == Qt.LeftButton and self.scribbling == False:
            # print("왼쪽")
            # print(self._start)
            self._start = event.pos()
            # PyQt5.QtCore.QPoint(265, 92)
            print(self._start.x())

            # self._start = event.screenPos()
            self.scribbling = True
        elif event.button() == Qt.RightButton :
            print("오른쪽")
        elif event.button() == Qt.LeftButton and self.scribbling:
            # print("다음번 왼쪽클릭")
            # print(self._end)
            self._end = event.pos()
            # self._end = event.screenPos()
            self.drawLineTo(self._start, self._end)
            self.scribbling = False


    def drawLineTo(self, startPoint, endPoint):
        # self.xy = QtCore.QLineF(startPoint, endPoint)
        # self.scene.addLine(20,100,100,100)
        # self.scene.addRect(self.xy)

        # self.click_positions.append(QtCore.QPointF(self.scene.mapToScene(startPoint)))
        # self.click_positions.append(QtCore.QPointF(self.scene.mapToScene(endPoint)))
        pen = QPen(QtCore.Qt.red)
        repointX, repointY = 265, 92
        self.scene.addLine(QtCore.QLineF(startPoint.x() - repointX, startPoint.y() - repointY,
                                         endPoint.x() - repointX, endPoint.y() - repointY), pen)
        pass
        # painter = QPainter(self.image)
        # painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
        #                     Qt.RoundCap, Qt.RoundJoin))
        # self.modified = True
        #
        # rad = self.myPenWidth / 2 + 2
        # self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        # self.lastPoint = QPoint(endPoint)
        # print("done")

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.lineEdit_2.setText(fileName)
        self.lineEdit.setText(filePath)

        try:
            img = Image.open(filePath)
            self.display_image(img)
        except:
            ctypes.windll.user32.MessageBoxW(0, "이미지파일만 선택가능합니다.", "이미지만 편집가능", set_foreground_flag)

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(0,0,w,h,1)
        self.scene.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('FileView')
    testPath = "C:/Users/Jeongkuk/PycharmProjects/androidADB/src/"
    # ui = SubWindow03("C:\\")
    ui = SubWindow03(testPath)
    ui.show()
    sys.exit(app.exec_())