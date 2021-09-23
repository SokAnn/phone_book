# Python version 3.8
import mariadb
# from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt

from en_win import Ui_MainWindow as EnWindow
from pas_win import Ui_MainWindow as PasWindow
from reg_win import Ui_MainWindow as RegWindow
# from main_window import Ui_MainWindow as main_Form

import sys

# Form, Window = uic.loadUiType("window.ui")

def print_hi(name):
    print('Hi, ' + name)

# 1 2 3 4
choosing_windows = ['', '', '', '']

# entrance window
class En_Window(QMainWindow, EnWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("Вход в систему")
        self.setMinimumHeight(280)
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(2))
        # self.setMinimumWidth(110)

    def widgets_adjust(self):
        # init NamelineEdit parameters
        self.NamelineEdit.setMaximumHeight(30)
        self.NamelineEdit.setMinimumHeight(30)
        self.NamelineEdit.setPlaceholderText("Имя пользователя")
        # init PasswordlineEdit parameters
        self.PasswordlineEdit.setMaximumHeight(30)
        self.PasswordlineEdit.setMinimumHeight(30)
        self.PasswordlineEdit.setPlaceholderText("Пароль")
        # init EntranceButton parameters
        self.EntranceButton.setMaximumHeight(30)
        self.EntranceButton.setMinimumHeight(30)
        self.EntranceButton.setMinimumWidth(100)
        self.EntranceButton.setText("Войти")
        self.EntranceButton.setStyleSheet("background-color: green;")
        # init RegistrationButton parameters
        self.RegistrationButton.setMaximumHeight(30)
        self.RegistrationButton.setMinimumHeight(30)
        self.RegistrationButton.setMinimumWidth(100)
        self.RegistrationButton.setText("Регистрация")
        # init CancelButton parameters
        self.CancelButton.setMaximumHeight(30)
        self.CancelButton.setMinimumHeight(30)
        self.CancelButton.setMinimumWidth(100)
        self.CancelButton.setText("Отмена")
        self.CancelButton.setStyleSheet("background-color: red;")
        # init RememberCheckBox parameters
        self.RememberCheckBox.setMaximumHeight(30)
        self.RememberCheckBox.setMinimumHeight(30)
        self.RememberCheckBox.setText("Запомнить меня")
        # init ShowCheckBox parameters
        self.ShowCheckBox.setMaximumHeight(30)
        self.ShowCheckBox.setMinimumHeight(30)
        self.ShowCheckBox.setText("Показать пароль")
        # init ForgotPassButton parameters
        self.ForgotPassButton.setText("Забыли пароль?")
        self.ForgotPassButton.setStyleSheet("text-decoration: underline;"
                                            "background-color: rgba(255,255,255,0);"
                                            "border:none;"
                                            "color: blue;")
        self.ForgotPassButton.setMaximumHeight(30)
        self.ForgotPassButton.setMinimumHeight(30)
        self.ForgotPassButton.setMinimumWidth(100)

        # actions when buttons & checkbox clicked
        self.EntranceButton.clicked.connect(self.clicked_en_b)
        self.RegistrationButton.clicked.connect(self.clicked_reg_b)
        self.CancelButton.clicked.connect(self.clicked_c_b)
        self.RememberCheckBox.stateChanged.connect(self.clicked_rem_chb)
        self.ShowCheckBox.stateChanged.connect(self.clicked_sh_chb)
        self.ForgotPassButton.clicked.connect(self.clicked_f_b)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_en_b(self):
        self.click_button(self.EntranceButton.text())
        self.switch_window.emit("1 -> 4")

    def clicked_reg_b(self):
        self.click_button(self.RegistrationButton.text())
        self.switch_window.emit("1 -> 3")

    def clicked_c_b(self):
        self.click_button(self.CancelButton.text())
        self.NamelineEdit.clear()
        self.PasswordlineEdit.clear()

    def clicked_rem_chb(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox -> remember')
        else:
            self.setWindowTitle("Вход в систему")

    def clicked_sh_chb(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox -> show')
            self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(0))
        else:
            self.setWindowTitle("Вход в систему")
            self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(2))

    def clicked_f_b(self):
        self.click_button(self.ForgotPassButton.text())
        self.ForgotPassButton.setStyleSheet("text-decoration: underline;"
                                            "background-color: rgba(255,255,255,0);"
                                            "border:none;"
                                            "color: fuchsia;")
        self.switch_window.emit("1 -> 2")


