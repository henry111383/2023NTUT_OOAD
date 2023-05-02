from .Label import Label

class LabelService():
    def __init__(self):
        self.NameList = set()

    def isCreateLabel(self, name, type, ptList)->Label:
        self.NameList.add(name)
        return Label(name, type, ptList)
    
    