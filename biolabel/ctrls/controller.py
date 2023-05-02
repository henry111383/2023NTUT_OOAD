from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QGraphicsPixmapItem,QDialog
from PyQt5.QtGui import QImage, QPixmap, QCursor

from views.Ui_MainWindow import Ui_MainWindow
from views.LabelNameDialog import LabelName_Dialog
from views.canvas import *
import numpy as np
import cv2
from model.LabelService import LabelService
from model.ImageProcessService import ImageProcessService
from model.LabelList import LabelList
from model.Image import Image

import matplotlib.pyplot as plt

CURSOR_DEFAULT = QtCore.Qt.ArrowCursor
CURSOR_POINT = QtCore.Qt.PointingHandCursor
CURSOR_DRAW = QtCore.Qt.CrossCursor
CURSOR_MOVE = QtCore.Qt.ClosedHandCursor
CURSOR_GRAB = QtCore.Qt.OpenHandCursor

class MainWindow_controller(QtWidgets.QMainWindow):
     
    current_file = []
    original_img = None
    current_img = None
    imgItem = None
    LabelNameList = []

    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.LabelNameDialog = LabelName_Dialog()

        self.setup_control()
        self.labelService = LabelService()
        self.imageProcessService = ImageProcessService()
        self.labelList = LabelList()
        self.templabelName = ""
        

    def setup_control(self):
        # menubar
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionOpenFolder.triggered.connect(self.open_folder)
        self.ui.actionExit.triggered.connect(lambda: exit())

        # toolBotton
        self.ui.actionCreateLabel.triggered.connect(self.Click_CreateLabel)
        self.ui.actionEditLabel.triggered.connect(self.Click_EditLabel)
        self.ui.actionDIP.triggered.connect(self.Click_DIP)

        # issueLabelCommand
        self.ui.canvas.scene.issueLabelCommand.connect(self.issueLabelCommand)
        # issueLabelCommand
        self.ui.canvas.scene.issueLabelNameDialogShow.connect(self.LabelNameDialogShow)

        #LabelNameDialogButton
        self.LabelNameDialog.AddLabelName.connect(self.LabelNameAccept)

        # === DIP 選單 ===
        self.DIPmenu = QtWidgets.QMenu()
        # Add menu options
        DIP_RGB2Gray = self.DIPmenu.addAction('GRAY')
        DIP_OTSUbinary = self.DIPmenu.addAction('BINARY')
        DIP_RGB2Hematoxylin = self.DIPmenu.addAction('Hematoxylin')
        DIP_RGB2Eosin = self.DIPmenu.addAction('Eosin')
        DIP_RGB2Dab = self.DIPmenu.addAction('Dab')
        self.DIPmenu.addSeparator()
        DIP_Back2Original = self.DIPmenu.addAction('Original Image')
        
        # Menu option events
        DIP_RGB2Gray.triggered.connect(lambda: self.issueImageProcessCommand('RGB2Gray'))
        DIP_OTSUbinary.triggered.connect(lambda: self.issueImageProcessCommand('OTSUbinary'))
        DIP_RGB2Hematoxylin.triggered.connect(lambda: self.issueImageProcessCommand('RGB2Hematoxylin'))
        DIP_RGB2Eosin.triggered.connect(lambda: self.issueImageProcessCommand('RGB2Eosin'))
        DIP_RGB2Dab.triggered.connect(lambda: self.issueImageProcessCommand('RGB2Dab'))
        DIP_Back2Original.triggered.connect(lambda: self.issueImageProcessCommand('Back2Original'))
        # =================================
        

    def changeshape(self,shape):
        self.ui.canvas.shape=shape

    # === toolBotton action : Create Label ===
    def Click_CreateLabel(self):
        if self.ui.canvas.scene.ImgLoad :
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
        if self.ui.canvas.scene.ImgLoad :
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
        if self.ui.canvas.scene.ImgLoad :
            self.DIPmenu.exec_(QCursor.pos())
        

    # === MenuBar action : OpenFile ===
    def open_file(self):
        self.current_file, filetype = QFileDialog.getOpenFileName(self, "Open file", "./")
        print(self.current_file, filetype)
        if self.current_file :
            self.resetMode()
            self.read_img_to_view(self.current_file)
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
    def read_img_to_view(self, imgFile):
        # read image
        img = cv2.cvtColor(cv2.imread(imgFile), cv2.COLOR_BGR2RGB)
        # create Image instance
        self.original_img = Image(img, channel='RGB', imageName='Original')
        # reset the view
        self.ui.canvas.scene.clear()
        # get size of image
        h, w, _ = img.shape
        # set QImage
        qImg = QImage(img, w, h, 3 * w, QImage.Format_RGB888)
        # set QPixmanp
        pix = QPixmap.fromImage(qImg)
        self.imgItem = QGraphicsPixmapItem(pix)
        self.ui.canvas.scene.setSceneRect(QRectF(0, 0, w, h))
        self.ui.canvas.scene.addItem(self.imgItem)
        self.ui.canvas.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        return
    
    # set text in StatusBar
    def StatusBarText(self, str):
        self.ui.statusBar.showMessage(str)
        return
    
    # change QGraphicsItem selectable
    def ChangeLabelSelectable(self, scene):
        if scene.EditMode :
            for item in scene.UILabelList:
                item.setFlag(QGraphicsItem.ItemIsSelectable, True)
                item.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
                item.setFlag(QGraphicsItem.ItemIsFocusable, True)
                item.setFlag(QGraphicsItem.ItemIsMovable, True) 
                item.EditMode = True
                
        else:
            for item in scene.UILabelList:
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
            
    # set LabelName
    def SetLabelNameList(self):
        for item in self.LabelNameList:
            self.ui.LabelNameList.addItem(item)
            self.LabelNameDialog.LabelNameList.addItem(item)
            
    def LabelNameDialogShow(self):
        self.templabelName = ""
        self.LabelNameDialog.exec_()

    def LabelNameAccept(self, str):
        if self.checkLabelNameSuccess(str):
            self.templabelName = str    
            if self.LabelNameList.count(str) == 0:
                self.LabelNameList.append(str)
                self.ui.LabelNameList.addItem(str)
                self.LabelNameDialog.LabelNameList.addItem(str)
        

    def checkLabelNameSuccess(self, str):
        print(str)
        if len(str) != 0: # sucess 
            self.ui.canvas.scene.inputLabelNameSuccess = True
            return True
        else : # fails
            self.ui.canvas.scene.inputLabelNameSuccess = False
            return False

    # Call LabelService
    def issueLabelCommand(self, cmd, type, ptList):
        if cmd == 'CreateLabel' and len(self.templabelName) !=0:
            new_label = self.labelService.isCreateLabel(self.templabelName, type, ptList) # 創建一個Label
            self.ui.canvas.scene.tempLabel.label = new_label # 每個UILabel對應一個Label
            self.labelList.AddLabel(new_label) # 加入labelList
            print(f"成功！目前有這些：{[x.GetName() for x in self.labelList.GetLabelList()]}")
        else:
            # LabelName為空則不創建Label
            self.ui.canvas.scene.drawing = True


    # Call DIPService
    def issueImageProcessCommand(self, str):
        if str == 'Back2Original':
            # get size of image
            h, w, _ = self.original_img.GetImg().shape
            # set QImage
            qImg = QImage(self.original_img.GetImg(), w, h, 3 * w, QImage.Format_RGB888)
            # set QPixmanp
            pix = QPixmap.fromImage(qImg)
            self.imgItem.setPixmap(pix)
            
        else:
            self.current_img = eval(f'self.imageProcessService.{str}(self.original_img)')
            img = self.current_img.GetImg()
            # get size of image
            h, w, _ = img.shape
            # set QImage
            qImg = QImage(img, w, h, 3 * w, QImage.Format_RGB888)
            # set QPixmanp
            pix = QPixmap.fromImage(qImg)
            self.imgItem.setPixmap(pix)
