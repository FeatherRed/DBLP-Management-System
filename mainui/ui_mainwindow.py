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
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(832, 658)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(80, 60, 681, 521))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_builddatabse = QPushButton(self.tab)
        self.pushButton_builddatabse.setObjectName(u"pushButton_builddatabse")
        self.pushButton_builddatabse.setGeometry(QRect(480, 220, 75, 23))
        self.plainTextEdit_builddatabse = QPlainTextEdit(self.tab)
        self.plainTextEdit_builddatabse.setObjectName(u"plainTextEdit_builddatabse")
        self.plainTextEdit_builddatabse.setGeometry(QRect(40, 130, 331, 221))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.stackedWidget = QStackedWidget(self.tab_2)
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
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(530, 230, 82, 83))
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

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.stackedWidget_2 = QStackedWidget(self.tab_3)
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
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(500, 190, 77, 112))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.widget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_7.addWidget(self.pushButton_18)

        self.pushButton_16 = QPushButton(self.widget)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_7.addWidget(self.pushButton_16)

        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_7.addWidget(self.pushButton_15)

        self.pushButton_17 = QPushButton(self.widget)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_7.addWidget(self.pushButton_17)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.pushButton_exit = QPushButton(self.tab_4)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(500, 210, 75, 23))
        self.plainTextEdit_exit = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_exit.setObjectName(u"plainTextEdit_exit")
        self.plainTextEdit_exit.setGeometry(QRect(50, 110, 331, 221))
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi
        ###### 三个按钮事件 ######
        self.pushButton_top1.clicked.connect(self.on_pushButton_top1_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.pushButton_18.clicked.connect(self.on_pushButton_18_clicked)
        self.pushButton_16.clicked.connect(self.on_pushButton_16_clicked)
        self.pushButton_15.clicked.connect(self.on_pushButton_15_clicked)
        self.pushButton_17.clicked.connect(self.on_pushButton_17_clicked)
        self.pushButton_builddatabse.clicked.connect(self.on_pushButton_builddatabse_clicked)

        # 按钮一：打开第一个面板

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

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_builddatabse.setText(QCoreApplication.translate("Form", u"\u5efa\u7acb\u6570\u636e\u5e93", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5efa\u7acb\u6570\u636e\u5e93", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5e74\u4efd\u4fe1\u606f", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_22.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u7edf\u8ba1", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())