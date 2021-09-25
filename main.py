# Python version 3.8
import mariadb
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDate, Qt

from en_win import En_Window
from pas_win import Pas_Window
from reg_win import Reg_Window
from example import Ui_MainWindow as MainWindow
from add_win import Add_Window
from edit_win import Edit_Window
from del_win import Del_Window

import sys
import pickle
import fuctions_db

def print_hi(name):
    print('Hi, ' + name)


class Main_Win(QMainWindow, MainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, list_users):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.list_users = list_users
        self.widgets_adjust(self.list_users)
        self.setWindowTitle("Телефонная книжка")
        ################################################################################
        # self.setMinimumHeight(500)
        # self.setMaximumHeight(500)
        # self.setMinimumWidth(550)
        # self.setMaximumWidth(550)
        self.setMinimumHeight(700)
        self.setMaximumHeight(700)
        self.setMinimumWidth(850)
        self.setMaximumWidth(850)

    def widgets_adjust(self, list_users):
        # init label parameters
        self.label.setText("Зашли как ")
        self.label.setStyleSheet("font-size: 12px;")
        # init UserButton parameters
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
        # init AddButton parameters
        self.AddButton.setMinimumHeight(30)
        self.AddButton.setMaximumWidth(100)
        self.AddButton.setText("Добавить")
        self.AddButton.setStyleSheet("border-radius: 8px;"
                                     "color: #000000;"
                                     "background: #d4d2d6;"
                                     "font-size: 12px;"
                                     "border-bottom: 3px solid #b9b5bd;")
        # self.AddButton.setStyleSheet("font-size: 12px;")
        # init EditButton parameters
        self.EditButton.setMinimumHeight(30)
        self.EditButton.setMaximumWidth(100)
        self.EditButton.setText("Изменить")
        self.EditButton.setStyleSheet("border-radius: 8px;"
                                      "color: #000000;"
                                      "background: #d4d2d6;"
                                      "font-size: 12px;"
                                      "border-bottom: 3px solid #b9b5bd;")
        # init DelButton parameters
        self.DelButton.setMinimumHeight(30)
        self.DelButton.setMaximumWidth(100)
        self.DelButton.setText("Удалить")
        self.DelButton.setStyleSheet("border-radius: 8px;"
                                     "color: #000000;"
                                     "background: #d4d2d6;"
                                     "font-size: 12px;"
                                     "border-bottom: 3px solid #b9b5bd;")
        # init tables: tableWidget - tableWidget_14
        tables = [self.tableWidget, self.tableWidget_2, self.tableWidget_3, self.tableWidget_4, self.tableWidget_5,
                  self.tableWidget_6, self.tableWidget_7, self.tableWidget_8, self.tableWidget_9, self.tableWidget_10,
                  self.tableWidget_11, self.tableWidget_12, self.tableWidget_13, self.tableWidget_14]
        for table in tables:
            table.setStyleSheet("font-size: 12px;")
            table.setMinimumWidth(680)
            table.setMaximumWidth(680)
            table.setColumnCount(3)
            table.setHorizontalHeaderLabels(["Имя", "Телефон", "Дата рождения"])
            table.setColumnWidth(0, 318)
            table.setColumnWidth(1, 180)
            table.setColumnWidth(2, 180)
            table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        alph = [['А', 'Б'], ['В', 'Г'], ['Д', 'Е'], ['Ж', 'З', 'И', 'Й'], ['К', 'Л'], ['М', 'Н'], ['О', 'П'],
                ['Р', 'С'], ['Т', 'У'], ['Ф', 'Х'], ['Ц', 'Ч', 'Ш', 'Щ'], ['Ъ', 'Ы', 'Ь', 'Э'], ['Ю', 'Я']]
        new_list = []
        for i in alph:
            new_list.append(get_list(list_users, i))

        for i_t in range(len(tables) - 1):
            for i in range(len(new_list)):
                if i_t == i and (True if new_list[i] else False):
                    tables[i_t].setRowCount(len(new_list[i]))  # init number of rows
                    for j in range(len(new_list[i])):
                        tables[i_t].setItem(j, 0, QTableWidgetItem(new_list[i][j][0]))
                        tables[i_t].setItem(j, 1, QTableWidgetItem(new_list[i][j][1]))
                        tables[i_t].setItem(j, 2, QTableWidgetItem(str(new_list[i][j][2])))
                    # tables[i_t].resizeColumnsToContents()

        # actions when buttons clicked
        self.ExitButton.clicked.connect(self.clicked_exit)
        self.AddButton.clicked.connect(self.clicked_add)
        self.EditButton.clicked.connect(self.clicked_edit)
        self.DelButton.clicked.connect(self.clicked_del)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_exit(self):
        self.click_button(self.ExitButton.text())
        self.switch_window.emit("4 -> 1")
        with open('data.pickle', 'wb') as f:
            pickle.dump(['', ''], f)

    def clicked_add(self):
        self.click_button(self.AddButton.text())
        self.switch_window.emit("4 -> add")

    def clicked_edit(self):
        self.click_button(self.EditButton.text())
        self.switch_window.emit("4 -> edit")

    def clicked_del(self):
        self.click_button(self.DelButton.text())
        self.switch_window.emit("4 -> del")


class Controller:
    def __init__(self, user, list_users):
        self.user = user
        self.list_users = list_users

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
            self.form4 = Main_Win(self.list_users)
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
            self.form4 = Main_Win(self.list_users)
            self.form4.UserButton.setText(user)
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
        if text == "4":
            self.form4 = Main_Win(self.list_users)
            self.form4.UserButton.setText(self.user)
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
        if text == "4 -> 1":
            self.form4.close()
            self.form1 = En_Window()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
        if text == "4 -> add":
            self.form_add = Add_Window()
            self.form_add.switch_window.connect(self.select_forms)
            self.form_add.show()
        if text == "4 -> edit":
            self.form_edit = Edit_Window()
            self.form_edit.switch_window.connect(self.select_forms)
            self.form_edit.show()
        if text == "4 -> del":
            self.form_del = Del_Window()
            self.form_del.switch_window.connect(self.select_forms)
            self.form_del.show()
        if text == "add -> 4":
            self.form_add.close()
        if text == "edit -> 4":
            self.form_edit.close()
        if text == "del -> 4":
            self.form_del.close()


def get_list(listik, chars):
    res = []
    for char in chars:
        for i in range(len(listik)):
            if listik[i][0].startswith(char):
                res.append(listik[i])
    return res

def application():
    # DB
    conn = mariadb.connect(user='root', password='root', host='localhost', port=3306, database="DB_users")
    cur = conn.cursor()
    list_users = fuctions_db.work_with_DB_users(cur, "SELECT * FROM db_users.users")

    app = QApplication(sys.argv)
    # load last saved user
    with open('data.pickle', 'rb') as f:
        User_Pas = pickle.load(f)
    controller = Controller(User_Pas[0], list_users)
    # check user -> form1 (user==false) or form4 (user==true)
    if True if User_Pas[0] and User_Pas[1] else False:
        controller.select_forms("4")
    else:
        controller.select_forms("1")
    sys.exit(app.exec_())

    conn.close()


if __name__ == '__main__':
    print_hi('PyCharm')
    application()

