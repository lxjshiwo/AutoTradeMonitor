# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import os
import Ui_SelectionPage 
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
from Ui_LoginPage import Ui_MainWindow
import SelectionPage

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.Selection_Page = SelectionPage.Dialog()
        self.pushButton.clicked.connect(self.showSelectionPage)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        pass
        
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        self.close()
    
    def  showSelectionPage(self):
        self.setVisible(0)
        self.Selection_Page.setVisible(1)
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    
    sys.exit(app.exec_())

