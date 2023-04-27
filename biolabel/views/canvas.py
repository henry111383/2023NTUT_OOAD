from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRectF, Qt, QPointF ,QLineF ,QSize
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QBrush,QFont, QColor ,QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene,QWidget ,QGraphicsItem , QGraphicsPathItem,QDialog,QGraphicsTextItem, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets
import cv2
from utils.point import Point
from utils.rect import getAccurateRect
from utils.label import *

class MyScene(QGraphicsScene):#自定场景

    ImgLoad = False
    CreateMode = False
    EditMode   = True
    drawing = False
    points = None
    tempLabel = None
    LabelList = []

    pen_color=Qt.red    #畫筆顏色
    pen_width = 5       #畫筆粗細

    def __init__(self):
        super(MyScene, self).__init__(parent=None) #实例化QGraphicsScene
        self.setSceneRect(0,0,400,400) #设置场景起始及大小，默认场景是中心为起始，不方便后面的代码

        self.shape= "rect"
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
        

    def mouseMoveEvent(self, event):
        # 滑鼠移動事件
        super(MyScene, self).mouseMoveEvent(event)
        pos = event.scenePos()
        self.wx = pos.x()
        self.wy = pos.y()
        if self.shape == 'rect':
            self.ShowRectBuffer(pos)
        return

        


    def isOutofScene(self, pt):
        w, h = self.width(), self.height()
        return not (0 <= pt.x() <= w - 1 and 0 <= pt.y() <= h - 1)

    def resetDrawing(self):
        self.drawing = False
        if self.points :
            self.points.clear()
        if self.tempLabel :
            self.removeItem(self.tempLabel)
        return
        
    def DrawRect(self, pos):
        if not self.drawing :
            self.drawing = True
            self.points = [Point(self.x, self.y)]
            
            # # 緩衝的圖
            # self.tempPath = QGraphicsPathItem()
            # self.tempPath.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable
            #                 | QtWidgets.QGraphicsItem.ItemIsMovable
            #                 | QtWidgets.QGraphicsItem.ItemIsFocusable
            #                 | QtWidgets.QGraphicsItem.ItemSendsGeometryChanges
            #                 | QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)

            # pp=QPen()    
            # pp.setColor(self.pen_color)
            # pp.setWidth(self.pen_width)
            # self.tempPath.setPen(pp)

            self.label_path = QPainterPath()
            self.label_path.moveTo(pos)

            # 緩衝用
            rectangle = getAccurateRect(self.points[0], Point(self.x+0.01, self.y+0.01))
            self.tempLabel = RectItem(self.pen_color, self.pen_width, rectangle)
            self.addItem(self.tempLabel)
            
        else:
            self.drawing = False
            self.removeItem(self.tempLabel)

            self.points.append(Point(self.x, self.y))
            rectangle = getAccurateRect(self.points[0], self.points[1])
            self.label_path.addRect(rectangle)
            self.r = RectItem(self.pen_color, self.pen_width, rectangle)
            self.addItem(self.r)
            self.LabelList.append(self.r)
        return

    def ShowRectBuffer(self, pos):
        if self.drawing:
            self.w = pos.x()-self.x
            self.h = pos.y()-self.y
            rectangle = getAccurateRect(self.points[0], Point(self.wx, self.wy))
            if rectangle :
                self.tempLabel.setRect(rectangle)
        return


