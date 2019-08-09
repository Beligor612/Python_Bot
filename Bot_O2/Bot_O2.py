import paramiko
import logging
import time 

import Mikrot
import Base_O2
import aiogram
import BackUp

#API_TOKEN = '855313094:AAFm36oeX-c72ps6itp3Icco8AQrcH4jDcY'
#logging.disable()
#bot = aiogram.Bot(token = API_TOKEN)
#dp = aiogram.Dispatcher(bot)

logging.basicConfig(level = logging.DEBUG, format = '--%(message)s')

# 1) Получить список активных комплекто
# 2) Взять список комплектов с О2 и сравнить их с активными
# 3) Запустить проверку траффика
# 3.1) Получить инфу о комплекте
# 3.2) Подключится к микротику комплекта О2 и вытащить траффик
# 3.3) Провести операции с траффиком и записи статусов 
# 3.4) Вернуть статус и вывести сообщение в бот
while True:
	#Часть кода для проверки даты и создания бэкапа таблицы с траффиком по О2
	backup = BackUp.Need_Beckup()
	backup.check_date()
	print("I finish beckup")
	bot_mikrotik = Mikrot.Mikrotik('vpnbus.test.net.ua', 'fiway', 'BusWifi')
	bot_mikrotik.Connect()
	list_All_active = bot_mikrotik.list_active_complect()
	bot_mikrotik.close_connection()
	print("I conected to complect ")
	list_O2 = Base_O2.Database_O2()
	bus_with_O2 = list_O2.list_bus_with_o2()
	list_checkup = [] # Список комплектов для проверки траффика
	for bus_O2 in bus_with_O2:
		if bus_O2 in list_All_active:
			list_checkup.append(bus_O2) # Создать список комплектов для проверки статуса
	print("Complects to checked: {0}".format(list_checkup))
	logging.debug("Online {0} complects with O2".format(len(list_checkup)))
	for bus in list_checkup:
		#logging.debug(list_O2.bus_info(bus))
		infostring = list_O2.bus_info(bus)
		logging.debug("Connected to {0}.....".format(bus))
		con_O2_mikrotik = Mikrot.Mikrotik(infostring[0], infostring[1], infostring[2])
		con_O2_mikrotik.Connect()
		try:
			trafic = con_O2_mikrotik.trafic('O2')
			logging.debug("Traffic record {0} Mb\n".format(trafic))
			con_O2_mikrotik.close_connection()
			list_O2.trafic_record(trafic, bus)
		except:
			logging.debug("Error. Connection Failed !")
			continue
	logging.debug("I Sleep a 20 second\n ")
	time.sleep(20)

list_O2.close_session()



