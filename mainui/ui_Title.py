# -*- coding: utf-8 -*-
'''
该文件是设计展示全部论文信息的页面
DEWidget为创建页面定义的类
DetailsWindow为界面的ui实现
'''
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QStandardItem, QStandardItemModel)
from PySide6.QtWidgets import (QHeaderView, QPushButton, QTableView, QWidget)

class DEWidget(QWidget):
    def __init__(self,title,record,parent=None):
        super().__init__(parent)
        self.ui = DetailsWindow()
        self.ui.setupUi(title,self) #注意这里修改了一下setupui 主要是为了设置页面标题
        # print(title)
        # print(record)
        self.ui.Datain(record)  #调用ui_Title中的Datain函数，显示论文全部信息

class DetailsWindow(object):
    def setupUi(self,Title,Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 600)
        Widget.setWindowTitle(Title)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 570, 93, 29))
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 30, 381, 531))
        # 隐藏行、列号
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.horizontalHeader().setVisible(False)
        #点击exit关闭
        self.pushButton.clicked.connect(Widget.close)
        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Exit", None))
    # retranslateUi

    def Datain(self,record):
        self.tableView.setModel(None)   #先置为None 初始化
        Len = len(record)
        #print(len(record))
        for ele in record:
            if ele == "authors":
                Len += len(record[ele])
            elif ele == "editors":
                Len += len(record[ele])
            else:
                Len += 1
        #print(Len)
        self.model = QStandardItemModel(Len,1)  #初始化model，设置大小
        Len1 = 0
        for ele in record:
            if ele == "authors":
                item = QStandardItem("authors")
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(Len1,0,item)
                for author in record[ele]:
                    Len1 += 1
                    self.model.setItem(Len1, 0, QStandardItem(author))
            elif ele == "editors":
                item = QStandardItem("editors")
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(Len1, 0, item)
                for editor in record[ele]:
                    Len1 += 1
                    self.model.setItem(Len1, 0, QStandardItem(editor))
            else:
                item = QStandardItem(ele)
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(Len1, 0, item)
                Len1 += 1
                self.model.setItem(Len1,0,QStandardItem(record[ele]))
            Len1 += 1
        self.tableView.setModel(self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)

