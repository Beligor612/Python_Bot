import sqlite3
import logging
import Check_All_Base

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -- %(message)s')
class Database_O2:

	connect = sqlite3.connect("DB_O2.db")
	cursor = connect.cursor()

	def list_bus_with_o2(self): #Bus_Archive
		Bus_archive = []
		Bus = []
		exe_1 = "SELECT Bus FROM Check_O2"
		Bus_List = self.cursor.execute(exe_1).fetchall()
		for bus in Bus_List:
			Bus_archive.append(bus[0])
		return Bus_archive

	def bus_info_all(self): #Login Bus From Archive
		""" Собираем список информации из БД по всем комплектам и делаем словарь с ключами 
		по именам автобуса и значениями инфа для входа и траффик по комплекту"""
		exe_2 = "SELECT Adress, Login, Password, Trafic, Trafic0, Status FROM Check_O2 WHERE Bus = ?"
		archive = self.list_bus_with_o2()
		bus_info_archive = {}
		for bus in archive:
			One_Line = self.cursor.execute(exe_2, [(bus)]).fetchall()
			bus_info_archive[bus] = One_Line
		return bus_info_archive

	def bus_info(self, bus):
		""" Функция возвращает список информации из БД по 1 комплекту """
		self.bus = bus
		bus_info_all_string = self.bus_info_all()
		info_bus_string = bus_info_all_string[bus]
		return info_bus_string[0]

	def trafic_record(self, trafic, bus):
		"""
		1.Берем текущий трафик trafic и сравниваем с предыдущм trafic_tempora. 
		2.Разницу между ними плюсуем к переменной
		compared_trafic и записываем в БД. 
		3.Полученный текущий трафик аписываем в переменную tempora_trafic
		"""
		#logging.debug("Step 1: Trafic: {0} and Bus {1}".format(trafic, bus))
		trafic_from_db_command = "SELECT Trafic FROM Check_O2 WHERE Bus = ?" # Трафик из таблицы
		trafic_from_db = self.cursor.execute(trafic_from_db_command, [bus]).fetchall()[0][0] # Берет текущий Трафик
		tempora_trafic_command = "SELECT Trafic0 FROM Check_O2 WHERE Bus = ?"
		tempora_trafic = self.cursor.execute(tempora_trafic_command, [bus]).fetchall()[0][0] # Берет из Трафик0 предыдущий трафик
		if tempora_trafic > trafic:
			update_to_null_tempora_command = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
			self.cursor.execute(update_to_null_tempora_command, [trafic, bus])
			tempora_trafic = self.cursor.execute(tempora_trafic_command, [bus]).fetchall()[0][0]
			tempora_trafic += trafic
		#logging.debug("Step 2: Trafic_Form_DB : {0} Tempora_Trafic: {1}".format(trafic_from_db, tempora_trafic))
		compared_trafic = abs(float(tempora_trafic) - float(trafic)) # Сравниваем 2 трафика
		#logging.debug("Сравниваем два траффика, предыдущий {0} и текущий {1}".format(tempora_trafic, trafic))
		final_trafic = round((trafic_from_db + compared_trafic),2)
		final_trafic_command = "UPDATE Check_O2 SET Trafic = ? WHERE Bus = ?"
		#logging.debug("FINAL TRAFFIC: {0}".format(final_trafic))
		final_trafic_record = self.cursor.execute(final_trafic_command, [final_trafic, bus])# Записывает трафик в трафик
		final_tempora_command = "UPDATE Check_O2 SET Trafic0 = ? WHERE Bus = ?"
		#logging.debug("Tempora Final Trafic: {0}".format(trafic))
		final_tempora_record = self.cursor.execute(final_tempora_command, [trafic, bus])# Записывает текущий Трафик0
		self.connect.commit()
		status = self.checkup_status(final_trafic, self.bus_info(bus)[5], bus)
		#logging.debug("Traffic record: {0} Mb at complect {1}".format(trafic, bus))
		return status
	
	def checkup_status(self, trafic, status, bus):

		# Принимает трафик и сравниваем с порогами
		# Если трафик вышел за порог проверь его статус
		# Если статус не соответсвует измени статус и выведи информацию

		logging.debug("Comming trafic: {0} with status {1}".format(trafic, status))
		status_dict = {10000.0 : 1, 
						15000.0 : 2,
						18000.0 : 3,
						20000.0 : 4,
						30000.0 : 5,
						35000.0 : 6,
						38000.0 : 7,
						40000.0 : 8,
						50000.0 : 9,
						55000.0 : 10,
						58000.0 : 11,
						60000.0 : 12,
						70000.0 : 13,
						75000.0 : 14,
						78000.0 : 15,
						80000.0 : 16}
		for status_trafic in status_dict.keys():
			if trafic > float(status_trafic) and status == status_dict[status_trafic]-1:
				#logging.debug("WARNING trafic UP at {0} with status {1}".format(status_trafic, status_dict[status_trafic]))
				status_two = status_dict[status_trafic]
				self.record_status(bus, status_two)
		if status != status_two:
			return status_two
		else:
			return 0
			

	def record_status(self, bus, status):
		#logging.debug("Recording status...")
		record_command = "UPDATE CHECK_O2 SET Status = ? WHERE Bus =?"
		record = self.cursor.execute(record_command, [status, bus])
		self.connect.commit()

	def close_session(self):
		logging.debug("Close Session with database")
		self.connect.close()

	def info_client(self, bus):
		All = Check_All_Base.All_Base()
		All_Chec = All.Check_From_Table(bus)
		return All_Chec


