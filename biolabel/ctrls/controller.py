from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
from utils.rect import InteractiveGraphicsRectItem
from views.Ui_MainWindow import Ui_MainWindow
from views.canvas import *
import cv2

class MainWindow_controller(QtWidgets.QMainWindow):
     
    current_file = []
    img = []
    qImg = []

    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        
        

    # def addRect(self):
    #     rect = QtCore.QRectF(0, 0, 100, 50)
    #     rectItem = InteractiveGraphicsRectItem(rect=rect, radius=3.5)
    #     self.ui.scene.addItem(rectItem)

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

    def Click_CreateLabel(self):
        self.ui.canvas.scene.CreateMode = True
        self.ui.toolButton_CreateLabel.setStyleSheet\
            ("background-color: {}".format(QColor(Qt.darkGray).name()))
        self.ui.canvas.scene.EditMode   = False
        self.ui.toolButton_EditLabel.setStyleSheet("background-color: auto")
        self.StatusBarText('Mode : CreateLabel')
        # print(f'You click the CreateLabel button, and CreateMode is {self.ui.canvas.scene.CreateMode}')

    def Click_EditLabel(self):
        self.ui.canvas.scene.CreateMode = False
        self.ui.toolButton_CreateLabel.setStyleSheet("background-color: auto")
        self.ui.canvas.scene.EditMode   = True
        self.ui.toolButton_EditLabel.setStyleSheet\
            ("background-color: {}".format(QColor(Qt.darkGray).name()))
        self.StatusBarText('Mode : EditLabel')
        # print(f'You click the EditLabel button, and CreateMode is {self.ui.canvas.scene.CreateMode}')

    def Click_DIP(self):
        print('You click the DIP button')

    def open_file(self):
        self.current_file, filetype = QFileDialog.getOpenFileName(self, "Open file", "./")
        print(self.current_file, filetype)
        if self.current_file :
            self.read_img_to_view()
            self.ui.canvas.scene.ImgLoad = True

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open folder", "./")
        print(folder_path)
        # print(self.current_file)


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
        self.ui.canvas.scene.setSceneRect(QRectF(0, 0, height, width))
        self.ui.canvas.scene.addItem(item)

        self.ui.canvas.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        return
    
    def StatusBarText(self, str):
        self.ui.statusBar.showMessage(str)
        return