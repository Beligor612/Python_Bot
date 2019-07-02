import logging
from Mikrotik import Active_Complekt, Active, Connection_O2
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from time import ctime
from DB_O2 import Exex_2, Exex_1, Exex_3
from Check_All_Base import Check_From_Table, Set_Koment, Set_Koment_Null
import DB_O2
import random
import async_timeout
import sys
API_TOKEN = '827561598:AAGquO8dzrIjwT5YbJbFFE0_GeqSiac6t0c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
pull_complects = []
async def Number_Complect_Converter(message):
	number_complect = message.text.split(" ")[1]
	if len(number_complect) == 1:
		number_complect = "bus000" + str(number_complect)
	if len(number_complect) == 2:
		number_complect = "bus00" + str(number_complect)
	if len(number_complect) == 3:
		number_complect = "bus0" + str(number_complect)
	if len(number_complect) == 4:
		number_complect = "bus" + str(number_complect)
	await asyncio.sleep(1)
	return number_complect

@dp.message_handler(commands = ['check'])
async def check(message: types.Message):
	print ("Message: ", message)
	print (message.from_user.username, message.from_user.id)
	number_complect = message.text.split(" ")[1]
	print ("Запущена конвертация номера комплекта")
	number_complect = await Number_Complect_Converter(message)
	Online = await Active_Complekt(number_complect)
	cft = Check_From_Table(number_complect)
	cft_print = "@{11} \n \u2705 Комплект {0} в сети \n Клиент:  {1} \n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n Был в сети: {10}".format(number_complect ,cft[0],cft[1],cft[5],cft[2],cft[6],cft[3],cft[7],cft[4],cft[8],cft[9],message.from_user.username)
	cft_print2 = "@{11} \n \u274c Комплект {0} не в сети \n Клиент:  {1} \n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n Был в сети: {10}".format(number_complect ,cft[0],cft[1],cft[5],cft[2],cft[6],cft[3],cft[7],cft[4],cft[8],cft[9],message.from_user.username)
	if Online == True:
		await bot.send_message(message.chat.id, cft_print)
	else:
		await bot.send_message(message.chat.id,  cft_print2)

@dp.message_handler(commands = ['online'])
async def online(message: types.Message):
	Onl = True
	print (message)
	await bot.send_message(message.chat.id, "Start")
	komment = message.text.split(" ")[2:]
	komment = ' '.join(komment)
	print("Коментарий :", komment,'\n')
	number_complect = await Number_Complect_Converter(message)
	if number_complect not in pull_complects:
		pull_complects.append(number_complect)
		print ("Pull_complects: ", pull_complects)
		Set_Koment(number_complect, komment)
		cft = Check_From_Table(number_complect)
		cft_print = "@{11} \n \u2705 Комплект {0} в сети \n \
		\u26a0\ufe0f Коментарий: {12} \
		\n Клиент:  {1} \
		\n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n \
		Был в сети: {10}".format(number_complect ,cft[0],cft[1],cft[5],cft[2],cft[6],cft[3],cft[7],cft[4],cft[8],cft[9], message.from_user.username, cft[10])
		while Onl:
			try:
				#cft_print = "@{11} \n \u2705 Комплект {0} в сети \n \u26a0\ufe0f Коментарий: {12} \n Клиент:  {1} \n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n Был в сети: {10}".format(number_complect ,cft[0],cft[1],cft[5],cft[2],cft[6],cft[3],cft[7],cft[4],cft[8],cft[9], message.from_user.username, cft[10])
				Online = await asyncio.wait_for(Active_Complekt(number_complect), 15)
					#print ("Number: ", number_complect, '\n',"Online: ",Online, '\n',"Time: ",ctime(), '\n',)	
				if Online == True:
					print (" ONLINE = True", ctime())
					#Online = False
					await bot.send_message(message.chat.id, cft_print)
					Set_Koment_Null(number_complect)
					pull_complects.remove(number_complect)
					await asyncio.sleep(1)
					Onl = False
				else:
					print ("ONLINE = False", ctime())
					Onl = True
					await asyncio.sleep(60)
			except Exception as e:
				print("Exception raising at : ", ctime(), e)
				pass
	else:
		await bot.send_message(message.chat.id, "\u26a0\ufe0f Checked already running")


"""@dp.message_handler(commands = ['Off'])
async def Offline(message: types.Message):
	print ("I am destroyed")
	await bot.delete_message(message.chat.id, message.message_id)
	sys.exit()"""


if __name__ == '__main__':
	executor.start_polling(dp)