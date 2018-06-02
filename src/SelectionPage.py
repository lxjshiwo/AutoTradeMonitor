# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
import Ui_InnerDayTrade
import Ui_InnerDayQuickTrade
import Ui_TradeRecord
import Ui_UnfinishRecord

from Ui_SelectionPage import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
    def showInnerDayTrade(self):
        Form_innerDayTrade = QtGui.QDialog()  
        innerDayTrade = Ui_InnerDayTrade.Ui_Dialog()
        innerDayTrade.setupUi(Form_innerDayTrade)  
        Form_innerDayTrade.show()  
        Form_innerDayTrade.exec_()
        
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        to init the InnerDayQuickTrade 
        """
        
        Form_innerDayTrade = QtGui.QDialog()  
        innerDayTrade = Ui_InnerDayTrade.Ui_Dialog()
        innerDayTrade.setupUi(Form_innerDayTrade)  
        Form_innerDayTrade.show()  
        Form_innerDayTrade.exec_()
        
        
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        to init the innerDayTrade
        """
        Form_innerDayTrade = QtGui.QDialog()  
        innerDayTrade = Ui_InnerDayQuickTrade.Ui_Dialog()
        innerDayTrade.setupUi(Form_innerDayTrade)  
        Form_innerDayTrade.show()  
        Form_innerDayTrade.exec_()
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        to init the TradeRecord 
        """
        # TODO: not implemented yet
        Form_innerDayTrade = QtGui.QDialog()  
        innerDayTrade = Ui_TradeRecord.Ui_Dialog()
        innerDayTrade.setupUi(Form_innerDayTrade)  
        Form_innerDayTrade.show()  
        Form_innerDayTrade.exec_()
        
        
        
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        to init the UnfinishRecord
        """
        # TODO: not implemented yet
        Form_innerDayTrade = QtGui.QDialog()  
        innerDayTrade = Ui_UnfinishRecord.Ui_Dialog()
        innerDayTrade.setupUi(Form_innerDayTrade)  
        Form_innerDayTrade.show()  
        Form_innerDayTrade.exec_()
        

