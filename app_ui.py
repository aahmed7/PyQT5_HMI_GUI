import sys
from PyQt5 import QtCore, QtWidgets
from GUI import LoginKeypad
from GUI import mainwindow
from GUI import basicsettings
from GUI import AdvancedSettings
from GUI import OutputTest
from GUI import calibration
from GUI import startstop
import os


class Controller:
    def __init__(self):
        self.login = LoginKeypad.Keypad()
        self.main = mainwindow.MainWindow()
        self.basic_settings = basicsettings.BasicSettings()
        self.adv_settings = AdvancedSettings.AdvancedSettings()
        self.output_test_settings = OutputTest.OutputSettings()
        self.calibration_settings = calibration.Calibration()
        self.startstop = startstop.StartStop()

    def hide_windows(self):
        self.adv_settings.close()
        self.basic_settings.close()
        self.login.close()
        self.main.close()
        self.output_test_settings.close()
        self.calibration_settings.close()

    def show_main(self):
        self.main.switch_settings.connect(self.show_basic_settings)
        self.main.dialog_startstop.connect(self.show_startstop)
        self.login.close()
        self.hide_windows()
        self.main.show()

    def show_startstop(self):
        self.startstop.show()

    def show_basic_settings(self):
        self.basic_settings.switch_adv_settings.connect(self.show_login)
        self.basic_settings.switch_menu.connect(self.show_main)
        self.hide_windows()
        self.basic_settings.show()

    def show_login(self):
        self.login.unlock_settings.connect(self.show_advanced_settings)
        self.login.show()

    def show_advanced_settings(self):
        self.adv_settings.switch_basic_settings.connect(
            self.show_basic_settings)
        self.adv_settings.switch_output_settings.connect(
            self.show_output_test_settings)
        self.adv_settings.switch_calibration_settings.connect(
            self.show_calibration_settings)
        self.hide_windows()
        self.adv_settings.show()

    def show_output_test_settings(self):
        self.output_test_settings.switch_adv_settings.connect(
            self.show_advanced_settings)
        self.hide_windows()
        self.output_test_settings.show()

    def show_calibration_settings(self):
        self.calibration_settings.switch_adv_settings.connect(
            self.show_advanced_settings)
        self.hide_windows()
        self.calibration_settings.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
