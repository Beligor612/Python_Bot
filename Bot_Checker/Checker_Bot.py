import New_Checker_Bot
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from time import ctime
import async_timeout



API_TOKEN = '827561598:AAGquO8dzrIjwT5YbJbFFE0_GeqSiac6t0c'
logging.getLogger("paramiko").setLevel(logging.ERROR)
logging.basicConfig(level=logging.DEBUG, format = '--%(message)s');
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
	Checker = New_Checker_Bot.Checker()
	logging.debug("Start")
	number_complect = await Number_Complect_Converter(message)
	logging.debug("Converted to: {0}".format(number_complect))
	online = Checker.check_bus(number_complect)
	inform = Checker.check_inform(number_complect)
	message_online = "@{11} \n \u2705 Комплект {0} в сети \n Клиент:  {1} \n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n Был в сети: {10}".format(number_complect,
		inform[0],inform[1],inform[5],inform[2],inform[6],inform[3],inform[7],inform[4],inform[8],inform[9],message.from_user.username)
	message_offline = "@{11} \n \u274c Комплект {0} не в сети \n Клиент:  {1} \n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n Был в сети: {10}".format(number_complect 
		,inform[0],inform[1],inform[5],inform[2],inform[6],inform[3],inform[7],inform[4],inform[8],inform[9],message.from_user.username)
	if online == True:
		await bot.send_message(message.chat.id, message_online)
	else:
		await bot.send_message(message.chat.id,  message_offline)

@dp.message_handler(commands = ['online'])
async def online(message: types.Message):
	Checker = New_Checker_Bot.Checker()
	online = True
	await bot.send_message(message.chat.id, "Start")
	komment = message.text.split(" ")[2:]
	komment = ' '.join(komment)
	number_complect = await Number_Complect_Converter(message)
	if number_complect not in pull_complects:
		pull_complects.append(number_complect)
		logging.debug("Pull Complect: {0}".format(pull_complects))
		Checker.insert_comment(number_complect, komment)
		inform = Checker.check_inform(number_complect)
		inform_prnt = "@{11} \n \u2705 Комплект {0} в сети \n \
		\u26a0\ufe0f Коментарий: {12} \
		\n Клиент:  {1} \
		\n Тарифы: \n {2} | {3} \n {4} | {5} \n {6} | {7}\n {8} | {9}\n \
		Был в сети: {10}".format(number_complect ,
			inform[0],inform[1],inform[5],inform[2],inform[6],inform[3],
			inform[7],inform[4],inform[8],inform[9], message.from_user.username, inform[10])
		while online:
			logging.debug("Start checker {0}".format(number_complect))
			logging.debug("Pull active complect: {0}".format(pull_complects))
			try:
				Online = Checker.check_bus(number_complect)
				if Online == True:
					await bot.send_message(message.chat.id, inform_prnt)
					Checker.insert_comment(number_complect)
					pull_complects.remove(number_complect)
					await asyncio.sleep(1)
					Online = False
					break
				else:
					Online = True
					logging.debug("I Sleep at {0}".format(ctime()))
					await asyncio.sleep(60)
			except Exception as e:
				logging.debug("Exception raising at : {0}, {1}".format(ctime(),e))
				pass
	else:
		await bot.send_message(message.chat.id, "\u26a0\ufe0f Checked already running")


if __name__ == '__main__':
	executor.start_polling(dp)