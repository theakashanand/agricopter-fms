# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newentry_spraymain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(150, 500, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.btn_submit.setFont(font)
        self.btn_submit.setObjectName("btn_submit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.cb_type = QtWidgets.QComboBox(self.centralwidget)
        self.cb_type.setGeometry(QtCore.QRect(150, 240, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.cb_type.setFont(font)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.lne_spraydens = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_spraydens.setGeometry(QtCore.QRect(150, 350, 71, 20))
        self.lne_spraydens.setObjectName("lne_spraydens")
        self.te_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.te_comments.setGeometry(QtCore.QRect(150, 400, 221, 71))
        self.te_comments.setObjectName("te_comments")
        self.cal_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.cal_calendar.setGeometry(QtCore.QRect(150, 60, 280, 155))
        self.cal_calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.cal_calendar.setObjectName("cal_calendar")
        self.lne_area = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_area.setGeometry(QtCore.QRect(150, 310, 71, 20))
        self.lne_area.setObjectName("lne_area")
        self.de_indate = QtWidgets.QDateEdit(self.centralwidget)
        self.de_indate.setGeometry(QtCore.QRect(150, 20, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.de_indate.setFont(font)
        self.de_indate.setObjectName("de_indate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.btn_showcal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_showcal.setGeometry(QtCore.QRect(270, 20, 31, 21))
        self.btn_showcal.setObjectName("btn_showcal")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 390, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 310, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lne_spraydesc = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_spraydesc.setGeometry(QtCore.QRect(150, 279, 221, 21))
        self.lne_spraydesc.setObjectName("lne_spraydesc")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 350, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_submit.setText(_translate("MainWindow", "SUBMIT"))
        self.label_5.setText(_translate("MainWindow", "Spray Density:"))
        self.cb_type.setItemText(0, _translate("MainWindow", "Fertiliser"))
        self.cb_type.setItemText(1, _translate("MainWindow", "Pesticide"))
        self.cb_type.setItemText(2, _translate("MainWindow", "Herbicide"))
        self.label.setText(_translate("MainWindow", "Date: "))
        self.btn_showcal.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Area Covered:"))
        self.label_6.setText(_translate("MainWindow", "Comments:"))
        self.label_2.setText(_translate("MainWindow", "Spray Description:"))
        self.label_3.setText(_translate("MainWindow", "Spray Type:"))
        self.label_7.setText(_translate("MainWindow", "hectares"))
        self.label_8.setText(_translate("MainWindow", "Litres/hectare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

