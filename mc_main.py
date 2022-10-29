# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mc_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

from DirsList import DirsList

class Ui_mc_main(object):
    def setupUi(self, mc_main):
        if not mc_main.objectName():
            mc_main.setObjectName(u"mc_main")
        mc_main.resize(657, 736)
        self.actionQuit = QAction(mc_main)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionSave_Config = QAction(mc_main)
        self.actionSave_Config.setObjectName(u"actionSave_Config")
        self.actionLoad_Config = QAction(mc_main)
        self.actionLoad_Config.setObjectName(u"actionLoad_Config")
        self.centralWidget = QWidget(mc_main)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout_4 = QGridLayout(self.centralWidget)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sheetBox = QGroupBox(self.centralWidget)
        self.sheetBox.setObjectName(u"sheetBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sheetBox.sizePolicy().hasHeightForWidth())
        self.sheetBox.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.sheetBox)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fileDirT = QCheckBox(self.sheetBox)
        self.fileDirT.setObjectName(u"fileDirT")
        self.fileDirT.setChecked(True)

        self.gridLayout.addWidget(self.fileDirT, 1, 2, 1, 1)

        self.fileDirL = QLabel(self.sheetBox)
        self.fileDirL.setObjectName(u"fileDirL")

        self.gridLayout.addWidget(self.fileDirL, 1, 0, 1, 1)

        self.fileQualL = QLabel(self.sheetBox)
        self.fileQualL.setObjectName(u"fileQualL")

        self.gridLayout.addWidget(self.fileQualL, 2, 0, 1, 1)

        self.fileOrderC = QComboBox(self.sheetBox)
        self.fileOrderC.addItem("")
        self.fileOrderC.addItem("")
        self.fileOrderC.setObjectName(u"fileOrderC")

        self.gridLayout.addWidget(self.fileOrderC, 8, 1, 1, 1)

        self.fileWidthL = QLabel(self.sheetBox)
        self.fileWidthL.setObjectName(u"fileWidthL")

        self.gridLayout.addWidget(self.fileWidthL, 3, 0, 1, 1)

        self.fileHeightE = QLineEdit(self.sheetBox)
        self.fileHeightE.setObjectName(u"fileHeightE")
        self.fileHeightE.setEnabled(False)

        self.gridLayout.addWidget(self.fileHeightE, 4, 1, 1, 1)

        self.fileQualE = QLineEdit(self.sheetBox)
        self.fileQualE.setObjectName(u"fileQualE")

        self.gridLayout.addWidget(self.fileQualE, 2, 1, 1, 1)

        self.fileOverwriteL = QLabel(self.sheetBox)
        self.fileOverwriteL.setObjectName(u"fileOverwriteL")

        self.gridLayout.addWidget(self.fileOverwriteL, 7, 0, 1, 1)

        self.fileHeightT = QCheckBox(self.sheetBox)
        self.fileHeightT.setObjectName(u"fileHeightT")
        self.fileHeightT.setChecked(True)

        self.gridLayout.addWidget(self.fileHeightT, 4, 2, 1, 1)

        self.fileOrderL = QLabel(self.sheetBox)
        self.fileOrderL.setObjectName(u"fileOrderL")

        self.gridLayout.addWidget(self.fileOrderL, 8, 0, 1, 1)

        self.fileExtE = QLineEdit(self.sheetBox)
        self.fileExtE.setObjectName(u"fileExtE")

        self.gridLayout.addWidget(self.fileExtE, 0, 1, 1, 1)

        self.fileWidthE = QLineEdit(self.sheetBox)
        self.fileWidthE.setObjectName(u"fileWidthE")

        self.gridLayout.addWidget(self.fileWidthE, 3, 1, 1, 1)

        self.fileBackgroundL = QLabel(self.sheetBox)
        self.fileBackgroundL.setObjectName(u"fileBackgroundL")

        self.gridLayout.addWidget(self.fileBackgroundL, 5, 0, 1, 1)

        self.fileHeightL = QLabel(self.sheetBox)
        self.fileHeightL.setObjectName(u"fileHeightL")

        self.gridLayout.addWidget(self.fileHeightL, 4, 0, 1, 1)

        self.fileExtL = QLabel(self.sheetBox)
        self.fileExtL.setObjectName(u"fileExtL")

        self.gridLayout.addWidget(self.fileExtL, 0, 0, 1, 1)

        self.fileOverwriteC = QComboBox(self.sheetBox)
        self.fileOverwriteC.addItem("")
        self.fileOverwriteC.addItem("")
        self.fileOverwriteC.setObjectName(u"fileOverwriteC")

        self.gridLayout.addWidget(self.fileOverwriteC, 7, 1, 1, 1)

        self.fileBackgroundB = QPushButton(self.sheetBox)
        self.fileBackgroundB.setObjectName(u"fileBackgroundB")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.fileBackgroundB.setPalette(palette)

        self.gridLayout.addWidget(self.fileBackgroundB, 5, 1, 1, 1)

        self.fileDirE = QPushButton(self.sheetBox)
        self.fileDirE.setObjectName(u"fileDirE")
        self.fileDirE.setEnabled(False)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.fileDirE.setPalette(palette1)

        self.gridLayout.addWidget(self.fileDirE, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.sheetBox, 0, 0, 1, 1)

        self.thumbBox = QGroupBox(self.centralWidget)
        self.thumbBox.setObjectName(u"thumbBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.thumbBox.sizePolicy().hasHeightForWidth())
        self.thumbBox.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.thumbBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.thumbHeightL = QLabel(self.thumbBox)
        self.thumbHeightL.setObjectName(u"thumbHeightL")

        self.gridLayout_2.addWidget(self.thumbHeightL, 0, 0, 1, 1)

        self.thumbHeightE = QLineEdit(self.thumbBox)
        self.thumbHeightE.setObjectName(u"thumbHeightE")

        self.gridLayout_2.addWidget(self.thumbHeightE, 0, 1, 1, 1)

        self.thumbBorderL = QLabel(self.thumbBox)
        self.thumbBorderL.setObjectName(u"thumbBorderL")

        self.gridLayout_2.addWidget(self.thumbBorderL, 1, 0, 1, 1)

        self.thumbBorderE = QLineEdit(self.thumbBox)
        self.thumbBorderE.setObjectName(u"thumbBorderE")

        self.gridLayout_2.addWidget(self.thumbBorderE, 1, 1, 1, 1)

        self.thumbCoverModeL = QLabel(self.thumbBox)
        self.thumbCoverModeL.setObjectName(u"thumbCoverModeL")

        self.gridLayout_2.addWidget(self.thumbCoverModeL, 2, 0, 1, 1)

        self.thumbCoverModeC = QComboBox(self.thumbBox)
        self.thumbCoverModeC.addItem("")
        self.thumbCoverModeC.addItem("")
        self.thumbCoverModeC.addItem("")
        self.thumbCoverModeC.setObjectName(u"thumbCoverModeC")

        self.gridLayout_2.addWidget(self.thumbCoverModeC, 2, 1, 1, 1)

        self.thumbCoverL = QLabel(self.thumbBox)
        self.thumbCoverL.setObjectName(u"thumbCoverL")

        self.gridLayout_2.addWidget(self.thumbCoverL, 3, 0, 1, 1)

        self.thumbCoverE = QLineEdit(self.thumbBox)
        self.thumbCoverE.setObjectName(u"thumbCoverE")

        self.gridLayout_2.addWidget(self.thumbCoverE, 3, 1, 1, 1)

        self.thumbCoverScaleL = QLabel(self.thumbBox)
        self.thumbCoverScaleL.setObjectName(u"thumbCoverScaleL")

        self.gridLayout_2.addWidget(self.thumbCoverScaleL, 4, 0, 1, 1)

        self.thumbCoverScaleS = QComboBox(self.thumbBox)
        self.thumbCoverScaleS.addItem("")
        self.thumbCoverScaleS.addItem("")
        self.thumbCoverScaleS.addItem("")
        self.thumbCoverScaleS.addItem("")
        self.thumbCoverScaleS.addItem("")
        self.thumbCoverScaleS.addItem("")
        self.thumbCoverScaleS.setObjectName(u"thumbCoverScaleS")

        self.gridLayout_2.addWidget(self.thumbCoverScaleS, 4, 1, 1, 1)

        self.thumbMinSizeL = QLabel(self.thumbBox)
        self.thumbMinSizeL.setObjectName(u"thumbMinSizeL")

        self.gridLayout_2.addWidget(self.thumbMinSizeL, 5, 0, 1, 1)

        self.thumbMinSizeE = QLineEdit(self.thumbBox)
        self.thumbMinSizeE.setObjectName(u"thumbMinSizeE")

        self.gridLayout_2.addWidget(self.thumbMinSizeE, 5, 1, 1, 1)


        self.gridLayout_4.addWidget(self.thumbBox, 0, 1, 1, 1)

        self.titleBox = QGroupBox(self.centralWidget)
        self.titleBox.setObjectName(u"titleBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleBox.sizePolicy().hasHeightForWidth())
        self.titleBox.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.titleBox)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.titleT = QCheckBox(self.titleBox)
        self.titleT.setObjectName(u"titleT")
        self.titleT.setEnabled(False)
        self.titleT.setChecked(True)

        self.gridLayout_3.addWidget(self.titleT, 1, 2, 1, 1)

        self.titleSizeE = QLineEdit(self.titleBox)
        self.titleSizeE.setObjectName(u"titleSizeE")
        self.titleSizeE.setEnabled(False)

        self.gridLayout_3.addWidget(self.titleSizeE, 2, 1, 1, 1)

        self.titleL = QLabel(self.titleBox)
        self.titleL.setObjectName(u"titleL")

        self.gridLayout_3.addWidget(self.titleL, 1, 0, 1, 1)

        self.titleStatsC = QComboBox(self.titleBox)
        self.titleStatsC.addItem("")
        self.titleStatsC.addItem("")
        self.titleStatsC.setObjectName(u"titleStatsC")
        self.titleStatsC.setEnabled(False)

        self.gridLayout_3.addWidget(self.titleStatsC, 5, 1, 1, 1)

        self.titleE = QLineEdit(self.titleBox)
        self.titleE.setObjectName(u"titleE")
        self.titleE.setEnabled(False)

        self.gridLayout_3.addWidget(self.titleE, 1, 1, 1, 1)

        self.titleEnableC = QCheckBox(self.titleBox)
        self.titleEnableC.setObjectName(u"titleEnableC")

        self.gridLayout_3.addWidget(self.titleEnableC, 0, 1, 1, 1)

        self.titleEnableL = QLabel(self.titleBox)
        self.titleEnableL.setObjectName(u"titleEnableL")

        self.gridLayout_3.addWidget(self.titleEnableL, 0, 0, 1, 1)

        self.titleStatsL = QLabel(self.titleBox)
        self.titleStatsL.setObjectName(u"titleStatsL")

        self.gridLayout_3.addWidget(self.titleStatsL, 5, 0, 1, 1)

        self.titleColorL = QLabel(self.titleBox)
        self.titleColorL.setObjectName(u"titleColorL")

        self.gridLayout_3.addWidget(self.titleColorL, 3, 0, 1, 1)

        self.titleSizeL = QLabel(self.titleBox)
        self.titleSizeL.setObjectName(u"titleSizeL")

        self.gridLayout_3.addWidget(self.titleSizeL, 2, 0, 1, 1)

        self.titleColorB = QPushButton(self.titleBox)
        self.titleColorB.setObjectName(u"titleColorB")
        self.titleColorB.setEnabled(False)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.titleColorB.setPalette(palette2)

        self.gridLayout_3.addWidget(self.titleColorB, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.titleBox, 1, 0, 1, 1)

        self.runB = QPushButton(self.centralWidget)
        self.runB.setObjectName(u"runB")

        self.gridLayout_4.addWidget(self.runB, 3, 0, 1, 2)

        self.dirsBox = QGroupBox(self.centralWidget)
        self.dirsBox.setObjectName(u"dirsBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.dirsBox.sizePolicy().hasHeightForWidth())
        self.dirsBox.setSizePolicy(sizePolicy3)
        self.gridLayout_5 = QGridLayout(self.dirsBox)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.dirsSubdirContactsB = QCheckBox(self.dirsBox)
        self.dirsSubdirContactsB.setObjectName(u"dirsSubdirContactsB")

        self.gridLayout_5.addWidget(self.dirsSubdirContactsB, 2, 0, 1, 1)

        self.dirsSubdirImagesB = QCheckBox(self.dirsBox)
        self.dirsSubdirImagesB.setObjectName(u"dirsSubdirImagesB")

        self.gridLayout_5.addWidget(self.dirsSubdirImagesB, 2, 1, 1, 1)

        self.dirsArchivesB = QCheckBox(self.dirsBox)
        self.dirsArchivesB.setObjectName(u"dirsArchivesB")

        self.gridLayout_5.addWidget(self.dirsArchivesB, 2, 2, 1, 1)

        self.dirsAddB = QPushButton(self.dirsBox)
        self.dirsAddB.setObjectName(u"dirsAddB")

        self.gridLayout_5.addWidget(self.dirsAddB, 1, 0, 1, 2)

        self.dirsClearB = QPushButton(self.dirsBox)
        self.dirsClearB.setObjectName(u"dirsClearB")

        self.gridLayout_5.addWidget(self.dirsClearB, 1, 2, 1, 1)

        self.dirsL = DirsList(self.dirsBox)
        self.dirsL.setObjectName(u"dirsL")
        self.dirsL.setAcceptDrops(True)
        self.dirsL.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.dirsL.setDragEnabled(True)

        self.gridLayout_5.addWidget(self.dirsL, 0, 0, 1, 3)


        self.gridLayout_4.addWidget(self.dirsBox, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelEnableL = QLabel(self.groupBox)
        self.labelEnableL.setObjectName(u"labelEnableL")

        self.gridLayout_6.addWidget(self.labelEnableL, 0, 0, 1, 1)

        self.labelEnableC = QCheckBox(self.groupBox)
        self.labelEnableC.setObjectName(u"labelEnableC")

        self.gridLayout_6.addWidget(self.labelEnableC, 0, 1, 1, 1)

        self.labelSizeL = QLabel(self.groupBox)
        self.labelSizeL.setObjectName(u"labelSizeL")

        self.gridLayout_6.addWidget(self.labelSizeL, 1, 0, 1, 1)

        self.labelSizeE = QLineEdit(self.groupBox)
        self.labelSizeE.setObjectName(u"labelSizeE")
        self.labelSizeE.setEnabled(False)

        self.gridLayout_6.addWidget(self.labelSizeE, 1, 1, 1, 1)

        self.labelColorL = QLabel(self.groupBox)
        self.labelColorL.setObjectName(u"labelColorL")

        self.gridLayout_6.addWidget(self.labelColorL, 2, 0, 1, 1)

        self.labelColorB = QPushButton(self.groupBox)
        self.labelColorB.setObjectName(u"labelColorB")
        self.labelColorB.setEnabled(False)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.labelColorB.setPalette(palette3)

        self.gridLayout_6.addWidget(self.labelColorB, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 1)

        mc_main.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(mc_main)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 657, 23))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        mc_main.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(mc_main)
        self.statusBar.setObjectName(u"statusBar")
        mc_main.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_Config)
        self.menuFile.addAction(self.actionSave_Config)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(mc_main)
        self.actionQuit.activated.connect(mc_main.close)

        self.thumbCoverScaleS.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(mc_main)
    # setupUi

    def retranslateUi(self, mc_main):
        mc_main.setWindowTitle(QCoreApplication.translate("mc_main", u"Make Contact Sheet(s)", None))
        self.actionQuit.setText(QCoreApplication.translate("mc_main", u"Quit", None))
        self.actionSave_Config.setText(QCoreApplication.translate("mc_main", u"Save Config", None))
        self.actionLoad_Config.setText(QCoreApplication.translate("mc_main", u"Load Config", None))
        self.sheetBox.setTitle(QCoreApplication.translate("mc_main", u"Sheet Output Specs", None))
        self.fileDirT.setText(QCoreApplication.translate("mc_main", u"Image Dir", None))
        self.fileDirL.setText(QCoreApplication.translate("mc_main", u"Output Directory", None))
        self.fileQualL.setText(QCoreApplication.translate("mc_main", u"Quality :", None))
        self.fileOrderC.setItemText(0, QCoreApplication.translate("mc_main", u"Alphabetical", None))
        self.fileOrderC.setItemText(1, QCoreApplication.translate("mc_main", u"Random", None))

        self.fileWidthL.setText(QCoreApplication.translate("mc_main", u"Width :", None))
        self.fileHeightE.setText("")