class GraphicView(QGraphicsView):
    
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        try:
            self.scene = MyScene()  # 设置管理QgraphicsItems的场景
            self.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            # self.scene.setSceneRect(0, 0, 50, 10)
            # 預設rectangle
            self.shape = "rect"   
            # 預設筆的顏色
            self.pen_color = Qt.red  # 预设笔的颜色
            self.pen_width = 5  # 预设笔的宽度


            # 预设以下参数的值，以防画板打开第一时间操作导入图片后self.wx-self.x=None-None而出错
            self.x=0
            self.y=0
            self.wx=0
            self.wy=0
            # print(self.frameSize().width())
            # self.setSceneRect(0,0,self.frameSize.width()-100,self.frameSize.height()-100)
            
            self.setScene(self.scene)  # Qgraphicsview设置场景MyScene()
            # self.scene.addRect(0, 0, 100, 100, QPen(Qt.black), QBrush(Qt.red))

            # 設置右鍵清單動作
            self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.right_menu)

        except Exception as e:
            print(e)

    def right_menu(self, pos):
        if self.scene.CreateMode :
            self.scene.resetDrawing()
            # === CreateMode下，右鍵會出現選單 ===
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
            create_polygons_option.triggered.connect(lambda: self.scene.ChangeShape("poly"))
            create_rect_option.triggered.connect(lambda: self.scene.ChangeShape("rect"))
            # create_line_option.triggered.connect(lambda: exit())
            # =================================
            # Position
            menu.exec_(self.mapToGlobal(pos))
            return

    # def Shape(self, s):
    #     """返回画笔属性状态"""
    #     self.shape = s
    #     if self.shape == "move":
    #         self.setDragMode(QGraphicsView.RubberBandDrag)   # 设置为支持橡皮筋框选模式
    #     else:
    #         self.setDragMode(QGraphicsView.NoDrag)     # 其他情况设置为不可拖拽模式
    #     return self.shape

    # def ChangePenColor(self, color):
    #     """返回变更的画笔颜色"""
    #     self.pen_color = QColor(color)    # 当画笔颜色变化时，设置画笔颜色
    #     return self.pen_color

    # def ChangePenThickness(self, thickness):
    #     """返回变更的画笔粗细"""
    #     self.pen_width=thickness   # 当画笔颜色变化时，设置画笔粗细

    # def get_item_at_click(self, event):  # 返回鼠标点击的QgraphicsItem
    #     """ 返回你所点击的item """
    #     pos = event.pos()     # 注意此时是Qgraphicsview的鼠标点击位置
    #     # x=self.graphicsView.mapFromParent(pos)
    #     # y=self.graphicsView.mapFromScene(pos)
    #     # z=self.graphicsView.mapFromGlobal(pos)
    #     # print(pos,x,y,z)
    #     # print(pos)
    #     item = self.itemAt(pos)
    #     return item


    # def mousePressEvent(self, event):
    #     """重载鼠标按下事件"""
    #     super(GraphicView,self).mousePressEvent(event)   # 此重置句必须要有，目的是为了画完Item后Item可被选择

    #     try:
    #         self.lastPoint = event.pos()  # 记录鼠标在Qgraphicsview按下的位置点
    #         print(self.lastPoint)
    #         self.x = self.lastPoint.x()
    #         self.y = self.lastPoint.y()

    #         pos = event.pos()   # 记录鼠标按下的位置
    #         self.t=self.mapToScene(pos)

    #         item = self.get_item_at_click(event)   # 记录鼠标点击Item的信息，若无Item，此函数返回None



    #         """"鼠标右键按下Item时，将其删除事件"""
    #         if event.button() == Qt.RightButton:
    #             if isinstance(item, QGraphicsItem):
    #                 self.scene.removeItem(item)

    #         """"触发鼠标左件事件"""
    #         if event.button() == Qt.LeftButton:

    #             self.tempPath = QGraphicsPathItem()  # 设置一个内存上的QGraphicsPathItem，方便MouseMoveEvent画图时有双缓冲绘图效果
    #             self.tempPath.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable
    #                                 | QtWidgets.QGraphicsItem.ItemIsMovable
    #                                 | QtWidgets.QGraphicsItem.ItemIsFocusable
    #                                 | QtWidgets.QGraphicsItem.ItemSendsGeometryChanges
    #                                 | QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)

    #             self.path1 = QPainterPath()    # 实例路径函数，用于自由画笔风格
    #             self.path1.moveTo(pos)    # 设置路径开始点

    #             if self.shape == "line":
    #                 self.a = Arrow(self.scene, self.pen_color, self.pen_width)   # 设置实例化自定义的箭头类，但不传入起始点位置参数
    #                 self.a.set_src(self.x, self.y)    # 设置自定义箭头类的箭头线起始点

    #             # 千万不要再初始化__init__那里设置画笔Qpen，不然笔颜色，大小无法修改
    #             pp=QPen()    # 实例QPen
    #             pp.setColor(self.pen_color)    #设置颜色
    #             pp.setWidth(self.pen_width)    #设置宽度

    #             self.tempPath.setPen(pp)     # self.tempPath应用笔
    #             if item != None:
    #                 self.wl=item.boundingRect().width()


    #     except Exception as e:
    #         print(e)


    # def mouseMoveEvent(self,event):
    #     """重载鼠标移动事件"""
    #     super(GraphicView, self).mouseMoveEvent(event)    # 此重置句必须要有，目的是为了画完Item后Item可被移动，可放在MouseMoveEvent最后

    #     self.endPoint = event.pos()    # 返回鼠标移动时的点位置
    #     self.wx = self.endPoint.x()
    #     self.wy = self.endPoint.y()

    #     self.w = self.wx-self.x   # 用于绘画矩形Rect和Ellipse图形时的宽（长）
    #     self.h = self.wy-self.y   # 用于绘画矩形Rect和Ellipse图形时的高（宽）

    #     self.m = self.mapFromScene(event.pos())
    #     item = self.get_item_at_click(event)

    #     if event.buttons() & Qt.LeftButton : #仅左键时触发，event.button返回notbutton，需event.buttons()判断，这应是对象列表，用&判断

    #         try:
    #             # if item != None and isinstance(item,QGraphicsRectItem)==False:
    #             if item != None and item.type() != 4:    # 判断自定义的图片类（自己设置了图片的type()=4）时，画笔可以在图片上画图，而不会使图片在绘图时移动
    #                 super(GraphicView, self).mouseMoveEvent(event)

    #             elif self.shape=="circle":    # 圆形的item.type()=3
    #                 self.setCursor(Qt.ArrowCursor)   # 设置鼠标形状
    #                 if item == None:    # 若无点击Item时，画笔可以画圆形
    #                     pass
    #                 else:   # 若鼠标有点击图片类Item，设置该图片图元不可被选择和不可移动
    #                     item.setFlag(QGraphicsItem.ItemIsMovable,enabled=False)
    #                     item.setFlag(QGraphicsItem.ItemIsSelectable,enabled=False)
    #                 self.path2 = QPainterPath()    # 为了实现双缓冲的效果，另设一个QPainterPath
    #                 self.path2.addEllipse(self.t.x(), self.t.y(), self.w, self.h)  # 添加绘图路径
    #                 self.tempPath.setPath(self.path2)  # 由于self.path2是在内存上一直刷新，并销毁之前的绘图路径，此时tempath设置路径就能在绘图时有双缓冲效果
    #                 self.scene.addItem(self.tempPath)  # Myscene()场景中添加图元


    #             elif self.shape=="rect":   # 矩形的item.type()=3
    #                 self.setCursor(Qt.ArrowCursor)
    #                 if item == None:
    #                     pass
    #                 else:
    #                     item.setFlag(QGraphicsItem.ItemIsSelectable, enabled=False)
    #                     item.setFlag(QGraphicsItem.ItemIsMovable,enabled=False)
    #                 self.path3 = QPainterPath()
    #                 self.path3.addRect(self.t.x(), self.t.y(), self.w, self.h)
    #                 self.tempPath.setPath(self.path3)
    #                 self.scene.addItem(self.tempPath)


    #             elif self.shape=="Free pen":    # 自由风格画笔绘图的图元item.type()==2
    #                 self.setCursor(Qt.ArrowCursor)
    #                 if item == None:
    #                     pass
    #                 elif item != None:
    #                     item.setFlag(QGraphicsItem.ItemIsSelectable, enabled=False)
    #                     item.setFlag(QGraphicsItem.ItemIsMovable,enabled=False)
    #                 if self.path1:  # 即self.path1==True
    #                     self.path1.lineTo(event.pos())      # 移动并连接点
    #                     self.tempPath.setPath(self.path1)   # self.QGraphicsPath添加路径，如果写在上面的函数，是没线显示的，写在下面则在松键才出现线
    #                     self.scene.addItem(self.tempPath)


    #             elif self.shape=="line":    # 箭头类图元item.type()==2
    #                 self.setCursor(Qt.ArrowCursor)
    #                 if item == None:
    #                     pass
    #                 else:
    #                     item.setFlag(QGraphicsItem.ItemIsSelectable, enabled=False)
    #                     item.setFlag(QGraphicsItem.ItemIsMovable, enabled=False)
    #                 self.a.set_dst(self.wx, self.wy)  # 更新箭头类线条的末端点位置
    #                 self.a.update()   # 自定义箭头类图元刷新，不然没有双缓冲绘图效果
    #                 self.scene.addItem(self.a)


    #             elif self.shape=="move":   # 设置当self.shape=="Move"时，不做其他附加操作
    #                 self.setCursor(Qt.SizeAllCursor)
    #                 if item==None:
    #                     pass
    #                 else:
    #                     item.setFlag(QGraphicsItem.ItemIsSelectable,enabled=True)
    #                     item.setFlag(QGraphicsItem.ItemIsMovable,enabled=True)


    #         except Exception as e:
    #             print(e)
    #     # super().mouseMoveEvent(event)  # 该重置鼠标移动事件语句也可以写在这里

    # def mouseReleaseEvent(self, event):
    #     super().mouseReleaseEvent(event)   # 此重置句必须要有，目的是为了画完Item后Item，Item不会出现移动bug
    #     item = self.get_item_at_click(event)
    #     try:
    #         if self.shape=="rect":
    #             if item.isSelected():
    #                 pass
    #             else:
    #                 self.scene.removeItem(self.tempPath)
    #                 self.r = RectItem(self.pen_color,self.pen_width,self.tempPath.boundingRect())
    #                 self.scene.addItem(self.r)

    #         elif self.shape == "circle":
    #                 self.scene.removeItem(self.tempPath)
    #                 self.e = EllipseItem(self.pen_color,self.pen_width,self.tempPath.boundingRect())
    #                 self.scene.addItem(self.e)

    #     except Exception as e:
    #         print(e)

    #     # super().mouseReleaseEvent(event)  # 该重置鼠标移动事件语句也可以写在这里


    # def get_items_at_rubber(self):
    #     """ 返回选择区域内的Items"""
    #     area = self.graphicsView.rubberBandRect()
    #     return self.graphicsView.items(area)

