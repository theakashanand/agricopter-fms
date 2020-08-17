import sys
import sqlite3

from newentry_spraymain_auto import *
import spray_trackernew_mod
from PyQt5 import QtSql, QtCore, QtGui,QtWidgets, uic

class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):

        def __init__(self, parent= None):
                QtGui.QMainWindow.__init__(self, parent)
                self.setupUi(self)

                self.conn = sqlite3.connect('sprays_agri')

                db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName('sprays_agri')
                db.open()

                QtCore.QObject.connect(self.btn_submit, QtCore.SIGNAL('clicked()'), self.submit)
                

        def submit(self):

                date = self.cal_calendar.selectedDate()
                intdate = date.getDate()
                year = int(intdate[0])
                month = int(intdate[1])
                dd = int(intdate[2])

                stype = self.cb_type.currentText()
                cat = self.catToInt(stype)

                curr = self.integerDate(year, month, dd)
                desc = self.lne_spraydesc.text()
                area = self.lne_area.text()
                dens = self.lne_spraydens.text()
                comments = self.te_comments.toPlainText()

                cursor = self.conn.cursor()
                cursor.execute("insert into sprays_agri \
                (date, category, sprayname, landarea, litresperhect,\
                comments) values (?,?,?,?,?,?)", (curr, cat, desc, area, dens, comments))
                self.conn.commit()

                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w, "Information Saved!", "Success!")

                self.close()
                #spray_trackernew_mod.retrieveAll(self)
                

        def catToInt(self, stype):
                if stype =="Fertiliser":
                        return 1;
                if stype =="Pesticide":
                        return 2;
                if stype =="Herbicide":
                        return 3;
                
        def integerDate(self, y, m ,d):
                return(y*10000 + m*100 + d)

                

                
