from File import *

class LabelFile(File):
    def __init__(self, labelList, parent=None):
        super(LabelFile, self).__init__(parent)
        self.__LabelInfo = labelList

    # getter
    def GetLabelInfo(self):
        return self.__LabelInfo
    
    # setter
    def SetLabelInfo(self, labelList):
        self.__LabelInfo = labelList
