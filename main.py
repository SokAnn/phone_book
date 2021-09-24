# Python version 3.8
import mariadb
# from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import QDate

from en_win import En_Window
from pas_win import Pas_Window
from reg_win import Reg_Window

###################################################################################################
# from main_win import Ui_MainWindow as MainWindow
from example import Ui_MainWindow as MainWindow

import sys
import pickle

def print_hi(name):
    print('Hi, ' + name)



class Main_Win(QMainWindow, MainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("Телефонная книжка")
        ##############################################################################################
        # self.setMinimumHeight(500)
        # self.setMaximumHeight(500)
        # self.setMinimumWidth(550)
        # self.setMaximumWidth(550)
        self.setMinimumHeight(700)
        self.setMaximumHeight(700)
        self.setMinimumWidth(850)
        self.setMaximumWidth(850)

    def widgets_adjust(self):
        # init label parameters
        self.label.setText("Зашли как ")
        self.label.setStyleSheet("font-size: 12px;")
        # init UserButton parameters
        #############################################################        поменять текс пользователя
        # self.UserButton.setText("Admin")
        self.UserButton.setStyleSheet("text-decoration: underline;"
                                      "background-color: rgba(255,255,255,0);"
                                      "font-size: 12px;"
                                      "border:none;"
                                      "color: blue;")
        # init ExitButton parameters
        self.ExitButton.setText("Выйти")
        self.ExitButton.setStyleSheet("border-radius: 8px;"
                                      "color: #000000;"
                                      "background: #d4d2d6;"
                                      "font-size: 12px;"
                                      "border-bottom: 3px solid #b9b5bd;")

        # actions when buttons clicked
        self.ExitButton.clicked.connect(self.clicked_exit)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_exit(self):
        self.click_button(self.ExitButton.text())
        self.switch_window.emit("4 -> 1")
        with open('data.pickle', 'wb') as f:
            pickle.dump(['', ''], f)

class Controller:
    def __init__(self, user):
        self.user = user

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
            # self.form1.close()
            self.form3 = Reg_Window()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
        if text == "1 -> 4":
            user = self.form1.NamelineEdit.text()
            self.form1.close()
            self.form4 = Main_Win()
            self.form4.UserButton.setText(user)
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
        if text == "2 -> 1":
            self.form2.close()
        # if text == "3 -> 1":
        #     pass
        if text == "3 -> 4":
            user = self.form3.NamelineEdit.text()
            self.form3.close()
            self.form4 = Main_Win()
            self.form4.UserButton.setText(user)
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
        if text == "4":
            self.form4 = Main_Win()
            self.form4.UserButton.setText(self.user)
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
        if text == "4 -> 1":
            self.form4.close()
            self.form1 = En_Window()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()


def application():
    app = QApplication(sys.argv)

    # load last saved user
    with open('data.pickle', 'rb') as f:
        User_Pas = pickle.load(f)
    controller = Controller(User_Pas[0])
    # check user -> form1 (user==false) or form4 (user==true)
    if True if User_Pas[0] and User_Pas[1] else False:
        controller.select_forms("4")
    else:
        controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    print_hi('PyCharm')
    # application()

    # DB
    conn = mariadb.connect(user='root', password='root', host='localhost', port=3306, database="DB_users")
    cur = conn.cursor()

    cur.execute("SELECT * FROM db_users.users")
    # print(len(cur))
    for Name, Telephone, Bdate in cur:
        print(f"Name: {Name}, \nTelephone: {Telephone}, \nDate: {Bdate}\n")


