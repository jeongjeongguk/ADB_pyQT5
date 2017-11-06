import sys, ctypes, os
currentPaths = os.getcwd()
currentPathsSet = currentPaths.replace("src","ui_py")
sys.path.insert(0, currentPathsSet)

import capture_ui
import adb_default
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QApplication, QLabel, QLineEdit, QGridLayout, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir, Qt
from PIL import Image, ImageQt
import win32com.shell.shell as win32shell
import consts_string

class SubWindow03(QtWidgets.QMainWindow, capture_ui.Ui_MainWindow, adb_default.defaultADB):
    def __init__(self, path, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.pathRoot = path
        self.setupUi(self)
        paths = self.pathRoot
        # Tab : [image]
        self.model = QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)
        self.model.setFilter(QDir.Files) # Display only files
        # self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.AllEntries ) # Display ALL.
        filter_jpg = (None, "*.jpg")
        self.model.setNameFilters(filter_jpg)
        self.indexRoot = self.model.index(self.model.rootPath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(1, Qt.AscendingOrder)

        # Tab : [mp4]
        self.model2 = QFileSystemModel(self)
        self.model2.setRootPath(self.pathRoot)
        self.model2.setFilter(QDir.Files)
        filter_mp4 = (None, "*.mp4")
        self.model2.setNameFilters(filter_mp4)
        self.indexRoot = self.model2.index(self.model2.rootPath())
        self.treeView_2.setModel(self.model2)
        self.treeView_2.setRootIndex(self.indexRoot)
        self.treeView_2.setSortingEnabled(True)
        self.treeView_2.sortByColumn(1, Qt.AscendingOrder)

        # Tab : [gif]
        self.model3 = QFileSystemModel(self)
        self.model3.setRootPath(self.pathRoot)
        self.model3.setFilter(QDir.Files)
        filter_gif = (None, "*.gif")
        self.model3.setNameFilters(filter_gif)
        self.indexRoot = self.model3.index(self.model3.rootPath())
        self.treeView_3.setModel(self.model3)
        self.treeView_3.setRootIndex(self.indexRoot)
        self.treeView_3.setSortingEnabled(True)
        self.treeView_3.sortByColumn(1, Qt.AscendingOrder)

        # Tab : [etc]
        self.model4 = QFileSystemModel(self)
        self.model4.setRootPath(self.pathRoot)
        self.model4.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.AllEntries ) # Display ALL.
        self.indexRoot = self.model4.index(self.model4.rootPath())
        self.treeView_4.setModel(self.model4)
        self.treeView_4.setRootIndex(self.indexRoot)
        self.treeView_4.setSortingEnabled(True)
        self.treeView_4.sortByColumn(1, Qt.AscendingOrder)

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.connect()

    def connect(self):
        self.treeView.clicked.connect(self.on_treeView_clicked)
        self.newCapture.clicked.connect(self.call_capture2image)
        self.link2mspaint.clicked.connect(self.call_mspaint2image)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.lineEdit_2.setText(fileName)
        self.lineEdit.setText(filePath)
        # file 실행시, 아래 커맨드 사용
        # win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + filePath)
        #
        try :
            img = Image.open(filePath)
            self.display_image(img)
        except:
            ctypes.windll.user32.MessageBoxW(0, "이미지파일만 선택가능합니다.", "이미지만 편집가능", consts_string.show_flag.foreground.value)

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(0,0,w,h,1)
        self.scene.update()

    def call_capture2image(self):
        self.newCapture.setEnabled(False)
        self.capture2image()
        self.newCapture.setEnabled(True)

    def call_mspaint2image(self):
        filepath = self.lineEdit.text()
        filepath = filepath.replace("/","\\\\")
        os.system("mspaint "+filepath)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('FileView')
    testPath = "C:/Users/Jeongkuk/PycharmProjects/androidADB/src/"
    # ui = SubWindow03("C:\\")
    ui = SubWindow03(testPath)
    ui.show()
    sys.exit(app.exec_())