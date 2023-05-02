
class LabelList():
    def __init__(self, labels=[]):
        self.__labels = labels

    def GetLabelList(self):
        return self.__labels
    
    def ReviseLabel(self, index, label):
        if len(self.__labels) > index:
            del self.__labels[index]
            self.__labels.insert(index, label)
        return
    
    def AddLabel(self, label):
        self.__labels.append(label)
        return
