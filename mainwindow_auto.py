# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 625)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMenuBar {\n"
"    /*background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 lightgray, stop:1 darkgray);*/\n"
"    background-color: #98f29e;\n"
"    \n"
"    font: 75 9pt \"Segoe UI Semilight\";\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    padding: 12px 4px;\n"
"    background: transparent;\n"
"    font: 75 10pt \"Segoe UI Semilight\";\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"   /*background: #a8a8a8;*/\n"
"    background: #639366;\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #639366;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 180, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 40))
        self.menubar.setObjectName("menubar")
        self.menuFarm_Manager = QtWidgets.QMenu(self.menubar)
        self.menuFarm_Manager.setObjectName("menuFarm_Manager")
        self.menuDrone_Tracking = QtWidgets.QMenu(self.menubar)
        self.menuDrone_Tracking.setObjectName("menuDrone_Tracking")
        self.menuSurvey_Analysis = QtWidgets.QMenu(self.menubar)
        self.menuSurvey_Analysis.setObjectName("menuSurvey_Analysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReport = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionReport.setFont(font)
        self.actionReport.setObjectName("actionReport")
        self.actionSpray_Tracker = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionSpray_Tracker.setFont(font)
        self.actionSpray_Tracker.setObjectName("actionSpray_Tracker")
        self.actionLive_Tracking = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionLive_Tracking.setFont(font)
        self.actionLive_Tracking.setObjectName("actionLive_Tracking")
        self.menuFarm_Manager.addAction(self.actionReport)
        self.menuFarm_Manager.addSeparator()
        self.menuFarm_Manager.addAction(self.actionSpray_Tracker)
        self.menuDrone_Tracking.addAction(self.actionLive_Tracking)
        self.menubar.addAction(self.menuFarm_Manager.menuAction())
        self.menubar.addAction(self.menuDrone_Tracking.menuAction())
        self.menubar.addAction(self.menuSurvey_Analysis.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", " AGRICOPTER\n"
"FARM MANAGEMENT SYSTEM"))
        self.menuFarm_Manager.setTitle(_translate("MainWindow", "Chemical Spray Analysis"))
        self.menuDrone_Tracking.setTitle(_translate("MainWindow", "Survey Analysis"))
        self.menuSurvey_Analysis.setTitle(_translate("MainWindow", "Drone Stats"))
        self.actionReport.setText(_translate("MainWindow", " Report"))
        self.actionSpray_Tracker.setText(_translate("MainWindow", "Spray Tracker"))
        self.actionLive_Tracking.setText(_translate("MainWindow", "Live Tracking"))

#import pics_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

