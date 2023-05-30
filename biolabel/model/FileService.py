from .File import File
from .ImageFile import ImageFile
from .LabelFile import LabelFile
from .LabelList import LabelList
from .Image import Image
import cv2
class FileService():
    def __init__(self):
        pass
    def StoreImage(self, IF:ImageFile, fileLocation:str)-> bool:
        pass    #todo 


    def LoadImage(self, fileLocation:str)-> bool:
        # read image
        img = cv2.cvtColor(cv2.imread(fileLocation), cv2.COLOR_BGR2RGB)
        # create Image instance
        return Image(img, channel='RGB', imageName='Original')

    def StoreLabel(self, LF:LabelFile, fileLocation:str)-> bool:
        pass    #todo 
    def LoadLabel(self, fileLocation:str)-> bool:
        pass    #todo 
    def ConvertLabel2File(self, label:LabelList )-> LabelFile: 
        pass    #todo 
    def ConvertFile2Label(self, file :File)-> LabelList:
        pass    #todo 
    def ConvertImage2File(self, img:Image ) -> ImageFile:
        pass    #todo 
    def ConvertFile2Image(self,  file :File) -> Image:
        pass    #todo 