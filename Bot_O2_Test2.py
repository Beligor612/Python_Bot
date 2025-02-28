import logging
from Mikrotik import Active_Complekt, Active, Connection_O2
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

async def Message(bus, check_trafic):
		print ("Hellow")
		await bot.send_message(386869436, "\u2705 Комплект %s \n \u267b\ufe0f Трафик: %s Mb"% (bus, check_trafic))
		#await asyncio.sleep(1)


"""async def Check_O2_Eline(bus):
	print ("Запущена проверка автобусов О2", ctime())
	online = True
	while online == True:
		try:
			print ("Check 1", bus)
			O2_Online = await asyncio.wait_for(Active_Complekt(bus),15)
			print("Комплект в сети: ", O2_Online)
			if O2_Online == True:
				print ("Checked 2: True")
				Bus_Info = Exex_3(bus)
				print (Bus_Info)
				check_trafic = Connection_O2(bus, Bus_Info[0][0], Bus_Info[0][1], Bus_Info[0][2])
				print ("Печатаю сообщение")
				task = asyncio.create_task(bot.send_message(386869436, "\u2705 Комплект %s \n \u267b\ufe0f Трафик: %s Mb"% (bus, check_trafic)))
				await task
				print("Засыпаю на 30 секунд ", ctime())
				await asyncio.sleep(60)
			else: 
				print ("Checked 2: False")
				print("Bus: ", bus)
				Db_null_trafic = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
				DB_O2.cursor.execute(Db_null_trafic, [0 ,bus])
				DB_O2.connect.commit()
				print ("Засыпаю на 5 минут ", ctime())
				await asyncio.sleep(60)
		except Exception as e:
			print("EXCEPTION :", e ,ctime())
			pass"""


async def Check_O2_Eline_Test(bus):
	print ("Запущена проверка автобусов О2", ctime())
	online = True
	while online == True:
		print ("Check 1", bus)
		O2_Online = await asyncio.create_task(Active_Complekt(bus))
		print("Комплект в сети: ", O2_Online)
		if O2_Online == True:
			print ("Checked 2: True")
			Bus_Info = Exex_3(bus)
			print (Bus_Info)
			check_trafic = Connection_O2(bus, Bus_Info[0][0], Bus_Info[0][1], Bus_Info[0][2])
			print ("Печатаю сообщение")
			await bot.send_message(386869436, "\u2705 Комплект %s \n \u267b\ufe0f Трафик: %s Mb"% (bus, check_trafic))
			#await asyncio.wait_for(await bot.send_message(386869436, "\u2705 Комплект %s \n \u267b\ufe0f Трафик: %s Mb"% (bus, check_trafic)),timeout = 1.0)
			#await Message(bus,check_trafic)
			print("Засыпаю на 30 секунд ", ctime())
			await asyncio.sleep(60)
		else: 
			print ("Checked 2: False")
			print("Bus: ", bus)
			Db_null_trafic = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
			DB_O2.cursor.execute(Db_null_trafic, [0 ,bus])
			DB_O2.connect.commit()
			print ("Засыпаю на 5 минут ", ctime())
			await asyncio.sleep(60)

async def Check_O2_Eline_Test2(bus):
	print ("Запущена проверка автобусов О2", ctime())
	online = True
	while online == True:
		try:
			print ("Check 1", bus)
			O2_Online = await asyncio.wait_for(Active_Complekt(bus),15)
			print("Комплект в сети: ", O2_Online)
			if O2_Online == True:
				#async_timeout.timeout(10)
				print ("Checked 2: True")
				Bus_Info = Exex_3(bus)
				print (Bus_Info)
				check_trafic = Connection_O2(bus, Bus_Info[0][0], Bus_Info[0][1], Bus_Info[0][2])
				print ("Печатаю сообщение")
				await Message(bus, check_trafic)
				#task = asyncio.create_task(bot.send_message(386869436, "\u2705 Комплект %s \n \u267b\ufe0f Трафик: %s Mb"% (bus, check_trafic)))
				#await task
				print("Засыпаю на 30 секунд ", ctime())
				await asyncio.sleep(60)
			else: 
				print ("Checked 2: False")
				print("Bus: ", bus)
				Db_null_trafic = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
				DB_O2.cursor.execute(Db_null_trafic, [0 ,bus])
				DB_O2.connect.commit()
				print ("Засыпаю на 5 минут ", ctime())
				await asyncio.sleep(60)
		except Exception as e:
			print("EXCEPTION :", e ,ctime())
			pass

async def Check_Status(bus_number):
	Status(bus_number)

async def Run_Check_O2():
	bus_archive = Exex_1()
	print ("Running Check O2")
	#print (type(bus_archive), bus_archive[0])
	tasks = []
	loop = asyncio.get_event_loop()
	for bus_number in bus_archive:
		#loop = asyncio.get_event_loop()
		loop.run_until_complete(asyncio.wait([asyncio.ensure_future(Check_O2_Eline_Test2(bus_number))]))
		loop.close()

if __name__ == "__main__":
	asyncio.create_task(Run_Check_O2())

	