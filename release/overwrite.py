# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overwrite.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(269, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.le_id = QtWidgets.QLineEdit(self.centralwidget)
        self.le_id.setGeometry(QtCore.QRect(120, 20, 141, 20))
        self.le_id.setObjectName("le_id")
        self.le_names = QtWidgets.QLineEdit(self.centralwidget)
        self.le_names.setGeometry(QtCore.QRect(120, 50, 141, 21))
        self.le_names.setObjectName("le_names")
        self.le_step = QtWidgets.QLineEdit(self.centralwidget)
        self.le_step.setGeometry(QtCore.QRect(120, 80, 141, 20))
        self.le_step.setObjectName("le_step")
        self.le_do = QtWidgets.QLineEdit(self.centralwidget)
        self.le_do.setGeometry(QtCore.QRect(120, 110, 141, 20))
        self.le_do.setObjectName("le_do")
        self.le_des = QtWidgets.QLineEdit(self.centralwidget)
        self.le_des.setGeometry(QtCore.QRect(120, 140, 141, 20))
        self.le_des.setObjectName("le_des")
        self.le_pri = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pri.setGeometry(QtCore.QRect(120, 170, 141, 20))
        self.le_pri.setObjectName("le_pri")
        self.le_vol = QtWidgets.QLineEdit(self.centralwidget)
        self.le_vol.setGeometry(QtCore.QRect(120, 200, 141, 20))
        self.le_vol.setObjectName("le_vol")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.label_7.setObjectName("label_7")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.save.setObjectName("save")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(120, 230, 75, 23))
        self.cancel.setObjectName("cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Название Сорта"))
        self.label_3.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "Молотый/В зёрнах"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.label_7.setText(_translate("MainWindow", "Объём упаковки"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
