from Command import *

class CommandHistory():
    def __init__(self):
        self.__CommandList = []

    def AddCommand(self, cmd):
        self.__CommandList.append(cmd)
        return
    
    def GetTheLastCommand(self, cmd)->Command:
        try:
            cmd_index = self.__CommandList.index(cmd)
            if cmd_index == 0:
                return None
            else:
                return self.__CommandList[cmd_index-1] 
        except:
            return None
        
    def GetTheNextCommand(self, cmd)->Command:
        try:
            cmd_index = self.__CommandList.index(cmd)
            if cmd_index == len(self.__CommandList)-1:
                return None
            else:
                return self.__CommandList[cmd_index+1] 
        except:
            return None



