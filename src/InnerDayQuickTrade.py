# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from PyQt4 import QtCore, QtGui


from Ui_InnerDayQuickTrade import Ui_Dialog



#query stock 
from pytdx.hq import TdxHq_API

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
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())