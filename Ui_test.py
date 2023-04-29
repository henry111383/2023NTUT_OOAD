from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem,QGraphicsItem
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import QPointF, Qt

class MyPointItem(QGraphicsEllipseItem):
    def __init__(self, x, y, radius=5, parent=None):
        super().__init__(parent)
        self.setPos(x, y)
        self.setRect(-radius, -radius, radius*2, radius*2)
        self.setBrush(QBrush(QColor(Qt.red)))
        self.setFlags(QGraphicsEllipseItem.ItemIsMovable | QGraphicsEllipseItem.ItemSendsScenePositionChanges)

    def itemChange(self, change, value):
        if change == QGraphicsEllipseItem.ItemScenePositionHasChanged:
            self.parentItem().updateLine()
        return super().itemChange(change, value)


class MyLineItem(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2, parent=None):
        super().__init__(x1, y1, x2, y2, parent)
        # self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.point1 = MyPointItem(x1, y1, parent=self)
        self.point2 = MyPointItem(x2, y2, parent=self)
        
    def updateLine(self):
        start = self.point1.scenePos()
        end = self.point2.scenePos()
        self.setLine(start.x(), start.y(), end.x(), end.y())

if __name__ == '__main__':
    app = QApplication([])
    scene = QGraphicsScene()
    view = QGraphicsView(scene)
    line = MyLineItem(100, 100, 300, 300)
    scene.addItem(line)
    view.show()
    app.exec_()