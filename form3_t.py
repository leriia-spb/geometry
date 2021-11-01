# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form3_t.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teor3(object):
    def setupUi(self, teor3):
        teor3.setObjectName("teor3")
        teor3.resize(936, 473)
        teor3.setDocumentMode(False)
        teor3.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(teor3)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(880, 0, 51, 41))
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
        self.label.setGeometry(QtCore.QRect(10, 0, 861, 41))
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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 921, 381))
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 901, 361))
        self.stackedWidget.setStyleSheet("color:white;\n"
"background:black;\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 901, 341))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.go1 = QtWidgets.QPushButton(self.page)
        self.go1.setGeometry(QtCore.QRect(690, 330, 91, 31))
        self.go1.setStyleSheet("QPushButton {\n"
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
        self.go1.setObjectName("go1")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.label_2.setStyleSheet("\n"
"font: 18pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, -10, 741, 51))
        self.textBrowser_2.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(500, 140, 371, 91))
        self.textBrowser_3.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 371, 251))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix3/Паралл.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.go2 = QtWidgets.QPushButton(self.page_2)
        self.go2.setGeometry(QtCore.QRect(690, 330, 91, 31))
        self.go2.setStyleSheet("QPushButton {\n"
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
        self.go2.setObjectName("go2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.label_5.setStyleSheet("\n"
"font: 18pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(0, 40, 451, 311))
        self.label_7.setStyleSheet("background-image: url(:/newPrefix3/параллA.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(140, 0, 741, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(460, 30, 451, 321))
        self.textBrowser_4.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.go3 = QtWidgets.QPushButton(self.page_3)
        self.go3.setGeometry(QtCore.QRect(690, 330, 91, 31))
        self.go3.setStyleSheet("QPushButton {\n"
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
        self.go3.setObjectName("go3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.label_6.setStyleSheet("\n"
"font: 18pt \"MS Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(40, 70, 371, 241))
        self.label_9.setStyleSheet("background-image: url(:/newPrefix3/параллБ.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(150, 0, 721, 51))
        self.textBrowser_5.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(480, 60, 381, 261))
        self.textBrowser_6.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.stackedWidget.addWidget(self.page_4)
        self.tomainbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.tomainbutton.setGeometry(QtCore.QRect(810, 340, 91, 31))
        self.tomainbutton.setStyleSheet("QPushButton {\n"
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
        self.tomainbutton.setObjectName("tomainbutton")
        self.groupBox_2.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        teor3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(teor3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName("menubar")
        teor3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(teor3)
        self.statusbar.setObjectName("statusbar")
        teor3.setStatusBar(self.statusbar)

        self.retranslateUi(teor3)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(teor3)

    def retranslateUi(self, teor3):
        _translate = QtCore.QCoreApplication.translate
        teor3.setWindowTitle(_translate("teor3", "MainWindow"))
        self.label.setText(_translate("teor3", "Применение комбинированный метода.Теория."))
        self.label_13.setText(_translate("teor3", "TextLabel"))
        self.label_14.setText(_translate("teor3", "TextLabel"))
        self.textBrowser.setHtml(_translate("teor3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic; color:#ffffff;\">Суть метода</span><span style=\" font-size:11pt; color:#ffffff;\"> состоит в применении теорем о параллельности прямых и плоскостей в пространстве в сочетании с аксиоматическим методом(методами следов и вспомогательных плоскостей). Применяется для построения сечения многогранника с условием параллельности.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">Построение сечения многогранника плоскостью α, проходящей через заданную прямую p параллельно другой заданной прямой q:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">1. Через вторую прямую q и какую-нибудь точку W первой прямой р провести плоскость β. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">2. В плоскости β через точку W провести прямую q‘ параллельную q.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">3. Пересекающимися прямыми p и q‘ определяется плоскость α. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">4. Непосредственное построение сечения многогранника плоскостью α.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Merriweather,Georgia,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\">Координатный метод построения сечений.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Merriweather,Georgia,sans-serif\'; font-size:11pt; font-weight:400; color:#ffffff;\">Суть координатного метода заключается в вычислении координат точек пересечения ребер или многогранника с секущей плоскостью, которая задается уравнением плоскости. Уравнение плоскости сечения вычисляется на основе условий задачи.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Merriweather,Georgia,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\">Заметим</span><span style=\" font-family:\'Merriweather,Georgia,sans-serif\'; font-size:11pt; font-weight:400; color:#ffffff;\">, что это способ построения сечения многогранника приемлем для компьютера, так как он связан с большим объемом вычислений и поэтому этот метод целесообразно реализовать с помощью ЭВМ.</span></p></body></html>"))
        self.go1.setText(_translate("teor3", "Далее"))
        self.label_2.setText(_translate("teor3", "Пример "))
        self.textBrowser_2.setHtml(_translate("teor3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; font-style:italic; color:#ffffff;\">Задача: </span><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">построить сечение параллелепипеда АВСDА1В1С1D1 плоскостью α, заданной точками Р, Q и R, если точка Р лежит на диагонали А1C1, точка Q - на ребре ВВ1 и точка R - на ребре DD1</span><span style=\" font-size:11pt; color:#ffffff;\"> </span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("teor3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">Решение:</span><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-style:italic; color:#ffffff;\">Вариантов решения этой задачи существует 2. Поэтому сейчас будут разобраны оба этих варианта.</span></p></body></html>"))
        self.go2.setText(_translate("teor3", "Далее"))
        self.label_5.setText(_translate("teor3", "Решение а"))
        self.label_12.setText(_translate("teor3", "Решим эту задачу с применением метода следов и теорем о параллельности прямых и плоскостей."))
        self.textBrowser_4.setHtml(_translate("teor3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">Решение:</span><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">Построим след секущей плоскости α = (РQR) на плоскости АВС Для этого строим точки Т1 = РQ ∩ Р1В, где PP1║AA1, P1 є AC, и T2 = RQ ∩ ВD. Построив след Т1Т2, замечаем, что точка Р лежит в плоскости А1B1C1, которая параллельна плоскости АВС. Это означает, что плоскость α пересекает плоскость А1B1C1 по прямой, проходящей через точку Р и параллельной прямой Т1Т2. Проведем эту прямую и обозначим через М и Е точки ее пересечения с ребрами соответственно А1B1 и А1D1. Получаем: М = α ∩ А1B1, Е =α∩ А1D1. Тогда отрезки ЕR и QМ являются сторонами искомого сечения.</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">Далее, так как плоскость ВСС1 параллельна плоскости грани ADD1A1, то плоскость α пересекает грань ВСC1B1 по от резку QF (F= α ∩ СС1), параллельному прямой ЕR. Таким образом, пятиугольник ERFQM - искомое сечение. Точку F можно получить, проведя RF║ MQ.</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p></body></html>"))
        self.go3.setText(_translate("teor3", "Далее"))
        self.label_6.setText(_translate("teor3", "Решение б"))
        self.textBrowser_5.setHtml(_translate("teor3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">Решим эту задачу, применяя метод внутреннего проектирования и теоремы о параллельности прямых и плоскостей.</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("teor3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Решение:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; color:#ffffff;\">Пусть Н=АС ∩ ВD (рис. 12). Проведя прямую НН1 параллельно ребру ВВ1 (Н1 є RQ), построим точку F: F=РН1 ∩ CC1.Tочка F является точкой пересечения плоскости α с ребром СС1, так как РН1 є α. Тогда отрезки RF и QF, по которым плоскость α пересекает соответственно грани CС1D1D и ВСС1В1 данного параллелепипеда, являются сторонами его искомого сечения.</span><span style=\" font-size:10pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; color:#ffffff;\">Так как плоскость АВВ1 параллельна плоскости CDD1, то пересечением плоскости α и грани АВВ1А1 является отрезок QМ (М є А1В1), параллельный отрезку FR; отрезок QМ - сторона сечения. Далее, точка Е = МР ∩ А1D1 является точкой пересечения плоскости α и ребра А1D1, так как МР є α. Поэтому точка Е - еще одна вершина искомого сечения. Таким образом, пятиугольник ERFQM - искомое сечение. Точку Е можно построить, проведя прямую RЕ ║ FQ. Тогда М = РЕ ∩ А1B1.</span><span style=\" font-size:10pt; color:#ffffff;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.tomainbutton.setText(_translate("teor3", "Главное меню"))
import photos
