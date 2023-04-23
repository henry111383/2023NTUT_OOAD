from PyQt5 import QtWidgets, QtGui, QtCore
from views.rect import InteractiveGraphicsRectItem
from views.Ui_MainWindow import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.addRect()
        #  # Menu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.right_menu)

    def addRect(self):
        rect = QtCore.QRectF(0, 0, 100, 50)
        rectItem = InteractiveGraphicsRectItem(rect=rect, radius=5)
        self.ui.scene.addItem(rectItem)

    def right_menu(self,pos):
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
        create_polygons_option.triggered.connect(lambda: self.addRect())
        create_rect_option.triggered.connect(lambda: print('Goodbye'))
        create_line_option.triggered.connect(lambda: exit())
        # Position
        menu.exec_(self.mapToGlobal(pos))