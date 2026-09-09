# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flashcards.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_flashcards(object):
    def setupUi(self, flashcards):
        if not flashcards.objectName():
            flashcards.setObjectName(u"flashcards")
        flashcards.resize(640, 480)
        self.button_know0 = QPushButton(flashcards)
        self.button_know0.setObjectName(u"button_know0")
        self.button_know0.setGeometry(QRect(200, 421, 91, 34))
        self.button_flip = QPushButton(flashcards)
        self.button_flip.setObjectName(u"button_flip")
        self.button_flip.setGeometry(QRect(260, 340, 121, 34))
        self.button_know3 = QPushButton(flashcards)
        self.button_know3.setObjectName(u"button_know3")
        self.button_know3.setGeometry(QRect(350, 421, 91, 34))
        self.label_question = QLabel(flashcards)
        self.label_question.setObjectName(u"label_question")
        self.label_question.setGeometry(QRect(10, 10, 621, 81))
        font = QFont()
        font.setPointSize(18)
        self.label_question.setFont(font)
        self.label_question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_answer = QLabel(flashcards)
        self.label_answer.setObjectName(u"label_answer")
        self.label_answer.setGeometry(QRect(10, 90, 621, 81))
        self.label_answer.setFont(font)
        self.label_answer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(flashcards)

        QMetaObject.connectSlotsByName(flashcards)
    # setupUi

    def retranslateUi(self, flashcards):
        flashcards.setWindowTitle(QCoreApplication.translate("flashcards", u"Dialog", None))
        self.button_know0.setText(QCoreApplication.translate("flashcards", u"Again", None))
        self.button_flip.setText(QCoreApplication.translate("flashcards", u"Reveal Answer", None))
        self.button_know3.setText(QCoreApplication.translate("flashcards", u"Got it", None))
        self.label_question.setText(QCoreApplication.translate("flashcards", u"TextLabel", None))
        self.label_answer.setText(QCoreApplication.translate("flashcards", u"TextLabel", None))
    # retranslateUi

