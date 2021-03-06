# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\OutputTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.skeleton.OutputTestSkeleton import Ui_Form

class OutputSettings(QtWidgets.QWidget, Ui_Form):
    switch_adv_settings = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.back.clicked.connect(self.backbutton_handler)
    
    def backbutton_handler(self):
        self.switch_adv_settings.emit()