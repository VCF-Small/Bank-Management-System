# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assets/Change_Password.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_Password(object):
    def setupUi(self, Change_Password):
        Change_Password.setObjectName("Change_Password")
        Change_Password.resize(1270, 590)
        Change_Password.setMinimumSize(QtCore.QSize(1270, 590))
        Change_Password.setMaximumSize(QtCore.QSize(1270, 590))
        Change_Password.setStyleSheet("#Change_Password{\n"
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
"#frame{\n"
"background:#d4d4d4;\n"
"}\n"
"Line{\n"
"background:rgb(6, 6, 6)\n"
"}\n"
"#label_12{\n"
"background:#000000;\n"
"color:white;\n"
"}\n"
"QGroupBox{\n"
"background:white;\n"
"}")
        self.bottomframe = QtWidgets.QFrame(Change_Password)
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
        self.sideframe = QtWidgets.QFrame(Change_Password)
        self.sideframe.setGeometry(QtCore.QRect(9, 119, 181, 401))
        self.sideframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideframe.setObjectName("sideframe")
        self.Admin_Home_btn_2 = QtWidgets.QPushButton(self.sideframe)
        self.Admin_Home_btn_2.setGeometry(QtCore.QRect(8, 189, 171, 31))
        self.Admin_Home_btn_2.setObjectName("Admin_Home_btn_2")
        self.User_Details_btn_2 = QtWidgets.QPushButton(self.sideframe)
        self.User_Details_btn_2.setGeometry(QtCore.QRect(7, 230, 171, 31))
        self.User_Details_btn_2.setObjectName("User_Details_btn_2")
        self.Log_out_btn_2 = QtWidgets.QPushButton(self.sideframe)
        self.Log_out_btn_2.setGeometry(QtCore.QRect(8, 270, 161, 31))
        self.Log_out_btn_2.setObjectName("Log_out_btn_2")
        self.label_12 = QtWidgets.QLabel(self.sideframe)
        self.label_12.setGeometry(QtCore.QRect(10, 165, 171, 21))
        self.label_12.setObjectName("label_12")
        self.User_Picture = QtWidgets.QLabel(self.sideframe)
        self.User_Picture.setGeometry(QtCore.QRect(10, 10, 161, 141))
        self.User_Picture.setText("")
        self.User_Picture.setObjectName("User_Picture")
        self.topframe = QtWidgets.QPushButton(Change_Password)
        self.topframe.setGeometry(QtCore.QRect(10, 10, 1251, 101))
        self.topframe.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets\\Images/Bank-Management-System.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topframe.setIcon(icon)
        self.topframe.setIconSize(QtCore.QSize(1300, 520))
        self.topframe.setObjectName("topframe")
        self.groupBox = QtWidgets.QGroupBox(Change_Password)
        self.groupBox.setGeometry(QtCore.QRect(440, 250, 501, 171))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_3.setObjectName("label_3")
        self.New_Password = QtWidgets.QLineEdit(self.groupBox)
        self.New_Password.setGeometry(QtCore.QRect(130, 50, 231, 22))
        self.New_Password.setObjectName("New_Password")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.label_4.setObjectName("label_4")
        self.Confirm_Password = QtWidgets.QLineEdit(self.groupBox)
        self.Confirm_Password.setGeometry(QtCore.QRect(140, 90, 231, 22))
        self.Confirm_Password.setObjectName("Confirm_Password")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(290, 127, 191, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Change_Password)
        self.textEdit.setGeometry(QtCore.QRect(350, 130, 701, 101))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Change_Password)
        QtCore.QMetaObject.connectSlotsByName(Change_Password)

    def retranslateUi(self, Change_Password):
        _translate = QtCore.QCoreApplication.translate
        Change_Password.setWindowTitle(_translate("Change_Password", "Bank Management System"))
        self.label.setText(_translate("Change_Password", "Project by: Ankit Choudhary "))
        self.label_2.setText(_translate("Change_Password", "ID: 19CS014   Anand International College of Engineering, Jaipur"))
        self.Admin_Home_btn_2.setText(_translate("Change_Password", "Change Password"))
        self.User_Details_btn_2.setText(_translate("Change_Password", "Change PIN No."))
        self.Log_out_btn_2.setText(_translate("Change_Password", "Sign/Log out"))
        self.label_12.setText(_translate("Change_Password", "Security Settings"))
        self.groupBox.setTitle(_translate("Change_Password", " :: Change Password :: "))
        self.label_3.setText(_translate("Change_Password", "New Password : "))
        self.label_4.setText(_translate("Change_Password", "Confirm Password :"))
        self.pushButton.setText(_translate("Change_Password", "Change Password"))
        self.textEdit.setHtml(_translate("Change_Password", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Change Password</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you feel that you have a weaker strength password, then plese change it. We recommend to change your password in every 45 days to make it secure.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Password Change guidline.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Change_Password = QtWidgets.QWidget()
    ui = Ui_Change_Password()
    ui.setupUi(Change_Password)
    Change_Password.show()
    sys.exit(app.exec_())
