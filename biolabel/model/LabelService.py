from .Label import Label
from .LabelList import LabelList
class LabelService():
    def __init__(self):
        self.NameList = set()
        self.labelList = LabelList([])
    def CreateLabel(self, name, type, ptList)->Label:
        self.NameList.add(name)
        return Label(name, type, ptList)
    # def moveLabel(self, name, type, ptList,parentLabel)->Label:
    #     if parentLabel
    #     return Label(name, type, ptList)
    
    