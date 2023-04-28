from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap

from views.Ui_MainWindow import Ui_MainWindow
from views.canvas import *
import cv2

CURSOR_DEFAULT = QtCore.Qt.ArrowCursor
CURSOR_POINT = QtCore.Qt.PointingHandCursor
CURSOR_DRAW = QtCore.Qt.CrossCursor
CURSOR_MOVE = QtCore.Qt.ClosedHandCursor
CURSOR_GRAB = QtCore.Qt.OpenHandCursor

class MainWindow_controller(QtWidgets.QMainWindow):
     
    current_file = []
    img = []
    qImg = []

    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        

    def setup_control(self):
        # menubar
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionOpenFolder.triggered.connect(self.open_folder)
        self.ui.actionExit.triggered.connect(lambda: exit())

        # toolBotton
        self.ui.actionCreateLabel.triggered.connect(self.Click_CreateLabel)
        self.ui.actionEditLabel.triggered.connect(self.Click_EditLabel)
        self.ui.actionDIP.triggered.connect(self.Click_DIP)
        

    def changeshape(self,shape):
        self.ui.canvas.shape=shape

    # === toolBotton action : Create Label ===
    def Click_CreateLabel(self):
        self.ui.canvas.scene.CreateMode = True
        self.ui.toolButton_CreateLabel.setStyleSheet\
            ("background-color: {}".format(QColor(Qt.darkGray).name()))
        self.ui.canvas.scene.EditMode   = False
        self.ui.toolButton_EditLabel.setStyleSheet("background-color: auto")
        self.StatusBarText('Mode : CreateLabel')
        self.ChangeLabelSelectable(self.ui.canvas.scene)
        self.CheckCursorStyle()
        
    # === toolBotton action : Edit Label ===    
    def Click_EditLabel(self):
        self.ui.canvas.scene.CreateMode = False
        self.ui.toolButton_CreateLabel.setStyleSheet("background-color: auto")
        self.ui.canvas.scene.EditMode   = True
        self.ui.toolButton_EditLabel.setStyleSheet\
            ("background-color: {}".format(QColor(Qt.darkGray).name()))
        self.StatusBarText('Mode : EditLabel')
        self.ChangeLabelSelectable(self.ui.canvas.scene)
        self.CheckCursorStyle()

    # === toolBotton action : DIP ===
    def Click_DIP(self):
        print('You click the DIP button')

    # === MenuBar action : OpenFile ===
    def open_file(self):
        self.current_file, filetype = QFileDialog.getOpenFileName(self, "Open file", "./")
        print(self.current_file, filetype)
        if self.current_file :
            self.resetMode()
            self.read_img_to_view()
            self.ui.canvas.scene.ImgLoad = True

    # === MenuBar action :OpenDir ===
    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open folder", "./")
        print(folder_path)
        # print(self.current_file)

    # reset Mode after OpenFile
    def resetMode(self):
        self.ui.canvas.scene.CreateMode = False
        self.ui.toolButton_CreateLabel.setStyleSheet("background-color: auto")
        self.ui.canvas.scene.EditMode   = False
        self.ui.toolButton_EditLabel.setStyleSheet("background-color: auto")
        self.StatusBarText("")
        self.CheckCursorStyle()


    # read image to view
    def read_img_to_view(self):
        # read image
        self.img = cv2.imread(self.current_file)
        # reset the view
        self.ui.canvas.scene.clear()
        # get size of image
        height, width, channel = self.img.shape
        # set QImage
        self.qImg = QImage(self.current_file)
        # set QPixmanp
        pix = QPixmap.fromImage(self.qImg)
        item = QGraphicsPixmapItem(pix)
        self.ui.canvas.scene.setSceneRect(QRectF(0, 0, width, height))
        self.ui.canvas.scene.addItem(item)

        self.ui.canvas.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        return
    
    # set text in StatusBar
    def StatusBarText(self, str):
        self.ui.statusBar.showMessage(str)
        return
    
    # change QGraphicsItem selectable
    def ChangeLabelSelectable(self, scene):
        if scene.EditMode :
            for item in scene.LabelList:
                item.setFlag(QGraphicsItem.ItemIsSelectable, True)
                item.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
                item.setFlag(QGraphicsItem.ItemIsFocusable, True)
                item.setFlag(QGraphicsItem.ItemIsMovable, True) 
                item.EditMode = True
                
        else:
            for item in scene.LabelList:
                item.setFlag(QGraphicsItem.ItemIsSelectable, False)
                item.setFlag(QGraphicsItem.ItemSendsGeometryChanges, False)
                item.setFlag(QGraphicsItem.ItemIsFocusable, False)
                item.setFlag(QGraphicsItem.ItemIsMovable, False) 
                item.EditMode = False

    # 讓鼠標可以變化
    def CheckCursorStyle(self):
        if self.ui.canvas.scene.CreateMode :
            self.ui.canvas.setCursor(CURSOR_DRAW)
        elif self.ui.canvas.scene.EditMode : 
            self.ui.canvas.setCursor(CURSOR_GRAB)
        else:
            self.ui.canvas.setCursor(CURSOR_DEFAULT)

