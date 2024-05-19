# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
QMetaObject, QObject, QPoint, QRect,
QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
QFont, QFontDatabase, QGradient, QIcon,
QImage, QKeySequence, QLinearGradient, QPainter,
QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
QWidget,QFileDialog,QMessageBox)

import os
import Datain
import create
class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)

        '------------------------------控件处-------------------------------------------'
        #此处控件为打开文件控件
        self.pushButton_openfile = QPushButton(Widget)
        self.pushButton_openfile.setObjectName(u"openfile")
        self.pushButton_openfile.setGeometry(QRect(300, 400, 131, 61))
        self.label_openfile = QLabel(Widget)
        self.label_openfile.setObjectName(u"label")
        self.label_openfile.setGeometry(QRect(280, 200, 161, 51))
        self.label_openfile.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        #建立数据库按钮处
        self.pushButton_db = QPushButton(Widget)
        self.pushButton_db.setObjectName(u"openfile")
        self.pushButton_db.setGeometry(QRect(150, 400, 131, 61))

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
        '------------------------------槽函数连接处-------------------------------------------'
        #打开文件处
        self.pushButton_openfile.clicked.connect(self.msg)
        #创建数据库
        self.pushButton_db.clicked.connect(self.createdb)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_openfile.setText("")
        self.pushButton_openfile.setText(QCoreApplication.translate("Widget", u"\u6253\u5f00\u6587\u4ef6", None))
        self.pushButton_db.setText(QCoreApplication.translate("Widget", "创建数据库", None))
    # retranslateUi

    def msg(self,Filepath):
        self.label_openfile.clear()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file, _ = QFileDialog.getOpenFileName(self.pushButton_openfile, "选取文件", current_dir, "Xml Files (*.xml)")  # 文件扩展名用双分号间隔
        #判断该file是否为空
        if not file:
            return
        else:
            print(file)
            ##设置文本框
            self.label_openfile.setText(file)

    def createdb(self):
        #先判断是否有路径
        file = self.label_openfile.text()
        if not file:
            QMessageBox.information(self.pushButton_db, "警告", "未找到路径，请重新打开路径")
        else:
            #判断当前是否已经处理好文件
            file_name = os.path.splitext(os.path.basename(file))[0]
            #判断该文件名有无deal
            if "_deal" not in file_name:
                Datain.preprocessing(file)
                print("已经处理完毕，正构建json")
            else:
                print("该文件已处理完毕，正构建json")
                file_name = file_name[:4]
                #存在_deal删掉
            #判断是否有json
            json_path = file_name + ".json"
            print(json_path)
            if(os.path.exists(json_path)):
                #存在json了 直接读就行
                print("直接读json")
            else:
                #不存在json 还得生成json并且保存跑后的record
                self.record = create.read_records_from_xml(file_name + "_deal.xml")
                create.createjson(self.record,file_name)



