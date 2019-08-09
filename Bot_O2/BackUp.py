import time
import datetime
import sqlite3
import os
import shutil
import logging
#logging.disable()
logging.basicConfig(level = logging.DEBUG, 
					format = '-- %(message)s')

class Need_Beckup:
	now_time = datetime.datetime.now()
	pool_data_list = []
	with open('Beckup.txt', 'r') as pool_date_file:
		pool_date_file = pool_date_file.readlines()
		for lines in pool_date_file:
			pool_data_list.append(lines)
	logging.debug(pool_data_list)

	def check_date(self):
		month = int(self.pool_data_list[0][0])
		date = int(self.pool_data_list[0][2]+self.pool_data_list[0][3])
		logging.debug(date)
		time_to_backup = datetime.datetime(2019,month,date,23,40,0)
		if self.now_time > time_to_backup:
			logging.debug('Now_Time not gone')
			base = os.path.abspath('DB_O2.db')
			new_path = 'D:\\Python_Bot\\Bot_O2\\O2_Backup'
			shutil.copy(base,'D:\\Python_Bot\\Bot_O2\\O2_Backup\\DB_O2-{0}-{1}-{2}.db'.format(self.now_time.day, 
																							self.now_time.month,
																							self.now_time.year))
			self.clear_database()
			if date != 15:
				self.clear_datalist()
		else:
			logging.debug('DONE !!!')
			logging.debug('{0} not {1}'.format(self.now_time, 
												time_to_backup))

	def clear_database(self):
		connect = sqlite3.connect("DB_O2.db")
		cursor = connect.cursor()
		exe_clear = "UPDATE Check_O2 SET Trafic= ?, Trafic0 = ?, Status = ?"
		exe_null = cursor.execute(exe_clear, ['0','0', '0'])
		connect.commit()

	def clear_datalist(self):
		logging.debug(self.pool_data_list[0])
		del self.pool_data_list[0]
		with open('Beckup.txt', 'w') as pool_date_file:
			for pool in self.pool_data_list:
				pool_date_file.write(pool)



