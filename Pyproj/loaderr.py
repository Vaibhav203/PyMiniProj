import sys
import time
import sqlite3
import json
import requests
import numpy as np

from array import *
from tkinter import *
from matplotlib import pyplot as plt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QSplashScreen
from PyQt5.QtCore import Qt



'''
con = sqlite3.connect("pyminproj")
q = "insert into signup (number, password) values ('" + "999999999" + "','" + "Asdf123#" + "')"
con.execute(q)
con.commit()
con.close()
'''


class LoadingScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\Loading.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def progress(self):
        for i in range(100):
            time.sleep(0.01)
            self.progressBar.setValue(i)


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\WelcomePage.ui", self)
        self.but_login.clicked.connect(self.gotologin)
        self.but_register.clicked.connect(self.gotoregister)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoregister(self):
        register = SignupScreen()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\SigninPage.ui', self)
        self.but_login.clicked.connect(self.gotovalidation)
        self.but_signup.clicked.connect(self.gotoregister)

    def gotoregister(self):
        register = SignupScreen()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotohome(self):
        hom = Homescreen_U()
        widget.addWidget(hom)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotovalidation(self):
        user = self.lab_num.text()
        pas = self.lab_pass.text()
        print(pas)
        if len(user) == 0 or len(pas) == 0:
            self.lab_error.setText('Please input all Fields')
        else:
            con = sqlite3.connect("pyminproj")
            cur = con.cursor()
            q = "SELECT password FROM signup WHERE number='" + user + "'"
            cur.execute(q)
            password = cur.fetchone()[0]
            if password != pas:
                self.lab_error.setText('Invalid Login Credentials')
            elif password == pas:
                self.gotohome()


