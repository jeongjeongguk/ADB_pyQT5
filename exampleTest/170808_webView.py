import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWebKit import *
# from PyQt5.QtWebKitWidgets import *
#
# https://codedump.io/share/W7lTLLqVSngO/1/cannot-import-qtwebkitwidgets-in-pyqt5
# QtWebKit got deprecated upstream in Qt 5.5 and removed in 5.6.
# You may want to switch to PyQt5.QtWebEngineWidgets :
# This supercedes the QtWebKit module and provides better and up-to-date support for HTML, CSS and JavaScript features
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

# web = QWebView()
web = QWebEngineView()
web.load(QUrl("http://www.altools.co.kr"))
web.show()

sys.exit(app.exec_())


# http://pyqt.sourceforge.net/Docs/PyQt5/QtWebEngineWidgets.html