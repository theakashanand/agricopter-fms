import sys
import sqlite3

from newentry_spray_auto import *

from PyQt5 import QtSql, QtCore, QtGui, uic

class Dialog_newSprayEntry(QtGui.QDialog):

        def __init__(self, parent= None):
                QtGui.QWidget.__init__(self, parent)
                self.ui = Ui_Dialog()
                self.ui.setupUi(self)

                self.conn = sqlite3.connect('sprays_agri')

                db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName('sprays_agri')
                db.open()

                QtCore.QObject.connect(self.ui.btn_submit, QtCore.SIGNAL('clicked()'), self.submit)

        def submit(self):

                date = self.cal_calendar.selectedDate()
                intdate = date.getDate()
                year = int(intdate[0])
                month = int(intdate[1])
                dd = int(intdate[2])

                stype = cb_type.currentText()
                cat = catToInt(stype)

                curr = self.integerDate(year, month, dd)
                desc = self.lne_spraydesc.text()
                area = self.lne_area.text()
                dens = self.lne_spraydens.text()
                comments = self.te_comments.text()

                cursor = self.conn.cursor()
                cursor.execute("insert into sprays_agri \
                (date, category, sprayname, landarea, litresperhect,\
                comments) values (?,?,?,?,?,?)", (curr, cat, desc, area, dens, comments))
                self.conn.commit()
                
                

        def catToInt(self, stype):
                if stype =="Fertiliser":
                        return 1;
                if stype =="Pesticide":
                        return 2;
                if stype =="Herbicide":
                        return 3;
                
        def integerDate(self, y, m ,d):
                return(y*10000 + m*100 + d)

                

                
