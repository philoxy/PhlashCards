# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wordEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_wordEdit(object):
    def setupUi(self, wordEdit):
        if not wordEdit.objectName():
            wordEdit.setObjectName(u"wordEdit")
        wordEdit.resize(640, 480)
        font = QFont()
        font.setFamilies([u"Ubuntu Sans"])
        font.setPointSize(10)
        wordEdit.setFont(font)
        self.button_back = QPushButton(wordEdit)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setGeometry(QRect(10, 10, 131, 34))
        self.button_back.setFont(font)
        self.button_ok = QPushButton(wordEdit)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(490, 440, 141, 34))
        self.button_ok.setFont(font)
        self.button_ok.setAutoDefault(True)
        self.button_ok.setFlat(False)
        self.line_a = QLineEdit(wordEdit)
        self.line_a.setObjectName(u"line_a")
        self.line_a.setGeometry(QRect(330, 190, 113, 31))
        self.hline = QFrame(wordEdit)
        self.hline.setObjectName(u"hline")
        self.hline.setGeometry(QRect(310, 180, 20, 51))
        self.hline.setFrameShape(QFrame.Shape.VLine)
        self.hline.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_q = QLineEdit(wordEdit)
        self.line_q.setObjectName(u"line_q")
        self.line_q.setGeometry(QRect(200, 190, 113, 31))
        self.line_q.setPlaceholderText(u"Add a question...")
        self.label_editmode = QLabel(wordEdit)
        self.label_editmode.setObjectName(u"label_editmode")
        self.label_editmode.setGeometry(QRect(200, 150, 241, 20))
        self.label_editmode.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(wordEdit)

        self.button_ok.setDefault(False)


        QMetaObject.connectSlotsByName(wordEdit)
    # setupUi

    def retranslateUi(self, wordEdit):
        wordEdit.setWindowTitle(QCoreApplication.translate("wordEdit", u"Dialog", None))
        self.button_back.setText(QCoreApplication.translate("wordEdit", u"Back", None))
        self.button_ok.setText(QCoreApplication.translate("wordEdit", u"OK", None))
        self.line_a.setPlaceholderText(QCoreApplication.translate("wordEdit", u"Add an answer...", None))
        self.label_editmode.setText(QCoreApplication.translate("wordEdit", u"Editing Word", None))
    # retranslateUi

