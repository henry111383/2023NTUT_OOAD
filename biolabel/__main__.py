import argparse
import codecs
import logging
import os
import os.path as osp
import sys
import yaml

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from biolabel import __appname__
from biolabel import __version__
from biolabel.app import MainWindow