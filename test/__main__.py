import unittest

from test_point import Point_PointShouldBeCorrect
from test_label import Label_RectLabelShouldBeCorrect 

if __name__ == '__main__':
    
    Alltest = []
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(Point_PointShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(Label_RectLabelShouldBeCorrect))
    
    testGroup = unittest.TestSuite(Alltest)
    unittest.TextTestRunner(verbosity=2).run(testGroup)