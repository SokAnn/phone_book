# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\any12\PycharmProjects\phone_book\en_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
