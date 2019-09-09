import TW
import telebot
import logging
import datetime

API = "826188556:AAEqXkTSO_fPPrsBZ7bXpFg86vl8jordYhw"
bot = telebot.TeleBot(API)
#logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s--%(message)s')

tw = TW.Ternwoyazh()
tw.Connect()
tw.CheckKlient()
lst = tw.Check_Online_Klient(tw.CheckKlient())
bot.send_message(386869436, " На момент {0} 3 дня и больше: ".format(datetime.datetime.now()))
for value,key in zip(lst.values(), lst.keys()):
    STR = ""
    if value != {}:
        for i in value.items():
            STR += i[0] + " : " + i[1] + "\n"
        bot.send_message(386869436, "{0} \n {1}".format(key, STR))
tw.CloseConnect()