class SignupScreen(QDialog):
    def __init__(self):
        super(SignupScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\SignupPage.ui', self)
        self.but_signup.clicked.connect(self.validation)
        self.but_login.clicked.connect(self.gotologin)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotohome(self):
        home = Homescreen_U()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def validation(self):
        user = self.le_name.text()
        pas = self.le_pass.text()
        aad = self.le_aadhar.text()
        num = self.le_number.text()
        dob = self.le_dob.text()
        mail = self.le_mail.text()
        print(user, pas, aad, num, dob, mail)
        if len(user) == 0 or len(pas) == 0 or len(aad) == 0 or len(num) == 0 or len(dob) == 0 or len(mail) == 0:
            self.lab_error1.setText('Please input all Fields')
        elif aad.isnumeric() == False:
            self.lab_error1.setText('Invalid Aadhar Card Number')
        elif len(aad)<=11:
            self.lab_error1.setText('Invalid Aadhar Card Number')
        elif len(dob)<=3:
            self.lab_error1.setText('Invalid Year of Birth')
        elif dob.isnumeric() == False:
            self.lab_error1.setText('Invalid Year of Birth')
        elif num.isnumeric() == False:
            self.lab_error1.setText('Invalid Number')
        elif len(num)<=9:
            self.lab_error1.setText('Invalid Number')
        elif mail.find('@') == -1 or mail.find('.') == -1:
            self.lab_error1.setText('Invalid Email')
        elif len(pas) < 7:
            self.lab_error1.setText('Password should be atleast 7 characters')
        elif not any(char.isdigit() for char in pas):
            self.lab_error1.setText('Password should contain atleast 1 number')
        elif not any(char.isupper() for char in pas):
            self.lab_error1.setText('Password should contain atleast 1 uppercase')
        elif not any(char.islower() for char in pas):
            self.lab_error1.setText('Password should contain atleast 1 lowercase')
        elif not any(char in ['#', '@', '$', '%', '!', '*', '&'] for char in pas):
            self.lab_error1.setText('Password should contain atleast 1 of !,@,#,$,%,&,*')
        else:
            pass
            con = sqlite3.connect("pyminproj")
            q = "insert into signup (username, password, aadhar, number, yob, mail) values ('" + user + "','" + pas + "','" + aad + "','" + num + "','" + dob + "','" + mail + "')"
            con.execute(q)
            con.commit()
            con.close()
            print('Data Entered Successfully')
            self.gotohome()


class Homescreen_U(QDialog):
    def __init__(self):
        super(Homescreen_U, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\HomePage_User.ui', self)

        self.but_assess.clicked.connect(self.gototest)
        self.but_abtus.clicked.connect(self.gotoabout)
        self.but_news.clicked.connect(self.gotonews)
        self.but_condoc.clicked.connect(self.gotocondoc)
        self.but_stat.clicked.connect(self.gotostats)
        self.but_log.clicked.connect(self.gotowelcome)

    def gotowelcome(self):
        w = WelcomeScreen()
        widget.addWidget(w)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gototest(self):
        asse = AssessmentScreen()
        widget.addWidget(asse)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoabout(self):
        abt = AboutScreen()
        widget.addWidget(abt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotonews(self):
        news = NewsScreen()
        widget.addWidget(news)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocondoc(self):
        condoc = DoctorContactScreen()
        widget.addWidget(condoc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotostats(self):
        stats = SummaryScreen()
        widget.addWidget(stats)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AssessmentScreen(QDialog):

    def __init__(self):
        super(AssessmentScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\AssessmentPage.ui', self)
        self.but_home.clicked.connect(self.gotohome)
        self.but_sub.clicked.connect(self.gotosubmit)

    def gotohome(self):
        home = Homescreen_U()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosubmit(self):
        if self.q11.isChecked() == False and self.q12.isChecked() == False and self.q13.isChecked() == False and self.q14.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q21.isChecked() == False and self.q22.isChecked() == False and self.q23.isChecked() == False and self.q24.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q31.isChecked() == False and self.q32.isChecked() == False and self.q33.isChecked() == False and self.q34.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q41.isChecked() == False and self.q42.isChecked() == False and self.q43.isChecked() == False and self.q44.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q51.isChecked() == False and self.q52.isChecked() == False and self.q53.isChecked() == False and self.q54.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q61.isChecked() == False and self.q62.isChecked() == False and self.q63.isChecked() == False and self.q64.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q71.isChecked() == False and self.q72.isChecked() == False and self.q73.isChecked() == False and self.q74.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q81.isChecked() == False and self.q82.isChecked() == False and self.q83.isChecked() == False and self.q84.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q91.isChecked() == False and self.q92.isChecked() == False and self.q93.isChecked() == False and self.q94.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q101.isChecked() == False and self.q102.isChecked() == False and self.q103.isChecked() == False and self.q104.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q111.isChecked() == False and self.q112.isChecked() == False and self.q113.isChecked() == False and self.q114.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q121.isChecked() == False and self.q122.isChecked() == False and self.q123.isChecked() == False and self.q124.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        elif self.q131.isChecked() == False and self.q132.isChecked() == False and self.q133.isChecked() == False and self.q134.isChecked() == False:
            self.lab_error3.setText('Please answer all questions!')
        else:
            p = ['q11', 'q12', 'q13', 'q14', 'q21', 'q22', 'q23', 'q24', 'q31', 'q32', 'q33', 'q34', 'q41', 'q42', 'q43', 'q44',
                 'q51', 'q52', 'q53', 'q54', 'q61', 'q62', 'q63', 'q64', 'q71', 'q72', 'q73', 'q74', 'q81', 'q82', 'q83', 'q84',
                 'q91', 'q92', 'q93', 'q94', 'q101', 'q102', 'q103', 'q104', 'q111', 'q112', 'q113', 'q114', 'q121', 'q122',
                 'q123', 'q124', 'q131', 'q132', 'q133', 'q134']
            con = sqlite3.connect("pyminproj")
            cur = con.cursor()

            for i in p:
                e = "select "+ i +" from assess where extra=1"
                cur.execute(e)
                o = cur.fetchone()
                if self.q11.isChecked():
                    for r in str(o):
                        print("qwer")
                        if r.isnumeric():
                            v = "update assess set "+ i + "="+ r + "+1 where extra=1"
                            cur.execute(v)
            con.commit()
            con.close()
            print('Data Entered Successfully')
            self.gotohome()


class NewsScreen(QDialog):
    def __init__(self):
        super(NewsScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\NewsPage.ui', self)
        self.but_home.clicked.connect(self.gotohome)
        self.but_refresh.clicked.connect(self.refresh)

    def gotohome(self):
        home = Homescreen_U()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def refresh(self):
        key = "97ef515a080048b1bd181f33bcdbf754"
        url = "https://newsapi.org/v2/top-headlines?q=covid&language=en&sortBy=popularity&apiKey=" + key
        news = requests.get(url).json()
        articles = news["articles"]
        myart = []
        mynews = ""
        for a in articles:
            myart.append(a["title"] + "\n" + a['url'])
        for i in range(10):
            mynews = mynews + str(i + 1) + ". " + myart[i] + "\n\n"
        self.labb.clear()
        print(mynews)
        self.labb.append(mynews)


class DoctorContactScreen(QDialog):
    def __init__(self):
        super(DoctorContactScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\DoctorContact.ui', self)
        self.but_home.clicked.connect(self.gotohome)

    def gotohome(self):
        home = Homescreen_U()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SummaryScreen(QDialog):
    def __init__(self):
        super(SummaryScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\SummaryPage.ui', self)
        self.but_home.clicked.connect(self.gotohome)
        self.q1.clicked.connect(self.graph1)
        self.q2.clicked.connect(self.graph2)
        self.q3.clicked.connect(self.graph3)
        self.q4.clicked.connect(self.graph4)
        self.q5.clicked.connect(self.graph5)
        self.q6.clicked.connect(self.graph6)
        self.q7.clicked.connect(self.graph7)
        self.q8.clicked.connect(self.graph8)
        self.q9.clicked.connect(self.graph9)
        self.q10.clicked.connect(self.graph10)
        self.q11.clicked.connect(self.graph11)
        self.q12.clicked.connect(self.graph12)
        self.q13.clicked.connect(self.graph13)

    def gotohome(self):
        home = Homescreen_U()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph1(self):
        a1 = ['1st Dose ', '2nd Dose', '3rd Dose', '4th Dose']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q11,q12,q13,q14 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a1, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph2(self):
        a2 = ['No', 'Mild', 'Severe', 'Past Injury']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q21,q22,q23,q24 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a2, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph3(self):
        a3 = ['No', '1 week', '2 week', '3 weeks']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q31,q32,q33,q34 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a3, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph4(self):
        a4 = ['No', 'Mild', 'Severe', 'Other Reason']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q41,q42,q43,q44 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a4, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph5(self):
        a5 = ['No', 'Sometimes', 'Many Times', 'Blood Womit']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q51,q52,q53,q54 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a5, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph6(self):
        a6 = ['No', '1 week', '2 week', '3 week']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q61,q62,q63,q64 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a6, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph7(self):
        a7 = ['No', '1 week', '2 week', '3 week']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q71,q72,q73,q74 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a7, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph8(self):
        a8 = ['No', '1 week', '2 week', '3 week']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q81,q82,q83,q84 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a8, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph9(self):
        a9 = ['No', '1 week', '2 week', '3 week']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q91,q92,q93,q94 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a9, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph10(self):
        a10 = ['No', 'Mild', 'Severe', 'Other Reason']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q101,q102,q103,q104 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a10, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph11(self):
        a11 = ['No', 'Mild', 'Severe', 'Totally']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q111,q112,q113,q114 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a11, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph12(self):
        a12 = ['No', '1 week', '2 week', '3 week']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q121,q122,q123,q124 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a12, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()

    def graph13(self):
        a13 = ['No', '1 week', '2 week', '3 week']
        b = []
        con = sqlite3.connect("pyminproj")
        cur = con.cursor()
        q = "select q131,q132,q133,q134 from assess where extra=1;"
        cur.execute(q)
        z = cur.fetchone()
        for x in z:
            b.append(x)
        con.commit()
        con.close()
        print('Data Entered Successfully')
        print(b)

        plt.style.use('fivethirtyeight')
        plt.bar(a13, b, 0.5, color="Red")
        plt.xlabel('Options')
        plt.ylabel('People')
        plt.tight_layout()
        plt.show()


class AboutScreen(QDialog):
    def __init__(self):
        super(AboutScreen, self).__init__()
        loadUi('D:\\Codes\\2nd_year_SEM4\\Python_Lab\\Designer_EXE\\AboutusPage.ui', self)
        self.but_home.clicked.connect(self.gotohome)

    def gotohome(self):
        home = Homescreen_U()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    load = LoadingScreen()
    wel = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    load.show()
    load.progress()
    widget.addWidget(wel)
    load.finish(widget)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

