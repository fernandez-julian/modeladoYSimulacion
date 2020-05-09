from PyQt5 import QtCore, QtGui, QtWidgets
from pvi import *


class Ui_MainWindow(object):
    def __init__(self):
        self.funcion = None
        self.xi = None
        self.ti = None
        self.tf = None
        self.h = None
        self.metodo = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 647)
        MainWindow.setWindowTitle("Modelado y Simulacion")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_metodos = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_metodos.setGeometry(QtCore.QRect(80, 190, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_metodos.setFont(font)
        self.comboBox_metodos.setObjectName("comboBox_metodos")
        self.comboBox_metodos.addItem("")
        self.comboBox_metodos.addItem("")
        self.comboBox_metodos.addItem("")
        self.label_seleccionMetodo = QtWidgets.QLabel(self.centralwidget)
        self.label_seleccionMetodo.setGeometry(QtCore.QRect(80, 140, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_seleccionMetodo.setFont(font)
        self.label_seleccionMetodo.setObjectName("label_seleccionMetodo")
        self.lineEdit_dxdt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dxdt.setGeometry(QtCore.QRect(160, 70, 221, 31))
        self.lineEdit_dxdt.setText("")
        self.lineEdit_dxdt.setObjectName("lineEdit_dxdt")
        self.label_pvi = QtWidgets.QLabel(self.centralwidget)
        self.label_pvi.setGeometry(QtCore.QRect(80, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_pvi.setFont(font)
        self.label_pvi.setObjectName("label_pvi")
        self.label_dxdt = QtWidgets.QLabel(self.centralwidget)
        self.label_dxdt.setGeometry(QtCore.QRect(80, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_dxdt.setFont(font)
        self.label_dxdt.setObjectName("label_dxdt")
        self.label_parametros = QtWidgets.QLabel(self.centralwidget)
        self.label_parametros.setGeometry(QtCore.QRect(80, 260, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_parametros.setFont(font)
        self.label_parametros.setObjectName("label_parametros")
        self.label_ti = QtWidgets.QLabel(self.centralwidget)
        self.label_ti.setGeometry(QtCore.QRect(80, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_ti.setFont(font)
        self.label_ti.setObjectName("label_ti")
        self.label_tf = QtWidgets.QLabel(self.centralwidget)
        self.label_tf.setGeometry(QtCore.QRect(80, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_tf.setFont(font)
        self.label_tf.setObjectName("label_tf")
        self.label_xi = QtWidgets.QLabel(self.centralwidget)
        self.label_xi.setGeometry(QtCore.QRect(80, 410, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_xi.setFont(font)
        self.label_xi.setObjectName("label_xi")
        self.label_h = QtWidgets.QLabel(self.centralwidget)
        self.label_h.setGeometry(QtCore.QRect(80, 470, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_h.setFont(font)
        self.label_h.setObjectName("label_h")
        self.lineEdit_ti = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ti.setGeometry(QtCore.QRect(170, 310, 91, 31))
        self.lineEdit_ti.setText("")
        self.lineEdit_ti.setObjectName("lineEdit_ti")
        self.lineEdit_tf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tf.setGeometry(QtCore.QRect(170, 360, 91, 31))
        self.lineEdit_tf.setText("")
        self.lineEdit_tf.setObjectName("lineEdit_tf")
        self.lineEdit_xi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xi.setGeometry(QtCore.QRect(170, 410, 91, 31))
        self.lineEdit_xi.setText("")
        self.lineEdit_xi.setObjectName("lineEdit_xi")
        self.lineEdit_h = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_h.setGeometry(QtCore.QRect(220, 470, 91, 31))
        self.lineEdit_h.setText("")
        self.lineEdit_h.setObjectName("lineEdit_h")
        self.pushButton_graficar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_graficar.setGeometry(QtCore.QRect(170, 550, 171, 41))
        self.pushButton_graficar.clicked.connect(self.clickMetodo)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_graficar.setFont(font)
        self.pushButton_graficar.setObjectName("pushButton_graficar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clickMetodo(self):
        self.funcion = self.lineEdit_dxdt.text()
        self.xi = self.lineEdit_xi
        self.ti = self.lineEdit_ti
        self.tf = self.lineEdit_tf
        self.h = self.lineEdit_h
        if (self.comboBox_metodos.currentIndex() == 0):
            euler() #falta
        if (self.comboBox_metodos.currentIndex() == 1):
            euler_mejorado() #falta
        if (self.comboBox_metodos.currentIndex() == 2):
            rungeKutta() #falta

    def getFuncion(self):
        return self.funcion

    def getXi(self):
        return self.xi

    def getTi(self):
        return self.ti

    def getTf(self):
        return self.tf

    def getH(self):
        return self.h

    def getMetodo(self):
        return self.metodo

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.comboBox_metodos.setItemText(0, _translate("MainWindow", "Euler"))
        self.comboBox_metodos.setItemText(1, _translate("MainWindow", "Euler mejorado"))
        self.comboBox_metodos.setItemText(2, _translate("MainWindow", "Runge-Kutta"))
        self.label_seleccionMetodo.setText(_translate("MainWindow", "Seleccionar metodo numerico"))
        self.label_pvi.setText(_translate("MainWindow", "Problemas de valor inicial"))
        self.label_dxdt.setText(_translate("MainWindow", "dx/dt ="))
        self.label_parametros.setText(_translate("MainWindow", "Parametros"))
        self.label_ti.setText(_translate("MainWindow", "t inicial ="))
        self.label_tf.setText(_translate("MainWindow", "t final ="))
        self.label_xi.setText(_translate("MainWindow", "x inicial ="))
        self.label_h.setText(_translate("MainWindow", "h (incremento) ="))
        self.pushButton_graficar.setText(_translate("MainWindow", "Graficar"))

