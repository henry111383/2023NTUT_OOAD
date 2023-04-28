from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRectF, Qt, QPointF ,QLineF ,QSize
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QBrush,QFont, QColor ,QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class Label(QGraphicsRectItem):
    PointList = []

class RectHandle(Label):  #QGraphicsRectItem
    """ 用矩形控制Label """

    # handles 按照順時針排列
    handle_names = ('left_top', 'middle_top', 'right_top', 'right_middle',
                    'right_bottom', 'middle_bottom', 'left_bottom', 'left_middle')
    
    # 設定在控制點的鼠標樣式
    handle_cursors = {
        0: Qt.SizeFDiagCursor,
        1: Qt.SizeVerCursor,
        2: Qt.SizeBDiagCursor,
        3: Qt.SizeHorCursor,
        4: Qt.SizeFDiagCursor,
        5: Qt.SizeVerCursor,
        6: Qt.SizeBDiagCursor,
        7: Qt.SizeHorCursor
    }
    # 控制點的圓點半徑大小
    offset = 6.0  
    
    # 讓鼠標能圈選的模式
    EditMode = False

    def update_handles_pos(self):
        """
        更新控制点的位置
        """
        o = self.offset  # 偏置量
        s = o*2  # handle 的大小
        b = self.rect()  # 获取内边框
        x1, y1 = b.left(), b.top()  # 左上角坐标
        offset_x = b.width()/2
        offset_y = b.height()/2
        # 设置 handles 的位置
        self.handles[0] = QRectF(x1-o, y1-o, s, s)
        self.handles[1] = self.handles[0].adjusted(offset_x, 0, offset_x, 0)
        self.handles[2] = self.handles[1].adjusted(offset_x, 0, offset_x, 0)
        self.handles[3] = self.handles[2].adjusted(0, offset_y, 0, offset_y)
        self.handles[4] = self.handles[3].adjusted(0, offset_y, 0, offset_y)
        self.handles[5] = self.handles[4].adjusted(-offset_x, 0, -offset_x, 0)
        self.handles[6] = self.handles[5].adjusted(-offset_x, 0, -offset_x, 0)
        self.handles[7] = self.handles[6].adjusted(0, -offset_y, 0, -offset_y)

