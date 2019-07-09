# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 380, 704, 169))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.up_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.up_btn.setFont(font)
        self.up_btn.setObjectName("up_btn")
        self.verticalLayout.addWidget(self.up_btn)
        self.save_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.cause_name = QtWidgets.QLabel(self.centralwidget)
        self.cause_name.setGeometry(QtCore.QRect(40, 70, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cause_name.setFont(font)
        self.cause_name.setObjectName("cause_name")
        self.keyword = QtWidgets.QLabel(self.centralwidget)
        self.keyword.setGeometry(QtCore.QRect(280, 170, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.keyword.setFont(font)
        self.keyword.setObjectName("keyword")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(560, 70, 201, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.keyword_cnt = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.keyword_cnt.setFont(font)
        self.keyword_cnt.setObjectName("keyword_cnt")
        self.horizontalLayout_2.addWidget(self.keyword_cnt)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 300, 702, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.yes_btn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.yes_btn.setFont(font)
        self.yes_btn.setIconSize(QtCore.QSize(20, 20))
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        self.soso_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.soso_btn.setFont(font)
        self.soso_btn.setObjectName("soso_btn")
        self.horizontalLayout.addWidget(self.soso_btn)
        self.no_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.no_btn.setFont(font)
        self.no_btn.setObjectName("no_btn")
        self.horizontalLayout.addWidget(self.no_btn)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.no_btn.clicked.connect(mainWindow.set_word_no)
        self.soso_btn.clicked.connect(mainWindow.set_word_soso)
        self.yes_btn.clicked.connect(mainWindow.set_word_yes)
        self.up_btn.clicked.connect(mainWindow.up_word)
        self.save_btn.clicked.connect(mainWindow.save_word)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.up_btn.setText(_translate("mainWindow", "上一个（点错时用）"))
        self.save_btn.setText(_translate("mainWindow", "保存（退出前一定要保存！！！）"))
        self.pushButton.setText(_translate("mainWindow", "选择文件路径"))
        self.cause_name.setText(_translate("mainWindow", "用于显示案由"))
        self.keyword.setText(_translate("mainWindow", "用于显示关键词"))
        self.label_3.setText(_translate("mainWindow", "数量："))
        self.keyword_cnt.setText(_translate("mainWindow", "TextLabel"))
        self.yes_btn.setText(_translate("mainWindow", "正确"))
        self.soso_btn.setText(_translate("mainWindow", "相似"))
        self.no_btn.setText(_translate("mainWindow", "错误"))

