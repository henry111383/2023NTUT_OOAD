
class Label():
    def __init__(self, name=None, type=None, ptList=[]):
        self.__LabelName = name
        self.__LabelType = type
        self.__ptList = ptList

    def GetPoint(self):
        return self.__ptList
    
    def AddPoint(self, pt):
        self.__ptList.append(pt)
        return
    
    def RemovePoint(self, index):
        if index :
            if len(self.__ptList) > index:
                del self.__ptList[index]
        return
    
    def UpdatePoint(self, index, pt):
        if len(self.__ptList) > index:
            del self.__ptList[index]
            self.__ptList.insert(index, pt)
        return
    
    def GetName(self):
        return self.__LabelName
    
    def SetName(self, name):
        self.__LabelName = name
        return
        
    def GetLabelType(self):
        return self.__LabelType