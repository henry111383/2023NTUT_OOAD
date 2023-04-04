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

from utils.qt import newIcon
from __init__ import __appname__

class MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super(MainWindow, self).__init__()
                self.setWindowTitle(__appname__)
                self.setWindowIcon(newIcon("icon"))
