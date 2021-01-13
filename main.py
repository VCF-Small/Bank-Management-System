# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assets/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from os import close
from PyQt5.QtWidgets import (QTableWidget, QWidget, QPushButton, QLineEdit,QFileDialog, QInputDialog, QApplication)

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from AdminLoginForm import Ui_Admin_Login_Form
from Admin_Home import Ui_Admin_Home
from Account_Information import Ui_Account_Information
from User_Profile_Detail import Ui_User_Profile
from User_Details import Ui_User_Details
from Account_Transaction_Statement import Ui_Account_Statement
from User_Login_System import Ui_User_Login_System
from Pin_validate import Ui_Pin_Validate
from New_Account import Ui_New_Account
from User_Profile_Home import Ui_User_Profile_Home
from Account_Registration_sucessful import Ui_Account_Registration_successful
from Change_Account_PIN import Ui_Change_Account_PIN
from Change_Password import Ui_Change_Password

class Ui_Form(object):

    def loadTransaction(self,Account):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+Account+"'")
        result = cursor.fetchall()
        transaction = cursor.execute("SELECT * FROM `bank_transactions` WHERE `Account Number` = '"+Account+"'")
        transaction = cursor.fetchall()
        self.AccountStatementUi.Account_Details_table.setRowCount(0)
        if(len(transaction) > 0):
            for row_number, row_data in enumerate(transaction):
                row_data = list(row_data[1:])
                row_data.append(result[0][4])
                row_data = tuple(row_data)
                self.AccountStatementUi.Account_Details_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.AccountStatementUi.Account_Details_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            for row_number, row_data in enumerate(tuple(transaction)):
                self.AccountStatementUi.Account_Details_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.AccountStatementUi.Account_Details_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()


    def TransactionStatement(self):
        text, ok = QInputDialog.getText(self.Account_Information, 'Input Dialog',
                                        'Enter Account Number:')
        if( ok and text):
            Account = str(text)
            conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+Account+"'")
            result = cursor.fetchall()
            if(len(result) > 0):
                self.Account_Statement = QtWidgets.QWidget()
                self.AccountStatementUi = Ui_Account_Statement()
                self.AccountStatementUi.setupUi(self.Account_Statement)
                self.Account_Statement.show()
                self.Account_Information.hide()
                self.loadTransaction(Account)
                self.AccountStatementUi.Admin_Home_btn.clicked.connect(self.TSAdminHome)
                self.AccountStatementUi.Account_Details_btn.clicked.connect(self.TSAccountInformation)
                self.AccountStatementUi.User_Details_btn.clicked.connect(self.TSUserProfileDetails)
                self.AccountStatementUi.Log_out_btn.clicked.connect(self.TSHome)
            else:
                self.showMessageBox("Warning", "Account does not exits")
            conn.close()
        elif(ok and text == ""):
                self.showMessageBox("Warning", "Invalid Account Number")


    def User(self):
        self.User_Detail = QtWidgets.QWidget()
        self.UserDetailUi = Ui_User_Details()
        self.UserDetailUi.setupUi(self.User_Detail)
        self.User_Detail.show()
        self.Admin_Home.hide()
        self.UserDetailUi.Account_Details_btn.clicked.connect(self.UAccountInformation)
        self.UserDetailUi.Admin_Home_btn.clicked.connect(self.UAdminHome)
        self.UserDetailUi.Log_out_btn.clicked.connect(self.UHome)
        self.UserDetailUi.User_Details_btn.clicked.connect(self.UUserProfileDetails)
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users`")
        result = cursor.fetchall()
        self.UserDetailUi.User_Details_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            res = []
            res.append(result[row_number][0])
            res.append(result[row_number][1])
            res.append(result[row_number][6])
            res.append(result[row_number][7])
            res.append(result[row_number][15])
            res.append(result[row_number][4])
            self.UserDetailUi.User_Details_table.insertRow(row_number)
            for colum_number, data in enumerate(tuple(res)):
                self.UserDetailUi.User_Details_table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def loadUserProfileDetail(self, Acc_No):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+Acc_No+"'")
        result = cursor.fetchall()
        result = result[0]
        self.UserProfileDetailsUi.Account_Holder_Name.setText(str(result[0]))
        self.UserProfileDetailsUi.Email_ID.setText(str(result[6]))
        self.UserProfileDetailsUi.Phone_Number.setText(str(result[7]))
        self.UserProfileDetailsUi.Address.setText(str(result[10]))
        self.UserProfileDetailsUi.City.setText(str(result[11]))
        self.UserProfileDetailsUi.State.setText(str(result[12]))
        self.UserProfileDetailsUi.Zip_Code.setText(str(result[13]))
        self.UserProfileDetailsUi.Account_Number.setNum(result[1])
        self.UserProfileDetailsUi.Current_Balance.setNum(result[2])
        with open("img.jpg", "wb") as f:
            f.write(result[16])
        f.close()

        self.UserProfileDetailsUi.User_Picture.setAutoFillBackground(False)
        self.UserProfileDetailsUi.User_Picture.setText("")
        image = QtGui.QPixmap("img.jpg")
        image = image.scaled(self.UserProfileDetailsUi.User_Picture.width(), self.UserProfileDetailsUi.User_Picture.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.UserProfileDetailsUi.User_Picture.setPixmap(image)
        

        conn.close()

    def TSUserProfileDetails(self):
        self.UserProfileDetails()
        self.Account_Statement.hide()

    def AIUserProfileDetails(self):
        self.UserProfileDetails()
        self.Account_Information.hide()

    def UUserProfileDetails(self):
        self.UserProfileDetails()
        self.User_Detail.hide()

    def UPDTransactionStatement(self):
        self.TransactionStatement()
        self.User_Profile_Detail.hide()

    def UserProfileDetails(self):
        text, ok = QInputDialog.getText(self.Admin_Home, 'Input Dialog',
                                        'Enter Account Number:')
        if( ok and text != ""):
            Account = str(text)
            conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+Account+"'")
            result = cursor.fetchall()
            if(len(result) > 0):
                self.User_Profile_Detail = QtWidgets.QWidget()
                self.UserProfileDetailsUi = Ui_User_Profile()
                self.UserProfileDetailsUi.setupUi(self.User_Profile_Detail)
                self.User_Profile_Detail.show()
                self.loadUserProfileDetail(Account)
                self.Admin_Home.hide()
                self.UserProfileDetailsUi.Transaction_History.clicked.connect(self.UPDTransactionStatement)
                self.UserProfileDetailsUi.Log_out_btn.clicked.connect(self.UPHome)
                self.UserProfileDetailsUi.Account_Details_btn.clicked.connect(self.UPAccountInformation)
                self.UserProfileDetailsUi.User_Details_btn.clicked.connect(self.UserProfileDetails)
                self.UserProfileDetailsUi.Admin_Home_btn.clicked.connect(self.UPAdminHome)
                self.UserProfileDetailsUi.Back_btn.clicked.connect(self.UPAdminHome)
                self.UserProfileDetailsUi.Back_btn_2.clicked.connect(self.ProceedTransaction)
            else:
                self.showMessageBox("Warning", "Account does not exits")
            conn.close()
        elif(ok and text == ""):
            self.showMessageBox("Warning", "Invalid Account Number")

    def ProceedTransaction(self):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` = '"+self.UserProfileDetailsUi.Account_Number.text()+"'")
        if(self.UserProfileDetailsUi.comboBox.currentText() != "--Select transaction type--" and self.UserProfileDetailsUi.Amount.text() != "" and self.UserProfileDetailsUi.Transaction_Description.toPlainText() != ""):
            if(self.UserProfileDetailsUi.comboBox.currentText() == "Credit"):
                cursor.execute("INSERT INTO `bank_transactions`(`Account Number`, `Transaction Date`, `Transaction Description`, `Credit`) VALUES('"+self.UserProfileDetailsUi.Account_Number.text()+"', '"+str((self.UserProfileDetailsUi.Date_of_Transfer.date()).toPyDate())+"', '"+self.UserProfileDetailsUi.Transaction_Description.toPlainText()+"', '"+self.UserProfileDetailsUi.Amount.text()+"')")
                self.showMessageBox("Successfully", "Amount Credited Successfully")
                balance = str(float(result[0][2]) - float(self.UserProfileDetailsUi.Amount.text()))
                cursor.execute("UPDATE `bank_users` SET `Balance` = '"+balance+"' WHERE `Account_No.` = '"+self.UserProfileDetailsUi.Account_Number.text()+"'")
            else:
                cursor.execute("INSERT INTO `bank_transactions`(`Account Number`, `Transaction Date`, `Transaction Description`, `Debit`) VALUES('"+self.UserProfileDetailsUi.Account_Number.text()+"', '"+str((self.UserProfileDetailsUi.Date_of_Transfer.date()).toPyDate())+"', '"+self.UserProfileDetailsUi.Transaction_Description.toPlainText()+"', '"+self.UserProfileDetailsUi.Amount.text()+"')")
                self.showMessageBox("Successfully", "Amount Credited Successfully")
                balance = str(float(result[0][2]) + float(self.UserProfileDetailsUi.Amount.text()))
                cursor.execute("UPDATE `bank_users` SET `Balance` = '"+balance+"' WHERE `Account_No.` = '"+self.UserProfileDetailsUi.Account_Number.text()+"'")
            self.loadUserProfileDetail(self.UserProfileDetailsUi.Amount.text())
        else:
            self.showMessageBox("Warning", "All field are mandatory to fill")
        conn.commit()
        conn.close()



    def loadAccountInfo(self):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users`")
        result = cursor.fetchall()
        self.AccountInformationUi.Account_Details_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.AccountInformationUi.Account_Details_table.insertRow(row_number)
            for colum_number, data in enumerate(row_data[:5]):
                self.AccountInformationUi.Account_Details_table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def ADAccount(self):
        items = ("Deactivate","Activate")
        item, okPressed = QInputDialog.getItem(self.Account_Information, "Input Dialog","Operation : ", items, 0, False)
        if okPressed and item:
            Account, Ok = QInputDialog.getText(self.Account_Information, "Input Dialog", "Enter Account Number : ")
            if Ok and Account:
                conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
                cursor = conn.cursor()
                result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+Account+"'")
                result = cursor.fetchall()
                if(len(result) > 0):
                    if(result[0][4] == "active" and item == "Activate"):
                        self.showMessageBox("Warning", "Account already activate")
                    elif(result[0][4] == "de-active" and item == "Deactivate"):
                        self.showMessageBox("Warning", "Account already deactivated")
                    else:
                        if(item == "Activate"):
                            cursor.execute("UPDATE `bank_users` SET `Account_Status` = 'active' WHERE `bank_users`.`Account_No.` = '"+Account+"'")
                        else:
                            cursor.execute("UPDATE `bank_users` SET `Account_Status` = 'de-active' WHERE `bank_users`.`Account_No.` = '"+Account+"'")
                        conn.commit()
                        self.loadAccountInfo()
                else:
                    self.showMessageBox("Warning", "Account does not exist")
                
                conn.close()
            else:
                self.showMessageBox("Warning", "Invalid Account Number")


    def AccountInformation(self):
        self.Account_Information = QtWidgets.QWidget()
        self.AccountInformationUi = Ui_Account_Information()
        self.AccountInformationUi.setupUi(self.Account_Information)
        self.Account_Information.show()
        self.loadAccountInfo()
        self.Admin_Home.hide()
        self.AccountInformationUi.Account_Details_btn.clicked.connect(self.AccountInformation)
        self.AccountInformationUi.Log_out_btn.clicked.connect(self.Home)
        self.AccountInformationUi.User_Details_btn.clicked.connect(self.AIUserProfileDetails)
        self.AccountInformationUi.Admin_Home_btn.clicked.connect(self.AIAdminHome)
        self.AccountInformationUi.Activare_Deactivae_Account_btn.clicked.connect(self.ADAccount)
        self.AccountInformationUi.View_Statement_btn.clicked.connect(self.TransactionStatement)


    def TSAccountInformation(self):
        self.AccountInformation()
        self.Account_Statement.hide()

    def UPAccountInformation(self):
        self.AccountInformation()
        self.User_Profile_Detail.hide()

    def UAccountInformation(self):
        self.AccountInformation()
        self.User_Detail.hide()

    def TSAdminHome(self):
        self.AdminHome()
        self.Account_Statement.hide()

    def UAdminHome(self):
        self.AdminHome()
        self.User_Detail.hide()

    def UPAdminHome(self):
        self.AdminHome()
        self.User_Profile_Detail.hide()

    def AIAdminHome(self):
        self.AdminHome()
        self.Account_Information.hide()

    
    def showMessageBox(self,title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def AdminHome(self):
        if(self.AdminLoginUi.Username.text() == "admin" and self.AdminLoginUi.Password.text() == "12345"):
            self.Admin_Home = QtWidgets.QWidget()
            self.AdminHomeUi = Ui_Admin_Home()
            self.AdminHomeUi.setupUi(self.Admin_Home)
            self.Admin_Home.show()
            self.Admin_Login_Form.hide()
            self.AdminHomeUi.Admin_Home_btn.clicked.connect(self.AdminHome)
            self.AdminHomeUi.Log_out_btn.clicked.connect(self.Home)
            self.AdminHomeUi.Account_Details_btn.clicked.connect(self.AccountInformation)
            self.AdminHomeUi.Account_Information_btn.clicked.connect(self.AccountInformation)
            self.AdminHomeUi.User_Details_btn.clicked.connect(self.UserProfileDetails)
            self.AdminHomeUi.Users_Details_btn.clicked.connect(self.User)
        else:
            self.showMessageBox("Warning", "Username and Password is Invalid")

    def UPHome(self):
        Form.show()
        self.User_Profile_Detail.hide()

    def UHome(self):
        Form.show()
        self.User_Detail.hide()

    def TSHome(self):
        Form.show()
        self.Account_Statement.hide()

    def AIHome(self):
        Form.show()
        self.Account_Information.hide()

    def Home(self):
        Form.show()
        self.Admin_Login_Form.hide()
        self.Admin_Home.hide()

    def USHome(self):
        Form.show()
        self.User_Login.hide()

    def Register(self):
        self.New_Account = QtWidgets.QWidget()
        self.RegisterUi = Ui_New_Account()
        self.RegisterUi.setupUi(self.New_Account)
        self.New_Account.show()
        self.User_Login.hide()
        self.RegisterUi.Login_btn.clicked.connect(self.RLogin)
        self.RegisterUi.Browse.clicked.connect(self.UploadImage)
        self.RegisterUi.Register_Account.clicked.connect(self.InsertData)

    def InsertData(self):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        if(self.RegisterUi.First_Name.text() != "" and self.RegisterUi.Email_Id.text() != "" and self.RegisterUi.Profile_Picture.text() != "" and self.RegisterUi.Phone_Number.text() != "" and self.RegisterUi.Date_of_Birth.text() != "" and self.RegisterUi.Address.toPlainText() != "" and self.RegisterUi.City.text() != "" and self.RegisterUi.State.text() != "" and self.RegisterUi.Zip_Code.text() != "" and self.RegisterUi.Pin.text() != "" and self.RegisterUi.Password.text() != "" and self.RegisterUi.Confirm_Password.text() != "" and self.RegisterUi.Account_type.currentText != "--Not Selected--" and self.RegisterUi.Gender.currentText() != "--Not Selected--" and self.RegisterUi.Verify_Pin.text() != ""):
            with open(str(self.RegisterUi.Profile_Picture.text()),"rb") as f:
                data = f.read()
            f.close()
            data = str(data)
            if(self.RegisterUi.Password.text() == self.RegisterUi.Confirm_Password.text()):
                if(self.RegisterUi.Pin.text() == self.RegisterUi.Verify_Pin.text()):
                    cursor.execute("INSERT INTO `bank_users`(`User_Name`, `Account_Type`, `Account_Status`, `Password`, `Email_ID`, `Phone_Number`, `Date_of_Birth`, `Gender`, `Address`, `City`, `State`, `Zip_Code`, `Account_PIN`, `Profile_Picture`) VALUES ('"+(str(self.RegisterUi.First_Name.text())+str(self.RegisterUi.Last_Name.text()))+"','"+self.RegisterUi.Account_type.currentText()+"', 'active', '"+self.RegisterUi.Password.text()+"', '"+self.RegisterUi.Email_Id.text()+"', '"+self.RegisterUi.Phone_Number.text()+"', '"+self.RegisterUi.Date_of_Birth.text()+"', '"+self.RegisterUi.Gender.currentText()+"', '"+self.RegisterUi.Address.toPlainText()+"', '"+self.RegisterUi.City.text()+"', '"+self.RegisterUi.State.text()+"', '"+self.RegisterUi.Zip_Code.text()+"', '"+self.RegisterUi.Pin.text()+"', '"+data+"'")
                    conn.commit()

                    result = cursor.execute("SELECT * FROM `bank_users`")
                    conn.close()
                    self.showMessageBox("Registered Successfully", "Your Account Number : {}".format(result[-1][1]))
                    self.RegisterSussfully = QtWidgets.QWidget()
                    self.SussfullyRegisterUi  = Ui_Account_Registration_successful()
                    self.SussfullyRegisterUi.setupUi(self.RegisterSussfully)
                    self.RegisterSussfully.show()
                    self.New_Account.hide()
                else:
                    self.showMessageBox("Warning", "Your Account Pin and Verify Pin is not same")
            else:
                self.showMessageBox("Warning", "Your Account Password and Confirm Password is not same")
        else:
            self.showMessageBox("Warning", "All field is mandatory to fill")
    def UploadImage(self):
        file = QFileDialog.getOpenFileName(self.New_Account,'Single File','C:\'','*.jpg')
        self.RegisterUi.Profile_Picture.setText(file[0])

    def RLogin(self):
        self.User_Login.show()
        self.New_Account.hide()

    def Validate(self):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+self.UserLoginUi.Account_Number.text()+"'")
        result = cursor.fetchall()
        if(str(self.PINUi.Password.text()) == str(result[0][14])):
            self.User_Home = QtWidgets.QWidget()
            self.UserHomeUi = Ui_User_Profile_Home()
            self.UserHomeUi.setupUi(self.User_Home)
            self.User_Home.show()
            self.PIN_Validate.hide()
            result = result[0]
            self.Userload()
            self.UserHomeUi.User_Name.setText(result[0])
            self.UserHomeUi.Email_ID.setText(result[6])
            self.UserHomeUi.Phone_Number.setText(result[7])
            self.UserHomeUi.Address.setText(result[10])
            self.UserHomeUi.City_State.setText("{} {}".format(result[11], result[12]))
            self.UserHomeUi.Zip_Code.setNum(result[13])
            self.UserHomeUi.Account_Number.setNum(result[1])
            self.UserHomeUi.Account_Balnce.setNum(result[2])
            self.UserHomeUi.Account_Pin_code.setText(result[14])

            self.UserHomeUi.Sender_Account_Number.setNum(result[1])

            with open("img.jpg", "wb") as f:
                f.write(result[16])
            f.close()

            self.UserHomeUi.User_Picture.setAutoFillBackground(False)
            self.UserHomeUi.User_Picture.setText("")
            image = QtGui.QPixmap("img.jpg")
            image = image.scaled(self.UserHomeUi.User_Picture.width(), self.UserHomeUi.User_Picture.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.UserHomeUi.User_Picture.setPixmap(image)
                
            self.UserHomeUi.Log_out_btn_2.clicked.connect(self.UHHome)
            self.UserHomeUi.User_Details_btn_2.clicked.connect(self.changePin)
            self.UserHomeUi.Admin_Home_btn_2.clicked.connect(self.changePassword)
            self.UserHomeUi.Fund_Transfer.clicked.connect(self.Transfer)
            

        else:
            self.showMessageBox("Warning", "Invalid PIN")
        conn.close()
    
    def Userload(self):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+self.UserLoginUi.Account_Number.text()+"'")
        result = cursor.fetchall()
        result = result[0]
        self.UserHomeUi.Balance.setNum(result[2])
        self.UserHomeUi.Account_Statement_Table.setRowCount(0)
        result1 = cursor.execute("SELECT * FROM `bank_transactions` WHERE `Account Number` = '"+self.UserLoginUi.Account_Number.text()+"'")
        result1 = cursor.fetchall()

        for row_number, row_data in enumerate(result1):
            res  = []
            res.append(row_data[1])
            res.append(row_data[3])
            res.append(row_data[4])
            res.append(row_data[5])
            self.UserHomeUi.Account_Statement_Table.insertRow(row_number)
            for colum_number, data in enumerate(res):
                self.UserHomeUi.Account_Statement_Table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        
        conn.close()

    def Transfer(self):
        if(self.UserHomeUi.Reciver_Name.text() != "" and self.UserHomeUi.Receiver_Account_Number.text() != "" and self.UserHomeUi.Amount_to_transfer.text() != "" ):
            conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` = '"+self.UserHomeUi.Receiver_Account_Number.text()+"' and `User_Name` = '"+self.UserHomeUi.Reciver_Name.text()+"'")
            result = cursor.fetchall()
            if(len(result) > 0):
                result1 = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` = '"+self.UserHomeUi.Sender_Account_Number.text()+"'")
                result1 = cursor.fetchall()
                if(result1[0][2] >= float(self.UserHomeUi.Amount_to_transfer.text())):
                    balance1 = str(float(result1[0][2]) - float(self.UserHomeUi.Amount_to_transfer.text()))
                    balance2 = str(float(result[0][2]) + float(self.UserHomeUi.Amount_to_transfer.text()))

                    cursor.execute("UPDATE `bank_users` SET `Balance` ='"+balance1+"' WHERE `Account_No.` = '"+self.UserHomeUi.Sender_Account_Number.text()+"'")
                    cursor.execute("UPDATE `bank_users` SET `Balance` ='"+balance2+"' WHERE `Account_No.` = '"+self.UserHomeUi.Receiver_Account_Number.text()+"'")
                    Transaction_DescriptionForSender = str(self.UserHomeUi.Transfer_Description.toPlainText()) + "Transferred to {}".format(self.UserHomeUi.Sender_Account_Number.text())
                    Transaction_DescriptionForReceiver = str(self.UserHomeUi.Transfer_Description.toPlainText()) + "Transferred by {}".format(self.UserHomeUi.Receiver_Account_Number.text())
                    cursor.execute("INSERT INTO `bank_transactions`(`Account Number`, `Transaction Date`, `Transaction Description`, `Debit`) VALUES('"+self.UserHomeUi.Sender_Account_Number.text()+"', '"+str((self.UserHomeUi.Date_of_transfer.date()).toPyDate())+"', '"+Transaction_DescriptionForSender+"', '"+self.UserHomeUi.Amount_to_transfer.text()+"')")
                    cursor.execute("INSERT INTO `bank_transactions`(`Account Number`, `Transaction Date`, `Transaction Description`, `Credit`) VALUES('"+self.UserHomeUi.Receiver_Account_Number.text()+"', '"+str((self.UserHomeUi.Date_of_transfer.date()).toPyDate())+"', '"+Transaction_DescriptionForReceiver+"', '"+self.UserHomeUi.Amount_to_transfer.text()+"')")
                    conn.commit()
                    conn.close()
                    self.Userload()
                    self.showMessageBox("Successfully", "Amount Transferred successfully")

                else:
                    self.showMessageBox("Warning", "Does not have enough amount to transferr")
            else:
                self.showMessageBox("Warning", "Receiver's Name or Account Number is wrong")
        else:
            self.showMessageBox("Warning", "All field is mandatory to fill")



    def changePin(self):
        self.Change_Account_Pin = QtWidgets.QWidget()
        self.changePinUi = Ui_Change_Account_PIN()
        self.changePinUi.setupUi(self.Change_Account_Pin)
        self.Change_Account_Pin.show()
        self.User_Home.hide()
        self.changePinUi.Admin_Home_btn_2.clicked.connect(self.CChangePassword)
        self.changePinUi.User_Details_btn_2.clicked.connect(self.changePin)
        self.changePinUi.Log_out_btn_2.clicked.connect(self.CPHome)
        self.changePinUi.pushButton.clicked.connect(self.change_Pin)

    def change_Pin(self):
        if(self.changePinUi.New_Account_Pin.text() == self.changePinUi.Confirm_Account_Pin.text() and self.changePinUi.New_Account_Pin.text() != ""):
            conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
            cursor = conn.cursor()
            cursor.execute("UPDATE `bank_users` SET `Account_PIN` ='"+self.changePinUi.Confirm_Account_Pin.text()+"' WHERE `Account_No.` ='"+self.UserLoginUi.Account_Number.text()+"'")
            self.showMessageBox("Susscessfull", "Your Account PIN is changed successfully")
            self.User_Home.show()
            self.Change_Account_Pin.hide()
            conn.commit()
            conn.close()
        else:
            self.showMessageBox("Warning", "New Account Pin and confirm Pin is not same")

    def change_Password(self):
        if(self.PasswordUi.New_Password.text() == self.PasswordUi.Confirm_Password.text() and self.PasswordUi.Confirm_Password.text() != ""):
            conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
            cursor = conn.cursor()
            cursor.execute("UPDATE `bank_users` SET `Password` ='"+self.PasswordUi.Confirm_Password.text()+"' WHERE `Account_No.` ='"+self.UserLoginUi.Account_Number.text()+"'")
            self.showMessageBox("Susscessfull", "Your Account Password is changed successfully")
            self.User_Home.show()
            self.Password.hide()
            conn.commit()
            conn.close()
        else:
            self.showMessageBox("Warning", "New Account Password and confirm Password is not same")
        

    def CChangePassword(self):
        self.changePassword()
        self.Change_Account_Pin.hide()

    def CChangePin(self):
        self.changePin()
        self.Password.hide()

    def changePassword(self):
        self.Password = QtWidgets.QWidget()
        self.PasswordUi = Ui_Change_Password()
        self.PasswordUi.setupUi(self.Password)
        self.Password.show()
        self.User_Home.hide()
        self.PasswordUi.Admin_Home_btn_2.clicked.connect(self.changePassword)
        self.PasswordUi.User_Details_btn_2.clicked.connect(self.CChangePin)
        self.PasswordUi.Log_out_btn_2.clicked.connect(self.CPHome)
        self.PasswordUi.pushButton.clicked.connect(self.change_Password)

    def CPHome(self):
        Form.show()
        self.Change_Account_Pin.hide()
    
    def CPSHome(self):
        Form.show()
        self.Password.hide()

    def UHHome(self):
        Form.show()
        self.User_Home.hide()

    def ValidatePIN(self):
        conn = mysql.connector.connect(host='localhost', database='bankproject', user='root', password='')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM `bank_users` WHERE `Account_No.` ='"+self.UserLoginUi.Account_Number.text()+"' and `Password` = '"+self.UserLoginUi.Password.text()+"'")
        result = cursor.fetchall()
        if(len(result) > 0 ):
            self.PIN_Validate = QtWidgets.QWidget()
            self.PINUi = Ui_Pin_Validate()
            self.PINUi.setupUi(self.PIN_Validate)
            self.PIN_Validate.show()
            self.User_Login.hide()
            self.PINUi.Login_btn.clicked.connect(self.Validate)
        else:
            self.showMessageBox("Warning", "Invalid Account Number or Password")

    def UserLoginWin(self):
        self.User_Login = QtWidgets.QWidget()
        self.UserLoginUi = Ui_User_Login_System()
        self.UserLoginUi.setupUi(self.User_Login)
        self.User_Login.show()
        Form.hide()
        self.UserLoginUi.Back_btn.clicked.connect(self.USHome)
        self.UserLoginUi.Register_btn.clicked.connect(self.Register)
        self.UserLoginUi.Login_btn.clicked.connect(self.ValidatePIN)

    def AdminLoginWin(self):
        self.Admin_Login_Form = QtWidgets.QWidget()
        self.AdminLoginUi = Ui_Admin_Login_Form()
        self.AdminLoginUi.setupUi(self.Admin_Login_Form)
        self.Admin_Login_Form.show()
        Form.hide()
        self.AdminLoginUi.Back_btn.clicked.connect(self.Home)
        self.AdminLoginUi.Login_btn.clicked.connect(self.AdminHome)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1270, 590)
        Form.setMinimumSize(QtCore.QSize(1270, 590))
        Form.setMaximumSize(QtCore.QSize(1270, 590))
        Form.setStyleSheet("#Form{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.02, y2:0.0340909, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(0, 0, 0, 199), stop:0.505 rgba(28, 28, 28, 255), stop:1 rgba(53, 53, 53, 255));\n"
"}\n"
"#topframe{\n"
"background-color: qconicalgradient(cx:0.000472637, cy:0, angle:227.8, stop:0 rgba(30, 0, 255, 255), stop:0.375 rgba(0, 195, 255, 252), stop:0.423533 rgba(37, 0, 255, 255), stop:0.45 rgba(0, 130, 255, 255), stop:0.477581 rgba(0, 56, 255, 252), stop:0.518717 rgba(71, 171, 255, 255), stop:0.542289 rgba(71, 171, 255, 255), stop:0.547264 rgba(68, 134, 249, 255), stop:0.55 rgba(0, 74, 255, 255), stop:0.552239 rgba(21, 93, 243, 255), stop:0.57754 rgba(102, 0, 255, 255), stop:0.625 rgba(0, 185, 255, 247), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"#textBrowser{\n"
"background-color: qconicalgradient(cx:0.000472637, cy:0, angle:227.8, stop:0 rgba(30, 0, 255, 255), stop:0.375 rgba(0, 195, 255, 252), stop:0.423533 rgba(37, 0, 255, 255), stop:0.45 rgba(0, 130, 255, 255), stop:0.477581 rgba(0, 56, 255, 252), stop:0.518717 rgba(71, 171, 255, 255), stop:0.542289 rgba(71, 171, 255, 255), stop:0.547264 rgba(68, 134, 249, 255), stop:0.55 rgba(0, 74, 255, 255), stop:0.552239 rgba(21, 93, 243, 255), stop:0.57754 rgba(102, 0, 255, 255), stop:0.625 rgba(0, 185, 255, 247), stop:1 rgba(255, 255, 0, 69));\n"
"border:none;\n"
"}\n"
"#bottomframe{\n"
"background-color: qlineargradient(spread:pad, x1:0.025, y1:0.892545, x2:0.0199005, y2:0, stop:0 rgba(244, 244, 244, 255), stop:0.495 rgba(218, 212, 186, 230), stop:0.505 rgba(236, 224, 224, 255), stop:1 rgba(253, 246, 246, 255));\n"
"}\n"
"QPushButton{\n"
"background:#22c4ff;\n"
"border-radius:15px;\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"}")
        self.bottomframe = QtWidgets.QFrame(Form)
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
        self.Admin_Login_btn = QtWidgets.QPushButton(Form)
        self.Admin_Login_btn.setGeometry(QtCore.QRect(352, 287, 151, 51))
        self.Admin_Login_btn.setObjectName("Admin_Login_btn")
        self.Admin_Login_btn.clicked.connect(self.AdminLoginWin)
        self.User_Login_btn = QtWidgets.QPushButton(Form)
        self.User_Login_btn.setGeometry(QtCore.QRect(632, 287, 141, 51))
        self.User_Login_btn.setObjectName("User_Login_btn")
        self.User_Login_btn.clicked.connect(self.UserLoginWin)
        self.topframe = QtWidgets.QPushButton(Form)
        self.topframe.setGeometry(QtCore.QRect(10, 10, 1251, 101))
        self.topframe.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Images/Bank-Management-System.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topframe.setIcon(icon)
        self.topframe.setIconSize(QtCore.QSize(1300, 520))
        self.topframe.setObjectName("topframe")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bank Management System"))
        self.label.setText(_translate("Form", "Project by: Ankit Choudhary "))
        self.label_2.setText(_translate("Form", "ID: 19CS014   Anand International College of Engineering, Jaipur"))
        self.Admin_Login_btn.setText(_translate("Form", "Admin Login"))
        self.User_Login_btn.setText(_translate("Form", "User Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
