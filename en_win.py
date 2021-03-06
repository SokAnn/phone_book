from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
import pickle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 299, 289))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.NamelineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.NamelineEdit.setObjectName("NamelineEdit")
        self.verticalLayout.addWidget(self.NamelineEdit)
        self.PasswordlineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.PasswordlineEdit.setObjectName("PasswordlineEdit")
        self.verticalLayout.addWidget(self.PasswordlineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EntranceButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.EntranceButton.setObjectName("EntranceButton")
        self.horizontalLayout.addWidget(self.EntranceButton)
        self.RegistrationButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.RegistrationButton.setObjectName("RegistrationButton")
        self.horizontalLayout.addWidget(self.RegistrationButton)
        self.CancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RememberCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.RememberCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RememberCheckBox.setObjectName("RememberCheckBox")
        self.verticalLayout_2.addWidget(self.RememberCheckBox)
        self.ShowCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.ShowCheckBox.setObjectName("ShowCheckBox")
        self.verticalLayout_2.addWidget(self.ShowCheckBox)
        self.ForgotPassButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ForgotPassButton.setObjectName("ForgotPassButton")
        self.verticalLayout_2.addWidget(self.ForgotPassButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EntranceButton.setText(_translate("MainWindow", "PushButton"))
        self.RegistrationButton.setText(_translate("MainWindow", "PushButton"))
        self.CancelButton.setText(_translate("MainWindow", "PushButton"))
        self.RememberCheckBox.setText(_translate("MainWindow", "CheckBox"))
        self.ShowCheckBox.setText(_translate("MainWindow", "CheckBox"))
        self.ForgotPassButton.setText(_translate("MainWindow", "PushButton"))


# entrance window
class En_Window(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, list_logs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.list_logs = list_logs
        self.widgets_adjust()
        self.setWindowTitle("???????? ?? ??????????????")
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
        self.NamelineEdit.setPlaceholderText("?????? ????????????????????????")
        self.NamelineEdit.setStyleSheet("font-size: 12px;")
        # init PasswordlineEdit parameters
        self.PasswordlineEdit.setMaximumHeight(30)
        self.PasswordlineEdit.setMinimumHeight(30)
        self.PasswordlineEdit.setMinimumWidth(50)
        self.PasswordlineEdit.setPlaceholderText("????????????")
        self.PasswordlineEdit.setStyleSheet("font-size: 12px;")
        # init EntranceButton parameters
        self.EntranceButton.setMinimumHeight(30)
        self.EntranceButton.setMinimumWidth(60)
        self.EntranceButton.setText("??????????")
        self.EntranceButton.setStyleSheet("border-radius: 8px;"
                                          "color: #000000;"
                                          "background: #66ff66;"
                                          "font-size: 12px;"
                                          "border-bottom: 3px solid #00cc00;")
        # init RegistrationButton parameters
        self.RegistrationButton.setMinimumHeight(30)
        self.RegistrationButton.setMinimumWidth(60)
        self.RegistrationButton.setText("??????????????????????")
        self.RegistrationButton.setStyleSheet("border-radius: 8px;"
                                              "color: #000000;"
                                              "background: #d4d2d6;"
                                              "font-size: 12px;"
                                              "border-bottom: 3px solid #b9b5bd;")
        # init CancelButton parameters
        self.CancelButton.setMinimumHeight(30)
        self.CancelButton.setMinimumWidth(60)
        self.CancelButton.setText("????????????")
        self.CancelButton.setStyleSheet("border-radius: 8px;"
                                        "color: #000000;"
                                        "background: #ff5757;"
                                        "font-size: 12px;"
                                        "border-bottom: 3px solid #ff2424;")
        # init RememberCheckBox parameters
        self.RememberCheckBox.setMaximumHeight(30)
        self.RememberCheckBox.setMinimumHeight(30)
        self.RememberCheckBox.setText("?????????????????? ????????")
        self.RememberCheckBox.setStyleSheet("font-size: 12px;")
        # init ShowCheckBox parameters
        self.ShowCheckBox.setMaximumHeight(30)
        self.ShowCheckBox.setMinimumHeight(30)
        self.ShowCheckBox.setText("???????????????? ????????????")
        self.ShowCheckBox.setStyleSheet("font-size: 12px;")
        # init ForgotPassButton parameters
        self.ForgotPassButton.setText("???????????? ?????????????")
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
        # save user in system
        if self.RememberCheckBox.isChecked():
            with open('data.pickle', 'wb') as f:
                pickle.dump([self.NamelineEdit.text(), self.PasswordlineEdit.text()], f)
                # print([self.NamelineEdit.text(), self.PasswordlineEdit.text()])

        if True if self.NamelineEdit.text() and self.PasswordlineEdit.text() else False:
            check = 0
            for i in range(len(self.list_logs)):
                if self.NamelineEdit.text() == self.list_logs[i][0] and self.PasswordlineEdit.text() == self.list_logs[i][1]:
                    # print(self.list_logs[i])
                    check = 1
                    break
            # print(check)
            if check == 1:
                self.switch_window.emit("1 -> 4")
            else:
                m = QMessageBox()  # init
                m.setWindowTitle("???????????? 404")  # set title
                m.setText("???????????????????????? ?? ???????????? ?????????????? ???? ????????????!")
                m.setIcon(QMessageBox.Critical)  # set icon
                m.setStandardButtons(QMessageBox.Ok)
                m.exec_()
        else:
            m = QMessageBox()  # init
            m.setWindowTitle("????????????!")  # set title
            m.setText("???????????????????? ?????????????????? ?????? ???????? ?????? ??????????????????????!")
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
            self.setWindowTitle("???????? ?? ??????????????")

    def clicked_sh_chb(self):
        if self.ShowCheckBox.isChecked():
            self.setWindowTitle('QCheckBox -> show')
            self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(0))
        else:
            self.setWindowTitle("???????? ?? ??????????????")
            self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode(2))

    def clicked_f_b(self):
        self.click_button(self.ForgotPassButton.text())
        self.ForgotPassButton.setStyleSheet("text-decoration: underline;"
                                            "background-color: rgba(255,255,255,0);"
                                            "border:none;"
                                            "color: fuchsia;")
        self.switch_window.emit("1 -> 2")
