from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import QDate
from functions_db import formating_date
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.RepeatlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.RepeatlineEdit.setObjectName("RepeatlineEdit")
        self.gridLayout.addWidget(self.RepeatlineEdit, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OkPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OkPushButton.setObjectName("OkPushButton")
        self.horizontalLayout.addWidget(self.OkPushButton)
        self.CancelPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CancelPushButton.setObjectName("CancelPushButton")
        self.horizontalLayout.addWidget(self.CancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.NamelineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.NamelineEdit.setObjectName("NamelineEdit")
        self.gridLayout.addWidget(self.NamelineEdit, 0, 0, 1, 1)
        self.PasswordlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PasswordlineEdit.setObjectName("PasswordlineEdit")
        self.gridLayout.addWidget(self.PasswordlineEdit, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DatelineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DatelineEdit.setObjectName("DatelineEdit")
        self.horizontalLayout_2.addWidget(self.DatelineEdit)
        self.DateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.DateEdit.setCalendarPopup(True)
        self.DateEdit.setObjectName("DateEdit")
        self.horizontalLayout_2.addWidget(self.DateEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OkPushButton.setText(_translate("MainWindow", "PushButton"))
        self.CancelPushButton.setText(_translate("MainWindow", "PushButton"))


class Reg_Window(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, list_logs, conn, cur):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.list_logs = list_logs
        self.conn = conn
        self.cur = cur
        self.widgets_adjust()
        self.setWindowTitle("??????????????????????")
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
        self.NamelineEdit.setPlaceholderText("?????? ????????????????????????")
        self.NamelineEdit.setStyleSheet("font-size: 12px;")
        # init PasswordlineEdit parameters
        self.PasswordlineEdit.setMaximumHeight(30)
        self.PasswordlineEdit.setMinimumHeight(30)
        self.PasswordlineEdit.setMaximumWidth(380)
        self.PasswordlineEdit.setPlaceholderText("????????????")
        self.PasswordlineEdit.setStyleSheet("font-size: 12px;")
        # init RepeatlineEdit parameters
        self.RepeatlineEdit.setMaximumHeight(30)
        self.RepeatlineEdit.setMinimumHeight(30)
        self.RepeatlineEdit.setMaximumWidth(380)
        self.RepeatlineEdit.setPlaceholderText("?????????????????? ????????????")
        self.RepeatlineEdit.setStyleSheet("font-size: 12px;")
        # init DatelineEdit & DateEdit parameters
        self.DatelineEdit.setMaximumHeight(30)
        self.DatelineEdit.setMinimumHeight(30)
        self.DatelineEdit.setMaximumWidth(290)
        self.DatelineEdit.setPlaceholderText("???????? ????????????????")
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
        self.OkPushButton.setText("????")
        self.OkPushButton.setStyleSheet("border-radius: 8px;"
                                        "color: #000000;"
                                        "background: #d4d2d6;"
                                        "font-size: 12px;"
                                        "border-bottom: 3px solid #b9b5bd;")
        # init CancelPushButton parameters
        self.CancelPushButton.setMaximumHeight(30)
        self.CancelPushButton.setMinimumHeight(30)
        self.CancelPushButton.setMaximumWidth(120)
        self.CancelPushButton.setText("????????????")
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
                m.setWindowTitle("???????????? ????????????????????")  # set title
                m.setText("???????????? ???? ??????????????????!")
                m.setIcon(QMessageBox.Critical)  # set icon
                m.setStandardButtons(QMessageBox.Ok)
                m.exec_()
            else:
                check = 0
                for i in range(len(self.list_logs)):
                    if self.NamelineEdit.text() == self.list_logs[i][0]:
                        check = 1
                        break
                #     check
                if check == 1:
                    m = QMessageBox()  # init
                    m.setWindowTitle("????????????!")  # set title
                    m.setText("???????????????????????? ?? ?????????? ???????????? ?????? ????????!")
                    m.setIcon(QMessageBox.Critical)  # set icon
                    m.setStandardButtons(QMessageBox.Ok)
                    m.exec_()
                else:
                    if datetime.datetime.strptime(formating_date(self.DateEdit.text()),
                                                  "%Y-%m-%d") > datetime.datetime.now():
                        m = QMessageBox()  # init
                        m.setWindowTitle("???????????? ????????????????????")  # set title
                        m.setText("???????? ???????????????? ???? ????????????????!")
                        m.setIcon(QMessageBox.Critical)  # set icon
                        m.setStandardButtons(QMessageBox.Ok)
                        m.exec_()
                    else:
                        self.cur.execute("INSERT INTO db_users.logins VALUES (?, ?, ?)",
                                         (self.NamelineEdit.text(), self.PasswordlineEdit.text(),
                                          formating_date(self.DatelineEdit.text())))
                        self.conn.commit()
                        self.switch_window.emit("3 -> 4")
        else:
            m = QMessageBox()  # init
            m.setWindowTitle("???????????? ????????????????????")  # set title
            m.setText("???? ?????? ???????? ??????????????????!")
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
        self.switch_window.emit("3 -> 1")
