import Mikrot

class Checker:
	mikrot_connect = Mikrot()

	def check_bus(self, bus_number):
		if bus_number in mikrot_connect.list_active_complect():
			return True
		else:
			return False

	
