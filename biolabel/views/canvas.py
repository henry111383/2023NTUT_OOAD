from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRectF, Qt, QPointF , QLineF , QSize, pyqtSignal
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QBrush,QFont, QColor ,QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene,QWidget ,QGraphicsItem , QGraphicsPathItem,QDialog,QGraphicsTextItem, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets
import cv2
from model.Point import Point
# from utils.rect import getAccurateRect
from .Ui_label import *

class MyScene(QGraphicsScene): # 用來放自己的圖或標註

    ImgLoad = False
    CreateMode = False
    EditMode   = True
    drawing = False
    points = []
    tempLabel = None
    UILabelList = []
    current = None
    issueLabelCommand = pyqtSignal(str, str, str, list) # cmd, name, type, ptlist

    pen_color=Qt.red    #畫筆顏色
    pen_width = 5       #畫筆粗細

    def __init__(self):
        super(MyScene, self).__init__(parent=None) # 初始化 QGraphicsScene
        self.setSceneRect(0,0,400,400) # 預設大小，載入檔案後會改大小

        self.shape= "rect" # 預設標注模式
        self.pen_color = Qt.red
        self.pen_width = 5 
        
        self.x=0
        self.y=0
        self.wx=0
        self.wy=0

    def drawBackground(self, painter: QPainter, rect: QRectF):
        # painter.drawRect(0,0,self.width(),self.height())
        return

    def ChangeShape(self, s):
        self.shape = s

    def ChangePenColor(self, color):
        self.pen_color = QColor(color)

    def ChangePenThickness(self, thickness):
        self.pen_width=thickness

    def ChangeEraserThickness(self,EraserThickness):
        self.Eraser_pen_width=EraserThickness
    
    
    def mousePressEvent(self, event):
        # 滑鼠按下事件
        super(MyScene, self).mousePressEvent(event)
        
        # get the cooridinate in scene
        pos = event.scenePos()
        self.x = pos.x()
        self.y = pos.y()
        # print(self.x, self.y)
        if self.ImgLoad and self.CreateMode :
            if (event.button() == Qt.LeftButton) and \
                not self.isOutofScene(Point(self.x, self.y)) :
                if self.shape == 'rect':
                    self.DrawRect(pos)
                elif self.shape == 'point':
                    self.points = [Point(self.x, self.y)] # done
                    point = MyPointItem(self.x, self.y)
                    self.addItem(point)
                    self.UILabelList.append(point)
                    self.issueLabelCommand.emit("CreateLabel", "Test", self.shape, self.points) ###
                elif self.shape == 'line':
                    self.DrawLine()
                elif self.shape == 'linestrip':
                    self.DrawLineStrip()
                elif self.shape == 'poly':
                    self.DrawLineStrip()
            elif event.button() == Qt.MiddleButton  and \
                not self.isOutofScene(Point(self.x, self.y)) :
                if (self.shape == 'linestrip' or self.shape == "poly")and self.drawing==True:
                    self.drawing = False
                    self.UILabelList.append(self.tempLabel) # points done
                    self.issueLabelCommand.emit("CreateLabel", "Test", self.shape, self.points) ###
        # event.accept()
                    
        
    def mouseMoveEvent(self, event):
        # 滑鼠移動事件
        super(MyScene, self).mouseMoveEvent(event)
        pos = event.scenePos()
        self.wx = pos.x()
        self.wy = pos.y()
        if self.CreateMode:
            if self.shape == 'rect':
                if self.drawing:
                    self.tempLabel.setEndPoint(pos.x(),pos.y())
                    self.tempLabel.updatePath()
            if self.shape == 'line':
                if self.drawing:
                    self.tempLabel.setEndPoint(pos.x(),pos.y())
                    self.tempLabel.updateLine()
            if self.shape == 'linestrip' or self.shape == "poly":
                if self.drawing:
                    self.tempLabel.setLastPoint(pos.x(),pos.y())
                    self.tempLabel.updatePath()
        return

    def isOutofScene(self, pt):
        w, h = self.width(), self.height()
        return not (0 <= pt.GetX() <= w - 1 and 0 <= pt.GetY() <= h - 1)

    def resetDrawing(self):
        if self.points :
            self.points.clear() # clear
        if self.tempLabel:
            if self.drawing:
                self.removeItem(self.tempLabel)
                del self.tempLabel
        self.drawing = False
        return
        
    def DrawRect(self, pos):
        if not self.drawing :
            self.drawing = True
            self.points = [Point(self.x, self.y)] # init
            self.tempLabel = MyRectItem(self.x, self.y, self.x, self.y)
            self.addItem(self.tempLabel)
            
        else:
            self.drawing = False

            self.points.append(Point(self.x, self.y)) # done
            self.tempLabel.setEndPoint(self.x, self.y)
            self.tempLabel.update()
            self.UILabelList.append(self.tempLabel)
            self.issueLabelCommand.emit("CreateLabel", "Test", self.shape, self.points) ###
        return

    def DrawLine(self):
        if not self.drawing :
            self.drawing = True
            self.points = [Point(self.x, self.y)] # init
            self.tempLabel = MyLineItem(self.x, self.y,self.x, self.y)
            self.addItem(self.tempLabel)
            
        else:
            self.drawing = False
            self.points.append(Point(self.x, self.y)) # done
            self.tempLabel.setEndPoint(self.x, self.y)
            self.tempLabel.update()
            self.UILabelList.append(self.tempLabel)
            self.issueLabelCommand.emit("CreateLabel", "Test", self.shape, self.points) ###
        return
    
    def DrawLineStrip(self):
        if not self.drawing :
            self.drawing = True
            self.points = [Point(self.x, self.y)] # init
            if self.shape=="poly":
                self.tempLabel = MyLineStrip([(self.x, self.y),(self.x, self.y)], shape="poly")
            else:
                self.tempLabel = MyLineStrip([(self.x, self.y),(self.x, self.y)])
            self.addItem(self.tempLabel)     
        else:
            self.points.append(Point(self.x, self.y))
            self.tempLabel.addPoint((self.x, self.y))
            self.tempLabel.updatePath()
        return

class GraphicView(QGraphicsView):
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        try:
            self.scene = MyScene()  # 设置管理QgraphicsItems的场景
            self.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.x=0
            self.y=0
            self.wx=0
            self.wy=0
            
            self.setScene(self.scene) 

            # === CreateMode下，右鍵會出現選單 ===
            self.menu = QtWidgets.QMenu()
            # Add menu options
            create_polygons_option = self.menu.addAction('Create Polygons')
            create_rect_option = self.menu.addAction('Create Rectangle')
            create_line_option = self.menu.addAction('Create Line')
            create_linestrip_option = self.menu.addAction('Create LineStrip')
            create_point_option = self.menu.addAction('Create Point')
            undo_option = self.menu.addAction('Undo')
            # Menu option events
            create_polygons_option.triggered.connect(lambda: self.scene.ChangeShape("poly"))
            create_rect_option.triggered.connect(lambda: self.scene.ChangeShape("rect"))
            create_point_option.triggered.connect(lambda: self.scene.ChangeShape("point"))
            create_line_option.triggered.connect(lambda: self.scene.ChangeShape("line"))
            create_linestrip_option.triggered.connect(lambda: self.scene.ChangeShape("linestrip"))
            # =================================
            
            # 設置右鍵清單動作
            self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.right_menu)

        except Exception as e:
            print(e)

    def right_menu(self, pos):
        if self.scene.CreateMode and self.scene.ImgLoad:
            self.scene.resetDrawing()
            # Position
            self.menu.exec_(self.mapToGlobal(pos))
            return
