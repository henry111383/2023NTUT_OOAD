# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class LabelName_Dialog(QtWidgets.QDialog):
    AddLabelName = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 370)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 368))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 20, 10, 20)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(False)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.LabelNameList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.LabelNameList.setObjectName("LabelNameList")
        self.gridLayout.addWidget(self.LabelNameList, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 10)

        # 添加取消事件
        self.buttonBox.rejected.connect(self.reject)
        # 為 "OK" 按鈕添加 "clicked" 事件
        self.buttonBox.accepted.connect(self.accept)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Input the Label Name", "Input the Label Name"))
        self.LabelNameList.itemClicked.connect(self.SetLabelName)


    def accept(self):
        new_LabelName =self.textEdit.text()
        # 若輸入的LabelName為空且不重複則加入LabelNameList
        self.AddLabelName.emit(new_LabelName)
        super().accept()

    def reject(self):
        self.textEdit.clear()
        self.AddLabelName.emit('')
        super().reject()
        
    # 根據點擊的Item將相對應內容設置到textEdit
    def SetLabelName(self,item):
        self.textEdit.setText(item.text())





    




