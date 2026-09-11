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
        self.button_know0.setGeometry(QRect(210, 440, 101, 34))
        self.button_flip = QPushButton(flashcards)
        self.button_flip.setObjectName(u"button_flip")
        self.button_flip.setGeometry(QRect(210, 180, 221, 34))
        self.button_know3 = QPushButton(flashcards)
        self.button_know3.setObjectName(u"button_know3")
        self.button_know3.setGeometry(QRect(330, 440, 101, 34))
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
        self.button_home = QPushButton(flashcards)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setGeometry(QRect(10, 10, 131, 34))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Sans"])
        font1.setPointSize(10)
        self.button_home.setFont(font1)
        self.label_stats = QLabel(flashcards)
        self.label_stats.setObjectName(u"label_stats")
        self.label_stats.setGeometry(QRect(170, 410, 301, 21))
        self.label_stats.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_acc = QLabel(flashcards)
        self.label_acc.setObjectName(u"label_acc")
        self.label_acc.setGeometry(QRect(210, 390, 221, 21))
        self.label_acc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(flashcards)

        QMetaObject.connectSlotsByName(flashcards)
    # setupUi

    def retranslateUi(self, flashcards):
        flashcards.setWindowTitle(QCoreApplication.translate("flashcards", u"Dialog", None))
        self.button_know0.setText(QCoreApplication.translate("flashcards", u"Again", None))
        self.button_flip.setText(QCoreApplication.translate("flashcards", u"Reveal Answer", None))
        self.button_know3.setText(QCoreApplication.translate("flashcards", u"Got it", None))
        self.label_question.setText(QCoreApplication.translate("flashcards", u"Question", None))
        self.label_answer.setText(QCoreApplication.translate("flashcards", u"Answer", None))
        self.button_home.setText(QCoreApplication.translate("flashcards", u"Back", None))
        self.label_stats.setText(QCoreApplication.translate("flashcards", u"0 Not guessed, 0 Guessed, 0 Remaining", None))
        self.label_acc.setText(QCoreApplication.translate("flashcards", u"Accuracy: 0%", None))
    # retranslateUi

