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
    QSize, QTime, QUrl, Qt, QRegularExpression)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator, QStandardItem, QStandardItemModel, QRegularExpressionValidator)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget, QLabel, QDialog, QFileDialog, QMessageBox, QTableView,
    QAbstractItemView, QHeaderView, QComboBox, QSpacerItem, QRadioButton)
import os, create, Datain, Function_index
from ui_Title import DEWidget
from ui_wordcloud import WordCloudWindow
from functools import partial

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
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_main1 = QLabel(self.tab_4)
        self.label_main1.setObjectName(u"label_main1")
        self.label_main1.setGeometry(QRect(170, 170, 351, 81))
        self.label_main1.setStyleSheet(u"font: 9pt \"\u534e\u6587\u884c\u6977\";")
        self.pushButton_exit = QPushButton(self.tab_4)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(300, 470, 75, 23))
        self.label_name2 = QLabel(self.tab_4)
        self.label_name2.setObjectName(u"label_name2")
        self.label_name2.setGeometry(QRect(550, 470, 54, 16))
        self.label_name3 = QLabel(self.tab_4)
        self.label_name3.setObjectName(u"label_name3")
        self.label_name3.setGeometry(QRect(550, 490, 54, 16))
        self.label_name1 = QLabel(self.tab_4)
        self.label_name1.setObjectName(u"label_name1")
        self.label_name1.setGeometry(QRect(550, 450, 54, 16))
        self.MainWidget.addTab(self.tab_4, "")
        self.DataBasetab = QWidget()
        self.DataBasetab.setObjectName(u"DataBasetab")
        self.pushButton_db = QPushButton(self.DataBasetab)
        self.pushButton_db.setObjectName(u"pushButton_db")
        self.pushButton_db.setGeometry(QRect(420, 400, 121, 61))
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
        self.pushButton_openfile.setGeometry(QRect(100, 400, 121, 61))
        self.MainWidget.addTab(self.DataBasetab, "")
        self.Searchtab = QWidget()
        self.Searchtab.setObjectName(u"Searchtab")
        self.stackedWidget = QStackedWidget(self.Searchtab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 60, 501, 431))
        self.page_searchnull = QWidget()
        self.page_searchnull.setObjectName(u"page_searchnull")
        self.stackedWidget.addWidget(self.page_searchnull)
        self.pagebasicsearch = QWidget()
        self.pagebasicsearch.setObjectName(u"pagebasicsearch")
        self.layoutWidget = QWidget(self.pagebasicsearch)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 491, 311))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_basicsearch = QComboBox(self.layoutWidget)
        self.comboBox_basicsearch.addItem("")
        self.comboBox_basicsearch.addItem("")
        self.comboBox_basicsearch.setObjectName(u"comboBox_basicsearch")
        self.comboBox_basicsearch.setEnabled(True)
        self.comboBox_basicsearch.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_basicsearch)

        self.lineEdit_basicsearch = QLineEdit(self.layoutWidget)
        self.lineEdit_basicsearch.setObjectName(u"lineEdit_basicsearch")
        self.lineEdit_basicsearch.setFrame(True)

        self.horizontalLayout.addWidget(self.lineEdit_basicsearch)

        self.pushButton_bs1 = QPushButton(self.layoutWidget)
        self.pushButton_bs1.setObjectName(u"pushButton_bs1")

        self.horizontalLayout.addWidget(self.pushButton_bs1)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableView_basicsearch = QTableView(self.layoutWidget)
        self.tableView_basicsearch.setObjectName(u"tableView_basicsearch")

        self.verticalLayout_2.addWidget(self.tableView_basicsearch)

        self.stackedWidget.addWidget(self.pagebasicsearch)
        self.page_relevancesearch = QWidget()
        self.page_relevancesearch.setObjectName(u"page_relevancesearch")
        self.layoutWidget_2 = QWidget(self.page_relevancesearch)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 50, 491, 311))
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

        self.tableView_relevancesearch = QTableView(self.layoutWidget_2)
        self.tableView_relevancesearch.setObjectName(u"tableView_relevancesearch")

        self.verticalLayout_3.addWidget(self.tableView_relevancesearch)

        self.stackedWidget.addWidget(self.page_relevancesearch)
        self.page_particalsearch = QWidget()
        self.page_particalsearch.setObjectName(u"page_particalsearch")
        self.layoutWidget_3 = QWidget(self.page_particalsearch)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 50, 491, 311))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_particalsearch = QRadioButton(self.layoutWidget_3)
        self.radioButton_particalsearch.setObjectName(u"radioButton_particalsearch")

        self.horizontalLayout_3.addWidget(self.radioButton_particalsearch)

        self.lineEdit_particalsearch = QLineEdit(self.layoutWidget_3)
        self.lineEdit_particalsearch.setObjectName(u"lineEdit_particalsearch")

        self.horizontalLayout_3.addWidget(self.lineEdit_particalsearch)

        self.pushButton_ps1 = QPushButton(self.layoutWidget_3)
        self.pushButton_ps1.setObjectName(u"pushButton_ps1")

        self.horizontalLayout_3.addWidget(self.pushButton_ps1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tableView_particalsearch = QTableView(self.layoutWidget_3)
        self.tableView_particalsearch.setObjectName(u"tableView_particalsearch")

        self.verticalLayout_4.addWidget(self.tableView_particalsearch)

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
        self.stackedWidget_2.setGeometry(QRect(30, 40, 471, 501))
        self.page_analysisnull = QWidget()
        self.page_analysisnull.setObjectName(u"page_analysisnull")
        self.stackedWidget_2.addWidget(self.page_analysisnull)
        self.page_authoranalysis = QWidget()
        self.page_authoranalysis.setObjectName(u"page_authoranalysis")
        self.layoutWidget_6 = QWidget(self.page_authoranalysis)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 20, 451, 421))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_authoranalysis = QLineEdit(self.layoutWidget_6)
        self.lineEdit_authoranalysis.setObjectName(u"lineEdit_authoranalysis")

        self.verticalLayout_8.addWidget(self.lineEdit_authoranalysis)

        self.pushButton_aa1 = QPushButton(self.layoutWidget_6)
        self.pushButton_aa1.setObjectName(u"pushButton_aa1")

        self.verticalLayout_8.addWidget(self.pushButton_aa1)

        self.tableView_authoranalysis = QTableView(self.layoutWidget_6)
        self.tableView_authoranalysis.setObjectName(u"tableView_authoranalysis")
        self.tableView_authoranalysis.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_authoranalysis.setShowGrid(True)

        self.verticalLayout_8.addWidget(self.tableView_authoranalysis)

        self.stackedWidget_2.addWidget(self.page_authoranalysis)
        self.page_hotspotanalysis = QWidget()
        self.page_hotspotanalysis.setObjectName(u"page_hotspotanalysis")
        self.layoutWidget_7 = QWidget(self.page_hotspotanalysis)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 20, 451, 421))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_hotspotanalysis = QLineEdit(self.layoutWidget_7)
        self.lineEdit_hotspotanalysis.setObjectName(u"lineEdit_hotspotanalysis")

        self.horizontalLayout_6.addWidget(self.lineEdit_hotspotanalysis)

        self.lineEdit_hotspotanalysis1 = QLineEdit(self.layoutWidget_7)
        self.lineEdit_hotspotanalysis1.setObjectName(u"lineEdit_hotspotanalysis1")

        self.horizontalLayout_6.addWidget(self.lineEdit_hotspotanalysis1)

        self.pushButton_hsa1 = QPushButton(self.layoutWidget_7)
        self.pushButton_hsa1.setObjectName(u"pushButton_hsa1")

        self.horizontalLayout_6.addWidget(self.pushButton_hsa1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.tableView_hotspotanalysis = QTableView(self.layoutWidget_7)
        self.tableView_hotspotanalysis.setObjectName(u"tableView_hotspotanalysis")

        self.verticalLayout_9.addWidget(self.tableView_hotspotanalysis)

        self.pushButton_wordcloud = QPushButton(self.layoutWidget_7)
        self.pushButton_wordcloud.setObjectName(u"pushButton_wordcloud")

        self.verticalLayout_9.addWidget(self.pushButton_wordcloud)

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
        self.layoutWidget_4 = QWidget(self.page_virtualanalysis)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 20, 451, 421))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_va1 = QLineEdit(self.layoutWidget_4)
        self.lineEdit_va1.setObjectName(u"lineEdit_va1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_va1.sizePolicy().hasHeightForWidth())
        self.lineEdit_va1.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.lineEdit_va1)

        self.comboBox_virtualanalysis = QComboBox(self.layoutWidget_4)
        self.comboBox_virtualanalysis.setObjectName(u"comboBox_virtualanalysis")
        sizePolicy.setHeightForWidth(self.comboBox_virtualanalysis.sizePolicy().hasHeightForWidth())
        self.comboBox_virtualanalysis.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.comboBox_virtualanalysis)

        self.pushButton_va1 = QPushButton(self.layoutWidget_4)
        self.pushButton_va1.setObjectName(u"pushButton_va1")

        self.horizontalLayout_4.addWidget(self.pushButton_va1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.lineEdit_va2 = QLineEdit(self.layoutWidget_4)
        self.lineEdit_va2.setObjectName(u"lineEdit_va2")

        self.verticalLayout_5.addWidget(self.lineEdit_va2)

        self.tableView_virtualanalysis = QTableView(self.layoutWidget_4)
        self.tableView_virtualanalysis.setObjectName(u"tableView_virtualanalysis")

        self.verticalLayout_5.addWidget(self.tableView_virtualanalysis)

        self.stackedWidget_2.addWidget(self.page_virtualanalysis)
        self.layoutWidget2 = QWidget(self.Analysistab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(530, 210, 95, 139))
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

        self.retranslateUi(Form)

        self.MainWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        # setupUi
        '-------------------------------页面设置处--------------------------------'
        self.MainWidget.setTabEnabled(2, False)
        self.MainWidget.setTabEnabled(3, False)
        '-------------------------------控件设置处--------------------------------'
        self.label_openfile.setWordWrap(True)  # Qlabel Text自动换行
        self.lineEdit_authoranalysis.setValidator(QIntValidator(1, 100))  # 设置作者统计只能为int类型
        regex = QRegularExpression(r"(19[0-9]{2}|20[0-1][0-9]|202[0-4])")  # 正则表达式1900~2024
        self.lineEdit_hotspotanalysis.setValidator(QRegularExpressionValidator(regex))  # 设置输入范围
        self.tableView_authoranalysis.verticalHeader().setVisible(False)  # 隐藏行号
        self.tableView_basicsearch.verticalHeader().setVisible(False)  # 隐藏行号
        self.tableView_basicsearch.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableView_relevancesearch.verticalHeader().setVisible(False)  # 隐藏行号
        self.tableView_relevancesearch.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableView_hotspotanalysis.verticalHeader().setVisible(False)  # 隐藏行号
        self.tableView_hotspotanalysis.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableView_particalsearch.verticalHeader().setVisible(False)  # 隐藏行号
        self.tableView_particalsearch.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        '-------------------------------槽函数连接处-------------------------------'
        self.pushButton_exit.clicked.connect(Form.close)
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

        '--------------------------------基本搜索连接处---------------------------'
        self.pushButton_bs1.clicked.connect(self.basicsearch)
        self.tableView_basicsearch.doubleClicked.connect(partial(self.show_info, self.tableView_basicsearch, 0))

        '--------------------------------相关搜索连接处---------------------------'
        self.pushButton_rs1.clicked.connect(self.relevanacesearch)
        '--------------------------------关键词搜索连接处---------------------------'
        self.pushButton_ps1.clicked.connect(self.particalsearch)
        self.tableView_particalsearch.doubleClicked.connect(partial(self.show_info, self.tableView_particalsearch, 1))
        '--------------------------------作者分析连接处---------------------------'
        self.pushButton_aa1.clicked.connect(self.authoranalysis)
        '--------------------------------年热频词连接处---------------------------'
        self.pushButton_hsa1.clicked.connect(self.hotspotanalysis)
        self.pushButton_wordcloud.clicked.connect(self.word_cloud_generation)
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_main1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">\u79d1\u5b66\u6587\u732e\u7ba1\u7406\u7cfb\u7edf</span></p></body></html>", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label_name2.setText(QCoreApplication.translate("Form", u"\u90b5\u5f08", None))
        self.label_name3.setText(QCoreApplication.translate("Form", u"\u6f58\u6cfd\u8f69", None))
        self.label_name1.setText(QCoreApplication.translate("Form", u"\u9a6c\u601d\u6377", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u9996\u9875", None))
        self.pushButton_db.setText(QCoreApplication.translate("Form", u"\u5efa\u7acb\u6570\u636e\u5e93", None))
        self.label_openfile.setText("")
        self.pushButton_openfile.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6587\u4ef6", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.DataBasetab), QCoreApplication.translate("Form", u"\u5efa\u7acb\u6570\u636e\u5e93", None))
        self.comboBox_basicsearch.setItemText(0, QCoreApplication.translate("Form", u"\u4f5c\u8005", None))
        self.comboBox_basicsearch.setItemText(1, QCoreApplication.translate("Form", u"\u8bba\u6587", None))

        self.lineEdit_basicsearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d\u6216\u5b8c\u6574\u8bba\u6587\u9898\u76ee", None))
        self.pushButton_bs1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.lineEdit_relevancesearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d", None))
        self.pushButton_rs1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.radioButton_particalsearch.setText(QCoreApplication.translate("Form", u"\u7cbe\u786e\u641c\u7d22", None))
        self.lineEdit_particalsearch.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5173\u952e\u5b57\u4fe1\u606f", None))
        self.pushButton_ps1.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_basicsearch.setText(QCoreApplication.translate("Form", u"\u57fa\u672c\u641c\u7d22", None))
        self.pushButton_relevancesearch.setText(QCoreApplication.translate("Form", u"\u76f8\u5173\u641c\u7d22", None))
        self.pushButton_particalsearch.setText(QCoreApplication.translate("Form", u"\u90e8\u5206\u5339\u914d\u641c\u7d22", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Searchtab), QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.lineEdit_authoranalysis.setText("")
        self.lineEdit_authoranalysis.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u4e2a\u6570", None))
        self.pushButton_aa1.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.lineEdit_hotspotanalysis.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5e74\u4efd\u4fe1\u606f", None))
        self.lineEdit_hotspotanalysis1.setText("")
        self.lineEdit_hotspotanalysis1.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u70ed\u70b9\u8bcd\u4e2a\u6570", None))
        self.pushButton_hsa1.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_wordcloud.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u8be5\u5e74\u4efd\u8bcd\u4e91\u56fe", None))
        self.pushButton_ca1.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.lineEdit_va1.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4f5c\u8005\u59d3\u540d", None))
        self.pushButton_va1.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.pushButton_authoranalysis.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.pushButton_hotspotanalysis.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_clusteranalysis.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_virtualanalysis.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Analysistab), QCoreApplication.translate("Form", u"\u7edf\u8ba1", None))
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
            return
        #判断当前是否已经处理好文件
        file_name = os.path.splitext(os.path.basename(file))[0]
        #判断该文件名有无deal
        if "_deal" not in file_name:
            Datain.preprocessing(file)
            print("已经处理完毕，正构建pkl")
        else:
            print("该文件已处理完毕，正构建pkl")
            file_name = file_name[:4]
            #存在_deal删掉
        #判断是否有pkl
        pkl_path = file_name + ".pkl"
        self.filename = file_name
        self.path = pkl_path
        print(pkl_path)
        if(os.path.exists(pkl_path)):
            #存在pkl了 直接读就行
            print("直接读pkl")
            allindex = create.readpkl(pkl_path)
        else:
            # 不存在pkl 还得生成pkl并且保存跑后的record
            # record = create.read_records_from_xml(file_name + "_deal.xml")
            # create.createpkl(record,file_name)
            # del record
            # 保存成索引值
            record = create.read_records_from_xml(file_name + "_deal.xml")
            allindex = create.createpkl(record,file_name)
            #保存类
        #修改成保存索引值
        self.author_to_titles, self.title_to_info, self.buckets, self.edge_author, self.top_n_keywords, self.inverted_index = allindex.reset()
        del allindex
        #创建完数据库或者得到路径后，打开功能
        self.MainWidget.setTabEnabled(2, True)
        self.MainWidget.setTabEnabled(3, True)
    def show_info(self,Table,index,Index):
        title = Table.currentIndex().data()     #获得标题
        row = Table.currentIndex().row()        #获得行号
        column = Table.currentIndex().column()  #获得列号
        #print("index",index)
        #print(self.title_to_info[title])
        match index:
            case 0: self.dewidget = DEWidget(title,self.basicsearch_info[row])
            case 1: self.dewidget = DEWidget(title,self.partical_publicationlist[row])
        self.dewidget.show()
    def basicsearch(self):
        self.tableView_basicsearch_model = None
        #查看combobox是什么
        choice = self.comboBox_basicsearch.currentIndex()
        searchtext = self.lineEdit_basicsearch.text()
        #choice = 0 作者
        #choice = 1 论文
        if choice == 0:
            self.basicsearch_author(searchtext)
        else:
            self.basicsearch_title(searchtext)
        self.tableView_basicsearch.setModel(self.tableView_basicsearch_model)
        self.tableView_basicsearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_basicsearch.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    def basicsearch_author(self,searchtext):
        self.tableView_basicsearch.setModel(None)
        author_title,self.basicsearch_info = Function_index.find_author(searchtext,self.author_to_titles)
        Len = len(author_title)
        if Len == 0:
            QMessageBox.warning(self.Searchtab,"没有找到","作者{}未发表论文".format(searchtext))
            self.lineEdit_basicsearch.clear()
            return
        self.tableView_basicsearch_model = QStandardItemModel(Len,1)
        self.tableView_basicsearch_model.setHorizontalHeaderLabels(["论文标题"])
        for i,title in enumerate(author_title):
            self.tableView_basicsearch_model.setItem(i,0,QStandardItem(title))

    def basicsearch_title(self,searchtext):
        self.tableView_basicsearch.setModel(None)
        self.basicsearch_info = self.title_to_info[searchtext]
        all_title = Function_index.find_title(searchtext,self.title_to_info)
        Len = len(all_title)
        if Len == 0:
            QMessageBox.warning(self.Searchtab,"没有找到","找不到论文{}".format(searchtext))
            self.lineEdit_basicsearch.clear()
            return
        self.tableView_basicsearch_model = QStandardItemModel(Len,1)
        self.tableView_basicsearch_model.setHorizontalHeaderLabels(["论文标题"])
        for i in range(Len):
            self.tableView_basicsearch_model.setItem(i,0,QStandardItem(searchtext))

    def relevanacesearch(self):
        search_author = self.lineEdit_relevancesearch.text()
        self.tableView_relevancesearch.setModel(None)
        #获得
        authors = self.edge_author[search_author]
        #print(authors)
        Len = len(authors)
        if Len == 0:
            QMessageBox.warning(self.Searchtab,"没有找到","没有作者和{}有合作关系".format(search_author))
            self.lineEdit_relevancesearch.clear()
            return
        self.tableView_relevancesearch_model = QStandardItemModel(Len,1)
        self.tableView_relevancesearch_model.setHorizontalHeaderLabels(["合作作者"])
        for i,author in enumerate(authors):
            self.tableView_relevancesearch_model.setItem(i,0,QStandardItem(author))
        self.tableView_relevancesearch.setModel(self.tableView_relevancesearch_model)
        self.tableView_relevancesearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_relevancesearch.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def particalsearch(self):
        self.tableView_particalsearch.setModel(None)
        #获得输入单词列表
        if not self.lineEdit_particalsearch.text():
            QMessageBox.warning(self.Searchtab,"错误","请输入关键词")
            return
        search_word = self.lineEdit_particalsearch.text()
        #判断是模糊搜索还是精确搜索
        choice = self.radioButton_particalsearch.isChecked()
        # 0 模糊 1 精确
        match choice:
            case 0:self.partical_titlelist,self.partical_publicationlist = Function_index.fuzzy_search(search_word,self.inverted_index,self.title_to_info)
            case 1:self.partical_titlelist,self.partical_publicationlist = Function_index.keywords_search(search_word,self.inverted_index,self.title_to_info)
        if not self.partical_titlelist:
            QMessageBox.information(self.Searchtab, "没有找到", "未找到匹配的文章")
            return 0
        #print(self.partical_titlelist,self.partical_publicationlist)
        #设置表格
        Len = len(self.partical_titlelist)
        self.tableView_particalsearch_model = QStandardItemModel(Len,1)
        self.tableView_particalsearch_model.setHorizontalHeaderLabels(["标题"])
        for i,title in enumerate(self.partical_titlelist):
            self.tableView_particalsearch_model.setItem(i,0,QStandardItem(title))
        self.tableView_particalsearch.setModel(self.tableView_particalsearch_model)
        self.tableView_particalsearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_particalsearch.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def authoranalysis(self):
        #获得数量
        if not self.lineEdit_authoranalysis.text():
            QMessageBox.warning(self.Analysistab, "错误", "请输入作者个数")
            return
        Len = int(self.lineEdit_authoranalysis.text())
        self.tableView_authoranalysis.setModel(None)
        self.tableView_authoranalysis_model = QStandardItemModel(Len,2)
        self.tableView_authoranalysis_model.setHorizontalHeaderLabels(["作者","文章数"])
        cnt = 0
        buckets = self.buckets
        for i in range(32766,0,-1):
            if len(buckets[i]) == 0:
                continue
            if cnt < Len:
                for author in buckets[i]:
                    if cnt < Len:
                        self.tableView_authoranalysis_model.setItem(cnt,0,QStandardItem(author))
                        self.tableView_authoranalysis_model.setItem(cnt,1,QStandardItem(str(i)))
                    cnt += 1
        self.tableView_authoranalysis.setModel(self.tableView_authoranalysis_model)
        self.tableView_authoranalysis.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def hotspotanalysis(self):
        self.tableView_hotspotanalysis.setModel(None)
        #先获得第几年
        if not self.lineEdit_hotspotanalysis.text():
            QMessageBox.warning(self.Analysistab, "错误", "请输入年份信息")
            return
        if not self.lineEdit_hotspotanalysis1.text():
            QMessageBox.warning(self.Analysistab, "错误", "请输入热点词个数")
            return
        analysis_year = self.lineEdit_hotspotanalysis.text()
        analysis_num = int(self.lineEdit_hotspotanalysis1.text())
        #调用函数得到列表
        keywords_list = Function_index.top_keyword_per_year(analysis_year,self.top_n_keywords,analysis_num)
        if not keywords_list:
            QMessageBox.information(self.Analysistab, "没有找到", "本年没有热点词频")
            return
        #开始可视化
        Len = len(keywords_list)
        if Len < analysis_num:
            QMessageBox.information(self.Analysistab, "分析结果", "该年热点词频只有{}个".format(Len))
        self.tableView_hotspotanalysis_model = QStandardItemModel(Len,2)
        self.tableView_hotspotanalysis_model.setHorizontalHeaderLabels(["热点词","频数"])
        for i,word in enumerate(keywords_list):
            item_word = QStandardItem(word[0])
            item_word.setTextAlignment(Qt.AlignCenter)
            item_fre = QStandardItem(str(word[1]))
            item_fre.setTextAlignment(Qt.AlignCenter)
            self.tableView_hotspotanalysis_model.setItem(i,0,item_word)
            self.tableView_hotspotanalysis_model.setItem(i,1,item_fre)
        self.tableView_hotspotanalysis.setModel(self.tableView_hotspotanalysis_model)
        self.tableView_hotspotanalysis.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_hotspotanalysis.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    def word_cloud_generation(self):
        # 先获得第几年
        if not self.lineEdit_hotspotanalysis.text():
            QMessageBox.warning(self.Analysistab, "错误", "请输入年份信息")
            return
        analysis_year = self.lineEdit_hotspotanalysis.text()
        self.wordcloud = Function_index.word_cloud(analysis_year, self.top_n_keywords)
        #首先保存图片
        wordcloud_path = self.filename + analysis_year + ".png"
        self.wordcloud.to_file(wordcloud_path)
        self.wordcloudwindow = WordCloudWindow(wordcloud_path)
        self.wordcloudwindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    with open("style.qss",encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    Form.show()
    sys.exit(app.exec())