# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace-py\TradeAuto\TradeRecord.ui'
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

    def initRecordTableHead(self, tableView, model):
        #the situation of Buy
        model.setHorizontalHeaderLabels([u'交易股票代号', u'交易方式', u'交易数量', u'交易金额', u'交易盈亏', u'交易时间'])
        tableView.setModel(model)
        tableView.horizontalHeader().setStretchLastSection(True)
        
    def tradeRecordTable(self, tableView,number=1):
        model_record=QStandardItemModel(number,6)
        self.initRecordTableHead(tableView, model_record)

        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(509, 434)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 131, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 60, 481, 351))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 30, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tradeRecordTable(self.tableView)
        
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "交易记录", None))
        self.label.setText(_translate("Dialog", "账户名称：", None))
        self.label_2.setText(_translate("Dialog", "账户代号：", None))
        self.pushButton.setText(_translate("Dialog", "查找", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

