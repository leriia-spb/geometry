# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formauth.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_authwindow(object):
    def setupUi(self, authwindow):
        authwindow.setObjectName("authwindow")
        authwindow.resize(276, 355)
        authwindow.setDocumentMode(False)
        authwindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(authwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(220, 0, 51, 41))
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
        self.label.setGeometry(QtCore.QRect(10, 0, 201, 41))
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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 261, 231))
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
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 101, 16))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.last = QtWidgets.QPushButton(self.groupBox_2)
        self.last.setGeometry(QtCore.QRect(60, 160, 121, 31))
        self.last.setStyleSheet("QPushButton {\n"
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
        self.last.setObjectName("last")
        self.other = QtWidgets.QPushButton(self.groupBox_2)
        self.other.setGeometry(QtCore.QRect(150, 200, 31, 23))
        self.other.setStyleSheet("QPushButton {\n"
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
        self.other.setObjectName("other")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(36, 120, 71, 20))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 101, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        authwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(authwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName("menubar")
        authwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(authwindow)
        self.statusbar.setObjectName("statusbar")
        authwindow.setStatusBar(self.statusbar)

        self.retranslateUi(authwindow)
        QtCore.QMetaObject.connectSlotsByName(authwindow)

    def retranslateUi(self, authwindow):
        _translate = QtCore.QCoreApplication.translate
        authwindow.setWindowTitle(_translate("authwindow", "MainWindow"))
        self.label.setText(_translate("authwindow", "Регистрация"))
        self.label_13.setText(_translate("authwindow", "TextLabel"))
        self.label_14.setText(_translate("authwindow", "TextLabel"))
        self.label_2.setText(_translate("authwindow", "Уже есть аккаунт?"))
        self.label_3.setText(_translate("authwindow", "Придумайте логин:"))
        self.label_4.setText(_translate("authwindow", "Придумайте пароль:"))
        self.last.setText(_translate("authwindow", "Зарегистрироваться"))
        self.other.setText(_translate("authwindow", "Да!"))
        self.pushButton.setText(_translate("authwindow", "Выбрать фото"))
import photos
