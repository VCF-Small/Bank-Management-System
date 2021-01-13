# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assets/User_Profile_Detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User_Profile(object):
    def setupUi(self, User_Profile):
        User_Profile.setObjectName("User_Profile")
        User_Profile.resize(1270, 590)
        User_Profile.setMinimumSize(QtCore.QSize(1270, 590))
        User_Profile.setMaximumSize(QtCore.QSize(1270, 590))
        User_Profile.setStyleSheet("#User_Profile{\n"
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
"background:#aaff00;\n"
"border:2px solid #aaff00;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"}\n"
"#Back_btn{\n"
"background:#aaff00;\n"
"}\n"
"#Account_Information_btn, #Users_Details_btn{\n"
"background:none;\n"
"border:none;\n"
"color:blue;\n"
"text-decoration: underline;\n"
"}\n"
"#frame{\n"
"background:#d4d4d4;\n"
"}\n"
"Line{\n"
"background:rgb(6, 6, 6)\n"
"}\n"
"#text{\n"
"color:white;\n"
"    font: 75 14pt \"MS Sans Serif\";\n"
"}\n"
"#Transaction_History{\n"
"font: 12pt \"MS Sans Serif\";\n"
"border:1px solid black;\n"
"}")
        self.bottomframe = QtWidgets.QFrame(User_Profile)
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
        self.sideframe = QtWidgets.QFrame(User_Profile)
        self.sideframe.setGeometry(QtCore.QRect(9, 119, 151, 401))
        self.sideframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideframe.setObjectName("sideframe")
        self.Admin_Home_btn = QtWidgets.QPushButton(self.sideframe)
        self.Admin_Home_btn.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.Admin_Home_btn.setObjectName("Admin_Home_btn")
        self.User_Details_btn = QtWidgets.QPushButton(self.sideframe)
        self.User_Details_btn.setGeometry(QtCore.QRect(9, 112, 141, 31))
        self.User_Details_btn.setObjectName("User_Details_btn")
        self.Account_Details_btn = QtWidgets.QPushButton(self.sideframe)
        self.Account_Details_btn.setGeometry(QtCore.QRect(11, 162, 141, 31))
        self.Account_Details_btn.setObjectName("Account_Details_btn")
        self.Log_out_btn = QtWidgets.QPushButton(self.sideframe)
        self.Log_out_btn.setGeometry(QtCore.QRect(10, 212, 141, 31))
        self.Log_out_btn.setObjectName("Log_out_btn")
        self.topframe = QtWidgets.QPushButton(User_Profile)
        self.topframe.setGeometry(QtCore.QRect(10, 10, 1251, 101))
        self.topframe.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets\\Images/Bank-Management-System.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topframe.setIcon(icon)
        self.topframe.setIconSize(QtCore.QSize(1300, 520))
        self.topframe.setObjectName("topframe")
        self.scrollArea = QtWidgets.QScrollArea(User_Profile)
        self.scrollArea.setGeometry(QtCore.QRect(170, 160, 1061, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1059, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 0, 171, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 141, 16))
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(-3, 50, 174, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(27, 57, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 146, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 172, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 199, 141, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 229, 141, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(20, 256, 141, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 284, 151, 16))
        self.label_11.setObjectName("label_11")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 77, 174, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 140, 174, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 166, 174, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 193, 174, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(0, 220, 174, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(-2, 250, 174, 3))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(0, 278, 174, 3))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.Account_Holder_Name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Account_Holder_Name.setGeometry(QtCore.QRect(174, 3, 381, 21))
        self.Account_Holder_Name.setText("")
        self.Account_Holder_Name.setObjectName("Account_Holder_Name")
        self.Email_ID = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Email_ID.setGeometry(QtCore.QRect(220, 23, 311, 21))
        self.Email_ID.setText("")
        self.Email_ID.setObjectName("Email_ID")
        self.Email_ID_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Email_ID_2.setGeometry(QtCore.QRect(175, 23, 51, 21))
        self.Email_ID_2.setObjectName("Email_ID_2")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(170, 50, 680, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setGeometry(QtCore.QRect(170, 77, 680, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_11.setGeometry(QtCore.QRect(170, 140, 680, 3))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_12.setGeometry(QtCore.QRect(170, 166, 890, 3))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_13.setGeometry(QtCore.QRect(170, 193, 890, 3))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_14.setGeometry(QtCore.QRect(170, 220, 890, 3))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_29 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_29.setGeometry(QtCore.QRect(170, 250, 890, 3))
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_30.setGeometry(QtCore.QRect(170, 278, 890, 3))
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.Email_ID_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Email_ID_5.setGeometry(QtCore.QRect(175, 56, 51, 21))
        self.Email_ID_5.setObjectName("Email_ID_5")
        self.Phone_Number = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Phone_Number.setGeometry(QtCore.QRect(225, 56, 311, 21))
        self.Phone_Number.setText("")
        self.Phone_Number.setObjectName("Phone_Number")
        self.Address = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Address.setGeometry(QtCore.QRect(190, 82, 311, 21))
        self.Address.setText("")
        self.Address.setObjectName("Address")
        self.Email_ID_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Email_ID_8.setGeometry(QtCore.QRect(192, 104, 51, 21))
        self.Email_ID_8.setObjectName("Email_ID_8")
        self.City = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.City.setGeometry(QtCore.QRect(225, 105, 81, 21))
        self.City.setText("")
        self.City.setObjectName("City")
        self.Email_ID_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Email_ID_10.setGeometry(QtCore.QRect(320, 104, 51, 21))
        self.Email_ID_10.setObjectName("Email_ID_10")
        self.State = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.State.setGeometry(QtCore.QRect(366, 103, 81, 21))
        self.State.setText("")
        self.State.setObjectName("State")
        self.Email_ID_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Email_ID_12.setGeometry(QtCore.QRect(193, 118, 61, 21))
        self.Email_ID_12.setObjectName("Email_ID_12")
        self.Zip_Code = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Zip_Code.setGeometry(QtCore.QRect(260, 119, 91, 21))
        self.Zip_Code.setText("")
        self.Zip_Code.setObjectName("Zip_Code")
        self.Account_Number = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Account_Number.setGeometry(QtCore.QRect(175, 146, 381, 21))
        self.Account_Number.setText("")
        self.Account_Number.setObjectName("Account_Number")
        self.Current_Balance = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Current_Balance.setGeometry(QtCore.QRect(174, 170, 381, 21))
        self.Current_Balance.setText("")
        self.Current_Balance.setObjectName("Current_Balance")
        self.line_31 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_31.setGeometry(QtCore.QRect(850, 0, 3, 166))
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.User_Picture = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.User_Picture.setGeometry(QtCore.QRect(864, 5, 181, 151))
        self.User_Picture.setText("")
        self.User_Picture.setObjectName("User_Picture")
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setGeometry(QtCore.QRect(180, 197, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Transaction_History = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Transaction_History.setGeometry(QtCore.QRect(526, 197, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Transaction_History.setFont(font)
        self.Transaction_History.setObjectName("Transaction_History")
        self.Amount = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Amount.setGeometry(QtCore.QRect(182, 226, 181, 22))
        self.Amount.setObjectName("Amount")
        self.Date_of_Transfer = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.Date_of_Transfer.setGeometry(QtCore.QRect(185, 255, 141, 22))
        self.Date_of_Transfer.setObjectName("Date_of_Transfer")
        self.Transaction_Description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Transaction_Description.setGeometry(QtCore.QRect(176, 284, 301, 31))
        self.Transaction_Description.setObjectName("Transaction_Description")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.text = QtWidgets.QLabel(User_Profile)
        self.text.setGeometry(QtCore.QRect(550, 124, 151, 21))
        self.text.setObjectName("text")
        self.Back_btn = QtWidgets.QPushButton(User_Profile)
        self.Back_btn.setGeometry(QtCore.QRect(475, 485, 161, 31))
        self.Back_btn.setObjectName("Back_btn")
        self.Back_btn_2 = QtWidgets.QPushButton(User_Profile)
        self.Back_btn_2.setGeometry(QtCore.QRect(700, 485, 201, 31))
        self.Back_btn_2.setObjectName("Back_btn_2")

        self.retranslateUi(User_Profile)
        QtCore.QMetaObject.connectSlotsByName(User_Profile)

    def retranslateUi(self, User_Profile):
        _translate = QtCore.QCoreApplication.translate
        User_Profile.setWindowTitle(_translate("User_Profile", "Bank Management System"))
        self.label.setText(_translate("User_Profile", "Project by: Ankit Choudhary "))
        self.label_2.setText(_translate("User_Profile", "ID: 19CS014   Anand International College of Engineering, Jaipur"))
        self.Admin_Home_btn.setText(_translate("User_Profile", "Admin Home"))
        self.User_Details_btn.setText(_translate("User_Profile", "User Details"))
        self.Account_Details_btn.setText(_translate("User_Profile", "Account Details"))
        self.Log_out_btn.setText(_translate("User_Profile", "Sign/Log out"))
        self.label_3.setText(_translate("User_Profile", "Account Holder Name : "))
        self.label_4.setText(_translate("User_Profile", "Mobile Number : "))
        self.label_5.setText(_translate("User_Profile", "Full Address : "))
        self.label_6.setText(_translate("User_Profile", "Account Number : "))
        self.label_7.setText(_translate("User_Profile", "Current Balance :"))
        self.label_8.setText(_translate("User_Profile", "Transaction Type : "))
        self.label_9.setText(_translate("User_Profile", "Amount(Cr/Dr) :"))
        self.label_10.setText(_translate("User_Profile", "Date of Transfer :"))
        self.label_11.setText(_translate("User_Profile", "Transaction Description :"))
        self.Email_ID_2.setText(_translate("User_Profile", "Email : "))
        self.Email_ID_5.setText(_translate("User_Profile", "Phone : "))
        self.Email_ID_8.setText(_translate("User_Profile", "City : "))
        self.Email_ID_10.setText(_translate("User_Profile", "State : "))
        self.Email_ID_12.setText(_translate("User_Profile", "Zip Code : "))
        self.comboBox.setItemText(0, _translate("User_Profile", "--Select transaction type--"))
        self.comboBox.setItemText(1, _translate("User_Profile", "Credit"))
        self.comboBox.setItemText(2, _translate("User_Profile", "Debit"))
        self.Transaction_History.setText(_translate("User_Profile", "View Transaction History"))
        self.text.setText(_translate("User_Profile", "User Details"))
        self.Back_btn.setText(_translate("User_Profile", "< Back to home"))
        self.Back_btn_2.setText(_translate("User_Profile", "Proceed Transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User_Profile = QtWidgets.QWidget()
    ui = Ui_User_Profile()
    ui.setupUi(User_Profile)
    User_Profile.show()
    sys.exit(app.exec_())
