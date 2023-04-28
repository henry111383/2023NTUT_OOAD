import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from biolabel.model.point import *
from biolabel.views.Ui_label import *

class Label_RectLabelShouldBeCorrect(unittest.TestCase):
    def setUp(self):
        self.A = Point(10,10)
        self.B = Point(30,30)
        self.C = Point(20,30)
        self.D = Point(40,50)
        self.RectLabel1 = RectLabel([self.A, self.B], Qt.red , 5)
        self.RectLabel2 = RectLabel([self.C, self.D], Qt.red , 5)
        

    def tearDown(self):
        del self.A
        del self.B
        del self.C
        del self.D
        del self.RectLabel1
        del self.RectLabel2
        

    def test_RectLabel1_getPointList(self):
        expected = [self.A ,self.B]
        result = self.RectLabel1.getPointList()
        self.assertEqual(expected, result)

    def test_RectLabel2_getPointList(self):
        expected = [self.C ,self.D]
        result = self.RectLabel2.getPointList()
        self.assertEqual(expected, result)