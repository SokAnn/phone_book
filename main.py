# Python version 3.8
import mariadb
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

from en_win import Ui_MainWindow as EnWindow
from pas_win import Ui_MainWindow as PasWindow
from reg_win import Ui_MainWindow as RegWindow
# from main_window import Ui_MainWindow as main_Form

import sys

# Form, Window = uic.loadUiType("window.ui")

def print_hi(name):
    print('Hi, ' + name)

# entrance window
class En_Window(QMainWindow, EnWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("Вход в систему")
        self.setMinimumHeight(250)
        # self.setMinimumWidth(110)

    def widgets_adjust(self):
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
        # init NameTextEdit parameters
        self.NameTextEdit.setMaximumHeight(30)
        self.NameTextEdit.setMinimumHeight(30)
        self.NameTextEdit.setToolTip("Имя пользователя")
        # init PasswordTextEdit parameters
        self.PasswordTextEdit.setMaximumHeight(30)
        self.PasswordTextEdit.setMinimumHeight(30)
        self.PasswordTextEdit.setToolTip("Пароль")
        # init RememberCheckBox parameters
        self.RememberCheckBox.setMaximumHeight(30)
        self.RememberCheckBox.setMinimumHeight(30)
        self.RememberCheckBox.setText("Запомнить меня")
        # init ShowCheckBox parameters
        self.ShowCheckBox.setMaximumHeight(30)
        self.ShowCheckBox.setMinimumHeight(30)
        self.ShowCheckBox.setText("Показать пароль")
        # init RememberCheckBox parameters & actions
        self.RememberCheckBox.stateChanged.connect(self.clicked_rem_chb)
        # init ShowCheckBox parameters & actions
        self.ShowCheckBox.stateChanged.connect(self.clicked_sh_chb)
        # init label parameters
        self.label.setText("Забыли пароль?")
        # self.label.setOpenExternalLinks(True)

        # actions when buttons clicked
        self.EntranceButton.clicked.connect(self.clicked_en_b)
        self.RegistrationButton.clicked.connect(self.clicked_reg_b)
        self.CancelButton.clicked.connect(self.clicked_c_b)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_en_b(self):
        self.click_button(self.EntranceButton.text())

    def clicked_reg_b(self):
        self.click_button(self.RegistrationButton.text())

    def clicked_c_b(self):
        self.click_button(self.CancelButton.text())

    def clicked_rem_chb(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox -> remember')
        else:
            self.setWindowTitle("Вход в систему")

    def clicked_sh_chb(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox -> show')
        else:
            self.setWindowTitle("Вход в систему")


class Pas_Window(QMainWindow, PasWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()

    def widgets_adjust(self):
        # init AddressTextEdit parameters
        self.AddressTextEdit.setMaximumHeight(30)
        self.AddressTextEdit.setMinimumHeight(30)
        self.AddressTextEdit.setToolTip("Имя пользователя")
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

    def clicked_c_b(self):
        self.click_button(self.CancelPushButton.text())


class Reg_Window(QMainWindow, RegWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()

    def widgets_adjust(self):
        # init NewNameTextEdit parameters
        self.NewNameTextEdit.setMaximumHeight(30)
        self.NewNameTextEdit.setMinimumHeight(30)
        self.NewNameTextEdit.setToolTip("Имя пользователя")
        # init NewPasswordTextEdit parameters
        self.NewPasswordTextEdit.setMaximumHeight(30)
        self.NewPasswordTextEdit.setMinimumHeight(30)
        self.NewPasswordTextEdit.setToolTip("Пароль")
        # init RepeatPasswordTextEdit parameters
        self.RepeatPasswordTextEdit.setMaximumHeight(30)
        self.RepeatPasswordTextEdit.setMinimumHeight(30)
        self.RepeatPasswordTextEdit.setToolTip("Повторите пароль")
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

    def clicked_c_b(self):
        self.click_button(self.CancelPushButton.text())


def application():
    app = QApplication(sys.argv)
    window = En_Window()
    # window = Pas_Window()
    # window = Reg_Window()

    # window.setWindowTitle("simple window")
    window.setGeometry(1300, 250, 350, 200)
    # window.setMinimumHeight(250)
    # window.setMaximumHeight(250)

    window.show()
    sys.exit(app.exec_())

    pass

if __name__ == '__main__':
    print_hi('PyCharm')
    print('test')
    application()



