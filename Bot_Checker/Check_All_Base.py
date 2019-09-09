import sqlite3
import time
import datetime

class All_Base:
	connect = sqlite3.connect("DB_All_For_Complect.db")
	cursor = connect.cursor()

	def Check_From_Table(self, bus):
		check = "SELECT Klient, Tarif1, Tarif2, Tarif3, Tarif4, Nomer1, Nomer2, Nomer3, Nomer4, VSeti, Komment From All_Complect WHERE Komplect = ?"
		Check_Where_Komplect = self.cursor.execute(check, [bus]).fetchall()
		#print("CWK: ", Check_Where_Komplect, len(Check_Where_Komplect))
		Klient = Check_Where_Komplect[0][0]
		Tarif1 = Check_Where_Komplect[0][1]
		Tarif2 = Check_Where_Komplect[0][2]
		Tarif3 = Check_Where_Komplect[0][3]
		Tarif4 = Check_Where_Komplect[0][4]
		Nomer1 = Check_Where_Komplect[0][5]
		Nomer2 = Check_Where_Komplect[0][6]
		Nomer3 = Check_Where_Komplect[0][7]
		Nomer4 = Check_Where_Komplect[0][8]
		VSeti = Check_Where_Komplect[0][9]
		Komment = Check_Where_Komplect[0][10]
		#print (Check_Where_Komplect)
		"""print ("Комплект: ", bus, '\n', 
				"Клиент: ", Klient, '\n',
				"Тарифы: ",'\n', 
				Tarif1, "|", Nomer1, '\n',
				Tarif2, "|", Nomer2,'\n',
				Tarif3, "|", Nomer3,'\n',
				Tarif4, "|", Nomer4,'\n', 
				"В сети: ", VSeti, '\n',
				"Комментарий: ", Komment)"""

		return Klient,Tarif1,Tarif2,Tarif3,Tarif4,Nomer1,Nomer2,Nomer3,Nomer4,VSeti, Komment

	def Set_Time(self, bus):
		dt = datetime.datetime.now()
		dt_string = dt.strftime('%d.%m.%Y %H:%M:%S')
		set_time = "UPDATE All_Complect SET VSeti = ? WHERE Komplect = ?"
		self.cursor.execute(set_time,[dt_string,bus])
		self.connect.commit()
		
		connect2 = sqlite3.connect("ADM.db")
		cursor2 = connect2.cursor()
		set_time = "UPDATE Admin SET Online = ? WHERE Komplect = ?"
		cursor2.execute(set_time,[dt_string,bus])
		connect2.commit()

	def Set_Koment(self, bus, komment):
		#print ("Запускаю запись в БД")
		#print ("Koment 2 : ", komment)
		set_koment = "UPDATE All_Complect SET Komment = ? WHERE Komplect = ?"
		self.cursor.execute(set_koment, [komment, bus])
		self.connect.commit()
		#print ("Коментарий записан")



