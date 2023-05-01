import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from biolabel.model.Point import *
from biolabel.model.Label import *
from biolabel.model.LabelList import *

class Label_RectLabelShouldBeCorrect(unittest.TestCase):
    def setUp(self):
        self.A = Point(10,10)
        self.B = Point(30,30)
        self.C = Point(20,30)
        self.D = Point(40,50)
        self.Label1 = Label("test1","rect", [self.A, self.B])
        

    def tearDown(self):
        del self.A
        del self.B
        del self.C
        del self.D
        del self.Label1        

    def test_GetPoint(self):
        expected = [self.A ,self.B]
        result = self.Label1.GetPoint()
        self.assertEqual(expected, result)

    def test_AddPoint(self):
        addPoint = Point(50,60)
        self.Label1.AddPoint(addPoint)
        self.assertEqual(addPoint,self.Label1.GetPoint()[-1])
    def test_RemovePoint(self):
        self.Label1.AddPoint(self.C)
        self.Label1.AddPoint(self.D)
        self.Label1.RemovePoint(1)
        result = self.Label1.GetPoint()
        self.assertEqual(self.A,result[0])
        self.assertEqual(self.C,result[1])
        self.assertEqual(self.D,result[2])
    def test_UpdatePoint(self):
        self.Label1.UpdatePoint(1,self.C)
        result = self.Label1.GetPoint()
        self.assertEqual(self.A,result[0])
        self.assertEqual(self.C,result[1])
    def test_GetName(self):
        expect = "test1"
        result = self.Label1.GetName()
        self.assertEqual(expect,result)
    def test_SetName(self):
        new_Name = "test2"
        self.Label1.SetName(new_Name)
        result = self.Label1.GetName()
        self.assertEqual(new_Name,result)
    def test_GetLabelType(self):
        expect = "rect"
        result = self.Label1.GetLabelType()
        self.assertEqual(expect,result)