from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
from views.rect import InteractiveGraphicsRectItem
from views.Ui_MainWindow import Ui_MainWindow
from views.canvas import *
import cv2

class MainWindow_controller(QtWidgets.QMainWindow):
    CreateMode = False 
    current_file = []
    img = []
    qImg = []

    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        
        # self.addRect()
        #  # Menu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menu)

    # def addRect(self):
    #     rect = QtCore.QRectF(0, 0, 100, 50)
    #     rectItem = InteractiveGraphicsRectItem(rect=rect, radius=3.5)
    #     self.ui.scene.addItem(rectItem)

    def setup_control(self):
        # menubar
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionOpenFolder.triggered.connect(self.open_folder)

        # toolBotton
        self.ui.actionCreateLabel.triggered.connect(self.Click_CreateLabel)
        self.ui.actionEditLabel.triggered.connect(self.Click_EditLabel)
        self.ui.actionDIP.triggered.connect(self.Click_DIP)
        

    def changeshape(self,shape):
        self.ui.canvas.shape=shape

    def right_menu(self,pos):
        if self.CreateMode :
            menu = QtWidgets.QMenu()

            # Add menu options
            create_polygons_option = menu.addAction('Create Polygons')
            create_rect_option = menu.addAction('Create Rectangle')
            create_line_option = menu.addAction('Create Line')
            create_linestrip_option = menu.addAction('Create LineStrip')
            create_point_option = menu.addAction('Create Point')
            edit_polygons_option = menu.addAction('Edit Polygons')
            edit_label_option = menu.addAction('Edit Label')
            delete_polygons_option = menu.addAction('Delete Polygons')
            undo_option = menu.addAction('Undo')
            
            # Menu option events
            create_polygons_option.triggered.connect(lambda: self.changeshape("rect"))
            create_rect_option.triggered.connect(lambda: print('Goodbye'))
            create_line_option.triggered.connect(lambda: exit())
            # Position
            menu.exec_(self.mapToGlobal(pos))

    def Click_CreateLabel(self):
        self.CreateMode = True
        print(f'You click the CreateLabel button, and CreateMode is {self.CreateMode}')

    def Click_EditLabel(self):
        self.CreateMode = False
        print(f'You click the EditLabel button, and CreateMode is {self.CreateMode}')

    def Click_DIP(self):
        print('You click the DIP button')

    def open_file(self):
        self.current_file, filetype = QFileDialog.getOpenFileName(self, "Open file", "./")
        print(self.current_file, filetype)
        self.read_img_to_view()

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open folder", "./")
        print(folder_path)
        # print(self.current_file)


    # read image to view
    def read_img_to_view(self):
        # read image
        self.img = cv2.imread(self.current_file)

        # reset the view
        self.ui.verticalLayout_canvas.removeWidget(self.ui.canvas)
        self.ui.canvas = GraphicView()
        self.ui.verticalLayout_canvas.addWidget(self.ui.canvas)
        
        # get size of image
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        # set QImage
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # set QPixmanp
        pix = QPixmap.fromImage(self.qImg)
        item = QGraphicsPixmapItem(pix)
        
        self.ui.canvas.scene.addItem(item)
        return
    