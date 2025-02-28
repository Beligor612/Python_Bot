import logging
from Mikrotik import Active_Complekt, Active, Connection_O2, Active_For_O2, Connection_For_O2
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from time import ctime
from DB_O2 import Exex_2, Exex_1, Exex_3, Status, Traffic_Null
from Check_All_Base import Check_From_Table
import random
import DB_O2
import async_timeout
import aiohttp

#nest_asyncio.apply()
API_TOKEN = '855313094:AAFm36oeX-c72ps6itp3Icco8AQrcH4jDcY'
# Configure logging
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(message)s')

# Initialize bot and dispatcher
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

async def Send_Message(bus, result_status):
	Klient = Check_From_Table(bus)[0]
	logging.debug("Send_Message KLIENT : {0}".format(Klient))
	logging.debug("Send_Message STATUS: {0}".format(result_status))
	if result_status == 0:
		logging.debug("Send_Message STATUS = 0 ---- Null")
	elif result_status == 1:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 10 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 10 GB".format(Klient ,bus, result_status))
	elif result_status == 2:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 15 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 15 GB".format(Klient ,bus, result_status))
	elif result_status == 3:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 18 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 18 GB".format(Klient ,bus, result_status))
	elif result_status == 4:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, "\u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f\n \
		 \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 20 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, "\u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f\n \
		 \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 20 GB".format(Klient ,bus, result_status))
	elif result_status == 5:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 30 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 30 GB".format(Klient ,bus, result_status))
	elif result_status == 6:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 30 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 35 GB".format(Klient ,bus, result_status))
	elif result_status == 7:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 30 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 38 GB".format(Klient ,bus, result_status))
	elif result_status == 8:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, "\u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f\n \
		 \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 40 GB ".format(Klient ,bus, result_status))
		await bot.send_message(892855145, "\u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f\n \
		 \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 40 GB ".format(Klient ,bus, result_status))
	elif result_status == 9:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 50 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 50 GB".format(Klient ,bus, result_status))
	elif result_status == 10:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 55 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 55 GB".format(Klient ,bus, result_status))
	elif result_status == 11:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 58 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 58 GB".format(Klient ,bus, result_status))
	elif result_status == 12:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, "\u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f\n \
		 \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 60 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, "\u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f \u26a0\ufe0f\n \
		 \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 60 GB".format(Klient ,bus, result_status))
	else:
		print ("Null")

async def Checked_O2(bus_number):
	logging.debug('Start programm')
	Bus_Info = Exex_3(bus_number)
	logging.debug("Bus info: {0}".format(Bus_Info))
	check_trafic = await asyncio.wait_for(Connection_For_O2(bus_number, Bus_Info[0][0], Bus_Info[0][1], Bus_Info[0][2]), 15)
	result_status = Status(bus_number)
	await Send_Message(bus_number, result_status)

async def Check_O2(bus_archive):
	#List_Checked = []
	while True:
		List_Checked = []
		try:
			logging.debug("LIST CHECKED IN START: {0}".format(List_Checked))
			bus_active = Active_For_O2()
			#print("bus_archive: ", bus_archive)
			for bus_number in bus_archive:
				if bus_number in bus_active:
					 List_Checked.append(bus_number)
					 #logging.debug(List_Checked)
					 #asyncio.wait_for(asyncio.create_task(bus_number),15)
				else:
					Traffic_Null(bus_number)
					logging.debug("Komplect {0} Offline".format(bus_number))
					logging.debug('%s Offline'%(bus_number))
			for bus in List_Checked:
				#logging.debug(List_Checked)
				await asyncio.wait_for(asyncio.create_task(Checked_O2(bus)),15)
				#del List_Checked[bus]
			#await asyncio.wait_for(asyncio.gather(*[Checked_O2(bus_number) for bus_number in List_Checked]), 15)
		except Exception as e:
			logging.debug("EXCEPTION : {0}".format(e))
			pass
			logging.debug("I Am Sleeep!!!!")
			logging.debug('List_Checked {0}'.format(List_Checked))
			logging.debug("End GAME")
			await asyncio.sleep(10)

async def Check_Status(bus_number):
	Status(bus_number)

async def Run_Check_O2():
	bus_archive = Exex_1()
	print ("Running Check O2")
	ioloop = asyncio.get_event_loop()
	tasks = [await asyncio.wait_for(ioloop.create_task(Check_O2(bus_archive)),timeout = 15)]
	ioloop.run_until_complete(tasks)

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait([asyncio.ensure_future(Run_Check_O2())]))
	loop.close()

	