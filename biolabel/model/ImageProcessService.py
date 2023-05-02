from model.Image import Image
import numpy as np
import cv2
import PIL.Image
from skimage.color import rgb2hed

class ImageProcessService():
    def __init__(self, img=Image()):
        pass
        
    def RGB2Gray(self, img):
        if img :
            return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    def Gray2RGB(self, img):
        if img.GetChannel()=='gray':
            ret, th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            return ret
        else:
            print("Image should be graylevel!")

    def RGB2HED(self, img):
        if img.GetChannel()=='RGB':
            rgb2hed(img)
        else:
            print("Image should be RGB!")
            

