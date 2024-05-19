# -*- coding: utf-8 -*-
import sys
'''
    主要是测试表格使用以及信息显示
    在基础上再创建一个widget对象来显示文章全部信息
    Tableview的实现方法主要是先创建一个model
    在这个model上传完数据以及修改格式后，就用setModel
    核心代码如下，不过有一些要修改的地方
    ui_title的大小应该锁定住

'''

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItem, QStandardItemModel)
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableView,
    QWidget)

from ui_Title import DetailsWindow

class DEWidget(QWidget):
    def __init__(self,title,record,parent=None):
        super().__init__(parent)
        self.ui = DetailsWindow()
        self.ui.setupUi(title,self) #注意这里修改了一下setupui 主要是为了设置页面标题
        print(title)
        self.ui.Datain(record)  #调用ui_Title中的Datain函数，显示论文全部信息

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(180, 130, 471, 361))
        self.model = QStandardItemModel(4,1)
        self.model.setHorizontalHeaderLabels(['Title'])
        self.model.setItem(0,0,QStandardItem("The unstable formula theorem revisited."))
        self.model.setItem(1, 0, QStandardItem("Immunization Strategies Based on the Overlapping Nodes in Networks with Community Structure."))
        self.tableView.setModel(self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)   #设置不可编辑

        self.tableView.doubleClicked.connect(self.show_info)    #连接函数 信号为双击 可以显示论文全部信息

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
    # retranslateUi


    def show_info(self):
        #测试用的publication
        publications = {
            "The unstable formula theorem revisited.": {
                "authors": [
                    "Maryanthe Malliaris",
                    "Shay Moran"
                ],
                "journal": "CoRR",
                "year": "2022",
                "volume": "abs/2212.05050",
                "url": "db/journals/corr/corr2212.html#abs-2212-05050",
                "ee": "https://doi.org/10.48550/arXiv.2212.05050"
            },
            "Immunization Strategies Based on the Overlapping Nodes in Networks with Community Structure.": {
                "authors": [
                    "Debayan Chakraborty",
                    "Anurag Singh 0001",
                    "Hocine Cherifi"
                ],
                "journal": "CoRR",
                "year": "2022",
                "volume": "abs/2212.14884",
                "url": "db/journals/corr/corr2212.html#abs-2212-14884",
                "ee": "https://doi.org/10.48550/arXiv.2212.14884"
            }
        }
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column()
        print(row,column)
        title = self.tableView.currentIndex().data()    #获得标题
        print(publications[title])
        self.dewidget = DEWidget(title,publications[title]) #创建一个新页面，附属于self
        self.dewidget.show()    #显示

