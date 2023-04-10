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
import utils


from __init__ import __appname__

# This is for app view
class MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(MainWindow, self).__init__()
                self.initUI()

        def initUI(self):
                self.setWindowTitle(__appname__)


                menuBar = self.menuBar()
                fileMenu = self.menu('&File')
                self.setAction(fileMenu, '&Open', 'Ctrl+O', 'Open image or label file', self.close)
                fileMenu.addSeparator() ## 加一個分隔線
                self.setAction(fileMenu, '&Exit', 'Ctrl+Q', 'Exit application', self.close)
                
               
                testMenu = self.menu('&Test')

                # let MacOS can also show the menu bar
                menuBar.setNativeMenuBar(False)
                
                self.setGeometry(300,300,1000,800)
                self.statusBar().showMessage("Ready")

                self.show()


        def menu(self, title):
                menu = self.menuBar().addMenu(title)
                return menu
        
        def setAction(self, menu, ActionName=None, Shortcut=None, StatusTip=None, TriggerAction=None):
                if isinstance(menu, QtWidgets.QMenu):
                        if Shortcut and StatusTip and TriggerAction:
                                Act = QtWidgets.QAction(ActionName, self)
                                Act.setShortcut(Shortcut)
                                Act.setStatusTip(StatusTip)
                                Act.triggered.connect(TriggerAction)
                                menu.addAction(Act)
                                return
                        
