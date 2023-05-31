from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRectF, Qt, QPointF , QLineF , QSize, pyqtSignal, QEvent, QTimer
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QBrush,QFont, QColor ,QIcon, QPixmap, QMouseEvent,QTransform
from PyQt5.QtWidgets import QLabel, QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene,QWidget ,QGraphicsItem , QGraphicsPathItem,QDialog,QGraphicsTextItem, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets
import cv2
from model.Point import Point
from views.LabelNameDialog import LabelName_Dialog
from .Ui_label import *

class MyScene(QGraphicsScene): # 用來放自己的圖或標註

    ImgLoad = False
    CreateMode = False
    EditMode   = True
    drawing = False
    points = []
    tempLabel = None
    UILabelList = []
    issueLabelCommand = pyqtSignal(str, str, list) # cmd, type, ptlist
    issueUpdateLabelCommand = pyqtSignal(float, float, int , object) # cmd, type, ptlist
    issueLabelNameDialogShow = pyqtSignal() 
    inputLabelNameSuccess = False
    keycode = None
    PressItem = None


    pen_color=Qt.red    #畫筆顏色
    pen_width = 5       #畫筆粗細

    def __init__(self):
        super(MyScene, self).__init__(parent=None) # 初始化 QGraphicsScene
        self.setSceneRect(0,0,400,400) # 預設大小，載入檔案後會改大小
        self.LabelNameDialog = LabelName_Dialog()
        self.shape= "rect" # 預設標注模式
        self.pen_color = Qt.red
        self.pen_width = 5 
        
        self.x=0
        self.y=0
        self.wx=0
        self.wy=0

    def ChangeShape(self, s):
        self.shape = s

    def ChangePenColor(self, color):
        self.pen_color = QColor(color)

    def ChangePenThickness(self, thickness):
        self.pen_width=thickness
    
    def mousePressEvent(self, event):
        # 滑鼠按下事件
        super(MyScene, self).mousePressEvent(event)

        # get the cooridinate in scene
        pos = event.scenePos()
        self.x = pos.x()
        self.y = pos.y()
        if self.ImgLoad and self.CreateMode and (not self.isOutofScene(Point(self.x, self.y))) :
            if (event.button() == Qt.LeftButton) :
                if self.shape == 'rect':
                    self.DrawRect()
                elif self.shape == 'point':
                    self.points = [Point(self.x, self.y)] # done
                    self.tempLabel = MyPointItem(self.x, self.y)
                    self.addItem(self.tempLabel)
                    self.issueLabelNameDialogShow.emit()
                    if self.inputLabelNameSuccess :
                        self.UILabelList.append(self.tempLabel)
                        self.issueLabelCommand.emit("CreateLabel", self.shape, self.points) ###
                    else:
                        self.removeItem(self.tempLabel)
                        del self.tempLabel

                elif self.shape == 'line':
                    self.DrawLine()
                elif self.shape == 'linestrip':
                    self.DrawLineStrip()
                elif self.shape == 'poly':
                    self.DrawLineStrip()

            elif (event.button() == Qt.RightButton) :
                if (self.shape == 'linestrip' or self.shape == "poly") and self.drawing==True:
                    self.issueLabelNameDialogShow.emit()
                    
                    if self.inputLabelNameSuccess:
                        self.UILabelList.append(self.tempLabel) # points done
                        self.points.append ( Point(self.x, self.y)) # init
                        self.issueLabelCommand.emit("CreateLabel", self.shape, self.points) ###
                    else:
                        self.removeItem(self.tempLabel)
                        del self.tempLabel
                    self.drawing = False
        elif self.ImgLoad and self.EditMode and (not self.isOutofScene(Point(self.x, self.y))):
            self.PressItem = self.itemAt(event.scenePos(), QTransform())
            
            
    def keyPressEvent(self, event):  
        self.keycode = event.key()
        print(self.keycode)
        if self.keycode == 16777216: # esc
            self.resetDrawing()


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
    def mouseReleaseEvent(self, event):
        # 滑鼠移動事件
        super(MyScene, self).mouseReleaseEvent(event)
        pos = event.scenePos()
        moveX = pos.x() - self.x  
        moveY = pos.y() - self.y
        if self.ImgLoad and self.EditMode:
            item = self.itemAt(pos, QTransform())
            parent= item.parentItem()
            index = 0
            if (item is self.PressItem) & self.CheckLabelInUiLabel(item):
                if parent == None :
                    index = len(item.childItems())
                    print(index)
                    self.issueUpdateLabelCommand.emit( moveX , moveY , index , item.label) ###
                else:
                    index = parent.childItems().index(item)
                    self.issueUpdateLabelCommand.emit( moveX , moveY , index , parent.label) ###
            else : 
                print(item)
                print(self.PressItem)
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
        
    def DrawRect(self):
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
            self.issueLabelNameDialogShow.emit()
            if self.inputLabelNameSuccess:
                self.UILabelList.append(self.tempLabel)
                self.issueLabelCommand.emit("CreateLabel", self.shape, self.points) ###
            else:
                self.removeItem(self.tempLabel)
                del self.tempLabel
                self.drawing = False
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
            self.issueLabelNameDialogShow.emit()
            if self.inputLabelNameSuccess:
                self.UILabelList.append(self.tempLabel)
                self.issueLabelCommand.emit("CreateLabel", self.shape, self.points) ###
            else:
                self.removeItem(self.tempLabel)
                del self.tempLabel
                self.drawing = False
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
    def CheckLabelInUiLabel(self,UiLabel):
        if isinstance(UiLabel,MyLineItem) | isinstance(UiLabel,MyLineStrip) | isinstance(UiLabel,MyPointItem) \
            | isinstance(UiLabel,MyRectItem) | isinstance(UiLabel,LinePoint) :
            return True
        else:
            return False
    
class GraphicView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)  # 禁用右鍵選單
        try:
            self.scene = MyScene()  # 設置管理QgraphicsItems的場景
            self.setAlignment(Qt.AlignTop | Qt.AlignCenter) 
            self.setScene(self.scene) 
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.scene.setFocus()
        return
