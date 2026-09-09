# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(643, 480)
        icon = QIcon()
        icon.addFile(u"../../../../phlashcards/assets/qt/img/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.sw = QStackedWidget(self.centralwidget)
        self.sw.setObjectName(u"sw")
        self.sw.setGeometry(QRect(0, 0, 640, 480))
        sizePolicy.setHeightForWidth(self.sw.sizePolicy().hasHeightForWidth())
        self.sw.setSizePolicy(sizePolicy)
        self.sw.setStyleSheet(u"QStackedWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0.46591, y1:0.634, x2:0.804, y2:0.0241245, stop:0 rgba(21, 85, 222, 255), stop:1 rgba(5, 162, 228, 255));\n"
"}\n"
"\n"
"QPushButton, QComboBox, QComboBox::drop-down, QListView, QCombBox:on {\n"
"	border: 1px solid rgb(38,103,255);\n"
"	border-radius: 7px;\n"
"	color: rgb(0,0,0);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.503, x2:1, y2:0, stop:0 rgba(75, 132, 255, 255), stop:1 rgba(94, 207, 255, 255));\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"\n"
"}\n"
"\n"
"QComboBox:on {\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down, QComboBox::item:pressed {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed, QComboBox:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.503, x2:1, y2:0, stop:0 rgba(24, 97, 255, 255), stop:1 rgba(6, 181, 255, 255));\n"
"}\n"
"\n"
"QPushButto"
                        "n:disabled, QComboBox:disabled {\n"
"	background-color: rgb(13, 54, 142);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed, QComboBox:hover:!pressed, QListView:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.503, x2:1, y2:0, stop:0 rgba(103, 151, 255, 255), stop:1 rgba(146, 223, 255, 255));\n"
"}\n"
"\n"
"QTableView {\n"
"	border: 0px;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.503, x2:1, y2:0, stop:0 rgba(13, 54, 142, 255), stop:1 rgba(73, 104, 170, 255));\n"
"	selection-background-color: qlineargradient(spread:pad, x1:1, y1:0.503, x2:1, y2:0, stop:0 rgba(24, 97, 255, 255), stop:1 rgba(6, 181, 255, 255));\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sw.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

