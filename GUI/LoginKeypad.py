from Settings import UserSettings
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Settings import Login
from GUI.skeleton.LoginSkeleton import Ui_Form


class Keypad(QtWidgets.QWidget, Ui_Form):
    unlock_settings = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn0.clicked.connect(self.press0)
        self.btn1.clicked.connect(self.press1)
        self.btn2.clicked.connect(self.press2)
        self.btn3.clicked.connect(self.press3)
        self.btn4.clicked.connect(self.press4)
        self.btn5.clicked.connect(self.press5)
        self.btn6.clicked.connect(self.press6)
        self.btn7.clicked.connect(self.press7)
        self.btn8.clicked.connect(self.press8)
        self.btn9.clicked.connect(self.press9)
        self.btnOk.clicked.connect(self.pressEnt)
        self.btnC.clicked.connect(self.pressC)
        self.passwordClear = True
        self.password = "c"

    def press1(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "1"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "1"

    def press2(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "2"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "2"

    def press3(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "3"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "3"

    def press4(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "4"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "4"

    def press5(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "5"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "5"

    def press6(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "6"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "6"

    def press7(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "7"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "7"

    def press8(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "8"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "8"

    def press9(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "9"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "9"

    def press0(self):
        if self.passwordClear == True:
            self.label.setText("*")
            self.passwordClear = False
            self.password = "0"
        else:
            self.label.setText(self.label.text()+"*")
            self.password = self.password + "0"

    def pressC(self):
        self.label.setText("Enter Password")
        self.passwordClear = True
        self.password = "C"

    # When Enter is pressed, check the password.
    def pressEnt(self):
        if Login.user_login.check_login_password(self.password):
            self.label.setText("Enter Password")
            self.passwordClear = True
            self.password = "C"
            self.unlock_settings.emit()
        else:
            msg = QMessageBox()
            msg.setText("Wrong password")
            msg.exec_()
