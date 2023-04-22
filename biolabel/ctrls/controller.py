from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QRectF
from views.rect import InteractiveGraphicsRectItem
from views.Ui_MainWindow import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.addRect()
    def addRect(self):
        scene = QGraphicsScene()
        self.ui.graphicsView_2.setScene(scene)
        rect = QRectF(0, 0, 100, 50)
        rectItem = InteractiveGraphicsRectItem(rect=rect, radius=5)
        scene.addItem(rectItem)