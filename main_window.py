# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1154, 640)
        mainWindow.setDocumentMode(False)
        mainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(1070, 0, 51, 41))
        self.closebutton.setMouseTracking(False)
        self.closebutton.setStyleSheet("QPushButton{\n"
"border: 1px solid #555;\n"
"padding: 5 px ;\n"
"border-top-right-radius: 11px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, \n"
"fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(58, 58, 58), stop: 1 rgb(50, 50, 50));\n"
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
        self.label.setGeometry(QtCore.QRect(10, 0, 1051, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font: 75 italic 22pt \"MS Sans Serif\";\n"
"color: white;\n"
"border: 1px solid #555;\n"
"border-top-left-radius: 11px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, \n"
"fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(58, 58, 58), stop: 1 rgb(50, 50, 50));\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"}")
        self.label.setObjectName("label")
        self.box1 = QtWidgets.QGroupBox(self.centralwidget)
        self.box1.setGeometry(QtCore.QRect(10, 50, 1111, 101))
        self.box1.setStyleSheet("QGroupBox{\n"
"background-color: grey;\n"
"color: #333;\n"
"border: 1 px solid #555;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, \n"
"fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(53, 53, 53), stop: 1 rgb(22, 22, 22));\n"
"}")
        self.box1.setTitle("")
        self.box1.setObjectName("box1")
        self.mainprogress = QtWidgets.QProgressBar(self.box1)
        self.mainprogress.setGeometry(QtCore.QRect(480, 32, 621, 31))
        self.mainprogress.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius:15px;\n"
"    color: white;\n"
"    background-color: rgb(50, 50, 50);\n"
"    font: 75 12pt  \"MS Sans Serif\";\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius:13px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgba(201, 81, 149, 255), stop:1 rgba(179, 65, 244, 255));\n"
"}")
        self.mainprogress.setProperty("value", 24)
        self.mainprogress.setObjectName("mainprogress")
        self.namelabel = QtWidgets.QLabel(self.box1)
        self.namelabel.setGeometry(QtCore.QRect(130, 30, 331, 41))
        self.namelabel.setStyleSheet("QLabel{\n"
"    font: 75 italic 22pt \"MS Sans Serif\";\n"
"color: white;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"}")
        self.namelabel.setObjectName("namelabel")
        self.photo = QtWidgets.QLabel(self.box1)
        self.photo.setGeometry(QtCore.QRect(20, 10, 91, 81))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.mainbox = QtWidgets.QGroupBox(self.centralwidget)
        self.mainbox.setGeometry(QtCore.QRect(10, 160, 1111, 431))
        self.mainbox.setStyleSheet("QGroupBox{\n"
"border-bottom-left-radius: 11px;\n"
"border-bottom-right-radius: 11px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, \n"
"fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(35, 35, 35), stop: 1 rgb(0, 0, 0));\n"
"}")
        self.mainbox.setTitle("")
        self.mainbox.setObjectName("mainbox")
        self.les1 = QtWidgets.QGroupBox(self.mainbox)
        self.les1.setGeometry(QtCore.QRect(20, 20, 1071, 81))
        self.les1.setStyleSheet("QGroupBox{\n"
"background-color: black;\n"
"color: #333;\n"
" border: 2px solid white;\n"
"  border-radius: 1px;\n"
"}")
        self.les1.setTitle("")
        self.les1.setObjectName("les1")
        self.butp1 = QtWidgets.QPushButton(self.les1)
        self.butp1.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.butp1.setMouseTracking(False)
        self.butp1.setStyleSheet("QPushButton {\n"
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
        self.butp1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photos/кнопка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butp1.setIcon(icon1)
        self.butp1.setDefault(False)
        self.butp1.setObjectName("butp1")
        self.butt1 = QtWidgets.QPushButton(self.les1)
        self.butt1.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.butt1.setFont(font)
        self.butt1.setStyleSheet("QPushButton {\n"
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
        self.butt1.setObjectName("butt1")
        self.progress1 = QtWidgets.QProgressBar(self.les1)
        self.progress1.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progress1.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius:15px;\n"
"    color: white;\n"
"    background-color: rgb(50, 50, 50);\n"
"    font: 12pt \"MS Sans Serif\";\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius:13px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(64, 83, 255), stop:1 rgb(0, 255, 255));\n"
"}")
        self.progress1.setProperty("value", 24)
        self.progress1.setObjectName("progress1")
        self.label_5 = QtWidgets.QLabel(self.les1)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 411, 61))
        self.label_5.setStyleSheet("QLabel{\n"
"font: 75 italic 26pt \"MS Sans Serif\";\n"
"color: white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.lesk = QtWidgets.QGroupBox(self.mainbox)
        self.lesk.setGeometry(QtCore.QRect(20, 320, 1071, 81))
        self.lesk.setStyleSheet("QGroupBox{\n"
"background-color: black;\n"
"color: #333;\n"
"border: 2px solid white;\n"
"border-radius: 1px;\n"
"font: 75 italic 22pt \"MS Sans Serif\";\n"
"color: white;\n"
"}")
        self.lesk.setTitle("")
        self.lesk.setObjectName("lesk")
        self.buttk = QtWidgets.QPushButton(self.lesk)
        self.buttk.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.buttk.setFont(font)
        self.buttk.setStyleSheet("QPushButton {\n"
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
        self.buttk.setObjectName("buttk")
        self.progress = QtWidgets.QProgressBar(self.lesk)
        self.progress.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progress.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius:15px;\n"
"    color: white;\n"
"    background-color: rgb(50, 50, 50);\n"
"    font: 12pt \"MS Sans Serif\";\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius:13px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(0, 255, 0), stop:1 rgb(255, 255, 127));\n"
"}")
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.label_2 = QtWidgets.QLabel(self.lesk)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 411, 61))
        self.label_2.setStyleSheet("QLabel{\n"
"font: 75 italic 26pt \"MS Sans Serif\";\n"
"color: white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.butpk = QtWidgets.QPushButton(self.lesk)
        self.butpk.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.butpk.setMouseTracking(False)
        self.butpk.setStyleSheet("QPushButton {\n"
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
        self.butpk.setText("")
        self.butpk.setIcon(icon1)
        self.butpk.setDefault(False)
        self.butpk.setObjectName("butpk")
        self.les2 = QtWidgets.QGroupBox(self.mainbox)
        self.les2.setGeometry(QtCore.QRect(20, 120, 1071, 81))
        self.les2.setStyleSheet("QGroupBox{\n"
"background-color: black;\n"
"color: #333;\n"
" border: 2px solid white;\n"
"  border-radius: 1px;\n"
"}")
        self.les2.setTitle("")
        self.les2.setObjectName("les2")
        self.butt2 = QtWidgets.QPushButton(self.les2)
        self.butt2.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.butt2.setFont(font)
        self.butt2.setStyleSheet("QPushButton {\n"
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
        self.butt2.setObjectName("butt2")
        self.progress2 = QtWidgets.QProgressBar(self.les2)
        self.progress2.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progress2.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius:15px;\n"
"    color: white;\n"
"    background-color: rgb(50, 50, 50);\n"
"    font: 12pt \"MS Sans Serif\";\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius:13px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(64, 83, 255), stop:1 rgb(0, 255, 255));\n"
"}")
        self.progress2.setProperty("value", 24)
        self.progress2.setObjectName("progress2")
        self.label_4 = QtWidgets.QLabel(self.les2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 521, 61))
        self.label_4.setStyleSheet("QLabel{\n"
"font: 75 italic 19pt \"MS Sans Serif\";\n"
"color: white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.butp2 = QtWidgets.QPushButton(self.les2)
        self.butp2.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.butp2.setMouseTracking(False)
        self.butp2.setStyleSheet("QPushButton {\n"
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
        self.butp2.setText("")
        self.butp2.setIcon(icon1)
        self.butp2.setDefault(False)
        self.butp2.setObjectName("butp2")
        self.les3 = QtWidgets.QGroupBox(self.mainbox)
        self.les3.setGeometry(QtCore.QRect(20, 220, 1071, 81))
        self.les3.setStyleSheet("QGroupBox{\n"
"background-color: black;\n"
"color: #333;\n"
" border: 2px solid white;\n"
"  border-radius: 1px;\n"
"}")
        self.les3.setTitle("")
        self.les3.setObjectName("les3")
        self.butt4 = QtWidgets.QPushButton(self.les3)
        self.butt4.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.butt4.setFont(font)
        self.butt4.setStyleSheet("QPushButton {\n"
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
        self.butt4.setObjectName("butt4")
        self.progress3 = QtWidgets.QProgressBar(self.les3)
        self.progress3.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progress3.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius:15px;\n"
"    color: white;\n"
"    background-color: rgb(50, 50, 50);\n"
"    font: 12pt \"MS Sans Serif\";\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius:13px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(64, 83, 255), stop:1 rgb(0, 255, 255));\n"
"}")
        self.progress3.setProperty("value", 24)
        self.progress3.setObjectName("progress3")
        self.label_3 = QtWidgets.QLabel(self.les3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 441, 61))
        self.label_3.setStyleSheet("QLabel{\n"
"font: 75 italic 26pt \"MS Sans Serif\";\n"
"color: white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.butp3 = QtWidgets.QPushButton(self.les3)
        self.butp3.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.butp3.setMouseTracking(False)
        self.butp3.setStyleSheet("QPushButton {\n"
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
        self.butp3.setText("")
        self.butp3.setIcon(icon1)
        self.butp3.setDefault(False)
        self.butp3.setObjectName("butp3")
        self.mainbox.raise_()
        self.box1.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "Построение сечений"))
        self.namelabel.setText(_translate("mainWindow", "1"))
        self.butt1.setText(_translate("mainWindow", "?"))
        self.label_5.setText(_translate("mainWindow", "Метод следов"))
        self.buttk.setText(_translate("mainWindow", "?"))
        self.label_2.setText(_translate("mainWindow", "Контрольное задание"))
        self.butt2.setText(_translate("mainWindow", "?"))
        self.label_4.setText(_translate("mainWindow", "Метод внутреннего проектирования"))
        self.butt4.setText(_translate("mainWindow", "?"))
        self.label_3.setText(_translate("mainWindow", "Комбинированный метод"))