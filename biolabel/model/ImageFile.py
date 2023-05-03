from .File import *

class ImageFile(File):
    def __init__(self, image,\
                    fileLocation=None, \
                    fileName=None, \
                    fileFormat=None, \
                    directory=None, \
                    parent=None):
        super(ImageFile, self).__init__(fileLocation,fileName,fileFormat,directory)
        self.__ImgInfo = image

    # getter
    def GetImgInfo(self):
        return self.__ImgInfo
    
    # setter
    def SetImgInfo(self, image):
        self.__ImgInfo = image