class Pas_Window(QMainWindow, PasWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("Восстановление пароля")

    def widgets_adjust(self):
        # init AddresslineEdit parameters
        self.AddresslineEdit.setMaximumHeight(30)
        self.AddresslineEdit.setMinimumHeight(30)
        self.AddresslineEdit.setPlaceholderText("Адрес электронной почты")
        # init ChangePasswordPushButton parameters
        self.ChangePasswordPushButton.setMaximumHeight(30)
        self.ChangePasswordPushButton.setMinimumHeight(30)
        self.ChangePasswordPushButton.setMinimumWidth(100)
        self.ChangePasswordPushButton.setText("Сменить пароль")
        # init CancelPushButton parameters
        self.CancelPushButton.setMaximumHeight(30)
        self.CancelPushButton.setMinimumHeight(30)
        self.CancelPushButton.setMinimumWidth(100)
        self.CancelPushButton.setText("Отмена")
        self.CancelPushButton.setStyleSheet("background-color: red;")

        # actions when buttons clicked
        self.ChangePasswordPushButton.clicked.connect(self.clicked_ch_p_b)
        self.CancelPushButton.clicked.connect(self.clicked_c_b)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_ch_p_b(self):
        self.click_button(self.ChangePasswordPushButton.text())
        self.switch_window.emit("2 -> 1")

    def clicked_c_b(self):
        self.click_button(self.CancelPushButton.text())
        self.AddresslineEdit.clear()


class Reg_Window(QMainWindow, RegWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("Регистрация")
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(2))
        self.RepeatlineEdit.setEchoMode(QLineEdit.EchoMode(2))

    def widgets_adjust(self):
        # init NamelineEdit parameters
        self.NamelineEdit.setMaximumHeight(30)
        self.NamelineEdit.setMinimumHeight(30)
        self.NamelineEdit.setPlaceholderText("Имя пользователя")
        # init PasswordlineEdit parameters
        self.PasswordlineEdit.setMaximumHeight(30)
        self.PasswordlineEdit.setMinimumHeight(30)
        self.PasswordlineEdit.setPlaceholderText("Пароль")
        # init RepeatlineEdit parameters
        self.RepeatlineEdit.setMaximumHeight(30)
        self.RepeatlineEdit.setMinimumHeight(30)
        self.RepeatlineEdit.setPlaceholderText("Повторите пароль")
        # init DateEdit parameters
        # self.DateEdit
        # init OkPushButton parameters
        self.OkPushButton.setMaximumHeight(30)
        self.OkPushButton.setMinimumHeight(30)
        self.OkPushButton.setMinimumWidth(100)
        self.OkPushButton.setText("Ок")
        # init CancelPushButton parameters
        self.CancelPushButton.setMaximumHeight(30)
        self.CancelPushButton.setMinimumHeight(30)
        self.CancelPushButton.setMinimumWidth(100)
        self.CancelPushButton.setText("Отмена")
        self.CancelPushButton.setStyleSheet("background-color: red;")

        # actions when buttons clicked
        self.OkPushButton.clicked.connect(self.clicked_ok_b)
        self.CancelPushButton.clicked.connect(self.clicked_c_b)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_ok_b(self):
        self.click_button(self.OkPushButton.text())
        self.switch_window.emit("3 -> 1")


    def clicked_c_b(self):
        self.click_button(self.CancelPushButton.text())
        self.NamelineEdit.clear()
        self.PasswordlineEdit.clear()
        self.RepeatlineEdit.clear()


class Controller:
    # def __init__(self): pass

    def select_forms(self, text):
        if text == "1":
            self.form1 = En_Window()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
        if text == "1 -> 2":
            self.form2 = Pas_Window()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
        if text == "1 -> 3":
            self.form3 = Reg_Window()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
        if text == "1 -> 4":
            pass
        if text == "2 -> 1":
            self.form2.close()
        if text == "3 -> 1":
            self.form3.close()
        if text == "4":
            pass

def application():
    app = QApplication(sys.argv)
    controller = Controller()
    # check user -> form1 (user==false) or form4 (user==true)
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    print_hi('PyCharm')
    print('test')
    application()