#if QT_CONFIG(accessibility)
        self.fileQualE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.fileQualE.setText(QCoreApplication.translate("mc_main", u"90", None))
        self.fileOverwriteL.setText(QCoreApplication.translate("mc_main", u"Overwrite :", None))
        self.fileHeightT.setText(QCoreApplication.translate("mc_main", u"Auto", None))
        self.fileOrderL.setText(QCoreApplication.translate("mc_main", u"Image Order :", None))
#if QT_CONFIG(accessibility)
        self.fileExtE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.fileExtE.setText(QCoreApplication.translate("mc_main", u"jpg", None))
        self.fileWidthE.setText(QCoreApplication.translate("mc_main", u"900", None))
        self.fileBackgroundL.setText(QCoreApplication.translate("mc_main", u"Background Color :", None))
        self.fileHeightL.setText(QCoreApplication.translate("mc_main", u"Height:", None))
        self.fileExtL.setText(QCoreApplication.translate("mc_main", u"File Type (ext) :", None))
        self.fileOverwriteC.setItemText(0, QCoreApplication.translate("mc_main", u"Keep Existing", None))
        self.fileOverwriteC.setItemText(1, QCoreApplication.translate("mc_main", u"Overwrite Existing", None))

        self.fileBackgroundB.setText("")
        self.fileDirE.setText("")
        self.thumbBox.setTitle(QCoreApplication.translate("mc_main", u"Thumbnail Specs", None))
        self.thumbHeightL.setText(QCoreApplication.translate("mc_main", u"Height :", None))
