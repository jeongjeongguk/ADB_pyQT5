class Install(object) :
    def FileSelect(self, parent, QtWidgets):
        self.fileDialog = QtWidgets.QFileDialog(parent)
        select = self.fileDialog.getOpenFileUrl(parent)
        path = str(select[0]).replace("PyQt5.QtCore.QUrl('file:///", "") + str(select[0]).replace("')", "")
        self.lineEdit.setText(path)