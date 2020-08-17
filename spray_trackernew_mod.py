import sys
import datetime
import calendar
import sqlite3
from PyQt5 import QtSql, QtCore, QtGui, uic

from spray_trackernew_auto import *
import newentry_spraymain_mod

class SprayTracker(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.makeVisible(False)

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("sprays_agri")
        db.open()

        

        QtCore.QObject.connect(self.btn_showcal, QtCore.SIGNAL('clicked()'), self.showCal)

        QtCore.QObject.connect(self.cal_calendar, QtCore.SIGNAL('selectionChanged()'), self.showDate)

        QtCore.QObject.connect(self.btn_addEntry, QtCore.SIGNAL('clicked()'), \
                           self.addEntry)
        QtCore.QObject.connect(self.btn_showcal, QtCore.SIGNAL('clicked()'), self.showCal)

        QtCore.QObject.connect(self.de_indate, QtCore.SIGNAL('dateChanged()'),self.showDater)

        QtCore.QObject.connect(self.btn_showAll, QtCore.SIGNAL('clicked()'), self.retrieveAll)

    def retrieveAll(self):
        self.modelw = QtSql.QSqlTableModel(self)
        self.modelw.setTable("sprays_agri")
        quer="SELECT * from sprays_agri "
        query = QtSql.QSqlQuery(quer)
        self.modelw.setQuery(query)
        self.tableView.setModel(self.modelw)

        self.modelw.setHeaderData(0, QtCore.Qt.Horizontal, "SL No.")
        self.modelw.setHeaderData(1, QtCore.Qt.Horizontal, "Date")
        self.modelw.setHeaderData(2, QtCore.Qt.Horizontal, "Type")
        self.modelw.setHeaderData(3, QtCore.Qt.Horizontal, "Description")
        self.modelw.setHeaderData(4, QtCore.Qt.Horizontal, "Land Area (hect)")
        self.modelw.setHeaderData(5, QtCore.Qt.Horizontal, "Spray Density (Lt/hect)")
        self.modelw.setHeaderData(6, QtCore.Qt.Horizontal, "Comments")


    def addEntry(self):
        print("Hello")
        next_w = newentry_spraymain_mod.MyWindowClass(self)
        next_w.show()
    def makeVisible(self, what):
        notwhat=not what
        print(notwhat)
        self.cal_calendar.setVisible(what)
        self.tableView.setVisible(notwhat)
        self.lbl_start.setVisible(notwhat)
        self.lbl_stop.setVisible(notwhat)
        self.lbl_showweek.setVisible(notwhat)
        self.label.setVisible(notwhat)
        self.label_2.setVisible(notwhat)
        self.label_3.setVisible(notwhat)

    def showCal(self):
        self.makeVisible(True)
        
    def showDater(self):
        print("HELLO")
    def integerDate(self, y, m ,d):
        return(y*10000 + m*100 + d)

    def isLeap(self, year):

        if(year%400==0):
            return 1
        elif(year%100==0):
            return 0
        elif(year%4==0):
            return 1
           
        return 0
    
    def retrieve(self, start, stop):
        #Read Model
        #self.model = QtSql.QSqlTableModel(self)
        print(start, stop)

        quer="SELECT * from sprays_agri WHERE DATE BETWEEN "+ str(start)+ " AND " + str(stop)
        query = QtSql.QSqlQuery(quer)
        #self.model.setQuery(query)
        #self.tableView_read.setModel(self.model)

        # Write Model
        self.modelw = QtSql.QSqlTableModel(self)
        self.modelw.setTable("sprays_agri")
        self.modelw.setFilter("DATE BETWEEN "+ str(start)+ " AND " + str(stop))
        #OnFieldChange
        self.modelw.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelw.select()
        self.tableView.setModel(self.modelw)
 

        
##        if(self.modelw.rowCount()==0):
##            self.modelw.insertRows(self.modelw.rowCount(),stop-start+1)
##            for i in range(0,stop-start+1):
##                self.modelw.setData(self.modelw.index(i,0), start+i)
    ##            QSqlRecord record = model.record(1)
    ##            record.setValue("date", start)
    ##            model.setRecord(1, record)
##        self.tableView.setModel(self.modelw)

        self.modelw.setHeaderData(0, QtCore.Qt.Horizontal, "SL No.")
        self.modelw.setHeaderData(1, QtCore.Qt.Horizontal, "Date")
        self.modelw.setHeaderData(2, QtCore.Qt.Horizontal, "Type")
        self.modelw.setHeaderData(3, QtCore.Qt.Horizontal, "Description")
        self.modelw.setHeaderData(4, QtCore.Qt.Horizontal, "Land Area (hect)")
        self.modelw.setHeaderData(5, QtCore.Qt.Horizontal, "Spray Density (Lt/hect)")
        self.modelw.setHeaderData(6, QtCore.Qt.Horizontal, "Comments")
        
        

    def dateString(self,dt):
        str_date = ""
        year = dt//10000
        dt = dt%10000
        month = dt//100
        dt=dt%100
        day = dt
        curr = datetime.date(year, month, day)
        str_date += calendar.day_name[curr.weekday()]

        str_date += " " + str(day) + " " + calendar.month_name[month]+ ", " +str(year)
        return str_date

    def showDate(self):
        date = self.cal_calendar.selectedDate()
        #print(date)
        #help(date)
        print(date.dayOfWeek())
        #self.lbl_showdate.setText(date.toString())
        self.de_indate.setDisplayFormat('dd MM yyyy')
        self.de_indate.setDate(date)
        self.makeVisible(False)

        intdate = date.getDate()
        year = int(intdate[0])
        month = int(intdate[1])
        dd = int(intdate[2])

        isodate = datetime.date(year, month, dd).isocalendar()
        firstweek = datetime.date(year, month, 1).isocalendar()[1]
        week = isodate[1] - firstweek + 1

        self.lbl_showweek.setText(str(week))

        if (month==2):
            if (self.isLeap(year)):
                lastday = 29
            else:
                lastday = 28
        elif(month<=7 and month%2==1):
            lastday = 31
        elif(month>7 and month%2==1):
            lastday = 30
        else:
            lastday = 31
            

        if(week==1):
            curr = self.integerDate(year, month, dd)
            start = self.integerDate(year, month, 1)
            stop = curr + (7-date.dayOfWeek())
    
        elif(week==5):
            curr = self.integerDate(year, month, dd)
            start = curr - date.dayOfWeek() + 1   
            stop = self.integerDate(year,month,lastday) 

        else:
            curr = self.integerDate(year, month, dd)
            stop = curr +  (7-date.dayOfWeek()) 
            start = curr - date.dayOfWeek() + 1


        self.lbl_start.setText(self.dateString(start))
        self.lbl_stop.setText(self.dateString(stop))
        self.retrieve(start, stop)
    



if (__name__ == "__main__"):
     app = QtGui.QApplication(sys.argv)
     feed = SprayTracker(None)
     feed.show()
     feed.setFixedSize(feed.size())
     app.exec_()
