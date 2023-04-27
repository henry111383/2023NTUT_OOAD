import math

class Point(object):
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def x(self)->float:
        return self.__X 
    
    def y(self)->float:
        return self.__Y
    
    def distance(self, pt)->float:
        dis = math.sqrt( math.pow(self.x()-pt.x(), 2) + math.pow(self.y()-pt.y(), 2) )
        return dis