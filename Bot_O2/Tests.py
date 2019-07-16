import Mikrot
import Base_O2
import time
a = Mikrot.Mikrotik('172.31.2.40', 'wifibus', 'BusWifi')
a.Connect()
#a.list_active_complect()
for i in range(60):
	a.check_speed("Lifecell")
	a.check_speed("O2")
	a.check_speed("Play")
	print('\n')
	time.sleep(1)
a.close_connection()

"""b = Base_O2.Database_O2()
print("List Connection O2: ", b.list_bus_with_o2())
print("List Info Connection O2: ", b.bus_info_all())
print("Info a Bus0009: ", b.bus_info("bus0009"))
b.check_status(15001.0, 2, "bus0009")"""