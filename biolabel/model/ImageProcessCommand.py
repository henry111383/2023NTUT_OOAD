from Command import *
from Image import *

class ImageProcessCommand(Command):
    def __init__(self, time=..., info=None):
        super().__init__(time, info)

    def HistoEQ(self, img)->Image:
        pass

    def Brightness(self, img, bright)->Image:
        pass

    def Constrast(self, img, constrast)->Image:
        pass

    def RGB2Gray(self, img)->Image:
        pass 

    def RGB2HED(self, img)->Image:
        pass

    def HED2RGB(self, img)->Image:
        pass