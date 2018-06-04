# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace-py\TradeAuto\AllAccountInfo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def initAccountRecordTableHead(self, tableView, model):
        #the situation of Buy
        model.setHorizontalHeaderLabels([u'账户名称', u'账户号码'])
        tableView.setModel(model)
        tableView.horizontalHeader().setStretchLastSection(True)
        
    def AccountRecordTable(self, tableView,number=1):
        model_record=QStandardItemModel(number,2)
        self.initAccountRecordTableHead(tableView, model_record)
    
    
    def initAccountStockTableHead(self, tableView, model):
        #the situation of Buy
        model.setHorizontalHeaderLabels([u'股票名称', u'股票号码'])
        tableView.setModel(model)
        tableView.horizontalHeader().setStretchLastSection(True)
        
    def AccountStockRecordTable(self, tableView,number=1):
        model_record=QStandardItemModel(number,2)
        self.initAccountStockTableHead(tableView, model_record)
    
    
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(606, 546)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 120, 251, 411))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 120, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 120, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 170, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 170, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(290, 220, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 220, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 140, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 140, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 190, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 190, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 240, 113, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(440, 240, 113, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.tableView_2 = QtGui.QTableView(Dialog)
        self.tableView_2.setGeometry(QtCore.QRect(290, 310, 301, 221))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(290, 280, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.AccountRecordTable(self.tableView)
        self.AccountStockRecordTable(self.tableView_2)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "账户信息", None))
        self.label.setText(_translate("Dialog", "当前用户", None))
        self.label_2.setText(_translate("Dialog", "关联账户:", None))
        self.label_3.setText(_translate("Dialog", "持仓单价", None))
        self.label_4.setText(_translate("Dialog", "持仓总价", None))
        self.label_5.setText(_translate("Dialog", "持仓数量", None))
        self.label_6.setText(_translate("Dialog", "当前权益", None))
        self.label_7.setText(_translate("Dialog", "盈利状况", None))
        self.label_8.setText(_translate("Dialog", "当前价格", None))
        self.label_9.setText(_translate("Dialog", "持仓股票", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

