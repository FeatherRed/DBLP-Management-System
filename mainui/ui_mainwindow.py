# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget, QLabel, QDialog, QFileDialog, QMessageBox)
import os, create, Datain
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.MainWidget = QTabWidget(Form)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setGeometry(QRect(0, 0, 800, 600))
        self.MainWidget.setStyleSheet(u"QTabBar::tab{width:90}\n"
"QTabBar::tab{height:150}")
        self.MainWidget.setTabPosition(QTabWidget.East)
        self.DataBasetab = QWidget()
        self.DataBasetab.setObjectName(u"DataBasetab")
        self.pushButton_db = QPushButton(self.DataBasetab)
        self.pushButton_db.setObjectName(u"pushButton_db")
        self.pushButton_db.setGeometry(QRect(440, 410, 161, 91))
        self.label_openfile = QLabel(self.DataBasetab)
        self.label_openfile.setObjectName(u"label_openfile")
        self.label_openfile.setEnabled(True)
        self.label_openfile.setGeometry(QRect(70, 140, 561, 151))
        self.label_openfile.setStyleSheet(u"color: #333333; /* \u6587\u672c\u989c\u8272 */\n"
"font-size: 20px; /* \u5b57\u4f53\u5927\u5c0f */\n"
"font-weight: bold; /* \u5b57\u4f53\u7c97\u7ec6 */\n"
"font-family: CMU Serif; /* \u5b57\u4f53\u5bb6\u65cf */\n"
"background-color: #abb8ff; /* \u80cc\u666f\u989c\u8272 */\n"
"border-style: solid; /* \u8fb9\u6846\u6837\u5f0f */\n"
"border-width: 2px; /* \u8fb9\u6846\u5bbd\u5ea6 */\n"
"border-color: #1c7cd6; /* \u8fb9\u6846\u989c\u8272 */\n"
"border-radius: 5px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"\n"
"")
        self.label_openfile.setTextFormat(Qt.RichText)
        self.label_openfile.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_openfile = QPushButton(self.DataBasetab)
        self.pushButton_openfile.setObjectName(u"pushButton_openfile")
        self.pushButton_openfile.setGeometry(QRect(120, 410, 161, 91))
        self.MainWidget.addTab(self.DataBasetab, "")
        self.Searchtab = QWidget()
        self.Searchtab.setObjectName(u"Searchtab")
        self.stackedWidget = QStackedWidget(self.Searchtab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 60, 391, 411))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.layoutWidget = QWidget(self.page_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 100, 371, 261))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.layoutWidget_2 = QWidget(self.page_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 90, 321, 251))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_4 = QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.plainTextEdit_2 = QPlainTextEdit(self.layoutWidget_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout_3.addWidget(self.plainTextEdit_2)

        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget_3 = QWidget(self.page_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 80, 351, 321))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_3 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.pushButton_5 = QPushButton(self.layoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.plainTextEdit_3 = QPlainTextEdit(self.layoutWidget_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.verticalLayout_4.addWidget(self.plainTextEdit_3)

        self.stackedWidget.addWidget(self.page_2)
        self.layoutWidget1 = QWidget(self.Searchtab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(530, 230, 101, 103))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_top1 = QPushButton(self.layoutWidget1)
        self.pushButton_top1.setObjectName(u"pushButton_top1")

        self.verticalLayout.addWidget(self.pushButton_top1)

        self.pushButton_2 = QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.MainWidget.addTab(self.Searchtab, "")
        self.Analysistab = QWidget()
        self.Analysistab.setObjectName(u"Analysistab")
        self.stackedWidget_2 = QStackedWidget(self.Analysistab)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(30, 40, 381, 411))
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.layoutWidget_6 = QWidget(self.page_6)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(70, 100, 241, 241))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.layoutWidget_6)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_8.addWidget(self.pushButton_19)

        self.plainTextEdit_6 = QPlainTextEdit(self.layoutWidget_6)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")

        self.verticalLayout_8.addWidget(self.plainTextEdit_6)

        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.layoutWidget_7 = QWidget(self.page_7)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 80, 361, 301))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_4 = QLineEdit(self.layoutWidget_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.pushButton_20 = QPushButton(self.layoutWidget_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_6.addWidget(self.pushButton_20)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.plainTextEdit_7 = QPlainTextEdit(self.layoutWidget_7)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")

        self.verticalLayout_9.addWidget(self.plainTextEdit_7)

        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.layoutWidget_8 = QWidget(self.page_8)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(30, 60, 311, 291))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.layoutWidget_8)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_10.addWidget(self.pushButton_21)

        self.plainTextEdit_8 = QPlainTextEdit(self.layoutWidget_8)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")

        self.verticalLayout_10.addWidget(self.plainTextEdit_8)

        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.layoutWidget_9 = QWidget(self.page_9)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(20, 80, 331, 261))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_22 = QPushButton(self.layoutWidget_9)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.verticalLayout_11.addWidget(self.pushButton_22)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.plainTextEdit_9 = QPlainTextEdit(self.layoutWidget_9)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")

        self.horizontalLayout_7.addWidget(self.plainTextEdit_9)

        self.plainTextEdit_10 = QPlainTextEdit(self.layoutWidget_9)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")

        self.horizontalLayout_7.addWidget(self.plainTextEdit_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stackedWidget_2.addWidget(self.page_9)
        self.layoutWidget2 = QWidget(self.Analysistab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(500, 190, 95, 139))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.layoutWidget2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_7.addWidget(self.pushButton_18)

        self.pushButton_16 = QPushButton(self.layoutWidget2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_7.addWidget(self.pushButton_16)

        self.pushButton_15 = QPushButton(self.layoutWidget2)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_7.addWidget(self.pushButton_15)

        self.pushButton_17 = QPushButton(self.layoutWidget2)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_7.addWidget(self.pushButton_17)

        self.MainWidget.addTab(self.Analysistab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.pushButton_exit = QPushButton(self.tab_4)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(500, 210, 75, 23))
        self.plainTextEdit_exit = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_exit.setObjectName(u"plainTextEdit_exit")
        self.plainTextEdit_exit.setGeometry(QRect(50, 110, 331, 221))
        self.MainWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)

        self.MainWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)

        '-------------------------------控件设置处--------------------------------'
        self.label_openfile.setWordWrap(True)                                           #Qlabel Text自动换行
        '-------------------------------槽函数连接处-------------------------------'
        self.pushButton_top1.clicked.connect(self.on_pushButton_top1_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.pushButton_18.clicked.connect(self.on_pushButton_18_clicked)
        self.pushButton_16.clicked.connect(self.on_pushButton_16_clicked)
        self.pushButton_15.clicked.connect(self.on_pushButton_15_clicked)
        self.pushButton_17.clicked.connect(self.on_pushButton_17_clicked)
        self.pushButton_db.clicked.connect(self.on_pushButton_builddatabse_clicked)

        '-------------------------------创建数据库连接处---------------------------'
        self.pushButton_openfile.clicked.connect(self.msg)
        self.pushButton_db.clicked.connect(self.createdb)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_db.setText(QCoreApplication.translate("Form", u"\u5efa\u7acb\u6570\u636e\u5e93", None))
        self.label_openfile.setText("")
        self.pushButton_openfile.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6587\u4ef6", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.DataBasetab), QCoreApplication.translate("Form", u"\u5efa\u7acb\u6570\u636e\u5e93", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d\u6216\u5b8c\u6574\u8bba\u6587\u9898\u76ee", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.plainTextEdit.setPlaceholderText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5173\u952e\u5b57\u4fe1\u606f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_top1.setText(QCoreApplication.translate("Form", u"\u57fa\u672c\u641c\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u76f8\u5173\u641c\u7d22", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u90e8\u5206\u5339\u914d\u641c\u7d22", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Searchtab), QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5e74\u4efd\u4fe1\u606f", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_22.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Analysistab), QCoreApplication.translate("Form", u"\u7edf\u8ba1", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi
    '--------------------------函数处--------------------------------'

    def on_pushButton_top1_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

        # 按钮二：打开第二个面板
    def on_pushButton_2_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

        # 按钮三：打开第三个面板
    def on_pushButton_3_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

        # 按钮一：打开第一个面板
    def on_pushButton_18_clicked(self):
        self.stackedWidget_2.setCurrentIndex(1)

            # 按钮二：打开第二个面板
    def on_pushButton_16_clicked(self):
        self.stackedWidget_2.setCurrentIndex(2)

            # 按钮三：打开第三个面板
    def on_pushButton_15_clicked(self):
        self.stackedWidget_2.setCurrentIndex(3)
    def on_pushButton_17_clicked(self):
        self.stackedWidget_2.setCurrentIndex(4)
    def on_pushButton_builddatabse_clicked(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
    '-------------------------创建数据库函数-------------------------'

    'openfile'
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
    'createdatabase'
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

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())