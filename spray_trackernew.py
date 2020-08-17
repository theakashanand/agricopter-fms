# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spray_trackernew.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(980, 667)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_save = QtGui.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(270, 540, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.btn_showcal = QtGui.QPushButton(self.centralwidget)
        self.btn_showcal.setGeometry(QtCore.QRect(280, 50, 31, 21))
        self.btn_showcal.setObjectName(_fromUtf8("btn_showcal"))
        self.de_indate = QtGui.QDateEdit(self.centralwidget)
        self.de_indate.setGeometry(QtCore.QRect(160, 50, 110, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.de_indate.setFont(font)
        self.de_indate.setObjectName(_fromUtf8("de_indate"))
        self.cal_calendar = QtGui.QCalendarWidget(self.centralwidget)
        self.cal_calendar.setGeometry(QtCore.QRect(50, 80, 280, 155))
        self.cal_calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.cal_calendar.setObjectName(_fromUtf8("cal_calendar"))
        self.btn_addEntry = QtGui.QPushButton(self.centralwidget)
        self.btn_addEntry.setGeometry(QtCore.QRect(50, 540, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setBold(True)
        font.setWeight(75)
        self.btn_addEntry.setFont(font)
        self.btn_addEntry.setObjectName(_fromUtf8("btn_addEntry"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_showweek = QtGui.QLabel(self.centralwidget)
        self.lbl_showweek.setGeometry(QtCore.QRect(110, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.lbl_showweek.setFont(font)
        self.lbl_showweek.setText(_fromUtf8(""))
        self.lbl_showweek.setObjectName(_fromUtf8("lbl_showweek"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 150, 821, 381))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet(_fromUtf8("QTableView{\n"
"border : 0.5px solid gray;\n"
"border-radius : 25px;\n"
"}\n"
" QHeaderView::section:first {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     border: 1px solid #6c6c6c;\n"
"     border-radius : 25px;/*does not work*/\n"
"     padding-left: 4px;\n"
"     margin-left  : 25px;\n"
" }"))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 110, 471, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lbl_start = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.lbl_start.setFont(font)
        self.lbl_start.setText(_fromUtf8(""))
        self.lbl_start.setObjectName(_fromUtf8("lbl_start"))
        self.horizontalLayout.addWidget(self.lbl_start)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lbl_stop = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stop.setFont(font)
        self.lbl_stop.setText(_fromUtf8(""))
        self.lbl_stop.setObjectName(_fromUtf8("lbl_stop"))
        self.horizontalLayout.addWidget(self.lbl_stop)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semilight"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_showAll = QtGui.QPushButton(self.centralwidget)
        self.btn_showAll.setGeometry(QtCore.QRect(160, 540, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Palatino Linotype"))
        font.setBold(True)
        font.setWeight(75)
        self.btn_showAll.setFont(font)
        self.btn_showAll.setObjectName(_fromUtf8("btn_showAll"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_save.setText(_translate("MainWindow", "SAVE", None))
        self.btn_showcal.setText(_translate("MainWindow", "...", None))
        self.btn_addEntry.setText(_translate("MainWindow", "ADD ENTRY", None))
        self.label_2.setText(_translate("MainWindow", "Week:", None))
        self.label.setText(_translate("MainWindow", "Start:", None))
        self.label_3.setText(_translate("MainWindow", "Stop:", None))
        self.label_4.setText(_translate("MainWindow", "Show by Week:", None))
        self.btn_showAll.setText(_translate("MainWindow", "SHOW ALL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

