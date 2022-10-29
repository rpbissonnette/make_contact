# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        if not ProgressDialog.objectName():
            ProgressDialog.setObjectName(u"ProgressDialog")
        ProgressDialog.resize(693, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressDialog.sizePolicy().hasHeightForWidth())
        ProgressDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(ProgressDialog)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ProgressDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(ProgressDialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_4 = QLabel(ProgressDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.composeBar = QProgressBar(ProgressDialog)
        self.composeBar.setObjectName(u"composeBar")
        self.composeBar.setValue(24)

        self.gridLayout.addWidget(self.composeBar, 3, 1, 1, 1)

        self.abortB = QPushButton(ProgressDialog)
        self.abortB.setObjectName(u"abortB")

        self.gridLayout.addWidget(self.abortB, 5, 0, 1, 2)

        self.dirsBar = QProgressBar(ProgressDialog)
        self.dirsBar.setObjectName(u"dirsBar")
        self.dirsBar.setValue(24)

        self.gridLayout.addWidget(self.dirsBar, 1, 1, 1, 1)

        self.layoutBar = QProgressBar(ProgressDialog)
        self.layoutBar.setObjectName(u"layoutBar")
        self.layoutBar.setValue(24)

        self.gridLayout.addWidget(self.layoutBar, 2, 1, 1, 1)

        self.label_2 = QLabel(ProgressDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.logT = QTextEdit(ProgressDialog)
        self.logT.setObjectName(u"logT")

        self.gridLayout.addWidget(self.logT, 4, 0, 1, 2)


        self.retranslateUi(ProgressDialog)

        QMetaObject.connectSlotsByName(ProgressDialog)
    # setupUi

    def retranslateUi(self, ProgressDialog):
        ProgressDialog.setWindowTitle(QCoreApplication.translate("ProgressDialog", u"Make Contact Sheet Progress", None))
        self.label_3.setText(QCoreApplication.translate("ProgressDialog", u"Layout", None))
        self.label.setText(QCoreApplication.translate("ProgressDialog", u"Contact Sheet Progress...", None))
        self.label_4.setText(QCoreApplication.translate("ProgressDialog", u"Compose", None))
        self.abortB.setText(QCoreApplication.translate("ProgressDialog", u"Abort", None))
        self.label_2.setText(QCoreApplication.translate("ProgressDialog", u"Directories:", None))
    # retranslateUi

