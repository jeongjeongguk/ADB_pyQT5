import sip, os
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QFileSystemModel, QTreeView, QLabel, QLineEdit, QGridLayout, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self, path, parent=None):
        super(MyWindow, self).__init__(parent)

        # self.pathRoot = QtCore.QDir.rootPath()
        # print(self.pathRoot)
        self.pathRoot = path
        self.model = QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)

        self.indexRoot = self.model.index(self.model.rootPath())

        self.treeView = QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.clicked.connect(self.on_treeView_clicked)

        self.labelFileName = QLabel(self)
        self.labelFileName.setText("File Name:")

        self.lineEditFileName = QLineEdit(self)

        self.labelFilePath = QLabel(self)
        self.labelFilePath.setText("File Path:")

        self.lineEditFilePath = QLineEdit(self)

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.labelFileName, 0, 0)
        self.gridLayout.addWidget(self.lineEditFileName, 0, 1)
        self.gridLayout.addWidget(self.labelFilePath, 1, 0)
        self.gridLayout.addWidget(self.lineEditFilePath, 1, 1)

        self.layout = QVBoxLayout(self)
        self.layout.addLayout(self.gridLayout)
        self.layout.addWidget(self.treeView)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        # fileName = self.model.fileName(indexItem)
        # filePath = self.model.filePath(indexItem)
        #
        # self.lineEditFileName.setText(fileName)
        # self.lineEditFilePath.setText(filePath)

        filePath = self.model.filePath(indexItem)
        import win32com.shell.shell as win32shell
        win32shell.ShellExecuteEx(lpFile='cmd.exe', lpParameters='/c ' + filePath)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow("C:/Users/Jeongkuk/PycharmProjects/androidADB/")
    main.resize(666, 333)
    main.move(app.desktop().screen().rect().center() - main.rect().center())
    main.show()

    sys.exit(app.exec_())