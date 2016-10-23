# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Code\Thready\controller\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Global_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Global_tabs.setEnabled(True)
        self.Global_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.Global_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Global_tabs.setDocumentMode(False)
        self.Global_tabs.setObjectName("Global_tabs")
        self.tab_Threads = QtWidgets.QWidget()
        self.tab_Threads.setObjectName("tab_Threads")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_Threads)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_Threads = QtWidgets.QVBoxLayout()
        self.verticalLayout_Threads.setObjectName("verticalLayout_Threads")
        self.lineEdit_ThreadFilter = QtWidgets.QLineEdit(self.tab_Threads)
        self.lineEdit_ThreadFilter.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_ThreadFilter.setObjectName("lineEdit_ThreadFilter")
        self.verticalLayout_Threads.addWidget(self.lineEdit_ThreadFilter)
        self.listView_ThreadList = QtWidgets.QListView(self.tab_Threads)
        self.listView_ThreadList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listView_ThreadList.setObjectName("listView_ThreadList")
        self.verticalLayout_Threads.addWidget(self.listView_ThreadList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_Threads)
        self.Global_tabs.addTab(self.tab_Threads, "")
        self.tab_Search = QtWidgets.QWidget()
        self.tab_Search.setObjectName("tab_Search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_Search)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Global_tabs.addTab(self.tab_Search, "")
        self.horizontalLayout.addWidget(self.Global_tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Global_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Global_tabs.setTabText(self.Global_tabs.indexOf(self.tab_Threads), _translate("MainWindow", "Threads"))
        self.Global_tabs.setTabText(self.Global_tabs.indexOf(self.tab_Search), _translate("MainWindow", "Search"))

