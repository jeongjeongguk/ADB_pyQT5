import sys, ctypes, os
src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
src_path = src_path_company if os.path.exists(src_path_company) else src_path_home
sys.path.insert(0, src_path)

import capture_ui
import adb_default
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QApplication, QLabel, QLineEdit, QGridLayout, QGraphicsScene, QGraphicsLineItem,QGraphicsView
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QPainter
from PyQt5.QtCore import Qt
from PIL import Image, ImageQt
import win32com.shell.shell as win32shell
import paint

set_foreground_flag = 0x00001000
class SubWindow03(QtWidgets.QMainWindow, capture_ui.Ui_MainWindow, adb_default.defaultADB):
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

        self.scribbling = False

    def connect(self):
        self.treeView.doubleClicked.connect(self.on_treeView_clicked)

    def mousePressEvent(self, event):
        # https://doc.qt.io/qt-5/qmouseevent.html#QMouseEvent-3 참고할것.
        if event.button() == Qt.LeftButton and self.scribbling == False:
            # print("왼쪽")
            # print(self._start)
            self._start = event.pos()
            self.scribbling = True
        elif event.button() == Qt.RightButton :
            print("오른쪽")
        elif event.button() == Qt.LeftButton and self.scribbling:
            # print("다음번 왼쪽클릭")
            # print(self._end)
            self._end = event.pos()
            self.scribbling = False


    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                            Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = QPoint(endPoint)

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