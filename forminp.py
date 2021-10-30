# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forminp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inputwindow(object):
    def setupUi(self, inputwindow):
        inputwindow.setObjectName("inputwindow")
        inputwindow.resize(276, 354)
        inputwindow.setDocumentMode(False)
        inputwindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(inputwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(200, 0, 51, 41))
        self.closebutton.setMouseTracking(False)
        self.closebutton.setStyleSheet("QPushButton{\n"
"border: 1px solid #555;\n"
"padding: 5 px ;\n"
"border-top-right-radius: 11px;\n"
"background: black;\n"
"}\n"
"QPushButton:hover { background: rgba(255,255,255,.2); }\n"
"QPushButton:pressed { background: white; }")
        self.closebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos/крестик.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setDefault(False)
        self.closebutton.setObjectName("closebutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font: 75 italic 22pt \"MS Sans Serif\";\n"
"color: white;\n"
"border: 1px solid #555;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"}")
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 241, 181))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"border-bottom-left-radius: 11px;\n"
"border-bottom-right-radius: 11px;\n"
"background: black;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_14.setObjectName("label_14")
        self.login = QtWidgets.QLineEdit(self.groupBox_2)
        self.login.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.groupBox_2)
        self.password.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.enter = QtWidgets.QPushButton(self.groupBox_2)
        self.enter.setGeometry(QtCore.QRect(80, 112, 71, 31))
        self.enter.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  outline: none;\n"
"  border: 2px solid white;\n"
"  border-radius: 1px;\n"
"  transition: 0.2s;\n"
"} \n"
"QPushButton:hover { background: rgba(255,255,255,.2); }\n"
"QPushButton:pressed { background: white; }")
        self.enter.setObjectName("enter")
        self.back = QtWidgets.QPushButton(self.groupBox_2)
        self.back.setGeometry(QtCore.QRect(60, 150, 111, 23))
        self.back.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  outline: none;\n"
"  border: 2px solid white;\n"
"  border-radius: 1px;\n"
"  transition: 0.2s;\n"
"} \n"
"QPushButton:hover { background: rgba(255,255,255,.2); }\n"
"QPushButton:pressed { background: white; }")
        self.back.setObjectName("back")
        self.groupBox_2.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        inputwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inputwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName("menubar")
        inputwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inputwindow)
        self.statusbar.setObjectName("statusbar")
        inputwindow.setStatusBar(self.statusbar)

        self.retranslateUi(inputwindow)
        QtCore.QMetaObject.connectSlotsByName(inputwindow)

    def retranslateUi(self, inputwindow):
        _translate = QtCore.QCoreApplication.translate
        inputwindow.setWindowTitle(_translate("inputwindow", "MainWindow"))
        self.label.setText(_translate("inputwindow", "Вход"))
        self.label_13.setText(_translate("inputwindow", "TextLabel"))
        self.label_14.setText(_translate("inputwindow", "TextLabel"))
        self.label_3.setText(_translate("inputwindow", "Введите логин:"))
        self.label_4.setText(_translate("inputwindow", "Введите пароль:"))
        self.enter.setText(_translate("inputwindow", "Вход"))
        self.back.setText(_translate("inputwindow", "Вернуться назад"))
import photos
