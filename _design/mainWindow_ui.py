# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 680)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(245, 16777215))
        self.frame.setStyleSheet(u"background-color: transparent;\n"
"width:40px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"Corporate_Management.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        font = QFont()
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"#searchButton\n"
"{\n"
"	text-align:left;\n"
"	padding-left:20px;\n"
"	border:none;\n"
"	border-left:6px solid dodgerblue;\n"
"	color:white;	\n"
"	background:#333333;\n"
"	height:45px\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Images/icons8_Find_User_Male_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.searchButton)

        self.addEmpButton = QPushButton(self.frame)
        self.addEmpButton.setObjectName(u"addEmpButton")
        self.addEmpButton.setFont(font)
        self.addEmpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addEmpButton.setStyleSheet(u"#addEmpButton\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:rgb(31,31,31);\n"
"	height:45px\n"
"}\n"
"#addEmpButton:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Images/icons8_Add_User_Male_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addEmpButton.setIcon(icon1)
        self.addEmpButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.addEmpButton)

        self.updateEmpButton = QPushButton(self.frame)
        self.updateEmpButton.setObjectName(u"updateEmpButton")
        self.updateEmpButton.setFont(font)
        self.updateEmpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateEmpButton.setStyleSheet(u"#updateEmpButton\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"	height:45px\n"
"}\n"
"#updateEmpButton:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Images/icons8_Registration_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateEmpButton.setIcon(icon2)
        self.updateEmpButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.updateEmpButton)

        self.deleteEmpButton = QPushButton(self.frame)
        self.deleteEmpButton.setObjectName(u"deleteEmpButton")
        self.deleteEmpButton.setFont(font)
        self.deleteEmpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteEmpButton.setStyleSheet(u"#deleteEmpButton\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"height:45px}\n"
"#deleteEmpButton:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Images/icons8_Remove_User_Male_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteEmpButton.setIcon(icon3)
        self.deleteEmpButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.deleteEmpButton)

        self.techButton = QPushButton(self.frame)
        self.techButton.setObjectName(u"techButton")
        self.techButton.setFont(font)
        self.techButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.techButton.setStyleSheet(u"#techButton\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"	height:45px\n"
"}\n"
"#techButton:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;	\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333333;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Images/icons8_Hand_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.techButton.setIcon(icon4)
        self.techButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.techButton)

        self.aboutButton = QPushButton(self.frame)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setFont(font)
        self.aboutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutButton.setStyleSheet(u"#aboutButton\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"	height:45px\n"
"}\n"
"#aboutButton:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;	\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333333;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Images/icons8_Money_50px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutButton.setIcon(icon5)
        self.aboutButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.aboutButton)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(191, 49, 49);\n"
"	border:none;\n"
"	height:100%;\n"
"	border-radius: 10px ;\n"
"	color:white;\n"
"	font-weight: 700;\n"
"	font-size: 15px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color:rgb(85, 124, 85);\n"
"border:none;\n"
"height:100%;\n"
"border-radius: 10px ;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 15px")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color:rgb(97, 163, 186);\n"
"border:none;\n"
"height:100%;\n"
"border-radius: 10px ;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 15px")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:20px;\n"
"font-weight: 700;\n"
"font-size: 15px;\n"
"color:white;")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px ;\n"
"height:30px")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.frame_3)

        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QHeaderView::section{\n"
"background:rgb(31,31,31);\n"
"color:white;\n"
"border:none;\n"
"height:35px\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout_3.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 997, 22))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.addEmpButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.updateEmpButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.deleteEmpButton.setText(QCoreApplication.translate("MainWindow", u"  Delete", None))
        self.techButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"  About App", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">App Version: 1.0.0</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Professors", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search :", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mobile", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Grade", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

