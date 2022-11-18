# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans_pynfQZrz.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(650, 559)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"/*/344854/*/\n"
"\n"
"QWidget{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"#Form{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:#EFF3F6;\n"
"	\n"
"	color: rgb(28, 40, 47);\n"
"	border-radius: 7px;\n"
"\n"
"}\n"
" QDialogButtonBox > QPushButton[text=\"&OK\"] {\n"
"        background-color: orange;\n"
"    }\n"
"/*/---------------------------QPushButton------------------------>>/*/\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(28, 40, 47);\n"
"	color: rgb(241, 242, 242);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"QToolButton{\n"
"	\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/*/---------------------------QScrollBar------------------------>>/*/\n"
"\n"
"QScrollBar::vertical {\n"
"	background-color: rgb(220, 220, 220);\n"
"	margin:0px 0 0px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color:rgb(28, 40, 47);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
""
                        "	background-color: rgb(239, 243, 246);\n"
"	margin:0px 0 0px 0;\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	background-color: rgb(220, 220, 220);\n"
"	margin:0px 0 0px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color:  rgb(220, 220, 220);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color:  rgb(220, 220, 220);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color:  rgb(220, 220, 220);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background-color:  rgb(220, 220, 220);\n"
"}\n"
"\n"
"/*/---------------------------QComboBox------------------------>>/*/\n"
"\n"
"QComboBox{\n"
"	color: rgb(28, 40, 47);\n"
"	background-color:rgb(239, 243, 246);\n"
"	padding-left: 10px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(Data/PNG/caret-circle-down_1.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	margin-right: 15px\n"
"}\n"
"\n"
""
                        "QComboBox QListView{\n"
"	border: 1px;\n"
"	color: rgb(28, 40, 47);\n"
"	background-color: rgb(239, 243, 246);\n"
"	outline: 0px\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left: 10px;\n"
"	background-color: rgb(255, 0, 255);\n"
"}\n"
"\n"
"QComboBox QListView::item::hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QComboBox QListView::item:selected{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.SelectPy = QLineEdit(Form)
        self.SelectPy.setObjectName(u"SelectPy")
        self.SelectPy.setGeometry(QRect(110, 130, 451, 31))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.SelectPy.setFont(font)
        self.SelectPy.setMouseTracking(True)
        self.SelectPy.setFocusPolicy(Qt.ClickFocus)
        self.SelectPy.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.SelectPy.setFrame(True)
        self.SelectIco = QLineEdit(Form)
        self.SelectIco.setObjectName(u"SelectIco")
        self.SelectIco.setGeometry(QRect(110, 180, 451, 31))
        self.SelectIco.setFont(font)
        self.SelectIco.setFocusPolicy(Qt.ClickFocus)
        self.Button_Ico = QPushButton(Form)
        self.Button_Ico.setObjectName(u"Button_Ico")
        self.Button_Ico.setGeometry(QRect(530, 180, 31, 31))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiBold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.Button_Ico.setFont(font1)
        self.Button_Ico.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Ico.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px")
        self.Button_Py = QPushButton(Form)
        self.Button_Py.setObjectName(u"Button_Py")
        self.Button_Py.setGeometry(QRect(530, 130, 31, 31))
        self.Button_Py.setFont(font1)
        self.Button_Py.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Py.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px")
        self.Button_Finsh = QPushButton(Form)
        self.Button_Finsh.setObjectName(u"Button_Finsh")
        self.Button_Finsh.setGeometry(QRect(176, 370, 311, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.Button_Finsh.setFont(font2)
        self.Button_Finsh.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Finsh.setStyleSheet(u"background-color:rgb(80, 216, 144);\n"
"\n"
"")
        self.radio_OneFile = QRadioButton(Form)
        self.radio_OneFile.setObjectName(u"radio_OneFile")
        self.radio_OneFile.setGeometry(QRect(110, 270, 82, 17))
        self.radio_OneFile.setFont(font2)
        self.radio_OneFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio_OneFile.setChecked(True)
        self.radio_Files = QRadioButton(Form)
        self.radio_Files.setObjectName(u"radio_Files")
        self.radio_Files.setGeometry(QRect(200, 270, 61, 17))
        self.radio_Files.setFont(font2)
        self.radio_Files.setCursor(QCursor(Qt.PointingHandCursor))
        self.Terminal = QTextEdit(Form)
        self.Terminal.setObjectName(u"Terminal")
        self.Terminal.setGeometry(QRect(20, 410, 611, 141))
        self.Terminal.setFont(font1)
        self.Terminal.setStyleSheet(u"color: rgb(239, 243, 246);\n"
"background-color: rgb(28, 40, 47);\n"
"border-radius: 7px;")
        self.Terminal.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Terminal.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Terminal.setAcceptRichText(True)
        self.Terminal.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.SaveFile = QLineEdit(Form)
        self.SaveFile.setObjectName(u"SaveFile")
        self.SaveFile.setGeometry(QRect(110, 230, 451, 31))
        self.SaveFile.setFont(font)
        self.SaveFile.setFocusPolicy(Qt.ClickFocus)
        self.Button_save = QPushButton(Form)
        self.Button_save.setObjectName(u"Button_save")
        self.Button_save.setGeometry(QRect(530, 230, 31, 31))
        self.Button_save.setFont(font1)
        self.Button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_save.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px")
        self.Enter_name = QLineEdit(Form)
        self.Enter_name.setObjectName(u"Enter_name")
        self.Enter_name.setGeometry(QRect(110, 80, 451, 31))
        self.Enter_name.setFont(font)
        self.Enter_name.setFocusPolicy(Qt.ClickFocus)
        self.Enter_name.setToolTipDuration(1)
        self.Enter_name.setLayoutDirection(Qt.LeftToRight)
        self.Button_Copy = QPushButton(Form)
        self.Button_Copy.setObjectName(u"Button_Copy")
        self.Button_Copy.setGeometry(QRect(600, 420, 21, 21))
        self.Button_Copy.setFont(font2)
        self.Button_Copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Copy.setStyleSheet(u"color: rgb(28, 40, 47);\n"
"background-color: rgba(0, 0, 0, 0);")
        icon = QIcon()
        icon.addFile(u"Data/PNG/duplicate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Copy.setIcon(icon)
        self.Button_Copy.setIconSize(QSize(20, 20))
        self.Button_Copy.setCheckable(True)
        self.Button_Copy.setChecked(False)
        self.Administrator = QPushButton(Form)
        self.Administrator.setObjectName(u"Administrator")
        self.Administrator.setGeometry(QRect(440, 270, 21, 21))
        self.Administrator.setFont(font2)
        self.Administrator.setCursor(QCursor(Qt.PointingHandCursor))
        self.Administrator.setStyleSheet(u"color: rgb(28, 40, 47);\n"
"background-color: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u"Data/PNG/low2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"Data/PNG/low1.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u"Data/PNG/low1.png", QSize(), QIcon.Disabled, QIcon.On)
        self.Administrator.setIcon(icon1)
        self.Administrator.setCheckable(True)
        self.Administrator.setChecked(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(464, 270, 81, 20))
        self.label.setFont(font2)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 270, 141, 20))
        self.label_2.setFont(font2)
        self.Remove_Console = QPushButton(Form)
        self.Remove_Console.setObjectName(u"Remove_Console")
        self.Remove_Console.setGeometry(QRect(276, 270, 21, 21))
        self.Remove_Console.setFont(font2)
        self.Remove_Console.setCursor(QCursor(Qt.PointingHandCursor))
        self.Remove_Console.setStyleSheet(u"color: rgb(28, 40, 47);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.Remove_Console.setIcon(icon1)
        self.Remove_Console.setCheckable(True)
        self.Remove_Console.setChecked(False)
        self.pushButton_24 = QPushButton(Form)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(20, 350, 51, 51))
        self.pushButton_24.setFont(font2)
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"color: rgb(28, 40, 47);\n"
"background-color: rgba(0, 0, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u"Data/PNG/Untitled-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon2)
        self.pushButton_24.setIconSize(QSize(60, 60))
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(False)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 90, 47, 13))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 140, 71, 20))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 190, 31, 16))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 240, 71, 16))
        self.label_6.setFont(font2)

        self.retranslateUi(Form)
        self.Button_Copy.released.connect(self.Terminal.selectAll)
        self.Button_Copy.released.connect(self.Terminal.copy)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.SelectPy.setInputMask("")
        self.SelectPy.setPlaceholderText(QCoreApplication.translate("Form", u"Select file (.py)", None))
        self.SelectIco.setPlaceholderText(QCoreApplication.translate("Form", u"Select icon (png, jpg, ico)", None))
        self.Button_Ico.setText(QCoreApplication.translate("Form", u"...", None))
        self.Button_Py.setText(QCoreApplication.translate("Form", u"...", None))
        self.Button_Finsh.setText(QCoreApplication.translate("Form", u"Finsh", None))
        self.radio_OneFile.setText(QCoreApplication.translate("Form", u"One file", None))
        self.radio_Files.setText(QCoreApplication.translate("Form", u"Files", None))
        self.Terminal.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift SemiBold'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vilda TransPy Copyright (C) Vilda Corporation. All rights reserved. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Using Library 'pyinstaller'.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Telegram: <a href=\"t.me/Vilda_TM\"><sp"
                        "an style=\" text-decoration: underline; color:#50d890;\">t.me/Vilda_TM</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Github: <a href=\"t.me/Vilda_TM\"><span style=\" text-decoration: underline; color:#50d890;\">github.com/vildacode</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">============================</p></body></html>", None))
        self.SaveFile.setPlaceholderText(QCoreApplication.translate("Form", u"Save folder (.exe)", None))
        self.Button_save.setText(QCoreApplication.translate("Form", u"...", None))
        self.Enter_name.setPlaceholderText(QCoreApplication.translate("Form", u"Name file .exe", None))
        self.Button_Copy.setText("")
        self.Administrator.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Administrator", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Remove console window", None))
        self.Remove_Console.setText("")
        self.pushButton_24.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"File python:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Icon:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Save folder:", None))
    # retranslateUi