#if QT_CONFIG(accessibility)
        self.thumbHeightE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.thumbHeightE.setText(QCoreApplication.translate("mc_main", u"200", None))
        self.thumbBorderL.setText(QCoreApplication.translate("mc_main", u"Border Width :", None))
#if QT_CONFIG(accessibility)
        self.thumbBorderE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.thumbBorderE.setText(QCoreApplication.translate("mc_main", u"0", None))
        self.thumbCoverModeL.setText(QCoreApplication.translate("mc_main", u"Cover Mode :", None))
        self.thumbCoverModeC.setItemText(0, QCoreApplication.translate("mc_main", u"No Cover", None))
        self.thumbCoverModeC.setItemText(1, QCoreApplication.translate("mc_main", u"Automatic Detection", None))
        self.thumbCoverModeC.setItemText(2, QCoreApplication.translate("mc_main", u"Explicit File Name", None))

        self.thumbCoverL.setText(QCoreApplication.translate("mc_main", u"Cover File :", None))
#if QT_CONFIG(accessibility)
        self.thumbCoverE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.thumbCoverE.setText("")
        self.thumbCoverScaleL.setText(QCoreApplication.translate("mc_main", u"Cover Scale :", None))
        self.thumbCoverScaleS.setItemText(0, QCoreApplication.translate("mc_main", u"1 Thumb High", None))
        self.thumbCoverScaleS.setItemText(1, QCoreApplication.translate("mc_main", u"2 Thumbs High", None))
        self.thumbCoverScaleS.setItemText(2, QCoreApplication.translate("mc_main", u"3 Thumbs High", None))
        self.thumbCoverScaleS.setItemText(3, QCoreApplication.translate("mc_main", u"4 Thumbs High", None))
        self.thumbCoverScaleS.setItemText(4, QCoreApplication.translate("mc_main", u"5 ThumbsHigh", None))
        self.thumbCoverScaleS.setItemText(5, QCoreApplication.translate("mc_main", u"Full Sheet Width", None))

        self.thumbMinSizeL.setText(QCoreApplication.translate("mc_main", u"Min Size :", None))
