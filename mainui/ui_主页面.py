# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '主页面.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)
from ui_基本搜索 import *
from ui_相关搜索 import *

class main_window(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(783, 580)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 30, 731, 491))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 80, 481, 341))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(80, 70, 561, 341))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_2 = QPlainTextEdit(self.widget1)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_9 = QPushButton(self.widget1)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget1)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    # 定义槽函数
        self.pushButton.clicked.connect(self.basic_search)
        self.pushButton_2.clicked.connect(self.related_search)


    def basic_search(self):
        ui_2.show()
        Form.hide()

    def related_search(self):
        ui_3.show()
        Form.hide()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316\u6570\u636e\u5e93", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u57fa\u672c\u641c\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u76f8\u5173\u641c\u7d22", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u90e8\u5206\u5339\u914d\u641c\u7d22", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316\u6570\u636e\u5e93", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7edf\u8ba1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u70ed\u70b9\u5206\u6790", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u805a\u56e2\u5206\u6790", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u7edf\u8ba1", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = main_window()
    ui_2 = basic_search()
    ui_3 = related_search()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())