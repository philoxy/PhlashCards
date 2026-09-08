# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importSets.ui'
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

class Ui_importSets(object):
    def setupUi(self, importSets):
        if not importSets.objectName():
            importSets.setObjectName(u"importSets")
        importSets.resize(640, 480)
        font = QFont()
        font.setFamilies([u"Ubuntu Sans"])
        font.setPointSize(10)
        importSets.setFont(font)
        self.button_refresh = QPushButton(importSets)
        self.button_refresh.setObjectName(u"button_refresh")
        self.button_refresh.setGeometry(QRect(250, 10, 141, 34))
        self.button_refresh.setFont(font)
        self.table = QTableWidget(importSets)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 50, 621, 381))
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
        self.button_home = QPushButton(importSets)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setGeometry(QRect(10, 10, 131, 34))
        self.button_home.setFont(font)
        self.label_currset = QLabel(importSets)
        self.label_currset.setObjectName(u"label_currset")
        self.label_currset.setGeometry(QRect(10, 446, 621, 21))
        self.label_currset.setFont(font)
        self.button_import = QPushButton(importSets)
        self.button_import.setObjectName(u"button_import")
        self.button_import.setGeometry(QRect(490, 10, 141, 34))
        self.button_import.setFont(font)
        self.button_import.setAutoDefault(True)
        self.button_import.setFlat(False)

        self.retranslateUi(importSets)

        self.button_import.setDefault(False)


        QMetaObject.connectSlotsByName(importSets)
    # setupUi

    def retranslateUi(self, importSets):
        importSets.setWindowTitle(QCoreApplication.translate("importSets", u"Dialog", None))
        self.button_refresh.setText(QCoreApplication.translate("importSets", u"Refresh", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("importSets", u"Name", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("importSets", u"Description", None))
        self.button_home.setText(QCoreApplication.translate("importSets", u"Home", None))
        self.label_currset.setText(QCoreApplication.translate("importSets", u"Current Set: None", None))
        self.button_import.setText(QCoreApplication.translate("importSets", u"Import", None))
    # retranslateUi

