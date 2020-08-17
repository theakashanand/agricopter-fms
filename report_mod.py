import sys
import sqlite3
import datetime
import calendar

from report_auto import *
from PyQt5 import QtSql, QtCore, QtGui,QtWidgets, uic

class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.conn = sqlite3.connect('sprays_agri')

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('sprays_agri')
        db.open()

        self.openAllSeason()
        self.calendar.selectionChanged.connect(self.showDate)
        self.btn_showCal.clicked.connect(self.showCal)
        self.actionAll_Season.triggered.connect(self.openAllSeason)
        self.actionWeekly.triggered.connect(self.openWeekly)


#        QtCore.QObject.connect(self.calendar, QtCore.SIGNAL('selectionChanged()'), self.showDate)
#        QtCore.QObject.connect(self.actionAll_Season, QtCore.SIGNAL('triggered()'), self.openAllSeason)
#        QtCore.QObject.connect(self.actionWeekly, QtCore.SIGNAL('triggered()'), self.openWeekly)
#        QtCore.QObject.connect(self.btn_showCal, QtCore.SIGNAL('clicked()'), self.showCal)
#        

    def openWeekly(self):
        self.makeVisible(True)
        self.lbl_header.setText("Weekly Report")
        self.de_date.setVisible(True)
        self.btn_showCal.setVisible(True)
        self.label.setVisible(True)

        
        
    def openAllSeason(self):
        
        self.makeVisible(False)
        self.label.setVisible(False)
        self.de_date.setVisible(False)
        self.btn_showCal.setVisible(False)
        self.lbl_header.setText("Season Report")

        cursor = self.conn.cursor()
        cursor.execute("SELECT MIN(date) from sprays_agri")
        start = cursor.fetchone()[0]
        cursor.execute("SELECT MAX(date) from sprays_agri")
        stop = cursor.fetchone()[0]

        self.lbl_startdate.setText(self.dateString(start))
        self.lbl_enddate.setText(self.dateString(stop))

        #self.lbl_startdate.setText(self.dateString(start))
        #self.lbl_stop.setText(self.dateString(stop))
        #self.retrieve(start, stop)

        cursor.execute('select sum(landarea*litresperhect) from sprays_agri where category=1 ')
        fert = cursor.fetchone()[0]
        cursor.execute('select sum(landarea*litresperhect) from sprays_agri where category=2 ')
        pest = cursor.fetchone()[0]
        cursor.execute('select sum(landarea*litresperhect) from sprays_agri where category=3 ')
        herb = cursor.fetchone()[0]

        try:
            self.lbl_fert.setText(str(round(fert,2))+" L")
        except:
            self.lbl_fert.setText("0 L")
        try:
            self.lbl_pest.setText(str(round(pest,2))+" L")
        except:
            self.lbl_pest.setText("0 L")
        try:
            self.lbl_herb.setText(str(round(herb,2))+"L")
        except:
            self.lbl_herb.setText("0 L")

        cursor.execute('select sum(landarea) from sprays_agri')
        area = cursor.fetchone()[0]
        try:
            self.lbl_larea.setText(str(round(area,2))+" hectares")
        except:
            self.lbl_larea.setText("0 hectares")
        

        

        

    def showDate(self):
        date = self.calendar.selectedDate()
        #print(date)
        #help(date)
        print(date.dayOfWeek())
        #self.lbl_showdate.setText(date.toString())
        self.de_date.setDisplayFormat('dd MM yyyy')
        self.de_date.setDate(date)
        self.makeVisible(False)

        intdate = date.getDate()
        year = int(intdate[0])
        month = int(intdate[1])
        dd = int(intdate[2])

        isodate = datetime.date(year, month, dd).isocalendar()
        firstweek = datetime.date(year, month, 1).isocalendar()[1]
        week = isodate[1] - firstweek + 1

        #self.lbl_showweek.setText(str(week))

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

        self.lbl_startdate.setText(self.dateString(start))
        self.lbl_enddate.setText(self.dateString(stop))

        cursor = self.conn.cursor()
        cursor.execute('select sum(landarea*litresperhect) from sprays_agri where category=1 and date between ? and ?', (start, stop))
        fert = cursor.fetchone()[0]
        cursor.execute('select sum(landarea*litresperhect) from sprays_agri where category=2 and date between ? and ?', (start, stop))
        pest = cursor.fetchone()[0]
        cursor.execute('select sum(landarea*litresperhect) from sprays_agri where category=3 and date between ? and ?', (start, stop))
        herb = cursor.fetchone()[0]
        try:
            self.lbl_fert.setText(str(round(fert,2))+" L")
        except:
            self.lbl_fert.setText("0 L")
        try:
            self.lbl_pest.setText(str(round(pest,2))+" L")
        except:
            self.lbl_pest.setText("0 L")
        try:
            self.lbl_herb.setText(str(round(herb,2))+"L")
        except:
            self.lbl_herb.setText("0 L")

        cursor.execute('select sum(landarea) from sprays_agri where date between ? and ?', (start, stop))
        area = cursor.fetchone()[0]
        try:
            self.lbl_larea.setText(str(round(area,2))+" hectares")
        except:
            self.lbl_larea.setText("0 L")


        
    def showDater(self):
        print("HELLO")

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

    def makeVisible(self, what):
        notwhat = not what
        self.calendar.setVisible(what)
        #self.de_date.setVisible(what)
        #self.btn_showCal.setVisible(what)
        #self.label.setVisible(what)
        self.label_11.setVisible(notwhat)
        self.label_12.setVisible(notwhat)
        self.label_3.setVisible(notwhat)
        self.label_4.setVisible(notwhat)
        self.label_5.setVisible(notwhat)
        self.label_10.setVisible(notwhat)
        self.lbl_larea.setVisible(notwhat)
        self.lbl_herb.setVisible(notwhat)
        self.lbl_pest.setVisible(notwhat)
        self.lbl_fert.setVisible(notwhat)
        self.lbl_enddate.setVisible(notwhat)
        self.lbl_startdate.setVisible(notwhat)

    def showCal(self):
        self.makeVisible(True)


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
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindowClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        

