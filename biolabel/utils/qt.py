import os.path as osp

# import numpy as np

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


here = osp.dirname(osp.dirname(osp.abspath(__file__)))

def newIcon(icon):
    icons_dir = osp.join(here, "icons")
    png_file = osp.join(":/", icons_dir, "%s.png" % icon)
    return QtGui.QIcon(png_file)