from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import QDate
from functions_db import formating_date
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 241, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NamelineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.NamelineEdit.setObjectName("NamelineEdit")
        self.verticalLayout.addWidget(self.NamelineEdit)
        self.TelephonelineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.TelephonelineEdit.setObjectName("TelephonelineEdit")
        self.verticalLayout.addWidget(self.TelephonelineEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OkpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OkpushButton.setObjectName("OkpushButton")
        self.horizontalLayout.addWidget(self.OkpushButton)
        self.CancelpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CancelpushButton.setObjectName("CancelpushButton")
        self.horizontalLayout.addWidget(self.CancelpushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OkpushButton.setText(_translate("MainWindow", "PushButton"))
        self.CancelpushButton.setText(_translate("MainWindow", "PushButton"))

class Add_Window(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, list_users, conn, cur):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.list_users = list_users
        self.conn = conn
        self.cur = cur
        self.widgets_adjust()
        self.setWindowTitle("???????????????????? ????????????????")
        self.setMinimumHeight(250)
        self.setMaximumHeight(250)
        self.setMinimumWidth(290)
        self.setMaximumWidth(290)

    def widgets_adjust(self):
        # init NamelineEdit parameters
        self.NamelineEdit.setPlaceholderText("?????? ????????????????")
        self.NamelineEdit.setStyleSheet("font-size: 12px;")
        # init TelephonelineEdit parameters
        self.TelephonelineEdit.setPlaceholderText("?????????????? ????????????????")
        self.TelephonelineEdit.setStyleSheet("font-size: 12px;")
        # init dateEdit parameters
        self.dateEdit.setStyleSheet("font-size: 12px;")
        self.dateEdit.setDate(QDate.currentDate())
        # init OkpushButton parameters
        self.OkpushButton.setText("????")
        self.OkpushButton.setMinimumHeight(30)
        self.OkpushButton.setMinimumWidth(60)
        self.OkpushButton.setStyleSheet("border-radius: 8px;"
                                        "color: #000000;"
                                        "background: #d4d2d6;"
                                        "font-size: 12px;"
                                        "border-bottom: 3px solid #b9b5bd;")
        # init CancelpushButton parameters
        self.CancelpushButton.setText("????????????")
        self.CancelpushButton.setMinimumHeight(30)
        self.CancelpushButton.setMinimumWidth(60)
        self.CancelpushButton.setStyleSheet("border-radius: 8px;"
                                            "color: #000000;"
                                            "background: #d4d2d6;"
                                            "font-size: 12px;"
                                            "border-bottom: 3px solid #b9b5bd;")
        # actions when buttons & checkbox clicked
        self.OkpushButton.clicked.connect(self.clicked_ok_b)
        self.CancelpushButton.clicked.connect(self.clicked_c_b)

    def click_button(self, label):
        print('The \"', label, '\" button is pressed!')

    def clicked_ok_b(self):
        self.click_button(self.OkpushButton.text())
        if self.NamelineEdit.text() and self.TelephonelineEdit.text() and self.dateEdit.text():
            check = 0
            for i in range(len(self.list_users)):
                if self.NamelineEdit.text() == self.list_users[i][0]:
                    check = 1
                    break
            #     check
            if check == 1:
                m = QMessageBox()  # init
                m.setWindowTitle("????????????!")  # set title
                m.setText("?????????? ?????????????? ?? ???????????????????? ?????????? ?????? ????????!")
                m.setIcon(QMessageBox.Critical)  # set icon
                m.setStandardButtons(QMessageBox.Ok)
                m.exec_()
            else:
                if datetime.datetime.strptime(formating_date(self.dateEdit.text()), "%Y-%m-%d") > datetime.datetime.now():
                    m = QMessageBox()  # init
                    m.setWindowTitle("???????????? ????????????????????")  # set title
                    m.setText("???????? ???????????????? ???? ????????????????!")
                    m.setIcon(QMessageBox.Critical)  # set icon
                    m.setStandardButtons(QMessageBox.Ok)
                    m.exec_()
                else:
                    self.cur.execute("INSERT INTO db_users.users VALUES (?, ?, ?)",
                                     (self.NamelineEdit.text(), self.TelephonelineEdit.text(),
                                      formating_date(self.dateEdit.text())))
                    self.conn.commit()
                    self.switch_window.emit("add -> 4")
        else:
            m = QMessageBox()  # init
            m.setWindowTitle("???????????? ????????????????????")  # set title
            m.setText("???????????????????? ?????????????????? ?????? ????????!")
            m.setIcon(QMessageBox.Critical)  # set icon
            m.setStandardButtons(QMessageBox.Ok)
            m.exec_()

    def clicked_c_b(self):
        self.click_button(self.CancelpushButton.text())
        self.NamelineEdit.clear()
        self.TelephonelineEdit.clear()
        self.dateEdit.setDate(QDate.currentDate())
        self.switch_window.emit("add -> 4")

