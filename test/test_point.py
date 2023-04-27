import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from biolabel.utils.point import Point

class Point_PointShouldBeCorrect(unittest.TestCase):
    def setUp(self):
        self.pt1 = Point(3,4)
        self.pt2 = Point(0,0)

    def tearDown(self):
        del self.pt1
        del self.pt2

    def test_pt1_x(self):
        expected = 3
        result = self.pt1.x()
        self.assertAlmostEqual(expected, result)

    def test_pt1_y(self):
        expected = 4
        result = self.pt1.y()
        self.assertAlmostEqual(expected, result)

    def test_pt2_x(self):
        expected = 0
        result = self.pt2.x()
        self.assertAlmostEqual(expected, result)

    def test_pt2_y(self):
        expected = 0
        result = self.pt2.y()
        self.assertAlmostEqual(expected, result)

    def test_distance(self):
        expected = 5
        result = self.pt1.distance(self.pt2)


