import sys, ctypes, os
src_path_company = 'C:\\Users\Jeongkuk\PycharmProjects\\androidADB\\ui_py'
src_path_home = 'C:\\Users\Administrator\PycharmProjects\\androidADB\\ui_py'
src_path = src_path_company if os.path.exists(src_path_company) else src_path_home
sys.path.insert(0, src_path)

# import adb_command_ui
import adb_default
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QApplication, QLabel, QLineEdit, QGridLayout
import win32com.shell.shell as win32shell

class SubWindow03(QtWidgets.QMainWindow, adb_default.defaultADB):
    def __init__(self, path, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.pathRoot = path
        self.model = QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)
        self.indexRoot = self.model.index(self.model.rootPath())
        self.treeView = QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.labelFileName = QLabel(self)
        self.labelFileName.setText("File Name")

        self.lineEditFileName = QLineEdit(self)

        self.labelFilePath = QLabel(self)
        self.labelFilePath.setText("File Path")

        self.lineEditFilePath = QLineEdit(self)

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.labelFileName, 0, 0)
        self.gridLayout.addWidget(self.lineEditFileName, 0, 1)
        self.gridLayout.addWidget(self.labelFilePath, 1, 0)
        self.gridLayout.addWidget(self.lineEditFilePath, 1, 1)

        self.layout = QVBoxLayout(self)
        self.layout.addLayout(self.gridLayout)
        self.layout.addWidget(self.treeView)
        self.layout.setGeometry(QtCore.QRect(10, 10, 480, 480))

        self.setWindowFlags(
            QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        self.resize(500, 500)
        self.connect()

    def connect(self):
        self.treeView.clicked.connect(self.on_treeView_clicked)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.lineEditFileName.setText(fileName)
        self.lineEditFilePath.setText(filePath)
        win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + filePath)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('FileView')
    ui = SubWindow03("C:\\")
    ui.show()
    sys.exit(app.exec_())