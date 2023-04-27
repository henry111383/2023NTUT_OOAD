import unittest

from test_point import Point_PointShouldBeCorrect

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(Point_PointShouldBeCorrect)
    unittest.TextTestRunner(verbosity=2).run(tests)