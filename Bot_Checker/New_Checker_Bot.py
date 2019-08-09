import Mikrot
import Check_All_Base

class Checker:
	def __init__(self):
		mikrot_connect = Mikrot.Mikrotik()
		mikrot_connect.Connect()
		self.list_acrive = mikrot_connect.list_active_complect()
		mikrot_connect.close_connection()
		self.cursor_base = Check_All_Base.All_Base()

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

	def insert_time_connection(self, bus_number):
		self.cursor_base.Set_Time(bus_number)
		return print("Time record")

	def insert_comment(self, bus_number = "bus0000", komment = " "):
		self.cursor_base.Set_Koment(bus_number, komment)
		return print ("Comment Record")







	









