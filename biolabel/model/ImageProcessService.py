from .Image import Image
import numpy as np
import cv2
import PIL.Image
import skimage 

class ImageProcessService():
    def __init__(self, img=Image()):
        pass
        
    def RGB2Gray(self, img):
        if img.GetChannel()=='RGB' :
            value = img.GetImg()
            return Image(cv2.cvtColor(value, cv2.COLOR_RGB2GRAY), channel='gray', imageName='RGB2Gray') 
        else:
            print("Image should be RGB")
        
    def OTSUbinary(self, img):
        if img.GetChannel()=='gray':
            value = img.GetImg()
            binary_val = cv2.threshold(value, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
            return Image(binary_val, channel='binary', imageName='OTSUbinary')
        else:
            print("Image should be graylevel!")

    def RGB2Hematoxylin(self, img):
        if img.GetChannel()=='RGB':
            value = img.GetImg()
            null = np.zeros_like(value[:, :, 0])
            Hematoxylin = skimage.color.rgb2hed(value)
            Hematoxylin = skimage.color.hed2rgb(np.stack((Hematoxylin[:, :, 0], null, null), axis=-1))
            return Image(Hematoxylin, channel='Hematoxylin', imageName='RGB2Hematoxylin')
        else:
            print("Image should be RGB!")
            

    def RGB2Eosin(self, img):
        if img.GetChannel()=='RGB':
            value = img.GetImg()
            null = np.zeros_like(value[:, :, 0])
            Eosin = skimage.color.rgb2hed(value)
            Eosin = skimage.color.hed2rgb(np.stack((null, Eosin[:, :, 1], null), axis=-1))
            return Image(Eosin, channel='Eosin', imageName='RGB2Eosin')
        else:
            print("Image should be RGB!")


    def RGB2Dab(self, img):
        if img.GetChannel()=='RGB':
            value = img.GetImg()
            null = np.zeros_like(value[:, :, 0])
            Dab = skimage.color.rgb2hed(value)
            Dab = skimage.color.hed2rgb(np.stack((null, null, Dab[:, :, 2]), axis=-1))
            return Image(Dab, channel='Dab', imageName='RGB2Dab')
        else:
            print("Image should be RGB!")