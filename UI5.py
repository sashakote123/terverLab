import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from main import *
from scipy.stats import rayleigh
from scipy.stats import ks_2samp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/task.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 201, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 230, 331, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(230, 150, 811, 71))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(350, 250, 691, 131))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 390, 161, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("src/max.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 400, 271, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 10, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(590, 10, 171, 31))
        self.checkBox.setObjectName("checkBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(590, 40, 171, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(770, 10, 271, 131))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_11)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 530, 201, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 480, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(350, 500, 691, 101))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(360, 480, 291, 16))
        self.label_14.setObjectName("label_14")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(350, 670, 271, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 560, 241, 71))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_19.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_20)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_24)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(10, 640, 171, 71))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("src/R0.PNG"))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(190, 640, 141, 71))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("src/qj.PNG"))
        self.label_22.setObjectName("label_22")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(710, 630, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(830, 630, 211, 41))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_26.setObjectName("label_26")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_27.setObjectName("label_27")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_28.setObjectName("label_28")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_29.setObjectName("label_29")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_29)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 660, 111, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(710, 610, 91, 16))
        self.label_25.setObjectName("label_25")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(380, 440, 171, 31))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("src/D.PNG"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(560, 440, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Плотность"))
        self.label_4.setText(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Параметр σ</p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "100"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Eη"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "x`"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "|x`-Eη|"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dη"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S^2"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "|Dη-S^2|"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Me"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "R"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "zj"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "fη(zj)"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "nj/|Δ`j|"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.checkBox.setText(_translate("MainWindow", "Строить гистограмму"))
        self.label_5.setText(_translate("MainWindow", "Min:"))
        self.label_7.setText(_translate("MainWindow", "Max:"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "На равные участки:"))
        self.lineEdit_3.setText(_translate("MainWindow", "5"))
        self.pushButton_3.setText(_translate("MainWindow", "Разбить"))
        self.label_11.setText(_translate("MainWindow", "Ввести границы вручную:"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.5"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить "))
        self.pushButton_5.setText(_translate("MainWindow", "Ok"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить лист"))
        self.label_12.setText(_translate("MainWindow", "Уровень значимости"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.05"))
        self.label_13.setText(_translate("MainWindow", "Проверка гипотезы"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "zj"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "qj"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        self.label_14.setText(_translate("MainWindow", "Границы интервалов и теоретические вероятности q"))
        self.label_16.setText(_translate("MainWindow", "Решение:"))
        self.label_15.setText(_translate("MainWindow", "-"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Критическое значение:</p></body></html>"))
        self.label_18.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:10pt;\">0</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:10pt;\">R</span><span style=\" font-size:10pt; vertical-align:sub;\">0</span><span style=\" font-size:10pt;\">=</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:10pt;\">0</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "Степени свободы"))
        self.label_24.setText(_translate("MainWindow", "0"))
        self.lineEdit_6.setText(_translate("MainWindow", "100"))
        self.label_26.setText(_translate("MainWindow", "Гипотеза принята:"))
        self.label_27.setText(_translate("MainWindow", "Гипотеза отвергнута:"))
        self.label_28.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "0"))
        self.pushButton_6.setText(_translate("MainWindow", "Ок"))
        self.label_25.setText(_translate("MainWindow", "Число опытов:"))
        self.label_31.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt;\">0</span></p></body></html>"))

        self.lineEdit_6.setText('100')

        self.pushButton.clicked.connect(lambda: self.setInfo())

        self.pushButton_3.clicked.connect(lambda: self.setA())
        self.pushButton_4.clicked.connect(lambda: self.popList())
        self.pushButton_5.clicked.connect(lambda: self.setA2())
        self.pushButton_2.clicked.connect(lambda: self.clearList())
        self.pushButton_6.clicked.connect(lambda: self.ProverkaGipotezy())

        self.a = 0
        self.deltaList2 = [0, 0.5]

    def clearList(self):
        self.deltaList2.clear()
        self.deltaList2.append(0)

    def setA(self):
        self.a = 1
        print(self.a)

    def setA2(self):
        self.a = 2
        print(self.a)

    def popList(self):
        data = self.deltaList2[-1]
        self.deltaList2.append(data + float(self.lineEdit_4.text()))
        print(self.deltaList2)

    def setInfo(self):
        list_r, list_g, list_x2, list_f = getData(int(self.lineEdit.text()), float(self.lineEdit_2.text()))
        Mat_Oj, Sredn, dif1, Dispersion, Vib_Dispersion, dif2, Mediana, Razmax = getCharacteristics(list_g, float(
            self.lineEdit_2.text()))
        sample = np.random.rayleigh(scale=float(self.lineEdit_2.text()), size=int(self.lineEdit.text()))
        sorted_sample = np.sort(sample)
        n = len(sorted_sample)
        cdf = np.arange(1, n + 1) / n
        x = np.linspace(0, list_g[-1], int(self.lineEdit.text()))
        theoretical_cdf = rayleigh.cdf(x, scale=float(self.lineEdit_2.text()))

        x = np.linspace(0, list_g[-1], 500)
        y = []
        y2 = []
        d_list = []
        for i in range(500):
            # y.append(math.sqrt(-2 * float(self.lineEdit_2.text()) ** 2 * math.log(1 - x[i], math.e)))
            y.append(1 - math.exp(-x[i] ** 2 / (2 * float(self.lineEdit_2.text()) ** 2)))

        x2 = np.linspace(list_g[0], list_g[-1], int(self.lineEdit.text()))
        count = getCount(x2, list_g, int(self.lineEdit.text()))
        for i in range(len(count)):
            count[i] /= int(self.lineEdit.text())
            y2.append(1 - math.exp(-x2[i] ** 2 / (2 * float(self.lineEdit_2.text()) ** 2)))

        sum = 0
        F_list = []
        for i in range(len(count)):
            sum += count[i]
            F_list.append(sum)
        print('Flist', F_list)
        print('Y', y2)

        for i in range(len(count)):
            d_list.append(abs(y2[i]-F_list[i]))

        print('count', count)
        print()

        # print('dlist:', d_list)
        print(np.max(d_list))
        self.label_31.setText(str(np.max(d_list)))

        if self.a == 1 and self.checkBox.isChecked():
            deltaList1 = np.linspace(list_g[0], list_g[-1], int(self.lineEdit_3.text()) + 2)
            vList, flist, z_list = getHistList(deltaList1, list_g, float(self.lineEdit_2.text()),
                                               int(self.lineEdit_3.text()), int(self.lineEdit.text()))

            rList = []
            for i in range(len(flist)):
                rList.append(abs(flist[i] - vList[i]))
            self.label_6.setText(str(np.max(rList)))
            self.tableWidget_3.setColumnCount(int(self.lineEdit_3.text()))
            for i in range(int(self.lineEdit_3.text())):
                self.tableWidget_3.setItem(0, i, QTableWidgetItem(str(z_list[i])))
                self.tableWidget_3.setItem(1, i, QTableWidgetItem(str(flist[i])))
                self.tableWidget_3.setItem(2, i, QTableWidgetItem(str(vList[i])))

            plt.subplot(1, 2, 1)
            plt.title('Функция распределения')
            plt.plot(x, y, '-g')
            plt.plot([list_g[0], list_g[0]], [0, cdf[0]], 'r')
            for i in range(n - 1):
                plt.plot([list_g[i], list_g[i + 1]], [cdf[i], cdf[i]], 'r')
                plt.plot([list_g[i + 1], list_g[i + 1]], [cdf[i], cdf[i + 1]], 'r')

            plt.subplot(1, 2, 2)
            plt.title('Плотность распределения')
            plt.plot(list_x2, list_f, '-r')
            for i in range(int(self.lineEdit_3.text())):
                plt.plot([deltaList1[i], deltaList1[i + 1], deltaList1[i + 1], deltaList1[i], deltaList1[i]],
                         [vList[i], vList[i], 0, 0, vList[i]], 'b')
                plt.plot([deltaList1[i], deltaList1[i + 1]], [vList[i], vList[i]], 'b')
            plt.show()

        if self.a == 2 and self.checkBox.isChecked():
            vList, flist, z_list = getHistList(self.deltaList2, list_g, float(self.lineEdit_2.text()),
                                               int(len(self.deltaList2) - 1), int(self.lineEdit.text()))

            rList = []
            for i in range(len(flist)):
                rList.append(abs(flist[i] - vList[i]))
            self.label_6.setText(str(np.max(rList)))

            self.tableWidget_3.setColumnCount(int(len(self.deltaList2) - 1))
            for i in range(int(len(self.deltaList2) - 1)):
                self.tableWidget_3.setItem(0, i, QTableWidgetItem(str(z_list[i])))
                self.tableWidget_3.setItem(1, i, QTableWidgetItem(str(flist[i])))
                self.tableWidget_3.setItem(2, i, QTableWidgetItem(str(vList[i])))

            plt.subplot(1, 2, 1)
            plt.title('Функция распределения')
            plt.plot(x, y, '-g')
            plt.plot([list_g[0], list_g[0]], [0, cdf[0]], 'r')
            for i in range(n - 1):
                plt.plot([list_g[i], list_g[i + 1]], [cdf[i], cdf[i]], 'r')
                plt.plot([list_g[i + 1], list_g[i + 1]], [cdf[i], cdf[i + 1]], 'r')

            for i in range(len(list_g) - 1):
                plt.plot([list_g[i], list_g[i + 1]], [list_r[i], list_r[i]], 'r')
                plt.plot([list_g[i + 1], list_g[i + 1]], [list_r[i], list_r[i + 1]], 'r')
            plt.subplot(1, 2, 2)
            plt.title('Плотность распределения')
            plt.plot(list_x2, list_f, '-r')
            for i in range(int(len(self.deltaList2)) - 1):
                plt.plot([self.deltaList2[i], self.deltaList2[i + 1], self.deltaList2[i + 1], self.deltaList2[i],
                          self.deltaList2[i]],
                         [vList[i], vList[i], 0, 0, vList[i]], 'b')
                plt.plot([self.deltaList2[i], self.deltaList2[i + 1]], [vList[i], vList[i]], 'b')
            plt.show()
        else:

            plt.subplot(1, 2, 1)
            plt.title('Функция распределения')
            plt.plot(x, y, '-g')
            plt.plot([list_g[0], list_g[0]], [0, cdf[0]], 'r')
            for i in range(n - 1):
                plt.plot([list_g[i], list_g[i + 1]], [cdf[i], cdf[i]], 'r')
                plt.plot([list_g[i + 1], list_g[i + 1]], [cdf[i], cdf[i + 1]], 'r')
            plt.subplot(1, 2, 2)
            plt.title('Плотность распределения')
            plt.plot(list_x2, list_f, 'black')
            plt.show()

        self.label_8.setText(str(list_g[0]))
        self.label_9.setText(str(list_g[-1]))

        self.tableWidget.setRowCount(int(self.lineEdit.text()))
        self.tableWidget_2.setRowCount(1)

        for i in range(int(self.lineEdit.text())):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(list_r[i])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(list_g[i])))

        self.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(Mat_Oj)))
        self.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(Sredn)))
        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(dif1)))
        self.tableWidget_2.setItem(0, 3, QTableWidgetItem(str(Dispersion)))
        self.tableWidget_2.setItem(0, 4, QTableWidgetItem(str(Vib_Dispersion)))
        self.tableWidget_2.setItem(0, 5, QTableWidgetItem(str(dif2)))
        self.tableWidget_2.setItem(0, 6, QTableWidgetItem(str(Mediana)))
        self.tableWidget_2.setItem(0, 7, QTableWidgetItem(str(Razmax)))

        delta2List2 = [-math.inf]
        for i in range(len(self.deltaList2)):
            delta2List2.append(self.deltaList2[i])
        delta2List2.append(math.inf)

        deltaList12 = np.linspace(list_g[0], list_g[-1], int(self.lineEdit_3.text()))

        deltaList1 = np.linspace(list_g[0], list_g[-1], int(self.lineEdit_3.text()))
        countList = getCount(deltaList1, list_g, len(deltaList1))
        qlist1 = getqList(deltaList1, float(self.lineEdit_2.text()), len(deltaList1))

        self.tableWidget_5.setColumnCount(len(qlist1))
        for i in range(len(qlist1)):
            self.tableWidget_5.setItem(1, i, QTableWidgetItem(str(qlist1[i])))
        # for i in range(len(deltaList1)):
        #    self.tableWidget_5.setItem(0, i, QTableWidgetItem(str(deltaList1[i])))

        sum2, critical2 = Gipoteza(countList, qlist1, int(self.lineEdit.text()), len(deltaList1), float(
            self.lineEdit_5.text()))

        print(sum2, critical2)
        self.label_20.setText(str(sum2))
        self.label_18.setText(str(critical2))

        if (sum2 > critical2):
            self.label_15.setText("Гипотеза отвергнута")
        else:
            self.label_15.setText("Гипотеза принята")

    def ProverkaGipotezy(self):
        count1 = 0
        count2 = 0
        for i in range(int(self.lineEdit_6.text())):

            list_g = getData(int(self.lineEdit.text()), float(self.lineEdit_2.text()))[1]
            deltaList1 = np.linspace(list_g[0], list_g[-1], int(self.lineEdit_3.text()) + 2)
            q_list = getqList(deltaList1, float(self.lineEdit_2.text()), len(deltaList1))
            countList = getCount(deltaList1, list_g, len(deltaList1))
            sum, critical = Gipoteza(countList, q_list, int(self.lineEdit.text()), len(deltaList1),
                                     float(self.lineEdit_5.text()))
            if sum > critical:
                count1 += 1
            else:
                count2 += 1
        self.label_29.setText(str(count2))
        self.label_28.setText(str(count1))

    def returnArray1(self, min, max, N):
        return np.linspace(min, max, N)

    def returnArray2(self, list, data):
        list.append(data)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