#if QT_CONFIG(accessibility)
        self.thumbMinSizeE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"Minimum width/height for image to be included in sheet", None))
#endif // QT_CONFIG(accessibility)
        self.thumbMinSizeE.setText(QCoreApplication.translate("mc_main", u"0", None))
        self.titleBox.setTitle(QCoreApplication.translate("mc_main", u"Title Specs", None))
        self.titleT.setText(QCoreApplication.translate("mc_main", u"Auto", None))
#if QT_CONFIG(accessibility)
        self.titleSizeE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.titleSizeE.setInputMask(QCoreApplication.translate("mc_main", u"999; ", None))
        self.titleSizeE.setText(QCoreApplication.translate("mc_main", u"24", None))
        self.titleL.setText(QCoreApplication.translate("mc_main", u"Title :", None))
        self.titleStatsC.setItemText(0, QCoreApplication.translate("mc_main", u"None", None))
        self.titleStatsC.setItemText(1, QCoreApplication.translate("mc_main", u"Image Size and Counts", None))

#if QT_CONFIG(accessibility)
        self.titleE.setAccessibleDescription(QCoreApplication.translate("mc_main", u"File type/extension to use for sheet", None))
#endif // QT_CONFIG(accessibility)
        self.titleE.setText("")
        self.titleEnableC.setText("")
        self.titleEnableL.setText(QCoreApplication.translate("mc_main", u"Enable:", None))
        self.titleStatsL.setText(QCoreApplication.translate("mc_main", u"Stats :", None))
        self.titleColorL.setText(QCoreApplication.translate("mc_main", u"Color :", None))
        self.titleSizeL.setText(QCoreApplication.translate("mc_main", u"Font Size :", None))
        self.titleColorB.setText("")
        self.runB.setText(QCoreApplication.translate("mc_main", u"Run", None))
        self.dirsBox.setTitle(QCoreApplication.translate("mc_main", u"Directories", None))
        self.dirsSubdirContactsB.setText(QCoreApplication.translate("mc_main", u"Create contacts for Subdirs", None))
        self.dirsSubdirImagesB.setText(QCoreApplication.translate("mc_main", u"Use images from subdirs", None))
        self.dirsArchivesB.setText(QCoreApplication.translate("mc_main", u"Use archives (zip/rar/7z) as image sources", None))
        self.dirsAddB.setText(QCoreApplication.translate("mc_main", u"Add ...", None))
        self.dirsClearB.setText(QCoreApplication.translate("mc_main", u"Clear", None))
        self.groupBox.setTitle(QCoreApplication.translate("mc_main", u"Image Label Specs", None))
        self.labelEnableL.setText(QCoreApplication.translate("mc_main", u"Enable", None))
        self.labelEnableC.setText("")
        self.labelSizeL.setText(QCoreApplication.translate("mc_main", u"Font Size", None))
        self.labelSizeE.setInputMask(QCoreApplication.translate("mc_main", u"999; ", None))
        self.labelSizeE.setText(QCoreApplication.translate("mc_main", u"8", None))
        self.labelColorL.setText(QCoreApplication.translate("mc_main", u"Color", None))
        self.labelColorB.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("mc_main", u"File", None))
    # retranslateUi

