# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace-py\TradeAuto\InnerDayQuickTrade.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import Ui_InstantTrade
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
    
class MyTableView(QTableView):
    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)

    def mouseDoubleClickEvent(self, event):
        QTableView.mouseDoubleClickEvent(self, event)
        pos = event.pos()
        item = self.indexAt(pos)
#        if item:
#            print "item clicked at ", item.row(), " ", item.column()
        Form_instantTrade = QtGui.QDialog()  
        instantTrade = Ui_InstantTrade.Ui_Dialog()
        instantTrade.setupUi(Form_instantTrade)  
        Form_instantTrade.show()  
        Form_instantTrade.exec_()

class Ui_Dialog(object):
    def initBuySituation(self, tableView, model):
        #the situation of Buy
        model.setHorizontalHeaderLabels([u'买入价', u'买入量'])
        for row in range(5):
            for column in range(2):
                if column == 1:
                    item = QStandardItem("%s" %('vol'))
                else:
                    item = QStandardItem("%s" %('price'))
                model.setItem(row, column, item)
        tableView.setModel(model)
        tableView.horizontalHeader().setStretchLastSection(True)
        
        
    def initSellSituation(self, tableView, model):
        #the situation of Sell
        model.setHorizontalHeaderLabels([u'卖出价', u'卖出量'])
        for row in range(5):
            for column in range(2):
                if column == 1:
                    item = QStandardItem("%s" %('vol'))
                else:
                    item = QStandardItem("%s" %('price'))
                model.setItem(row, column, item)
        tableView.setModel(model)
        tableView.horizontalHeader().setStretchLastSection(True)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(271, 629)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 90, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 120, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 91, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 30, 91, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 30, 51, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#         self.tableView = QtGui.QTableView(Dialog)
        self.tableView = MyTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 180, 231, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView_2 = QtGui.QTableView(Dialog)
        self.tableView_2.setGeometry(QtCore.QRect(20, 420, 231, 192))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(120, 160, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 400, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        model_sell=QStandardItemModel(5,2)
        model_buy=QStandardItemModel(5,2)
        self.initBuySituation(self.tableView_2, model_sell)
        self.initSellSituation(self.tableView, model_buy)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "日内快速交易", None))
        self.label.setText(_translate("Dialog", "股票名称", None))
        self.label_2.setText(_translate("Dialog", "股票代号", None))
        self.label_3.setText(_translate("Dialog", "当前价格", None))
        self.label_4.setText(_translate("Dialog", "涨跌价格", None))
        self.label_5.setText(_translate("Dialog", "涨跌百分比", None))
        self.pushButton.setText(_translate("Dialog", "查找", None))
        self.label_6.setText(_translate("Dialog", "卖盘", None))
        self.label_7.setText(_translate("Dialog", "买盘", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

