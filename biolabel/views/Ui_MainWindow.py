# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRectF, Qt, QPointF ,QLineF ,QSize
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QBrush,QFont, QColor ,QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene,QWidget ,QGraphicsItem , QGraphicsPathItem,QDialog,QGraphicsTextItem, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setSpacing(0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        # === font of toolButton ===
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        # ==========================

        # === toolButton: CreateLabel ===
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("biolabel/icons/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_11.addWidget(self.toolButton)

        # === toolButton: EditLabel ===
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("biolabel/icons/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_11.addWidget(self.toolButton_2)

        # === toolButton: DIP ===
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("biolabel/icons/edit-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout_11.addWidget(self.toolButton_3)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.listWidget_6 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_6.setObjectName("listWidget_6")
        self.verticalLayout_11.addWidget(self.listWidget_6)
        self.horizontalLayout_1.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.graphicsView_2 = GraphicView()
        self.graphicsView_2.setObjectName("graphicsView_2")
        # self.canvas = QGraphicsView()
        self.verticalLayout_10.addWidget(self.graphicsView_2)
        self.horizontalLayout_1.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setObjectName("listView_3")
        self.verticalLayout_9.addWidget(self.listView_3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setObjectName("listWidget_5")
        self.verticalLayout_9.addWidget(self.listWidget_5)
        self.horizontalLayout_1.addLayout(self.verticalLayout_9)
        self.horizontalLayout_1.setStretch(0, 1)
        self.horizontalLayout_1.setStretch(1, 7)
        self.horizontalLayout_1.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpenFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenFolder.setObjectName("actionOpenDir")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport_2 = QtWidgets.QAction(MainWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExport_Labeels = QtWidgets.QAction(MainWindow)
        self.actionExport_Labeels.setObjectName("actionExport_Labeels")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpenFolder)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_2)
        self.menuFile.addAction(self.actionExport_Labeels)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "Create Label"))
        self.toolButton_2.setText(_translate("MainWindow", "Edit Label"))
        self.toolButton_3.setText(_translate("MainWindow", "DIP"))
        self.label_9.setText(_translate("MainWindow", "Label Name"))
        self.label_8.setText(_translate("MainWindow", "Label List"))
        self.label_7.setText(_translate("MainWindow", " File List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "OpenFile"))
        self.actionOpenFolder.setText(_translate("MainWindow", "OpenFolder"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExport_2.setText(_translate("MainWindow", "Export Image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExport_Labeels.setText(_translate("MainWindow", "Export Labels"))


class MyScene(QGraphicsScene):#自定场景
    pen_color=Qt.red    #畫筆顏色
    pen_width = 5       #畫筆粗細
    def __init__(self):#初始函数
        super(MyScene, self).__init__(parent=None) #实例化QGraphicsScene
        # self.setSceneRect(0,0,300,400) #设置场景起始及大小，默认场景是中心为起始，不方便后面的代码

        # self.setForegroundBrush(Qt.white)
        self.EraseMode=False

        self.shape= "Free pen"
        
        # rect=QGraphicsRectItem(0,0,50,50)
        # rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        # rect.setPos(60,100)
        # self.addItem(rect)

    def drawBackground(self, painter: QPainter, rect: QRectF):
        painter.drawRect(0,0,600,500)


    def Eraser(self,b=False):
        self.EraseMode = b
        return self.EraseMode

    def Shape(self, s):
         self.shape = s
         return self.Shape


    def ChangePenColor(self, color):
        self.pen_color = QColor(color)

    def ChangePenThickness(self, thickness):
        self.pen_width=thickness

    def ChangeEraserThickness(self,EraserThickness):
        self.Eraser_pen_width=EraserThickness
    def mousePressEvent(self, event):
        """重载鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            # 获取鼠标在场景中的坐标
            pos = event.scenePos()
            # 在场景中添加一个新的矩形
            print(pos)

class GraphicView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            self.scene = QGraphicsScene()  # 设置管理QgraphicsItems的场景
            self.shape = "rect"   # 预设画笔为自由风格画笔
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
            self.scene.addRect(0, 0, 100, 100, QPen(Qt.black), QBrush(Qt.red))
        except Exception as e:
            print(e)

    def Shape(self, s):
        """返回画笔属性状态"""
        self.shape = s
        if self.shape == "move":
            self.setDragMode(QGraphicsView.RubberBandDrag)   # 设置为支持橡皮筋框选模式
        else:
            self.setDragMode(QGraphicsView.NoDrag)     # 其他情况设置为不可拖拽模式
        return self.shape

    def ChangePenColor(self, color):
        """返回变更的画笔颜色"""
        self.pen_color = QColor(color)    # 当画笔颜色变化时，设置画笔颜色
        return self.pen_color

    def ChangePenThickness(self, thickness):
        """返回变更的画笔粗细"""
        self.pen_width=thickness   # 当画笔颜色变化时，设置画笔粗细

    def get_item_at_click(self, event):  # 返回鼠标点击的QgraphicsItem
        """ 返回你所点击的item """
        pos = event.pos()     # 注意此时是Qgraphicsview的鼠标点击位置
        # x=self.graphicsView.mapFromParent(pos)
        # y=self.graphicsView.mapFromScene(pos)
        # z=self.graphicsView.mapFromGlobal(pos)
        # print(pos,x,y,z)
        # print(pos)
        item = self.itemAt(pos)
        return item


    def mousePressEvent(self, event):
        """重载鼠标按下事件"""
        super(GraphicView,self).mousePressEvent(event)   # 此重置句必须要有，目的是为了画完Item后Item可被选择

        try:
            self.lastPoint = event.pos()  # 记录鼠标在Qgraphicsview按下的位置点
            print(self.lastPoint)
            self.x = self.lastPoint.x()
            self.y = self.lastPoint.y()

            pos = event.pos()   # 记录鼠标按下的位置
            self.t=self.mapToScene(pos)

            item = self.get_item_at_click(event)   # 记录鼠标点击Item的信息，若无Item，此函数返回None



            """"鼠标右键按下Item时，将其删除事件"""
            if event.button() == Qt.RightButton:
                if isinstance(item, QGraphicsItem):
                    self.scene.removeItem(item)

            """"触发鼠标左件事件"""
            if event.button() == Qt.LeftButton:

                self.tempPath = QGraphicsPathItem()  # 设置一个内存上的QGraphicsPathItem，方便MouseMoveEvent画图时有双缓冲绘图效果
                self.tempPath.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable
                                    | QtWidgets.QGraphicsItem.ItemIsMovable
                                    | QtWidgets.QGraphicsItem.ItemIsFocusable
                                    | QtWidgets.QGraphicsItem.ItemSendsGeometryChanges
                                    | QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)

                self.path1 = QPainterPath()    # 实例路径函数，用于自由画笔风格
                self.path1.moveTo(pos)    # 设置路径开始点

                if self.shape == "line":
                    self.a = Arrow(self.scene, self.pen_color, self.pen_width)   # 设置实例化自定义的箭头类，但不传入起始点位置参数
                    self.a.set_src(self.x, self.y)    # 设置自定义箭头类的箭头线起始点

                # 千万不要再初始化__init__那里设置画笔Qpen，不然笔颜色，大小无法修改
                pp=QPen()    # 实例QPen
                pp.setColor(self.pen_color)    #设置颜色
                pp.setWidth(self.pen_width)    #设置宽度

                self.tempPath.setPen(pp)     # self.tempPath应用笔
                if item != None:
                    self.wl=item.boundingRect().width()


        except Exception as e:
            print(e)


    def mouseMoveEvent(self,event):
        """重载鼠标移动事件"""
        super(GraphicView, self).mouseMoveEvent(event)    # 此重置句必须要有，目的是为了画完Item后Item可被移动，可放在MouseMoveEvent最后

        self.endPoint = event.pos()    # 返回鼠标移动时的点位置
        self.wx = self.endPoint.x()
        self.wy = self.endPoint.y()

        self.w = self.wx-self.x   # 用于绘画矩形Rect和Ellipse图形时的宽（长）
        self.h = self.wy-self.y   # 用于绘画矩形Rect和Ellipse图形时的高（宽）

        self.m = self.mapFromScene(event.pos())
        item = self.get_item_at_click(event)

        if event.buttons() & Qt.LeftButton : #仅左键时触发，event.button返回notbutton，需event.buttons()判断，这应是对象列表，用&判断

            try:
                # if item != None and isinstance(item,QGraphicsRectItem)==False:
                if item != None and item.type() != 4:    # 判断自定义的图片类（自己设置了图片的type()=4）时，画笔可以在图片上画图，而不会使图片在绘图时移动
                    super(GraphicView, self).mouseMoveEvent(event)

                elif self.shape=="circle":    # 圆形的item.type()=3
                    self.setCursor(Qt.ArrowCursor)   # 设置鼠标形状
                    if item == None:    # 若无点击Item时，画笔可以画圆形
                        pass
                    else:   # 若鼠标有点击图片类Item，设置该图片图元不可被选择和不可移动
                        item.setFlag(QGraphicsItem.ItemIsMovable,enabled=False)
                        item.setFlag(QGraphicsItem.ItemIsSelectable,enabled=False)
                    self.path2 = QPainterPath()    # 为了实现双缓冲的效果，另设一个QPainterPath
                    self.path2.addEllipse(self.t.x(), self.t.y(), self.w, self.h)  # 添加绘图路径
                    self.tempPath.setPath(self.path2)  # 由于self.path2是在内存上一直刷新，并销毁之前的绘图路径，此时tempath设置路径就能在绘图时有双缓冲效果
                    self.scene.addItem(self.tempPath)  # Myscene()场景中添加图元


                elif self.shape=="rect":   # 矩形的item.type()=3
                    self.setCursor(Qt.ArrowCursor)
                    if item == None:
                        pass
                    else:
                        item.setFlag(QGraphicsItem.ItemIsSelectable, enabled=False)
                        item.setFlag(QGraphicsItem.ItemIsMovable,enabled=False)
                    self.path3 = QPainterPath()
                    self.path3.addRect(self.x, self.y, self.w, self.h)
                    self.tempPath.setPath(self.path3)
                    self.scene.addItem(self.tempPath)


                elif self.shape=="Free pen":    # 自由风格画笔绘图的图元item.type()==2
                    self.setCursor(Qt.ArrowCursor)
                    if item == None:
                        pass
                    elif item != None:
                        item.setFlag(QGraphicsItem.ItemIsSelectable, enabled=False)
                        item.setFlag(QGraphicsItem.ItemIsMovable,enabled=False)
                    if self.path1:  # 即self.path1==True
                        self.path1.lineTo(event.pos())      # 移动并连接点
                        self.tempPath.setPath(self.path1)   # self.QGraphicsPath添加路径，如果写在上面的函数，是没线显示的，写在下面则在松键才出现线
                        self.scene.addItem(self.tempPath)


                elif self.shape=="line":    # 箭头类图元item.type()==2
                    self.setCursor(Qt.ArrowCursor)
                    if item == None:
                        pass
                    else:
                        item.setFlag(QGraphicsItem.ItemIsSelectable, enabled=False)
                        item.setFlag(QGraphicsItem.ItemIsMovable, enabled=False)
                    self.a.set_dst(self.wx, self.wy)  # 更新箭头类线条的末端点位置
                    self.a.update()   # 自定义箭头类图元刷新，不然没有双缓冲绘图效果
                    self.scene.addItem(self.a)


                elif self.shape=="move":   # 设置当self.shape=="Move"时，不做其他附加操作
                    self.setCursor(Qt.SizeAllCursor)
                    if item==None:
                        pass
                    else:
                        item.setFlag(QGraphicsItem.ItemIsSelectable,enabled=True)
                        item.setFlag(QGraphicsItem.ItemIsMovable,enabled=True)


            except Exception as e:
                print(e)
        # super().mouseMoveEvent(event)  # 该重置鼠标移动事件语句也可以写在这里

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)   # 此重置句必须要有，目的是为了画完Item后Item，Item不会出现移动bug
        item = self.get_item_at_click(event)
        try:
            if self.shape=="rect":
                if item.isSelected():
                    pass
                else:
                    self.scene.removeItem(self.tempPath)
                    self.r = RectItem(self.pen_color,self.pen_width,self.tempPath.boundingRect())
                    self.scene.addItem(self.r)

            elif self.shape == "circle":
                    self.scene.removeItem(self.tempPath)
                    self.e = EllipseItem(self.pen_color,self.pen_width,self.tempPath.boundingRect())
                    self.scene.addItem(self.e)

        except Exception as e:
            print(e)

        # super().mouseReleaseEvent(event)  # 该重置鼠标移动事件语句也可以写在这里


    def get_items_at_rubber(self):
        """ 返回选择区域内的Items"""
        area = self.graphicsView.rubberBandRect()
        return self.graphicsView.items(area)

class RectHandle(QGraphicsRectItem):  #QGraphicsRectItem
    """ 自定义小handles的名称、序号、控制点位置"""
    # handles 按照顺时针排列
    handle_names = ('left_top', 'middle_top', 'right_top', 'right_middle',
                    'right_bottom', 'middle_bottom', 'left_bottom', 'left_middle')
    # 设定在控制点上的光标形状
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
    offset = 6.0  # 外边界框相对于内边界框的偏移量，也是控制点的大小
    #min_size = 8 * offset  # 矩形框的最小尺寸

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

class RectItem(RectHandle):
    """ 自定义可变矩形类"""
    def __init__(self, color,width,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handles = {}  # 控制点的字典
        self.setAcceptHoverEvents(True)  # 设定为接受 hover 事件
        self.setFlags(QGraphicsItem.ItemIsSelectable |  # 设定矩形框为可选择的
                      QGraphicsItem.ItemSendsGeometryChanges |  # 追踪图元改变的信息
                      QGraphicsItem.ItemIsFocusable |  # 可聚焦
                      QGraphicsItem.ItemIsMovable)  # 可移动
        self.update_handles_pos()  # 初始化控制点
        self.reset_Ui()  # 初始化 UI 变量
        self.pen_color=color
        self.pen_width=width

    def reset_Ui(self):
        '''初始化 UI 变量'''
        self.handleSelected = None  # 被选中的控制点
        self.mousePressPos = None  # 鼠标按下的位置
        #self.mousePressRect = None  # 鼠标按下的位置所在的图元的外边界框

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
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return

    def hoverMoveEvent(self, event):
        """
        当鼠标移到该 item（未按下）上时执行。
        """
        super().hoverMoveEvent(event)
        handle = self.handle_at(event.pos())
        cursor = self.handle_cursors[handle] if handle in self.handles else Qt.ArrowCursor
        self.setCursor(cursor)

    def hoverLeaveEvent(self, event):
        """
        当鼠标离开该形状（未按下）上时执行。
        """
        super().hoverLeaveEvent(event)
        self.setCursor(Qt.ArrowCursor)  # 设定鼠标光标形状

    def mousePressEvent(self, event):
        """
        当在 item 上按下鼠标时执行。
        """
        super().mousePressEvent(event)
        self.handleSelected = self.handle_at(event.pos())
        if self.handleSelected in self.handles:
            self.mousePressPos = event.pos()

    def mouseReleaseEvent(self, event):
        """
        Executed when the mouse is released from the item.
        """
        super().mouseReleaseEvent(event)
        self.update()
        self.reset_Ui()

    def mouseMoveEvent(self, event):
        """
        Executed when the mouse is being moved over the item while being pressed.
        """
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

class EllipseItem(RectHandle):
    """ 自定义可变椭圆类"""
    def __init__(self, color,width,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handles = {}  # 控制点的字典
        self.setAcceptHoverEvents(True)  # 设定为接受 hover 事件
        self.setFlags(QGraphicsItem.ItemIsSelectable |  # 设定矩形框为可选择的
                      QGraphicsItem.ItemSendsGeometryChanges |  # 追踪图元改变的信息
                      QGraphicsItem.ItemIsFocusable |  # 可聚焦
                      QGraphicsItem.ItemIsMovable)  # 可移动
        self.update_handles_pos()  # 初始化控制点
        self.reset_Ui()  # 初始化 UI 变量
        self.pen_color=color
        self.pen_width=width

    def reset_Ui(self):
        '''初始化 UI 变量'''
        self.handleSelected = None  # 被选中的控制点
        self.mousePressPos = None  # 鼠标按下的位置
        #self.mousePressRect = None  # 鼠标按下的位置所在的图元的外边界框

    def boundingRect(self):
        """
        限制图元的可视化区域，且防止出现图元移动留下残影的情况
        """
        o = self.offset
        # 添加一个间隔为 o 的外边框
        return self.rect().adjusted(-o, -o, o, o)

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        # painter.setBrush(QBrush(QColor(255, 0, 0, 100)))
        painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
        # painter.drawRect(self.rect())
        painter.drawEllipse(self.rect())



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
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return

    def hoverMoveEvent(self, event):
        """
        当鼠标移到该 item（未按下）上时执行。
        """
        super().hoverMoveEvent(event)
        handle = self.handle_at(event.pos())
        cursor = self.handle_cursors[handle] if handle in self.handles else Qt.ArrowCursor
        self.setCursor(cursor)

    def hoverLeaveEvent(self, event):
        """
        当鼠标离开该形状（未按下）上时执行。
        """
        super().hoverLeaveEvent(event)
        self.setCursor(Qt.ArrowCursor)  # 设定鼠标光标形状

    def mousePressEvent(self, event):
        """
        当在 item 上按下鼠标时执行。
        """
        super().mousePressEvent(event)
        self.handleSelected = self.handle_at(event.pos())
        if self.handleSelected in self.handles:
            self.mousePressPos = event.pos()

    def mouseReleaseEvent(self, event):
        """
        Executed when the mouse is released from the item.
        """
        super().mouseReleaseEvent(event)
        self.update()
        self.reset_Ui()

    def mouseMoveEvent(self, event):
        """
        Executed when the mouse is being moved over the item while being pressed.
        """
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

class Arrow(QGraphicsPathItem):
    """ 自定义箭头类，类重写的是QGraphicsPathItem"""
    def __init__(self, scene, color, penwidth, parent=None):
        super().__init__(parent)
        self.pen_color = color    # 从Qgraphicsview导入笔的颜色
        self.pen_width = penwidth    # 从Qgraphicsview导入笔的宽度

        self.scene = scene     #从Qgraphicsview导入Myscene()这个场景，并设置为它

        self.pos_src = [0, 0]
        self.pos_dst = [0, 0]

        self.setFlags(QGraphicsItem.ItemIsSelectable |  # 设定矩形框为可选择的
                      QGraphicsItem.ItemSendsGeometryChanges |  # 追踪图元改变的信息
                      QGraphicsItem.ItemIsFocusable |  # 可聚焦
                      QGraphicsItem.ItemIsMovable)  # 可移动

    def set_src(self, x, y):
        self.pos_src = [x, y]

    def set_dst(self, x, y):
        self.pos_dst = [x, y]

    def calc_path(self):
        path = QPainterPath(QPointF(self.pos_src[0], self.pos_src[1]))
        path.lineTo(self.pos_dst[0], self.pos_dst[1])
        return path

    def boundingRect(self):
        o=self.offset=self.pen_width*10
        x1, y1 = self.pos_src
        x2=self.shape().boundingRect().width()
        y2=self.shape().boundingRect().height()
        self.QF=QRectF(x1,y1,x2,y2)
        return self.shape().boundingRect().adjusted(-o, -o, o, o)
        # return self.QF.adjusted(-o,-o,o,o)


    def shape(self):
        return self.calc_path()

    def paint(self, painter, option, widget=None):
        self.setPath(self.calc_path())
        path = self.path()
        painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
        painter.drawPath(path)

        x1, y1 = self.pos_src
        x2, y2 = self.pos_dst

        self.source = QPointF(x1, y1)
        self.dest = QPointF(x2, y2)
        self.line = QLineF(self.source, self.dest)
        # 设置垂直向量
        v = self.line.unitVector()
        v.setLength(self.pen_width*4)
        v.translate(QPointF(self.line.dx(), self.line.dy()))
        # 设置水平向量
        n = v.normalVector()
        n.setLength(n.length() * 0.5)
        n2 = n.normalVector().normalVector()
        # 设置箭头三角形的三个点
        p1 = v.p2()
        p2 = n.p2()
        p3 = n2.p2()
        # 以下用于绘制箭头，外边框粗为1.0
        painter.setPen(QPen(self.pen_color, 1.0, Qt.SolidLine))
        painter.setBrush(self.pen_color)
        painter.drawPolygon(p1, p2, p3)

