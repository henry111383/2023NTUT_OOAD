from .File import File
from .ImageFile import ImageFile
from .LabelFile import LabelFile
from .LabelList import LabelList
from .Image import Image
class FileService():
    def __init__(self):
        pass
    def StoreImage(self):
        pass    #todo 
    def LoadImage(self):
        pass    #todo 
    def StoreLabel(self):
        pass    #todo 
    def LoadLabel(self):
        pass    #todo 
    def ConvertLabel2File(self, Label:LabelList )-> LabelFile: 
        pass    #todo 
    def ConvertFile2Label(self, File :File)-> LabelList:
        pass    #todo 
    def ConvertImage2File(self, Img:Image ) -> ImageFile:
        pass    #todo 
    def ConvertFFile2Image(self,  File :File) -> Image:
        pass    #todo 