class RectLabel(RectHandle):
    """ 自定义可变矩形类"""
    def __init__(self, ptList, color, width, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handles = {}  # 控制点的字典
        self.setAcceptHoverEvents(True)  # 设定为接受 hover 事件
        # self.setFlags(QGraphicsItem.ItemIsSelectable |  # 设定矩形框为可选择的
        #               QGraphicsItem.ItemSendsGeometryChanges |  # 追踪图元改变的信息
        #               QGraphicsItem.ItemIsFocusable |  # 可聚焦
        #               QGraphicsItem.ItemIsMovable)  # 可移动
        self.update_handles_pos()  # 初始化控制点
        self.reset_Ui()  # 初始化 UI 变量
        self.pen_color = color
        self.pen_width = width
        self.PointList.clear()
        self.PointList = ptList

    def reset_Ui(self):
        '''初始化 UI 变量'''
        self.handleSelected = None  # 被选中的控制点
        self.mousePressPos = None  # 鼠标按下的位置
        #self.mousePressRect = None  # 鼠标按下的位置所在的图元的外边界框

    def getPointList(self):
        return self.PointList

    def boundingRect(self):
        """
        限制图元的可视化区域，且防止出现图元移动留下残影的情况
        """
        o = self.offset
        # 添加一个间隔为 o 的外边框
        return self.rect().adjusted(-o,-o,o,o)

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        # painter.setBrush(QBrush(QColor(255, 0, 0, 100)))
        painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
        painter.drawRect(self.rect())
        # painter.drawEllipse(self.rect())


        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 0, 200)))
        painter.setPen(QPen(QColor(0, 0, 0, 255), 0,
                                  Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

        for shape in self.handles.values():
            if self.isSelected():
                painter.drawEllipse(shape)

    def handle_at(self, point):
        """
        返回给定 point 下的控制点 handle
        """
        if self.EditMode :
            for k, v, in self.handles.items():
                if v.contains(point):
                    return k
            return

    def hoverMoveEvent(self, event):
        """
        当鼠标移到该 item（未按下）上时执行。
        """
        if self.EditMode :
            super().hoverMoveEvent(event)
            handle = self.handle_at(event.pos())
            cursor = self.handle_cursors[handle] if handle in self.handles else Qt.ArrowCursor
            self.setCursor(cursor)

    def hoverLeaveEvent(self, event):
        """
        当鼠标离开该形状（未按下）上时执行。
        """
        if self.EditMode :
            super().hoverLeaveEvent(event)
            self.setCursor(Qt.ArrowCursor)  # 设定鼠标光标形状

    def mousePressEvent(self, event):
        """
        当在 item 上按下鼠标时执行。
        """
        if self.EditMode :
            super().mousePressEvent(event)
            self.handleSelected = self.handle_at(event.pos())
            if self.handleSelected in self.handles:
                self.mousePressPos = event.pos()

    def mouseReleaseEvent(self, event):
        """
        Executed when the mouse is released from the item.
        """
        if self.EditMode :
            super().mouseReleaseEvent(event)
            self.update()
            self.reset_Ui()

    def mouseMoveEvent(self, event):
        """
        Executed when the mouse is being moved over the item while being pressed.
        """
        if self.EditMode :
            if self.handleSelected in self.handles:
                self.interactiveResize(event.pos())
            else:
                super().mouseMoveEvent(event)

    def interactiveResize(self, mousePos):
        """
        Perform shape interactive resize.
        """
        rect = self.rect()
        self.prepareGeometryChange()
        # movePos = mousePos - self.mousePressPos
        # move_x, move_y = movePos.x(), movePos.y()
        if self.handleSelected == 0:
            rect.setTopLeft(mousePos)
        elif self.handleSelected == 1:
            rect.setTop(mousePos.y())
        elif self.handleSelected == 2:
            rect.setTopRight(mousePos)
        elif self.handleSelected == 3:
            rect.setRight(mousePos.x())
        elif self.handleSelected == 4:
            rect.setBottomRight(mousePos)
        elif self.handleSelected == 5:
            rect.setBottom(mousePos.y())
        elif self.handleSelected == 6:
            rect.setBottomLeft(mousePos)
        elif self.handleSelected == 7:
            rect.setLeft(mousePos.x())
        self.setRect(rect)
        self.update_handles_pos()

# class EllipseItem(RectHandle):
#     """ 自定义可变椭圆类"""
#     def __init__(self, color,width,*args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.handles = {}  # 控制点的字典
#         self.setAcceptHoverEvents(True)  # 设定为接受 hover 事件
#         self.setFlags(QGraphicsItem.ItemIsSelectable |  # 设定矩形框为可选择的
#                       QGraphicsItem.ItemSendsGeometryChanges |  # 追踪图元改变的信息
#                       QGraphicsItem.ItemIsFocusable |  # 可聚焦
#                       QGraphicsItem.ItemIsMovable)  # 可移动
#         self.update_handles_pos()  # 初始化控制点
#         self.reset_Ui()  # 初始化 UI 变量
#         self.pen_color=color
#         self.pen_width=width

#     def reset_Ui(self):
#         '''初始化 UI 变量'''
#         self.handleSelected = None  # 被选中的控制点
#         self.mousePressPos = None  # 鼠标按下的位置
#         #self.mousePressRect = None  # 鼠标按下的位置所在的图元的外边界框

#     def boundingRect(self):
#         """
#         限制图元的可视化区域，且防止出现图元移动留下残影的情况
#         """
#         o = self.offset
#         # 添加一个间隔为 o 的外边框
#         return self.rect().adjusted(-o, -o, o, o)

#     def paint(self, painter, option, widget=None):
#         """
#         Paint the node in the graphic view.
#         """
#         # painter.setBrush(QBrush(QColor(255, 0, 0, 100)))
#         painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
#         # painter.drawRect(self.rect())
#         painter.drawEllipse(self.rect())



#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setBrush(QBrush(QColor(255, 255, 0, 200)))
#         painter.setPen(QPen(QColor(0, 0, 0, 255), 0,
#                                   Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

#         for shape in self.handles.values():
#             if self.isSelected():
#                 painter.drawEllipse(shape)

#     def handle_at(self, point):
#         """
#         返回给定 point 下的控制点 handle
#         """
#         for k, v, in self.handles.items():
#             if v.contains(point):
#                 return k
#         return

#     def hoverMoveEvent(self, event):
#         """
#         当鼠标移到该 item（未按下）上时执行。
#         """
#         super().hoverMoveEvent(event)
#         handle = self.handle_at(event.pos())
#         cursor = self.handle_cursors[handle] if handle in self.handles else Qt.ArrowCursor
#         self.setCursor(cursor)

#     def hoverLeaveEvent(self, event):
#         """
#         当鼠标离开该形状（未按下）上时执行。
#         """
#         super().hoverLeaveEvent(event)
#         self.setCursor(Qt.ArrowCursor)  # 设定鼠标光标形状

#     def mousePressEvent(self, event):
#         """
#         当在 item 上按下鼠标时执行。
#         """
#         super().mousePressEvent(event)
#         self.handleSelected = self.handle_at(event.pos())
#         if self.handleSelected in self.handles:
#             self.mousePressPos = event.pos()

#     def mouseReleaseEvent(self, event):
#         """
#         Executed when the mouse is released from the item.
#         """
#         super().mouseReleaseEvent(event)
#         self.update()
#         self.reset_Ui()

#     def mouseMoveEvent(self, event):
#         """
#         Executed when the mouse is being moved over the item while being pressed.
#         """
#         if self.handleSelected in self.handles:
#             self.interactiveResize(event.pos())
#         else:
#             super().mouseMoveEvent(event)

#     def interactiveResize(self, mousePos):
#         """
#         Perform shape interactive resize.
#         """
#         rect = self.rect()
#         self.prepareGeometryChange()
#         # movePos = mousePos - self.mousePressPos
#         # move_x, move_y = movePos.x(), movePos.y()
#         if self.handleSelected == 0:
#             rect.setTopLeft(mousePos)
#         elif self.handleSelected == 1:
#             rect.setTop(mousePos.y())
#         elif self.handleSelected == 2:
#             rect.setTopRight(mousePos)
#         elif self.handleSelected == 3:
#             rect.setRight(mousePos.x())
#         elif self.handleSelected == 4:
#             rect.setBottomRight(mousePos)
#         elif self.handleSelected == 5:
#             rect.setBottom(mousePos.y())
#         elif self.handleSelected == 6:
#             rect.setBottomLeft(mousePos)
#         elif self.handleSelected == 7:
#             rect.setLeft(mousePos.x())
#         self.setRect(rect)
#         self.update_handles_pos()

# class Arrow(QGraphicsPathItem):
#     """ 自定义箭头类，类重写的是QGraphicsPathItem"""
#     def __init__(self, scene, color, penwidth, parent=None):
#         super().__init__(parent)
#         self.pen_color = color    # 从Qgraphicsview导入笔的颜色
#         self.pen_width = penwidth    # 从Qgraphicsview导入笔的宽度

#         self.scene = scene     #从Qgraphicsview导入Myscene()这个场景，并设置为它

#         self.pos_src = [0, 0]
#         self.pos_dst = [0, 0]

#         self.setFlags(QGraphicsItem.ItemIsSelectable |  # 设定矩形框为可选择的
#                       QGraphicsItem.ItemSendsGeometryChanges |  # 追踪图元改变的信息
#                       QGraphicsItem.ItemIsFocusable |  # 可聚焦
#                       QGraphicsItem.ItemIsMovable)  # 可移动

#     def set_src(self, x, y):
#         self.pos_src = [x, y]

#     def set_dst(self, x, y):
#         self.pos_dst = [x, y]

#     def calc_path(self):
#         path = QPainterPath(QPointF(self.pos_src[0], self.pos_src[1]))
#         path.lineTo(self.pos_dst[0], self.pos_dst[1])
#         return path

#     def boundingRect(self):
#         o=self.offset=self.pen_width*10
#         x1, y1 = self.pos_src
#         x2=self.shape().boundingRect().width()
#         y2=self.shape().boundingRect().height()
#         self.QF=QRectF(x1,y1,x2,y2)
#         return self.shape().boundingRect().adjusted(-o, -o, o, o)
#         # return self.QF.adjusted(-o,-o,o,o)


#     def shape(self):
#         return self.calc_path()

#     def paint(self, painter, option, widget=None):
#         self.setPath(self.calc_path())
#         path = self.path()
#         painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
#         painter.drawPath(path)

#         x1, y1 = self.pos_src
#         x2, y2 = self.pos_dst

#         self.source = QPointF(x1, y1)
#         self.dest = QPointF(x2, y2)
#         self.line = QLineF(self.source, self.dest)
#         # 设置垂直向量
#         v = self.line.unitVector()
#         v.setLength(self.pen_width*4)
#         v.translate(QPointF(self.line.dx(), self.line.dy()))
#         # 设置水平向量
#         n = v.normalVector()
#         n.setLength(n.length() * 0.5)
#         n2 = n.normalVector().normalVector()
#         # 设置箭头三角形的三个点
#         p1 = v.p2()
#         p2 = n.p2()
#         p3 = n2.p2()
#         # 以下用于绘制箭头，外边框粗为1.0
#         painter.setPen(QPen(self.pen_color, 1.0, Qt.SolidLine))
#         painter.setBrush(self.pen_color)
#         painter.drawPolygon(p1, p2, p3)

