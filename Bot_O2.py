import logging
from Mikrotik import Active_Complekt, Active, Connection_O2, Active_For_O2
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from time import ctime
from DB_O2 import Exex_2, Exex_1, Exex_3, Status
from Check_All_Base import Check_From_Table
import random
import DB_O2
import async_timeout
import aiohttp

#nest_asyncio.apply()
API_TOKEN = '855313094:AAFm36oeX-c72ps6itp3Icco8AQrcH4jDcY'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

async def Send_Message(bus, result_status):
	Klient = Check_From_Table(bus)[0]
	print("KLIENT : ",Klient)
	print ("STATUS: ", result_status)
	if result_status == 0:
		print ("Null")
	elif result_status == 1:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 10 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 10 GB".format(Klient ,bus, result_status))
	elif result_status == 2:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 10 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 15 GB".format(Klient ,bus, result_status))
	elif result_status == 3:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 10 GB".format(Klient ,bus, result_status))
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
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 50 GB".format(Klient ,bus, result_status))
		await bot.send_message(892855145, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 55 GB".format(Klient ,bus, result_status))
	elif result_status == 11:
		print("PECHAT: ", Klient, bus, result_status)
		await bot.send_message(386869436, " \nКлиент: {0} \n Комплект: {1} \n Статус: {2} \n Расходы: 50 GB".format(Klient ,bus, result_status))
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
	print("Step 1 Start")
	print("Komplect {0} online".format(bus_number))
	print("Start Checked")
	Bus_Info = Exex_3(bus_number)
	print ("Bus info: ", Bus_Info)
	check_trafic = Connection_O2(bus_number, Bus_Info[0][0], Bus_Info[0][1], Bus_Info[0][2])
	print("Timer: ", ctime())
	result_status = Status(bus_number)
	await Send_Message(bus_number, result_status)

async def Check_O2(bus_archive):
	List_Checked = []
	while True:
		try:
			bus_active = Active_For_O2()
			print("bus_archive: ", bus_archive)
			for bus_number in bus_archive:
				if bus_number in bus_active:
					 List_Checked.append(bus_number)
				else:
					print("Komplect {0} Offline".format(bus_number))

			await asyncio.gather(*[Checked_O2(bus_number) for bus_number in List_Checked])
		except Exception as e:
			print("EXCEPTION :", e ,ctime())
			pass
		print("I Am Sleeep!!!!")
		print("List_Checked: ", List_Checked)
		await asyncio.sleep(1)

async def Check_Status(bus_number):
	Status(bus_number)

async def Run_Check_O2():
	bus_archive = Exex_1()
	#print("Bus_Checked:", bus_checked)
	#print("Active active_complect: ", active_complect)
	print ("Running Check O2")
	task = asyncio.create_task(Check_O2(bus_archive))
	await task
	#print (type(bus_archive), bus_archive[0])
	#tasks = []
	#await asyncio.gather(*[Check_O2(bus_number) for bus_number in bus_checked])
	#await asyncio.sleep(120)

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait([asyncio.ensure_future(Run_Check_O2())]))
	loop.close()

	