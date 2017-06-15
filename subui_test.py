from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

notifyDialog = QtWidgets.QDialog()
notifyDialog.resize(300, 300)
layout = QtWidgets.QVBoxLayout(notifyDialog)
scroll = QtWidgets.QScrollArea()
scroll.setWidgetResizable(True)
layout.addWidget(scroll)

scrollContents = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(scrollContents)
scroll.setWidget(scrollContents)

label = QtWidgets.QLabel()
label.setText("1\n2\n3\n4\n5\n6\n7n\n8\n9\n")

layout.addWidget(label)

notifyDialog.show()
notifyDialog.raise_()
app.exec_()