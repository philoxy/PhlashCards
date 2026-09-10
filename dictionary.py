# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dictionary.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_dictionary(object):
    def setupUi(self, dictionary):
        if not dictionary.objectName():
            dictionary.setObjectName(u"dictionary")
        dictionary.resize(640, 480)
        font = QFont()
        font.setFamilies([u"Ubuntu Sans"])
        font.setPointSize(10)
        dictionary.setFont(font)
        self.button_edit = QPushButton(dictionary)
        self.button_edit.setObjectName(u"button_edit")
        self.button_edit.setGeometry(QRect(250, 440, 141, 34))
        self.button_edit.setFont(font)
        self.table = QTableWidget(dictionary)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 50, 621, 341))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setFont(font)
        self.table.setAutoFillBackground(False)
        self.table.setFrameShape(QFrame.Shape.NoFrame)
        self.table.setFrameShadow(QFrame.Shadow.Plain)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table.setGridStyle(Qt.PenStyle.NoPen)
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.button_home = QPushButton(dictionary)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setGeometry(QRect(10, 10, 131, 34))
        self.button_home.setFont(font)
        self.label_currset = QLabel(dictionary)
        self.label_currset.setObjectName(u"label_currset")
        self.label_currset.setGeometry(QRect(150, 10, 481, 31))
        self.label_currset.setFont(font)
        self.button_remove = QPushButton(dictionary)
        self.button_remove.setObjectName(u"button_remove")
        self.button_remove.setGeometry(QRect(490, 440, 141, 34))
        self.button_remove.setFont(font)
        self.button_remove.setAutoDefault(True)
        self.button_remove.setFlat(False)
        self.button_add = QPushButton(dictionary)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setGeometry(QRect(10, 440, 141, 34))
        self.button_add.setFont(font)
        self.button_hideq = QPushButton(dictionary)
        self.button_hideq.setObjectName(u"button_hideq")
        self.button_hideq.setGeometry(QRect(130, 400, 141, 34))
        self.button_hideq.setFont(font)
        self.button_hidea = QPushButton(dictionary)
        self.button_hidea.setObjectName(u"button_hidea")
        self.button_hidea.setGeometry(QRect(370, 400, 141, 34))
        self.button_hidea.setFont(font)

        self.retranslateUi(dictionary)

        self.button_remove.setDefault(False)


        QMetaObject.connectSlotsByName(dictionary)
    # setupUi

    def retranslateUi(self, dictionary):
        dictionary.setWindowTitle(QCoreApplication.translate("dictionary", u"Dialog", None))
        self.button_edit.setText(QCoreApplication.translate("dictionary", u"Edit", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dictionary", u"Question", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dictionary", u"Answer", None))
        self.button_home.setText(QCoreApplication.translate("dictionary", u"Back", None))
        self.label_currset.setText(QCoreApplication.translate("dictionary", u"Current Set: None", None))
        self.button_remove.setText(QCoreApplication.translate("dictionary", u"Remove", None))
        self.button_add.setText(QCoreApplication.translate("dictionary", u"Add", None))
        self.button_hideq.setText(QCoreApplication.translate("dictionary", u"Hide Questions", None))
        self.button_hidea.setText(QCoreApplication.translate("dictionary", u"Hide Answers", None))
    # retranslateUi

