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
        self.pushButton_db.setGeometry(QRect(440, 420, 121, 61))
        self.label_openfile = QLabel(self.DataBasetab)
        self.label_openfile.setObjectName(u"label_openfile")
        self.label_openfile.setEnabled(False)
        self.label_openfile.setGeometry(QRect(90, 190, 481, 121))
        self.label_openfile.setStyleSheet(u"color: #333333;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"font-family: CMU Serif;\n"
"background-color: #abb8ff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #1c7cd6;\n"
"border-radius: 5px;")
        self.pushButton_openfile = QPushButton(self.DataBasetab)
        self.pushButton_openfile.setObjectName(u"pushButton_openfile")
        self.pushButton_openfile.setGeometry(QRect(130, 420, 121, 61))
        self.MainWidget.addTab(self.DataBasetab, "")
        self.Searchtab = QWidget()
        self.Searchtab.setObjectName(u"Searchtab")
        self.stackedWidget = QStackedWidget(self.Searchtab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 60, 391, 411))
        self.page_searchnull = QWidget()
        self.page_searchnull.setObjectName(u"page_searchnull")
        self.stackedWidget.addWidget(self.page_searchnull)
        self.pagebasicsearch = QWidget()
        self.pagebasicsearch.setObjectName(u"pagebasicsearch")
        self.layoutWidget = QWidget(self.pagebasicsearch)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 100, 371, 261))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_basicsearch = QLineEdit(self.layoutWidget)
        self.lineEdit_basicsearch.setObjectName(u"lineEdit_basicsearch")

        self.horizontalLayout.addWidget(self.lineEdit_basicsearch)

        self.pushButton_bs1 = QPushButton(self.layoutWidget)
        self.pushButton_bs1.setObjectName(u"pushButton_bs1")

        self.horizontalLayout.addWidget(self.pushButton_bs1)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.plainTextEdit_basicsearch = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_basicsearch.setObjectName(u"plainTextEdit_basicsearch")

        self.verticalLayout_2.addWidget(self.plainTextEdit_basicsearch)

        self.stackedWidget.addWidget(self.pagebasicsearch)
        self.page_relevancesearch = QWidget()
        self.page_relevancesearch.setObjectName(u"page_relevancesearch")
        self.layoutWidget_2 = QWidget(self.page_relevancesearch)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 90, 321, 251))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_relevancesearch = QLineEdit(self.layoutWidget_2)
        self.lineEdit_relevancesearch.setObjectName(u"lineEdit_relevancesearch")

        self.horizontalLayout_2.addWidget(self.lineEdit_relevancesearch)

        self.pushButton_rs1 = QPushButton(self.layoutWidget_2)
        self.pushButton_rs1.setObjectName(u"pushButton_rs1")

        self.horizontalLayout_2.addWidget(self.pushButton_rs1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.plainTextEdit_relevancesearch = QPlainTextEdit(self.layoutWidget_2)
        self.plainTextEdit_relevancesearch.setObjectName(u"plainTextEdit_relevancesearch")

        self.verticalLayout_3.addWidget(self.plainTextEdit_relevancesearch)

        self.stackedWidget.addWidget(self.page_relevancesearch)
        self.page_particalsearch = QWidget()
        self.page_particalsearch.setObjectName(u"page_particalsearch")
        self.layoutWidget_3 = QWidget(self.page_particalsearch)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 80, 351, 321))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_particalsearch = QLineEdit(self.layoutWidget_3)
        self.lineEdit_particalsearch.setObjectName(u"lineEdit_particalsearch")

        self.horizontalLayout_3.addWidget(self.lineEdit_particalsearch)

        self.pushButton_ps1 = QPushButton(self.layoutWidget_3)
        self.pushButton_ps1.setObjectName(u"pushButton_ps1")

        self.horizontalLayout_3.addWidget(self.pushButton_ps1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.plainTextEdit_particalsearch = QPlainTextEdit(self.layoutWidget_3)
        self.plainTextEdit_particalsearch.setObjectName(u"plainTextEdit_particalsearch")

        self.verticalLayout_4.addWidget(self.plainTextEdit_particalsearch)

        self.stackedWidget.addWidget(self.page_particalsearch)
        self.layoutWidget1 = QWidget(self.Searchtab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(530, 230, 101, 103))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_basicsearch = QPushButton(self.layoutWidget1)
        self.pushButton_basicsearch.setObjectName(u"pushButton_basicsearch")

        self.verticalLayout.addWidget(self.pushButton_basicsearch)

        self.pushButton_relevancesearch = QPushButton(self.layoutWidget1)
        self.pushButton_relevancesearch.setObjectName(u"pushButton_relevancesearch")

        self.verticalLayout.addWidget(self.pushButton_relevancesearch)

        self.pushButton_particalsearch = QPushButton(self.layoutWidget1)
        self.pushButton_particalsearch.setObjectName(u"pushButton_particalsearch")

        self.verticalLayout.addWidget(self.pushButton_particalsearch)

        self.MainWidget.addTab(self.Searchtab, "")
        self.Analysistab = QWidget()
        self.Analysistab.setObjectName(u"Analysistab")
        self.stackedWidget_2 = QStackedWidget(self.Analysistab)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(30, 40, 381, 411))
        self.page_analysisnull = QWidget()
        self.page_analysisnull.setObjectName(u"page_analysisnull")
        self.stackedWidget_2.addWidget(self.page_analysisnull)
        self.page_authoranalysis = QWidget()
        self.page_authoranalysis.setObjectName(u"page_authoranalysis")
        self.layoutWidget_6 = QWidget(self.page_authoranalysis)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(70, 100, 241, 241))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_aa1 = QPushButton(self.layoutWidget_6)
        self.pushButton_aa1.setObjectName(u"pushButton_aa1")

        self.verticalLayout_8.addWidget(self.pushButton_aa1)

        self.plainTextEdit_authoranalysis = QPlainTextEdit(self.layoutWidget_6)
        self.plainTextEdit_authoranalysis.setObjectName(u"plainTextEdit_authoranalysis")

        self.verticalLayout_8.addWidget(self.plainTextEdit_authoranalysis)

        self.stackedWidget_2.addWidget(self.page_authoranalysis)
        self.page_hotspotanalysis = QWidget()
        self.page_hotspotanalysis.setObjectName(u"page_hotspotanalysis")
        self.layoutWidget_7 = QWidget(self.page_hotspotanalysis)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 80, 361, 301))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_hotspotanalysis = QLineEdit(self.layoutWidget_7)
        self.lineEdit_hotspotanalysis.setObjectName(u"lineEdit_hotspotanalysis")

        self.horizontalLayout_6.addWidget(self.lineEdit_hotspotanalysis)

        self.pushButton_hsa1 = QPushButton(self.layoutWidget_7)
        self.pushButton_hsa1.setObjectName(u"pushButton_hsa1")

        self.horizontalLayout_6.addWidget(self.pushButton_hsa1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.plainTextEdit_hotspotanalysis = QPlainTextEdit(self.layoutWidget_7)
        self.plainTextEdit_hotspotanalysis.setObjectName(u"plainTextEdit_hotspotanalysis")

        self.verticalLayout_9.addWidget(self.plainTextEdit_hotspotanalysis)

        self.stackedWidget_2.addWidget(self.page_hotspotanalysis)
        self.page_clusteranalysis = QWidget()
        self.page_clusteranalysis.setObjectName(u"page_clusteranalysis")
        self.layoutWidget_8 = QWidget(self.page_clusteranalysis)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(30, 60, 311, 291))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ca1 = QPushButton(self.layoutWidget_8)
        self.pushButton_ca1.setObjectName(u"pushButton_ca1")

        self.verticalLayout_10.addWidget(self.pushButton_ca1)

        self.plainTextEdit_clusteranalysis = QPlainTextEdit(self.layoutWidget_8)
        self.plainTextEdit_clusteranalysis.setObjectName(u"plainTextEdit_clusteranalysis")

        self.verticalLayout_10.addWidget(self.plainTextEdit_clusteranalysis)

        self.stackedWidget_2.addWidget(self.page_clusteranalysis)
        self.page_virtualanalysis = QWidget()
        self.page_virtualanalysis.setObjectName(u"page_virtualanalysis")
        self.layoutWidget_9 = QWidget(self.page_virtualanalysis)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(20, 80, 331, 261))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_va1 = QPushButton(self.layoutWidget_9)
        self.pushButton_va1.setObjectName(u"pushButton_va1")

        self.verticalLayout_11.addWidget(self.pushButton_va1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.plainTextEdit_va1 = QPlainTextEdit(self.layoutWidget_9)
        self.plainTextEdit_va1.setObjectName(u"plainTextEdit_va1")

        self.horizontalLayout_7.addWidget(self.plainTextEdit_va1)

        self.plainTextEdit_va2 = QPlainTextEdit(self.layoutWidget_9)
        self.plainTextEdit_va2.setObjectName(u"plainTextEdit_va2")

        self.horizontalLayout_7.addWidget(self.plainTextEdit_va2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stackedWidget_2.addWidget(self.page_virtualanalysis)
        self.layoutWidget2 = QWidget(self.Analysistab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(500, 190, 95, 139))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_authoranalysis = QPushButton(self.layoutWidget2)
        self.pushButton_authoranalysis.setObjectName(u"pushButton_authoranalysis")

        self.verticalLayout_7.addWidget(self.pushButton_authoranalysis)

        self.pushButton_hotspotanalysis = QPushButton(self.layoutWidget2)
        self.pushButton_hotspotanalysis.setObjectName(u"pushButton_hotspotanalysis")

        self.verticalLayout_7.addWidget(self.pushButton_hotspotanalysis)

        self.pushButton_clusteranalysis = QPushButton(self.layoutWidget2)
        self.pushButton_clusteranalysis.setObjectName(u"pushButton_clusteranalysis")

        self.verticalLayout_7.addWidget(self.pushButton_clusteranalysis)

        self.pushButton_virtualanalysis = QPushButton(self.layoutWidget2)
        self.pushButton_virtualanalysis.setObjectName(u"pushButton_virtualanalysis")

        self.verticalLayout_7.addWidget(self.pushButton_virtualanalysis)

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
        self.stackedWidget_2.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
        '-------------------------------控件设置处--------------------------------'
        self.label_openfile.setWordWrap(True)                                           #Qlabel Text自动换行
        '-------------------------------槽函数连接处-------------------------------'
        self.pushButton_basicsearch.clicked.connect(self.on_pushButton_basicsearch_clicked)
        self.pushButton_relevancesearch.clicked.connect(self.on_pushButton_relevancesearch_clicked)
        self.pushButton_particalsearch.clicked.connect(self.on_pushButton_particalsearch_clicked)
        self.pushButton_authoranalysis.clicked.connect(self.on_pushButton_authoranalysis_clicked)
        self.pushButton_hotspotanalysis.clicked.connect(self.on_pushButton_hotspotanalysis_clicked)
        self.pushButton_clusteranalysis.clicked.connect(self.on_pushButton_clusteranalysis_clicked)
        self.pushButton_virtualanalysis.clicked.connect(self.on_pushButton_virtualanalysis_clicked)
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
        self.lineEdit_basicsearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d\u6216\u5b8c\u6574\u8bba\u6587\u9898\u76ee", None))
        self.pushButton_bs1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.plainTextEdit_basicsearch.setPlaceholderText("")
        self.lineEdit_relevancesearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d", None))
        self.pushButton_rs1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.lineEdit_particalsearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5173\u952e\u5b57\u4fe1\u606f", None))
        self.pushButton_ps1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_basicsearch.setText(QCoreApplication.translate("Form", u"\u57fa\u672c\u641c\u7d22", None))
        self.pushButton_relevancesearch.setText(QCoreApplication.translate("Form", u"\u76f8\u5173\u641c\u7d22", None))
        self.pushButton_particalsearch.setText(QCoreApplication.translate("Form", u"\u90e8\u5206\u5339\u914d\u641c\u7d22", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Searchtab), QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_aa1.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.lineEdit_hotspotanalysis.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5e74\u4efd\u4fe1\u606f", None))
        self.pushButton_hsa1.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_ca1.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_va1.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.pushButton_authoranalysis.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.pushButton_hotspotanalysis.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_clusteranalysis.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_virtualanalysis.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Analysistab), QCoreApplication.translate("Form", u"\u7edf\u8ba1", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

    '--------------------------函数处--------------------------------'

    def on_pushButton_basicsearch_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

        # 按钮二：打开第二个面板
    def on_pushButton_relevancesearch_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

        # 按钮三：打开第三个面板
    def on_pushButton_particalsearch_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

        # 按钮一：打开第一个面板
    def on_pushButton_authoranalysis_clicked(self):
        self.stackedWidget_2.setCurrentIndex(1)

            # 按钮二：打开第二个面板
    def on_pushButton_hotspotanalysis_clicked(self):
        self.stackedWidget_2.setCurrentIndex(2)

            # 按钮三：打开第三个面板
    def on_pushButton_clusteranalysis_clicked(self):
        self.stackedWidget_2.setCurrentIndex(3)

        # 按钮四：打开第四个面板
    def on_pushButton_virtualanalysis_clicked(self):
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