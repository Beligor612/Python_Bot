import sqlite3
import datetime
import telebot
import logging
import time


class Ternwoyazh:
    def Connect(self):
        self.connect = sqlite3.connect("DB_All_For_Complect.db")
        self.cursor = self.connect.cursor()

    def CloseConnect(self):
        self.connect.close()

    """ def _DataFromDatabase(self):
        lst = {}
        command = "SELECT VSeti From All_Complect WHERE Klient = ?"
        command2 = "SELECT Komplect From All_Complect WHERE Klient = ?"
        exe = self.cursor.execute(command, ['ПП "Тернвояж"']).fetchall()
        exe2 = self.cursor.execute(command2, ['ПП "Тернвояж"']).fetchall()
        for k,i in zip(exe2,exe):
            lst.update({k[0]:i[0]})
        return lst

    def Datetime(self, date):
        self.date = date
        #print("date: ", date)
        now = datetime.datetime.now()
        delta = datetime.timedelta(days = -3) + now
        #print(delta)
        date_time = datetime.datetime.strptime(date,'%d.%m.%Y')
        if date_time <= delta:
            return True
        else:
            return False
    
    def _CheckDatetime(self):
        checklist = []
        lst = self._DataFromDatabase()
        for k,i in zip(lst.keys(), lst.values()):
            date = i[0:10]
            if self.Datetime(date) == True:
                checklist.append([k,i[0:10]])
            else:
                continue
        return checklist """

    def CheckKlient(self):
        connect = sqlite3.connect("ADM.db")
        cursor = connect.cursor()
        command = "SELECT Klient From Admin"
        set_klient = set(cursor.execute(command).fetchall())
        connect.close()
        return set_klient

    def Check_Online_Klient(self, set_klient):
        lst_klient_and_komplect = {}
        command2 = "SELECT Komplect, VSeti From All_Complect WHERE Klient = ?"
        for kl in set_klient:
            lst_active = self.cursor.execute(command2, [kl[0]]).fetchall()
            #print(kl[0], " ", lst_active, "\n")
            not_active_lst = self.Check_Status(lst_active)
            lst_klient_and_komplect[kl[0]] = not_active_lst
        return lst_klient_and_komplect
    
    def Check_Status(self, lst_active):
        #print(lst_active)
        lst_not_active = {}
        for l in lst_active:
            if not len(l[1]) <= 1:
                date_form_lst = datetime.datetime.strptime(l[1][0:10], '%d.%m.%Y')
                if self.Compare_Date(date_form_lst) == True:
                    lst_not_active[l[0]] = l[1]
        #print("NOT ACTIVE: ", lst_not_active)
        return lst_not_active

    def Compare_Date(self, date):
        self.date = date
        now = datetime.datetime.now()
        delta = datetime.timedelta(days = -3) + now
        if date <= delta:
            return True
        else:
            return False
        





""" API = "826188556:AAEqXkTSO_fPPrsBZ7bXpFg86vl8jordYhw"
bot = telebot.TeleBot(API)
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s--%(message)s')
bot.send_message(892855145, "Hellow")
TW = Ternwoyazh()
logging.debug("Connection to database")
while True:
    TW.Connect()
    stR = '12:51:0'
    now = datetime.datetime.now()
    str2 = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    #print(str2)
    if stR == str2:
        STR = "Комплекты которых давно не было в сети \n"
        check_list = TW._CheckDatetime()
        logging.debug("CHECK_LIST: {0}".format(check_list))
        logging.debug("STR: {0}".format(STR))
        for i in check_list:
            STR += '\u26a0\ufe0f {0}   {1} \n'.format(i[0],i[1])
            logging.debug("STR: {0}".format(STR))
        if len(STR) > 0:
            logging.debug("STR1: {0}".format(STR))
            bot.send_message(386869436, STR)
            TW.CloseConnect()
            time.sleep(82000) """