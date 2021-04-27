# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impact_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgImpact(object):
    def setupUi(self, dlgImpact):
        dlgImpact.setObjectName("dlgImpact")
        dlgImpact.resize(400, 300)
        self.tblImpact = QtWidgets.QTableWidget(dlgImpact)
        self.tblImpact.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.tblImpact.setAlternatingRowColors(True)
        self.tblImpact.setObjectName("tblImpact")
        self.tblImpact.setColumnCount(3)
        self.tblImpact.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpact.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpact.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpact.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgImpact)
        QtCore.QMetaObject.connectSlotsByName(dlgImpact)

    def retranslateUi(self, dlgImpact):
        _translate = QtCore.QCoreApplication.translate
        dlgImpact.setWindowTitle(_translate("dlgImpact", "Impact Report"))
        item = self.tblImpact.horizontalHeaderItem(0)
        item.setText(_translate("dlgImpact", "Project"))
        item = self.tblImpact.horizontalHeaderItem(1)
        item.setText(_translate("dlgImpact", "Type"))
        item = self.tblImpact.horizontalHeaderItem(2)
        item.setText(_translate("dlgImpact", "Distance"))

