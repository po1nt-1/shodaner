# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 740)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 740))
        MainWindow.setMaximumSize(QSize(1210, 740))
        font = QFont()
        font.setFamily(u"Open Sans Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"color: #FFF;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_ip_list = QPlainTextEdit(self.centralwidget)
        self.text_ip_list.setObjectName(u"text_ip_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_ip_list.sizePolicy().hasHeightForWidth())
        self.text_ip_list.setSizePolicy(sizePolicy1)
        self.text_ip_list.setMinimumSize(QSize(240, 40))
        self.text_ip_list.setMaximumSize(QSize(240, 400))
        font1 = QFont()
        font1.setFamily(u"Open Sans Light")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.text_ip_list.setFont(font1)
        self.text_ip_list.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.text_ip_list.setMouseTracking(True)
        self.text_ip_list.setStyleSheet(u"QPlainTextEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.text_ip_list.setInputMethodHints(Qt.ImhMultiLine)
        self.text_ip_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.text_ip_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_ip_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.text_ip_list.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.text_ip_list.setReadOnly(False)
        self.text_ip_list.setOverwriteMode(False)
        self.text_ip_list.setBackgroundVisible(False)
        self.text_ip_list.setCenterOnScroll(False)

        self.verticalLayout_2.addWidget(self.text_ip_list)

        self.button_send_request = QPushButton(self.centralwidget)
        self.button_send_request.setObjectName(u"button_send_request")
        sizePolicy.setHeightForWidth(self.button_send_request.sizePolicy().hasHeightForWidth())
        self.button_send_request.setSizePolicy(sizePolicy)
        self.button_send_request.setMinimumSize(QSize(240, 40))
        self.button_send_request.setMaximumSize(QSize(240, 40))
        self.button_send_request.setFont(font1)
        self.button_send_request.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_send_request)

        self.button_save_last = QPushButton(self.centralwidget)
        self.button_save_last.setObjectName(u"button_save_last")
        sizePolicy.setHeightForWidth(self.button_save_last.sizePolicy().hasHeightForWidth())
        self.button_save_last.setSizePolicy(sizePolicy)
        self.button_save_last.setMinimumSize(QSize(240, 40))
        self.button_save_last.setMaximumSize(QSize(240, 40))
        self.button_save_last.setFont(font1)
        self.button_save_last.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_save_last)

        self.button_save_last_10 = QPushButton(self.centralwidget)
        self.button_save_last_10.setObjectName(u"button_save_last_10")
        sizePolicy.setHeightForWidth(self.button_save_last_10.sizePolicy().hasHeightForWidth())
        self.button_save_last_10.setSizePolicy(sizePolicy)
        self.button_save_last_10.setMinimumSize(QSize(240, 40))
        self.button_save_last_10.setMaximumSize(QSize(240, 40))
        self.button_save_last_10.setFont(font1)
        self.button_save_last_10.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_save_last_10)

        self.button_upload_to_table = QPushButton(self.centralwidget)
        self.button_upload_to_table.setObjectName(u"button_upload_to_table")
        sizePolicy.setHeightForWidth(self.button_upload_to_table.sizePolicy().hasHeightForWidth())
        self.button_upload_to_table.setSizePolicy(sizePolicy)
        self.button_upload_to_table.setMinimumSize(QSize(240, 40))
        self.button_upload_to_table.setMaximumSize(QSize(240, 40))
        self.button_upload_to_table.setFont(font1)
        self.button_upload_to_table.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_upload_to_table)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_token = QLineEdit(self.centralwidget)
        self.lineEdit_token.setObjectName(u"lineEdit_token")
        self.lineEdit_token.setMinimumSize(QSize(300, 40))
        self.lineEdit_token.setMaximumSize(QSize(300, 40))
        self.lineEdit_token.setFont(font1)
        self.lineEdit_token.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_token.setMaxLength(32)
        self.lineEdit_token.setEchoMode(QLineEdit.Password)
        self.lineEdit_token.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_token.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_token)

        self.button_change_token = QPushButton(self.centralwidget)
        self.button_change_token.setObjectName(u"button_change_token")
        sizePolicy.setHeightForWidth(self.button_change_token.sizePolicy().hasHeightForWidth())
        self.button_change_token.setSizePolicy(sizePolicy)
        self.button_change_token.setMinimumSize(QSize(160, 40))
        self.button_change_token.setMaximumSize(QSize(160, 40))
        self.button_change_token.setFont(font1)
        self.button_change_token.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.horizontalLayout_3.addWidget(self.button_change_token)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.tableWidget_user = QTableWidget(self.centralwidget)
        if (self.tableWidget_user.columnCount() < 3):
            self.tableWidget_user.setColumnCount(3)
        self.tableWidget_user.setObjectName(u"tableWidget_user")
        sizePolicy.setHeightForWidth(self.tableWidget_user.sizePolicy().hasHeightForWidth())
        self.tableWidget_user.setSizePolicy(sizePolicy)
        self.tableWidget_user.setMinimumSize(QSize(281, 75))
        self.tableWidget_user.setMaximumSize(QSize(281, 75))
        self.tableWidget_user.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Open Sans Light")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.tableWidget_user.setFont(font2)
        self.tableWidget_user.setMouseTracking(False)
        self.tableWidget_user.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_user.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_user.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_user.setAutoFillBackground(False)
        self.tableWidget_user.setStyleSheet(u"QHeaderView::section {\n"
"    padding: 4px;\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QTableWidget {\n"
"    gridline-color: rgb(48, 50, 62);\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(34, 36, 44);\n"
"	width: 10px;\n"
"	margin: 25px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	border-radius: 4px;\n"
"	border-color: rgba(216, 216, 216, 75%);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	background-color: rgba(216, 216, 216, 75%);\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"	width: 0px;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	width: 0px;\n"
"	height: 0px;\n"
"}")
        self.tableWidget_user.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_user.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_user.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_user.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_user.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_user.setShowGrid(True)
        self.tableWidget_user.setGridStyle(Qt.DashLine)
        self.tableWidget_user.setRowCount(0)
        self.tableWidget_user.setColumnCount(3)
        self.tableWidget_user.horizontalHeader().setVisible(False)
        self.tableWidget_user.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_user.horizontalHeader().setMinimumSectionSize(93)
        self.tableWidget_user.horizontalHeader().setDefaultSectionSize(93)
        self.tableWidget_user.horizontalHeader().setHighlightSections(True)
        self.tableWidget_user.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_user.verticalHeader().setVisible(False)
        self.tableWidget_user.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget_user.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_user.verticalHeader().setHighlightSections(True)
        self.tableWidget_user.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_3.addWidget(self.tableWidget_user)

        self.horizontalSpacer_2 = QSpacerItem(36, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableWidget_main = QTableWidget(self.centralwidget)
        if (self.tableWidget_main.columnCount() < 10):
            self.tableWidget_main.setColumnCount(10)
        self.tableWidget_main.setObjectName(u"tableWidget_main")
        sizePolicy.setHeightForWidth(self.tableWidget_main.sizePolicy().hasHeightForWidth())
        self.tableWidget_main.setSizePolicy(sizePolicy)
        self.tableWidget_main.setMinimumSize(QSize(905, 600))
        self.tableWidget_main.setMaximumSize(QSize(905, 600))
        self.tableWidget_main.setSizeIncrement(QSize(0, 0))
        self.tableWidget_main.setFont(font2)
        self.tableWidget_main.setMouseTracking(False)
        self.tableWidget_main.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_main.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_main.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_main.setAutoFillBackground(False)
        self.tableWidget_main.setStyleSheet(u"QHeaderView::section {\n"
"    padding: 4px;\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QTableWidget {\n"
"    gridline-color: rgb(48, 50, 62);\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(34, 36, 44);\n"
"	width: 10px;\n"
"	margin: 25px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	border-radius: 4px;\n"
"	border-color: rgba(216, 216, 216, 75%);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	background-color: rgba(216, 216, 216, 75%);\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"	width: 0px;\n"
"	height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	width: 0px;\n"
"	height: 0px;\n"
"}")
        self.tableWidget_main.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_main.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_main.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_main.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_main.setGridStyle(Qt.DashLine)
        self.tableWidget_main.setSortingEnabled(False)
        self.tableWidget_main.setRowCount(0)
        self.tableWidget_main.setColumnCount(10)
        self.tableWidget_main.horizontalHeader().setVisible(False)
        self.tableWidget_main.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_main.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_main.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_main.verticalHeader().setVisible(False)
        self.tableWidget_main.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_main.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_main.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_main.verticalHeader().setHighlightSections(True)
        self.tableWidget_main.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout.addWidget(self.tableWidget_main)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"parser", None))
#if QT_CONFIG(whatsthis)
        self.text_ip_list.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.text_ip_list.setDocumentTitle("")
        self.text_ip_list.setPlaceholderText("")
        self.button_send_request.setText(QCoreApplication.translate("MainWindow", u"Send request", None))
        self.button_save_last.setText(QCoreApplication.translate("MainWindow", u"Save last result to csv", None))
        self.button_save_last_10.setText(QCoreApplication.translate("MainWindow", u"Save last 10 results to csv", None))
        self.button_upload_to_table.setText(QCoreApplication.translate("MainWindow", u"Upload from csv", None))
        self.lineEdit_token.setText("")
        self.lineEdit_token.setPlaceholderText(QCoreApplication.translate("MainWindow", u"API Key", None))
        self.button_change_token.setText(QCoreApplication.translate("MainWindow", u"Set new API Key", None))
    # retranslateUi

