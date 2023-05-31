from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QGraphicsPixmapItem,QDialog,QMessageBox,QWidget
from PyQt5.QtGui import QImage, QPixmap, QCursor

from views.Ui_MainWindow import Ui_MainWindow
from views.canvas import *
import os
import numpy as np
import cv2
from model.LabelService import LabelService
from model.ImageProcessService import ImageProcessService
from model.FileService import FileService
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
        

        self.setup_control()
        self.labelService = LabelService()
        self.imageProcessService = ImageProcessService()
        self.fileService = FileService()
        self.templabelName = ""
        self.Color = "#ffffff"
        self.EditLabel = None
        self.EditUIlabel = None
        

    def setup_control(self):
        # menubar
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionOpenFolder.triggered.connect(self.open_folder)
        self.ui.actionExit.triggered.connect(lambda: exit())

        # toolBotton
        self.ui.actionCreateLabel.triggered.connect(self.Click_CreateLabel)
        self.ui.actionEditLabel.triggered.connect(self.Click_EditLabel)
        self.ui.actionDIP.triggered.connect(self.Click_DIP)
        self.ui.actionSave.triggered.connect(self.saveMyLabel)
        # self.ui.actionSave_as.triggered.connect(self.)

        # issueLabelCommand
        self.ui.canvas.scene.issueLabelCommand.connect(self.issueCreateLabelCommand)
        # issueUpdateLabelCommand
        self.ui.canvas.scene.issueUpdateLabelCommand.connect(self.issueMoveLabelCommand)
        # issueLabelCommand
        self.ui.canvas.scene.issueLabelNameDialogShow.connect(self.LabelNameDialogShow)

        #LabelNameDialogButton
        self.ui.canvas.scene.LabelNameDialog.AddLabelName.connect(self.LabelNameAccept)

        # === CreateLabel選單 ===
        self.CreateLabelmenu = QtWidgets.QMenu()
        # Add menu options
        create_polygons_option = self.CreateLabelmenu.addAction('Create Polygons')
        create_rect_option = self.CreateLabelmenu.addAction('Create Rectangle')
        create_line_option = self.CreateLabelmenu.addAction('Create Line')
        create_linestrip_option = self.CreateLabelmenu.addAction('Create LineStrip')
        create_point_option = self.CreateLabelmenu.addAction('Create Point')
        undo_option = self.CreateLabelmenu.addAction('Undo')
        # Menu option events
        create_polygons_option.triggered.connect(lambda: self.ui.canvas.scene.ChangeShape("poly"))
        create_rect_option.triggered.connect(lambda: self.ui.canvas.scene.ChangeShape("rect"))
        create_point_option.triggered.connect(lambda: self.ui.canvas.scene.ChangeShape("point"))
        create_line_option.triggered.connect(lambda: self.ui.canvas.scene.ChangeShape("line"))
        create_linestrip_option.triggered.connect(lambda: self.ui.canvas.scene.ChangeShape("linestrip"))
        # =================================


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
        
        # self.ui.LabelListWidget.itemClicked.connect(self.item_clicked)
        self.ui.LabelListWidget.itemClicked.connect(self.handle_item_click)

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
            self.ChangeLabelSelectable()
            self.CheckCursorStyle()
            self.CreateLabelmenu.exec_(QCursor.pos())
        
    # === toolBotton action : Edit Label ===    
    def Click_EditLabel(self):
        if self.ui.canvas.scene.ImgLoad :
            self.ui.canvas.scene.CreateMode = False
            self.ui.toolButton_CreateLabel.setStyleSheet("background-color: auto")
            self.ui.canvas.scene.EditMode   = True
            self.ui.toolButton_EditLabel.setStyleSheet\
                ("background-color: {}".format(QColor(Qt.darkGray).name()))
            self.StatusBarText('Mode : EditLabel')
            self.ChangeLabelSelectable()
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
            self.read_img_to_view(self.current_file)
            if self.original_img :
                self.resetMode()
                self.ui.canvas.scene.ImgLoad = True
            else:
                self.wrongFormatDialog('Not Supported Format')

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
        self.resetComponent()
        self.CheckCursorStyle()
    
    def resetComponent(self):
        self.LabelNameList.clear()  
        # ViewWidgets
        self.ui.LabelNameList.clear()
        # ViewWidgets
        self.ui.canvas.scene.LabelNameDialog.LabelNameList.clear()
        self.labelService.labelList.ClearAllLabel()
        self.ui.canvas.scene.UILabelList.clear()
        self.ui.LabelListWidget.clear()


    # read image to view
    def read_img_to_view(self, imgFile):
        self.original_img = self.fileService.LoadImage(self.current_file)
        if self.original_img :
            # reset the view
            self.ui.canvas.scene.clear()
            # get size of image
            img = self.original_img.GetImg()
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
    
    def store_current_img(self, img, name, directory, format):
        pass  #todo
        # imgFile = self.fileService.ConvertImage2File(self.current_img)
        # self.fileService.StoreImage()
    
    # set text in StatusBar
    def StatusBarText(self, str):
        self.ui.statusBar.showMessage(str)
        return
    
    # change QGraphicsItem selectable
    def ChangeLabelSelectable(self):
        scene = self.ui.canvas.scene
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
            self.ui.canvas.scene.LabelNameDialog.LabelNameList.addItem(item)
            
    def LabelNameDialogShow(self): # for Create
        self.templabelName = ""
        self.ui.canvas.scene.LabelNameDialog.toolButton.setStyleSheet("")
        self.ui.canvas.scene.LabelNameDialog.toolButton.setDisabled(True)
        self.ui.canvas.scene.LabelNameDialog.exec_()
        self.ui.canvas.scene.setFocus()
        QApplication.processEvents()

    def LabelNameDialogShowForEdit(self,label,UIlabel,item): # for Edit
        self.EditLabel=label
        self.UIlabel=UIlabel
        self.EditItem = item
        self.ui.canvas.scene.LabelNameDialog.textEdit.setText(label.GetName())
        color = QColor(label.GetLabelColor())
        self.ui.canvas.scene.LabelNameDialog.toolButton.setDisabled(False)
        self.ui.canvas.scene.LabelNameDialog.toolButton.setStyleSheet(f"background-color: {color.name()}")
        self.ui.canvas.scene.LabelNameDialog.exec_()
        self.ui.canvas.scene.LabelNameDialog.color = label.GetLabelColor()
        
    def LabelNameAccept(self, str, color):
        if self.checkLabelNameSuccess(str):
            if self.ui.canvas.scene.CreateMode == True:
                self.templabelName = str    
                if self.LabelNameList.count(str) == 0:
                    self.LabelNameList.append(str)
                    self.ui.LabelNameList.addItem(str)
                    self.ui.canvas.scene.LabelNameDialog.LabelNameList.addItem(str)
            elif self.ui.canvas.scene.EditMode == True:
                print("qweqweqweqwe")
                label = self.EditLabel
                print (color)
                print(label.GetLabelColor())
                if label.GetName() != str:
                    self.issueEditLabelNameCommand(str ,label)
                    self.EditItem.setText(str)
                if label.GetLabelColor() != color:
                    self.issueEditLabelColorCommand(color ,label)
                    print("qweqwe")
                    self.UIlabel.setLineColor(color)

        self.Color = color   #不管LabelName是否合法都可以改顏色
        
    def checkLabelNameSuccess(self, str):
        print(str)
        if len(str) != 0: # sucess 
            self.ui.canvas.scene.inputLabelNameSuccess = True
            return True
        else : # fails
            self.ui.canvas.scene.inputLabelNameSuccess = False
            return False

    # Call LabelService
    def issueCreateLabelCommand(self, cmd, type, ptList):
        if cmd == 'CreateLabel' and len(self.templabelName) !=0:
            new_label = self.labelService.CreateLabel(self.templabelName, type, self.Color, ptList) # 創建一個Label
            item = QtWidgets.QListWidgetItem()
            item.setText(self.templabelName)
            item.setData(4, new_label)  
            item.setData(5, self.ui.canvas.scene.tempLabel)  
            self.ui.LabelListWidget.addItem(item)
            self.ui.canvas.scene.tempLabel.label = new_label # 每個UILabel對應一個Label
            self.labelService.labelList.AddLabel(new_label) # 加入labelList
            print(f"成功！目前有這些：{[x.GetName() for x in self.labelService.labelList.GetLabelList()]}")
        else:
            # LabelName為空則不創建Label
            self.ui.canvas.scene.drawing = True

    def handle_item_click(self,item):
        if(self.ui.canvas.scene.EditMode):
            self.LabelNameDialogShowForEdit(item.data(4),item.data(5),item)

    # Call LabelService
    def issueMoveLabelCommand(self, moveX , moveY , index , Label):
        self.labelService.moveLabel( moveX , moveY , index , Label) 

    def issueEditLabelNameCommand(self, labelname, Label):
        self.labelService.EditLabelName( labelname, Label) 

    def issueEditLabelColorCommand(self, color , Label):
        self.labelService.EditLabelColor(color , Label) 

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


    # Save My label to Json
    def saveMyLabel(self):
        current_labellist = self.labelService.labelList
        # into File
        MyLabelFile = self.fileService.ConvertLabel2File(label=current_labellist)
        # save LabelFile
        FileName = os.path.splitext(self.current_file)[0] + '.json'
        MyLabelFile.SetFileLocation(FileName)
        print(FileName)
        self.fileService.StoreLabel(LF=MyLabelFile, format='My')
        
    # Save DIP image 
    def exportImage(self):
        pass




    # ======== message ========
    def wrongFormatDialog(self, msg):
        dlg = QMessageBox()
        # dlg.setWindowTitle('D')
        dlg.setText(msg)
        button = dlg.exec()
        # button = QPushButton("Press me for a dialog!")

