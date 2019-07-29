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
