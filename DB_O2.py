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

def Check_Status(trafic, status, bus):
	if trafic >= 10000.0 and status == 0:
		status = 1
		Status_up(bus, status)
		return status
	elif trafic >= 15000.0 and status == 1:
		status = 2
		Status_up(bus, status)
		return status
	elif trafic >= 18000.0 and status == 2:
		status = 3
		Status_up(bus, status)
		return status
	elif trafic >= 20000.0 and status == 3:
		status = 4
		Status_up(bus, status)
		return status
	elif trafic >= 30000.0 and status == 4:
		status = 5
		Status_up(bus, status)
		return status
	elif trafic >= 35000.0 and status == 5:
		status = 6
		Status_up(bus, status)
		return status
	elif trafic >= 38000.0 and status == 6:
		status = 7
		Status_up(bus, status)
		return status
	elif trafic >= 40000.0 and status == 7:
		status = 8
		Status_up(bus, status)
		return status
	elif trafic >= 50000.0 and status == 8:
		status = 9
		Status_up(bus, status)
		return status
	elif trafic >= 55000.0 and status == 9:
		status = 10
		Status_up(bus, status)
		return status
	elif trafic >= 58000.0 and status == 10:
		status = 11
		Status_up(bus, status)
		return status
	elif trafic >= 60000.0 and status == 11:
		status = 12
		Status_up(bus, status)
		return status
	else:
		print ("None")
	return status
def Status_up(bus, status):
	exe = "UPDATE CHECK_O2 SET Status = ? WHERE Bus =?"
	status_up = cursor.execute(exe, [status, bus])
	connect.commit()

def Status(bus):
	exe = "SELECT Trafic FROM CHECK_O2 WHERE Bus =?"
	exe_status = "SELECT Status FROM CHECK_O2 WHERE Bus =?"
	trafic = cursor.execute(exe, [bus]).fetchall()[0][0]
	status = cursor.execute(exe_status, [bus]).fetchall()[0][0]
	result_status = Check_Status(trafic, status, bus)
	#print ("result_status: " ,result_status)
	return result_status

if __name__ == "__main__":
	Exex_1()
	Exex_2()

