# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assets/Account_Registration_successful.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Account_Registration_successful(object):
    def setupUi(self, Account_Registration_successful):
        Account_Registration_successful.setObjectName("Account_Registration_successful")
        Account_Registration_successful.resize(1270, 590)
        Account_Registration_successful.setMinimumSize(QtCore.QSize(1270, 590))
        Account_Registration_successful.setMaximumSize(QtCore.QSize(1270, 590))
        Account_Registration_successful.setStyleSheet("#Account_Registration_successful{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.02, y2:0.0340909, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(0, 0, 0, 199), stop:0.505 rgba(28, 28, 28, 255), stop:1 rgba(53, 53, 53, 255));\n"
"}\n"
"#topframe{\n"
"background-color: qconicalgradient(cx:0.000472637, cy:0, angle:227.8, stop:0 rgba(30, 0, 255, 255), stop:0.375 rgba(0, 195, 255, 252), stop:0.423533 rgba(37, 0, 255, 255), stop:0.45 rgba(0, 130, 255, 255), stop:0.477581 rgba(0, 56, 255, 252), stop:0.518717 rgba(71, 171, 255, 255), stop:0.542289 rgba(71, 171, 255, 255), stop:0.547264 rgba(68, 134, 249, 255), stop:0.55 rgba(0, 74, 255, 255), stop:0.552239 rgba(21, 93, 243, 255), stop:0.57754 rgba(102, 0, 255, 255), stop:0.625 rgba(0, 185, 255, 247), stop:1 rgba(255, 255, 0, 69));\n"
"border:none;\n"
"}\n"
"#bottomframe{\n"
"background-color: qlineargradient(spread:pad, x1:0.025, y1:0.892545, x2:0.0199005, y2:0, stop:0 rgba(244, 244, 244, 255), stop:0.495 rgba(218, 212, 186, 230), stop:0.505 rgba(236, 224, 224, 255), stop:1 rgba(253, 246, 246, 255));\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"border:2px solid #aaff00;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"}\n"
"QGroupBox{\n"
"background:#c2c7cf;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"    text-decoration: underline;\n"
"}\n"
"#Back_btn{\n"
"background:#aaff00;\n"
"}\n"
"QLineEdit{\n"
"border-radius:15px;\n"
"border-bottom:3px solid #aaff00;\n"
"}")
        self.bottomframe = QtWidgets.QFrame(Account_Registration_successful)
        self.bottomframe.setGeometry(QtCore.QRect(10, 520, 1251, 61))
        self.bottomframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomframe.setObjectName("bottomframe")
        self.label = QtWidgets.QLabel(self.bottomframe)
        self.label.setGeometry(QtCore.QRect(490, 10, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bottomframe)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 381, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Account_Registration_successful)
        self.groupBox.setGeometry(QtCore.QRect(410, 210, 561, 201))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 511, 21))
        self.label_4.setObjectName("label_4")
        self.Login_btn = QtWidgets.QPushButton(self.groupBox)
        self.Login_btn.setGeometry(QtCore.QRect(220, 130, 151, 31))
        self.Login_btn.setObjectName("Login_btn")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(140, 70, 311, 21))
        self.label_5.setObjectName("label_5")
        self.Back_btn = QtWidgets.QPushButton(Account_Registration_successful)
        self.Back_btn.setGeometry(QtCore.QRect(472, 452, 161, 41))
        self.Back_btn.setObjectName("Back_btn")
        self.sideframe = QtWidgets.QFrame(Account_Registration_successful)
        self.sideframe.setGeometry(QtCore.QRect(9, 119, 141, 401))
        self.sideframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideframe.setObjectName("sideframe")
        self.topframe = QtWidgets.QPushButton(Account_Registration_successful)
        self.topframe.setGeometry(QtCore.QRect(10, 10, 1251, 101))
        self.topframe.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets\\Images/Bank-Management-System.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topframe.setIcon(icon)
        self.topframe.setIconSize(QtCore.QSize(1300, 520))
        self.topframe.setObjectName("topframe")

        self.retranslateUi(Account_Registration_successful)
        QtCore.QMetaObject.connectSlotsByName(Account_Registration_successful)

    def retranslateUi(self, Account_Registration_successful):
        _translate = QtCore.QCoreApplication.translate
        Account_Registration_successful.setWindowTitle(_translate("Account_Registration_successful", "Bank Management System"))
        self.label.setText(_translate("Account_Registration_successful", "Project by: Ankit Choudhary "))
        self.label_2.setText(_translate("Account_Registration_successful", "ID: 19CS014   Anand International College of Engineering, Jaipur"))
        self.groupBox.setTitle(_translate("Account_Registration_successful", "                 :: Account Registration successful ::                  "))
        self.label_4.setText(_translate("Account_Registration_successful", "Please wait till administrator validate yoour account, then you can login to you account."))
        self.Login_btn.setText(_translate("Account_Registration_successful", "LOGIN"))
        self.label_5.setText(_translate("Account_Registration_successful", "If you are already register, or active user then please."))
        self.Back_btn.setText(_translate("Account_Registration_successful", "< Back to home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account_Registration_successful = QtWidgets.QWidget()
    ui = Ui_Account_Registration_successful()
    ui.setupUi(Account_Registration_successful)
    Account_Registration_successful.show()
    sys.exit(app.exec_())
