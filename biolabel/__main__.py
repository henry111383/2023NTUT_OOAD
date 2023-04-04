import argparse
import codecs
import logging
import os
import os.path as osp
import sys
# import yaml

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from __init__ import __appname__
from __init__ import __version__
from app import MainWindow
from utils.qt import newIcon

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

# this main block is required to generate executable by pyinstaller
if __name__ == "__main__":
    main()