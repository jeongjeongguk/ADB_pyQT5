import sys, ctypes, os
src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
src_path = src_path_company if os.path.exists(src_path_company) else src_path_home
sys.path.insert(0, src_path)

import capture_ui
import adb_default
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QApplication, QLabel, QLineEdit, QGridLayout, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageQt
import win32com.shell.shell as win32shell

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

    def connect(self):
        self.treeView.clicked.connect(self.on_treeView_clicked)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.lineEdit_2.setText(fileName)
        self.lineEdit.setText(filePath)

        # TODO: 실행하는거 말고, graphicView에 그리는걸로 변경필요
        # win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + filePath)
        try :
            img = Image.open(filePath)
            self.display_image(img)
        except:
            ctypes.windll.user32.MessageBoxW(0, "이미지파일만 선택가능합니다.", "이미지만 편집가능", set_foreground_flag)

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
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