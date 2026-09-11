# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(640, 480)
        font = QFont()
        font.setFamilies([u"Ubuntu Sans"])
        font.setPointSize(10)
        home.setFont(font)
        self.label_title = QLabel(home)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 50, 621, 61))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Sans"])
        font1.setPointSize(36)
        font1.setBold(False)
        self.label_title.setFont(font1)
        self.label_title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dropdown_type = QComboBox(home)
        self.dropdown_type.addItem("")
        self.dropdown_type.addItem("")
        self.dropdown_type.addItem("")
        self.dropdown_type.setObjectName(u"dropdown_type")
        self.dropdown_type.setGeometry(QRect(250, 240, 141, 25))
        self.button_start = QPushButton(home)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(250, 150, 141, 25))
        self.button_start.setFont(font)
        self.button_import = QPushButton(home)
        self.button_import.setObjectName(u"button_import")
        self.button_import.setGeometry(QRect(250, 180, 141, 25))
        self.button_import.setFont(font)
        self.label_selectset = QLabel(home)
        self.label_selectset.setObjectName(u"label_selectset")
        self.label_selectset.setEnabled(True)
        self.label_selectset.setGeometry(QRect(240, 430, 161, 16))
        self.label_selectset.setFont(font)
        self.label_selectset.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_type = QLabel(home)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setGeometry(QRect(250, 220, 141, 20))
        self.groupBox = QGroupBox(home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(240, 270, 161, 81))
        self.check_shuffle = QCheckBox(self.groupBox)
        self.check_shuffle.setObjectName(u"check_shuffle")
        self.check_shuffle.setGeometry(QRect(10, 25, 141, 21))
        self.check_flip = QCheckBox(self.groupBox)
        self.check_flip.setObjectName(u"check_flip")
        self.check_flip.setGeometry(QRect(10, 52, 141, 21))

        self.retranslateUi(home)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"Dialog", None))
        self.label_title.setText(QCoreApplication.translate("home", u"PhlashCards", None))
        self.dropdown_type.setItemText(0, QCoreApplication.translate("home", u"Flashcards", None))
        self.dropdown_type.setItemText(1, QCoreApplication.translate("home", u"Multiple Choice", None))
        self.dropdown_type.setItemText(2, QCoreApplication.translate("home", u"Quiz", None))

        self.button_start.setText(QCoreApplication.translate("home", u"Start", None))
        self.button_import.setText(QCoreApplication.translate("home", u"Select Question Set", None))
        self.label_selectset.setText(QCoreApplication.translate("home", u"Please select a set.", None))
        self.label_type.setText(QCoreApplication.translate("home", u"Quiz Type", None))
        self.groupBox.setTitle(QCoreApplication.translate("home", u"Quiz Settings", None))
        self.check_shuffle.setText(QCoreApplication.translate("home", u"Shuffle Card Order", None))
        self.check_flip.setText(QCoreApplication.translate("home", u"Flipped Questions", None))
    # retranslateUi

