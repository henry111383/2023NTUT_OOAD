from .Label import Label
from .Point import Point
from .LabelList import LabelList
class LabelService():
    def __init__(self):
        self.NameList = set()
        self.labelList = LabelList([])
    def CreateLabel(self, name, type, Color, ptList)->Label:
        self.NameList.add(name)
        return Label(name, type, Color , ptList)
    def moveLabel(self, moveX, moveY , index , Label)->Label:
        ptList = Label.GetPoint()
        ptNumber = len(ptList)
        if(index == ptNumber):
            for i in range (0,index):
                NewPoint = Point(0,0)
                pointX = ptList[i].GetX()+moveX
                pointY = ptList[i].GetY()+moveY
                NewPoint.SetX(pointX)
                NewPoint.SetY(pointY)
                Label.UpdatePoint(i,NewPoint)
        else:
            NewPoint = Point(30,0)
            pointX = ptList[index].GetX()+moveX
            pointY = ptList[index].GetY()+moveY
            NewPoint.SetX(pointX)
            NewPoint.SetY(pointY)
            Label.UpdatePoint(index,NewPoint)
        return Label
    def EditLabelName(self, Name, Label)->Label:
        Label.SetName(Name)
        return Label
    
    def EditLabelColor(self, color, Label)->Label:
        Label.SetLabelColor(color)
        return Label
    
    def DeleteLabel(self , label ) :
        try:
            self.labelList.RemoveLabel(label)
            return True
        except:
            print('Error! Not Found This Label')
            return False
    