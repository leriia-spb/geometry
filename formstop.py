# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formstop.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stopwindow(object):
    def setupUi(self, stopwindow):
        stopwindow.setObjectName("stopwindow")
        stopwindow.resize(276, 228)
        stopwindow.setDocumentMode(False)
        stopwindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(stopwindow)
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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 261, 101))
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
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 241, 20))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.tomain = QtWidgets.QPushButton(self.groupBox_2)
        self.tomain.setGeometry(QtCore.QRect(130, 60, 121, 31))
        self.tomain.setStyleSheet("QPushButton {\n"
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
        self.tomain.setObjectName("tomain")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 251, 20))
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.groupBox_2.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        stopwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(stopwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName("menubar")
        stopwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(stopwindow)
        self.statusbar.setObjectName("statusbar")
        stopwindow.setStatusBar(self.statusbar)

        self.retranslateUi(stopwindow)
        QtCore.QMetaObject.connectSlotsByName(stopwindow)

    def retranslateUi(self, stopwindow):
        _translate = QtCore.QCoreApplication.translate
        stopwindow.setWindowTitle(_translate("stopwindow", "MainWindow"))
        self.label.setText(_translate("stopwindow", "Ошибка"))
        self.label_13.setText(_translate("stopwindow", "TextLabel"))
        self.label_14.setText(_translate("stopwindow", "TextLabel"))
        self.label_3.setText(_translate("stopwindow", "Увы! Пока этот урок не доступен..."))
        self.tomain.setText(_translate("stopwindow", "В главное меню"))
        self.label_2.setText(_translate("stopwindow", "Пройдите предыдущие уроки и возвращайтесь"))
import photos