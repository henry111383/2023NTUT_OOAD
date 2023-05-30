import unittest
import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from biolabel.model.LabelService import *
from biolabel.model.Label import *
class LabelService_LabelServiceShouldBeCorrect(unittest.TestCase):
    def setUp(self):
        self.LabelService = LabelService()
        self.A = Point(10,10)
        self.B = Point(30,30)
        self.C = Point(20,30)
        self.D = Point(40,50)
        self.E = Point(100,100)
        self.PolyLabel1 = Label('poly1', 'poly' ,[self.A, self.B, self.E])
        self.RectLabel2 = Label('RectLabel2', 'rect',[self.C, self.D])

    def tearDown(self):
        del self.A
        del self.B
        del self.C
        del self.D 
        del self.E
        del self.PolyLabel1 
        del self.RectLabel2
        
    def test_LabelService_CreateLabel(self):
        ExpectName = 'poly1'
        ExpectType = 'poly'
        ExpectptList = [self.A, self.B, self.E]
        NewLabel = self.LabelService.CreateLabel(ExpectName, ExpectType, ExpectptList)
        self.assertEqual(ExpectName ,NewLabel.GetName())
        self.assertEqual(ExpectType ,NewLabel.GetLabelType())
        self.assertEqual(ExpectptList ,NewLabel.GetPoint())
    def test_LabelService_MoveLabelOnePoint(self):
        MoveX = 40
        MoveY = 10
        index = 1
        MoveLabel = self.LabelService.moveLabel(MoveX,MoveY,index,self.PolyLabel1)
        ptList = MoveLabel.GetPoint()
        ExceptPoint = Point(70,40)
        self.assertEqual(ExceptPoint.GetX() , ptList[1].GetX())
        self.assertEqual(ExceptPoint.GetY() , ptList[1].GetY())
    def test_LabelService_MoveLabelAllePoint(self):
        MoveX = 10
        MoveY = 10
        index = len(self.PolyLabel1.GetPoint())
        MoveLabel = self.LabelService.moveLabel(MoveX,MoveY,index,self.PolyLabel1)
        ptList = MoveLabel.GetPoint()
        ExceptPoint0 = Point(20,20)
        ExceptPoint1 = Point(40,40)
        ExceptPoint2 = Point(110,110)
        self.assertEqual(ExceptPoint0.GetX() , ptList[0].GetX())
        self.assertEqual(ExceptPoint0.GetY() , ptList[0].GetY())
        self.assertEqual(ExceptPoint1.GetX() , ptList[1].GetX())
        self.assertEqual(ExceptPoint1.GetY() , ptList[1].GetY())
        self.assertEqual(ExceptPoint2.GetX() , ptList[2].GetX())
        self.assertEqual(ExceptPoint2.GetY() , ptList[2].GetY())
    def test_LabelService_UpdateLabelName(self):
        Name = "RectLabel1"
        UpdatedLabel = self.LabelService.UpdateLabelName(Name,self.RectLabel2)
        self.assertEqual(Name , UpdatedLabel.GetName())

   