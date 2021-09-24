# Python version 3.8
import mariadb
# from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import QDate

from en_win import Ui_MainWindow as EnWindow
from pas_win import Ui_MainWindow as PasWindow
from reg_win import Ui_MainWindow as RegWindow
# from main_window import Ui_MainWindow as main_Form

import sys
import pickle

# Form, Window = uic.loadUiType("window.ui")

def print_hi(name):
    print('Hi, ' + name)

# entrance window
class En_Window(QMainWindow, EnWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("Вход в систему")
        self.setMinimumHeight(270)
        self.setMaximumHeight(270)
        self.setMinimumWidth(320)
        self.setMaximumWidth(320)
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(2))

    def widgets_adjust(self):
        # init NamelineEdit parameters
        self.NamelineEdit.setMaximumHeight(30)
        self.NamelineEdit.setMinimumHeight(30)
        self.NamelineEdit.setMinimumWidth(50)
        self.NamelineEdit.setPlaceholderText("Имя пользователя")
        self.NamelineEdit.setStyleSheet("font-size: 12px;")
        # init PasswordlineEdit parameters
        self.PasswordlineEdit.setMaximumHeight(30)
        self.PasswordlineEdit.setMinimumHeight(30)
        self.PasswordlineEdit.setMinimumWidth(50)
        self.PasswordlineEdit.setPlaceholderText("Пароль")
        self.PasswordlineEdit.setStyleSheet("font-size: 12px;")
        # init EntranceButton parameters
        self.EntranceButton.setMinimumHeight(30)
        self.EntranceButton.setMinimumWidth(60)
        self.EntranceButton.setText("Войти")
        self.EntranceButton.setStyleSheet("border-radius: 8px;"
                                          "color: #000000;"
                                          "background: #66ff66;"
                                          "font-size: 12px;"
                                          "border-bottom: 3px solid #00cc00;")
        # init RegistrationButton parameters
        self.RegistrationButton.setMinimumHeight(30)
        self.RegistrationButton.setMinimumWidth(60)
        self.RegistrationButton.setText("Регистрация")
        self.RegistrationButton.setStyleSheet("border-radius: 8px;"
                                              "color: #000000;"
                                              "background: #d4d2d6;"
                                              "font-size: 12px;"
                                              "border-bottom: 3px solid #b9b5bd;")
        # init CancelButton parameters
        self.CancelButton.setMinimumHeight(30)
        self.CancelButton.setMinimumWidth(60)
        self.CancelButton.setText("Отмена")
        self.CancelButton.setStyleSheet("border-radius: 8px;"
                                        "color: #000000;"
                                        "background: #ff5757;"
                                        "font-size: 12px;"
                                        "border-bottom: 3px solid #ff2424;")
        # init RememberCheckBox parameters
        self.RememberCheckBox.setMaximumHeight(30)
        self.RememberCheckBox.setMinimumHeight(30)
        self.RememberCheckBox.setText("Запомнить меня")
        self.RememberCheckBox.setStyleSheet("font-size: 12px;")
        # init ShowCheckBox parameters
        self.ShowCheckBox.setMaximumHeight(30)
        self.ShowCheckBox.setMinimumHeight(30)
        self.ShowCheckBox.setText("Показать пароль")
        self.ShowCheckBox.setStyleSheet("font-size: 12px;")
        # init ForgotPassButton parameters
        self.ForgotPassButton.setText("Забыли пароль?")
        self.ForgotPassButton.setStyleSheet("text-decoration: underline;"
                                            "background-color: rgba(255,255,255,0);"
                                            "font-size: 12px;"
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

        # save user
        if self.RememberCheckBox.isChecked():
            with open('data.pickle', 'wb') as f:
                pickle.dump([self.NamelineEdit.text(), self.PasswordlineEdit.text()], f)
                print([self.NamelineEdit.text(), self.PasswordlineEdit.text()])

        # # load saved user
        # with open('data.pickle', 'rb') as f:
        #     User_Pas = pickle.load(f)
        #     print(User_Pas)

        if True if self.NamelineEdit.text() and self.PasswordlineEdit.text() else False:
            self.switch_window.emit("1 -> 4")
        else:
            m = QMessageBox()  # init
            m.setWindowTitle("Ошибка 404")  # set title
            m.setText("Такой пользователь не найден!!!")
            m.setIcon(QMessageBox.Critical)  # set icon
            m.setStandardButtons(QMessageBox.Ok)
            m.exec_()

    def clicked_reg_b(self):
        self.click_button(self.RegistrationButton.text())
        self.switch_window.emit("1 -> 3")

    def clicked_c_b(self):
        self.click_button(self.CancelButton.text())
        self.NamelineEdit.clear()
        self.PasswordlineEdit.clear()

    def clicked_rem_chb(self):
        if self.RememberCheckBox.isChecked():
            self.setWindowTitle('QCheckBox -> remember')
        else:
            self.setWindowTitle("Вход в систему")

    def clicked_sh_chb(self):
        if self.ShowCheckBox.isChecked():
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
        self.setMinimumHeight(270)
        self.setMaximumHeight(270)
        self.setMinimumWidth(320)
        self.setMaximumWidth(320)

    def widgets_adjust(self):
        # init AddresslineEdit parameters
        self.AddresslineEdit.setMinimumHeight(30)
        self.AddresslineEdit.setPlaceholderText("Адрес электронной почты")
        self.AddresslineEdit.setStyleSheet("font-size: 12px;")
        # init ChangePasswordPushButton parameters
        self.ChangePasswordPushButton.setMinimumHeight(30)
        self.ChangePasswordPushButton.setMinimumWidth(60)
        self.ChangePasswordPushButton.setText("Сменить пароль")
        self.ChangePasswordPushButton.setStyleSheet("border-radius: 8px;"
                                                    "color: #000000;"
                                                    "background: #d4d2d6;"
                                                    "font-size: 12px;"
                                                    "border-bottom: 3px solid #b9b5bd;")
        # init CancelPushButton parameters
        self.CancelPushButton.setMinimumHeight(30)
        self.CancelPushButton.setMinimumWidth(60)
        self.CancelPushButton.setText("Отмена")
        self.CancelPushButton.setStyleSheet("border-radius: 8px;"
                                            "color: #000000;"
                                            "background: #ff5757;"
                                            "font-size: 12px;"
                                            "border-bottom: 3px solid #ff2424;")

        # actions when buttons clicked
        self.ChangePasswordPushButton.clicked.connect(self.clicked_ch_p_b)
        self.CancelPushButton.clicked.connect(self.clicked_c_b)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_ch_p_b(self):
        self.click_button(self.ChangePasswordPushButton.text())
        # check email
        if self.AddresslineEdit.text():
            self.switch_window.emit("2 -> 1")
        else:
            m = QMessageBox()  # init
            m.setWindowTitle("Ошибка заполнения")  # set title
            m.setText("Поле 'Адрес электронной почты' не заполнено!")
            m.setIcon(QMessageBox.Critical)  # set icon
            m.setStandardButtons(QMessageBox.Ok)
            m.exec_()

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
        self.setMinimumHeight(400)
        self.setMaximumHeight(400)
        self.setMinimumWidth(360)
        self.setMaximumWidth(360)
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(2))
        self.RepeatlineEdit.setEchoMode(QLineEdit.EchoMode(2))
        self.DatelineEdit.setReadOnly(True)

    def widgets_adjust(self):
        # init NamelineEdit parameters
        self.NamelineEdit.setMaximumHeight(30)
        self.NamelineEdit.setMinimumHeight(30)
        self.NamelineEdit.setMaximumWidth(380)
        self.NamelineEdit.setPlaceholderText("Имя пользователя")
        self.NamelineEdit.setStyleSheet("font-size: 12px;")
        # init PasswordlineEdit parameters
        self.PasswordlineEdit.setMaximumHeight(30)
        self.PasswordlineEdit.setMinimumHeight(30)
        self.PasswordlineEdit.setMaximumWidth(380)
        self.PasswordlineEdit.setPlaceholderText("Пароль")
        self.PasswordlineEdit.setStyleSheet("font-size: 12px;")
        # init RepeatlineEdit parameters
        self.RepeatlineEdit.setMaximumHeight(30)
        self.RepeatlineEdit.setMinimumHeight(30)
        self.RepeatlineEdit.setMaximumWidth(380)
        self.RepeatlineEdit.setPlaceholderText("Повторите пароль")
        self.RepeatlineEdit.setStyleSheet("font-size: 12px;")
        # init DatelineEdit & DateEdit parameters
        self.DatelineEdit.setMaximumHeight(30)
        self.DatelineEdit.setMinimumHeight(30)
        self.DatelineEdit.setMaximumWidth(290)
        self.DatelineEdit.setPlaceholderText("Дата рождения")
        self.DatelineEdit.setStyleSheet("font-size: 12px;")
        self.DateEdit.setMaximumHeight(30)
        self.DateEdit.setMinimumHeight(30)
        self.DateEdit.setMaximumWidth(90)
        self.DateEdit.setDate(QDate.currentDate())
        self.DateEdit.setStyleSheet("font-size: 12px;")
        # init OkPushButton parameters
        self.OkPushButton.setMaximumHeight(30)
        self.OkPushButton.setMinimumHeight(30)
        self.OkPushButton.setMaximumWidth(120)
        self.OkPushButton.setText("Ок")
        self.OkPushButton.setStyleSheet("border-radius: 8px;"
                                        "color: #000000;"
                                        "background: #d4d2d6;"
                                        "font-size: 12px;"
                                        "border-bottom: 3px solid #b9b5bd;")
        # init CancelPushButton parameters
        self.CancelPushButton.setMaximumHeight(30)
        self.CancelPushButton.setMinimumHeight(30)
        self.CancelPushButton.setMaximumWidth(120)
        self.CancelPushButton.setText("Отмена")
        self.CancelPushButton.setStyleSheet("border-radius: 8px;"
                                            "color: #000000;"
                                            "background: #ff5757;"
                                            "font-size: 12px;"
                                            "border-bottom: 3px solid #ff2424;")

        # actions when buttons clicked
        self.DateEdit.dateChanged.connect(self.date_changed)
        self.OkPushButton.clicked.connect(self.clicked_ok_b)
        self.CancelPushButton.clicked.connect(self.clicked_c_b)

    def date_changed(self):
        self.DatelineEdit.setText(self.DateEdit.text())

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_ok_b(self):
        self.click_button(self.OkPushButton.text())
        if self.NamelineEdit.text() and self.PasswordlineEdit.text() and self.RepeatlineEdit.text() and self.DatelineEdit.text():
            if self.PasswordlineEdit.text() != self.RepeatlineEdit.text():
                m = QMessageBox()  # init
                m.setWindowTitle("Ошибка заполнения")  # set title
                m.setText("Пароли не совпадают!")
                m.setIcon(QMessageBox.Critical)  # set icon
                m.setStandardButtons(QMessageBox.Ok)
                m.exec_()
            else:
                ################################################################## или переход на 4 окно сразу???
                self.switch_window.emit("3 -> 1")
        else:
            m = QMessageBox()  # init
            m.setWindowTitle("Ошибка заполнения")  # set title
            m.setText("Не все поля заполнены!")
            m.setIcon(QMessageBox.Critical)  # set icon
            m.setStandardButtons(QMessageBox.Ok)
            m.exec_()

    def clicked_c_b(self):
        self.click_button(self.CancelPushButton.text())
        self.NamelineEdit.clear()
        self.PasswordlineEdit.clear()
        self.RepeatlineEdit.clear()
        self.DateEdit.setDate(QDate.currentDate())
        self.DatelineEdit.clear()


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
        if text == "4 -> 1":
            pass

def application():
    app = QApplication(sys.argv)
    controller = Controller()
    # check user -> form1 (user==false) or form4 (user==true)
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    print_hi('PyCharm')
    # print('test pickle')
    # name_user = 'Admin'
    # with open('data.pickle', 'wb') as f:
    #     pickle.dump(name_user, f)
    application()



