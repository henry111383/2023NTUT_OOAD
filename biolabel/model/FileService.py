from .File import File
from .ImageFile import ImageFile
from .LabelFile import LabelFile
from .LabelList import LabelList
from .Image import Image
import cv2
import json
class FileService():
    def __init__(self):
        pass
    def StoreImage(self, IF:ImageFile, fileLocation:str)-> bool:
        pass    #todo 


    def LoadImage(self, fileLocation:str)-> Image:
        # read image
        try:
            img = cv2.cvtColor(cv2.imread(fileLocation), cv2.COLOR_BGR2RGB)
            # create Image instance
            return Image(img, channel='RGB', imageName='Original')
        except:
            print('Error! Wrong format!')
            return
        

    def StoreLabel(self, LF:LabelFile, format:str)-> bool:
        MyJson = {}
        labellist = LF.GetLabelInfo().GetLabelList()
        for index, label in enumerate(labellist):
            Name = label.GetName()
            Color = label.GetColor()
            Type = label.GetLabelType()
            PointList =  label.GetPoint()
            Points = []
            for pt in PointList:
                Points.append([pt.GetX(), pt.GetY()])
            LabelDict={'Name': Name, 'Color': Color, 'Type': Type, 'Points': Points}

            MyJson[index] = LabelDict
        json_data = json.dumps(MyJson)
        with open(LF.GetFileLocation(), "w") as file:
            file.write(json_data)
        return
        

    
    def LoadLabel(self, fileLocation:str)-> bool:
        pass    #todo 

    def ConvertLabel2File(self, label:LabelList )-> LabelFile: 
        labellist = label
        labelfile = LabelFile(labelList=label)
        return labelfile
        
    def ConvertFile2Label(self, file :File)-> LabelList:
        pass    #todo 

    def ConvertImage2File(self, img:Image) -> ImageFile:
        # ImageFile(image=img)
        pass    #todo 

    def ConvertFile2Image(self,  file :File) -> Image:
        pass    #todo 