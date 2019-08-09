import paramiko
import logging
import re

#logging.disable()
logging.getLogger("paramiko").setLevel(logging.WARNING)
#logging.disable()
logging.basicConfig(level = logging.DEBUG, format = '%(message)s')

class Mikrotik:
	def __init__(self, ip = "vpnbus.test.net.ua", login = 'fiway', password = 'BusWifi', timeout = 40):
		self.ip = ip
		self.login = login
		self.password = password

	def Connect(self): # Инициализация подключения к микротику
		try:
			logging.debug(self.ip+' '+self.login)
			logging.debug("CONNECTION!!")
			self.ssh = paramiko.SSHClient()
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(self.ip, port = 22, username = self.login, password = self.password)
			logging.debug("CONNECT TO {0} SACCESSFULL".format(self.ip))
		except:
			logging.debug("CONNECTION FAILED")
			
	def close_connection(self): # Инициализация свертывания подключения
		#logging.debug("Close CONNECTION!!")
		self.ssh.close()

	def list_active_complect(self):
		# Проводит сканироваение списка активных комплектов и выдаем список
		command = "/ppp active print"
		exe_command = self.ssh.exec_command(command)[1].read()
		exe_command = exe_command.decode("utf-8")
		status_command = exe_command[103:len(exe_command)].split("  ")

		for i in range(status_command.count('')):
			status_command.remove('')

		active_complects = [] # Список активности с комплекта
		active_bus_complects = [] # Сисок активных комплектов

		k = 0
		for k in range(int(len(status_command)/6)): # Выводим список активности с комплекта в список
			active_complects.append(status_command[0:6])
			del status_command[0:6]

		for i in range(len(active_complects)): # Перебераем список и выводим список комплектом
			komplect_online = active_complects[i][0].lstrip().rstrip()
			active_bus_complects.append(komplect_online)

		logging.debug("{0} COMPLECTS ONLINE".format(i))

		return active_bus_complects # Показать список активных комплектов

	def trafic(self, interface):
		self.interface = interface
		command_upload = "put [interface get [find name={0}] rx-byte]".format(interface)
		command_download = "put [interface get [find name={0}] tx-byte]".format(interface)
		upload = self.ssh.exec_command(command_upload)[1].read()
		download = self.ssh.exec_command(command_download)[1].read()
		#logging.debug("Upload: {0} Download: {1}".format(upload, download))
		upload_result = int(upload)/1000000
		download_result = int(download)/1000000
		sum_trafic = round((upload_result + download_result),2)
		return sum_trafic # Собрать суммарный трафик комплекта с указанного интерфейса

	def check_speed(self,interface):
		self.interface = interface
		command_upload_speed = ':put ([/interface monitor-traffic {0} once as-value]->"rx-bits-per-second"+[/interface monitor-traffic {0} once as-value]->"tx-bits-per-second")'.format(interface)
		upload_speed = self.ssh.exec_command(command_upload_speed)[1].read()
		upload_speed = round(((int(upload_speed)/1024)/1024),3)
		logging.debug("Speed {0}:  {1} ".format(interface, upload_speed)) # Собрать суммарную скорсть с указанного интерфейса модема
