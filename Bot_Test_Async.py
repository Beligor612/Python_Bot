import logging
import asyncio
import aiogram
import time 
import nest_asyncio
#nest_asyncio.apply()

API_TOKEN = '855313094:AAFm36oeX-c72ps6itp3Icco8AQrcH4jDcY'
logging.basicConfig(level=logging.INFO)
bot = aiogram.Bot(token = API_TOKEN)
dp = aiogram.Dispatcher(bot)


#bot.send_message(386869436, "Начинаю тестирование !!")


async def Raisen(number):
	await bot.send_message(386869436, "Начинаю тестирование {0}!!".format(number))

async def main():
	loop =asyncio.get_event_loop()
	#task = asyncio.create_task(Raisen(4))
	loop.run_until_complete(asyncio.wait([asyncio.ensure_future(Raisen(4))]))
	loop.close()

#asyncio.run(Raisen(4))

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait([asyncio.ensure_future(Raisen(4))]))
	loop.close()