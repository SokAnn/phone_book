from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AddresslineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.AddresslineEdit.setObjectName("AddresslineEdit")
        self.verticalLayout.addWidget(self.AddresslineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ChangePasswordPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ChangePasswordPushButton.setObjectName("ChangePasswordPushButton")
        self.horizontalLayout.addWidget(self.ChangePasswordPushButton)
        self.CancelPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CancelPushButton.setObjectName("CancelPushButton")
        self.horizontalLayout.addWidget(self.CancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ChangePasswordPushButton.setText(_translate("MainWindow", "PushButton"))
        self.CancelPushButton.setText(_translate("MainWindow", "PushButton"))


class Pas_Window(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()
        self.setWindowTitle("???????????????????????????? ????????????")
        self.setMinimumHeight(270)
        self.setMaximumHeight(270)
        self.setMinimumWidth(320)
        self.setMaximumWidth(320)

    def widgets_adjust(self):
        # init AddresslineEdit parameters
        self.AddresslineEdit.setMinimumHeight(30)
        self.AddresslineEdit.setPlaceholderText("?????????? ?????????????????????? ??????????")
        self.AddresslineEdit.setStyleSheet("font-size: 12px;")
        # init ChangePasswordPushButton parameters
        self.ChangePasswordPushButton.setMinimumHeight(30)
        self.ChangePasswordPushButton.setMinimumWidth(60)
        self.ChangePasswordPushButton.setText("?????????????? ????????????")
        self.ChangePasswordPushButton.setStyleSheet("border-radius: 8px;"
                                                    "color: #000000;"
                                                    "background: #d4d2d6;"
                                                    "font-size: 12px;"
                                                    "border-bottom: 3px solid #b9b5bd;")
        # init CancelPushButton parameters
        self.CancelPushButton.setMinimumHeight(30)
        self.CancelPushButton.setMinimumWidth(60)
        self.CancelPushButton.setText("????????????")
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
            m.setWindowTitle("???????????? ????????????????????")  # set title
            m.setText("???????? '?????????? ?????????????????????? ??????????' ???? ??????????????????!")
            m.setIcon(QMessageBox.Critical)  # set icon
            m.setStandardButtons(QMessageBox.Ok)
            m.exec_()

    def clicked_c_b(self):
        self.click_button(self.CancelPushButton.text())
        self.AddresslineEdit.clear()
