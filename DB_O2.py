import sqlite3
import asyncio


connect = sqlite3.connect("DB_O2_Test.db")
cursor = connect.cursor()


def Exex_1(): #Bus_Archive
	Bus_archive = []
	Bus = []
	exe_1 = "SELECT Bus FROM Check_O2"
	Bus_List = cursor.execute(exe_1).fetchall()
	for i in Bus_List:
		Bus_archive.append(i[0])
	#print(Bus_archive)
	#print (Bus_archive)
	return Bus_archive

def Exex_2(): #Login Bus From Archive
	exe_2 = "SELECT Adress, Login, Password, Trafic, Trafic0 FROM Check_O2 WHERE Bus = ?"
	Archive = Exex_1()
	for i in Archive:
		One_Line = cursor.execute(exe_2, [(i)]).fetchall()
		Adress = One_Line[0][0]
		Login = One_Line[0][1]
		Password = One_Line[0][2]
		Trafic = One_Line[0][3]
		print(" Adress: ",Adress,'\n',
			"Login: ",Login,'\n',
			"Password: ",Password,'\n', 
			"Trafic: ",Trafic,'\n')

def Exex_3(bus):
	exe_2 = "SELECT Adress, Login, Password, Trafic FROM Check_O2 WHERE Bus = ?"
	Archive = Exex_1()
	One_Line = cursor.execute(exe_2, [bus]).fetchall()
	print ("OneList from DB_O2: ", One_Line)
	#print(bus, '\n',
			#One_Line[0][0], '\n',
			#One_Line[0][1], '\n',
			#One_Line[0][2], '\n',)
	return One_Line

def Trafic_Down(trafic, bus):
		"""
		1.Берем текущий трафик trafic и сравниваем с предыдущм Trafic01. 
		2.Разницу между ними плюсуем к переменной
		Trafic_up и записываем в БД. 
		3.Полученный текущий трафик аписываем в переменную Trafic0
		"""
		exe = "SELECT Trafic FROM Check_O2 WHERE Bus = ?"
		Trafic_up = cursor.execute(exe, [bus]).fetchall()[0][0] # Берет текущий Трафик
		#print ("Trafic: ", Trafic_up)
		exe_4 = "SELECT Trafic0 FROM Check_O2 WHERE Bus = ?"
		Trafic01 = cursor.execute(exe_4, [bus]).fetchall()[0][0] # Берет из Трафик0 предыдущий трафик
		if Trafic01 > trafic:
			exe_3 = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
			Trafic0 = cursor.execute(exe_3, [trafic, bus])
			Trafic_up2 = trafic # Сравниваем 2 трафика
			Trafic_up2 = round((Trafic_up + Trafic_up2),2)
		else:
			Trafic_up2 = abs(Trafic01 - trafic) # Сравниваем 2 трафика
			Trafic_up2 = round((Trafic_up + Trafic_up2),2)
		#print ("Trafic01: ", Trafic01)
		Trafic_up2 = abs(trafic - Trafic01) # Сравниваем 2 трафика
		Trafic_up2 = round((Trafic_up + Trafic_up2),2)
		exe_2 = "UPDATE Check_O2 SET Trafic = ? WHERE Bus = ?"
		Trafic_down = cursor.execute(exe_2, [Trafic_up2, bus])# Записывает трафик в трафик
		exe_3 = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
		Trafic0 = cursor.execute(exe_3, [trafic, bus])# Записывает текущий Трафик0
		#print("Trafic0: ", Trafic0)
		#print (type (Trafic_up), type(Trafic01), type(trafic))
		#print ("Trafic = {0} + ({1}-{2})".format(Trafic_up, trafic, Trafic01))
		#print ("SummaTraffica: ", Trafic_up2)
		#print ("Trafic: ", Trafic_down)
		connect.commit()
		print ("Трафик по комплекту {0} удачно отложено {1} !!!!".format(bus, trafic), '\n')
		return True

async def Status(bus):
	exe = "SELECT Status FROM CHECK_O2 WHERE Bus =?"
	status = cursor.execute(exe, [bus]).fetchall()
	print (status)
	return status


if __name__ == "__main__":
	Exex_1()
	Exex_2()

