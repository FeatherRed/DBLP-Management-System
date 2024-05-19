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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget, QLabel)
import os
class WordCloudWindow(QWidget):
    def __init__(self,imgpath,parent=None):
        super().__init__(parent)
        self.ui = WordCloud()
        self.ui.setupUi(self)
        self.ui.draw(imgpath)

class WordCloud(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 450)
        self.exit = QPushButton(Widget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(350, 410, 100, 30))
        self.wordcloud = QLabel(Widget)
        self.wordcloud.setObjectName(u"wordcloud")
        self.wordcloud.setGeometry(QRect(0, 0, 800, 400))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        self.exit.clicked.connect(Widget.close)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"词云图", None))
        self.exit.setText(QCoreApplication.translate("Widget", u"\u9000\u51fa", None))
        self.wordcloud.setText("")
    # retranslateUi
    def draw(self,imgpath):
        self.wordcloud.clear()
        pixmap = QPixmap(imgpath)
        self.wordcloud.setPixmap(pixmap)
        os.remove(imgpath)
