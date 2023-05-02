from File import *

class ImageFile(File):
    def __init__(self, image, parent=None):
        super(ImageFile, self).__init__(parent)
        self.__ImgInfo = image

    # getter
    def GetImgInfo(self):
        return self.__ImgInfo
    
    # setter
    def SetImgInfo(self, image):
        self.__ImgInfo = image
