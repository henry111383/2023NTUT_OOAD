import functools
import html
import math
import os
import os.path as osp
import re
import webbrowser


# import imgviz
# import natsort
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5 import QtWidgets


from __init__ import __appname__

class MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(MainWindow, self).__init__()
                self.initUI()

        def initUI(self):
                self.setWindowTitle(__appname__)

                exitAct = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
                exitAct.setShortcut('Ctrl+Q')
                exitAct.setStatusTip('Exit application')
                exitAct.triggered.connect(QtWidgets.qApp.quit)

                menuBar = self.menuBar()
                fileMenu = menuBar.addMenu('&File')
                fileMenu.addAction(exitAct)
                testMenu = menuBar.addMenu('&Test')
                menuBar.setNativeMenuBar(False)
                
                self.setGeometry(300,300,1000,800)
                self.statusBar().showMessage("Ready")

                self.show()

                