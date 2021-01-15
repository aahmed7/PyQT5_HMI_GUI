from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.skeleton.MainwindowSkeleton import Ui_Form

class MainWindow(QtWidgets.QWidget, Ui_Form):
    switch_settings = QtCore.pyqtSignal()
    dialog_startstop = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
        self.settings_btn.clicked.connect(self.settingsbutton_handler)
        self.start.clicked.connect(self.startstopbutton_handler)

    def settingsbutton_handler(self):
        self.switch_settings.emit()

    def startstopbutton_handler(self):
        self.dialog_startstop.emit()