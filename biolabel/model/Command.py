import datetime 

class Command():
    def __init__(self, info=None, time=datetime.datetime.now()):
        self.__Info = info
        self.__Time = time

    def GetTime(self):
        return self.__Time

    def GetInfo(self):
        return self.__Info
    
    def undo():
        pass

    def redo():
        pass

