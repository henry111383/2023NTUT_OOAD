import unittest

from test_point import Point_PointShouldBeCorrect
from test_label import Label_RectLabelShouldBeCorrect 
from test_labellist import LabelListTest 
from test_image import Image_ImageShouldBeCorrect 
from test_imageProcessService import ImageProcessService_ImageProcessServiceShouldBeCorrect
from test_imagefile import ImageFileShouldBeCorrect 
from test_labelfile import LabelFileShouldBeCorrect
from test_labelService import LabelService_LabelServiceShouldBeCorrect
if __name__ == '__main__':
    
    Alltest = []
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(Point_PointShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(Label_RectLabelShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(LabelListTest))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(Image_ImageShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(ImageProcessService_ImageProcessServiceShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(ImageFileShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(LabelFileShouldBeCorrect))
    Alltest.append(unittest.TestLoader().loadTestsFromTestCase(LabelService_LabelServiceShouldBeCorrect))
    testGroup = unittest.TestSuite(Alltest)
    unittest.TextTestRunner(verbosity=2).run(testGroup)