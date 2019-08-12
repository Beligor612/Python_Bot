import Mikrot
import Check_All_Base
import datetime
import sqlite3
class Checker:
	def __init__(self):
		mikrot_connect = Mikrot.Mikrotik()
		mikrot_connect.Connect()
		self.list_acrive = mikrot_connect.list_active_complect()
		mikrot_connect.close_connection()
		self.cursor_base = Check_All_Base.All_Base()
		self.insert_time_connection()
	def check_bus(self, bus_number): # Проверяет активен ли сейчас комплект
		if bus_number in self.list_acrive:
			return True
		else:
			return False
	def online_bus(self, bus_number, komment):
		pass

	def check_inform(self, bus_number):
		lst_inform = self.cursor_base.Check_From_Table(bus_number)
		return lst_inform

	def insert_time_connection(self):
		if self.check_time() == True:
			for bus_number in self.list_acrive:
				self.cursor_base.Set_Time(bus_number);
			self.database()
		return print("Time record")

	def insert_comment(self, bus_number = "bus0000", komment = " "):
		self.cursor_base.Set_Koment(bus_number, komment)
		return print ("Comment Record")
	
	def check_time(self):
		connect = sqlite3.connect("New_Time.db")
		cusrsor = connect.cursor()
		exe_command = "SELECT Delta FROM Date"
		now_time = cusrsor.execute(exe_command).fetchall()[0][0]
		""" now_time = datetime.datetime.strptime((now_time), '%Y-%b-%d %I:%M:%S') """
		now = datetime.datetime.strftime (datetime.datetime.now(),'%Y-%b-%d %I:%M:%S')
		if now_time < now:
			return True
		else: 
			print ("Delta: ", now_time, " ", " Won_time: ", now)
			return False
	
	def database(self):
		now = datetime.datetime.now()
		delta = datetime.timedelta(minutes = 2) + now
		delta = datetime.datetime.strftime(delta, '%Y-%b-%d %I:%M:%S')
		now = datetime.datetime.strftime(now,'%Y-%b-%d %I:%M:%S')
		connect = sqlite3.connect("New_Time.db")
		cusrsor = connect.cursor()
		exe_command = "UPDATE Date SET Date = ?"
		cusrsor.execute(exe_command,[now])
		exe_command = "UPDATE Date SET Delta = ?"
		cusrsor.execute(exe_command,[delta])
		connect.commit()
		return delta





	









