import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

from mainwindow_auto import *
import spray_trackernew_mod
import report_mod

class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


        #QtCore.QObject.connect(self.actionSpray_Tracker, QtCore.SIGNAL('triggered()'), self.openSprayTracker)
        #QtCore.QObject.connect(self.actionReport, QtCore.SIGNAL('triggered()'), self.openReport)

        self.actionSpray_tracker.triggered.connect(self.openSprayTracker)
        self.actionReport.triggered.connect(self.openReport)


    def openSprayTracker(self):
##        next_dialog = Dialog_SprayTracker(self)
##        next_dialog.show()
        print("SPRAY")
        nextWin = spray_trackernew_mod.SprayTracker(self)
        nextWin.show()

    def openReport(self):
        nextWin = report_mod.MyWindowClass(self)
        nextWin.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyWindowClass()
    sys.exit(app.exec_())

        
