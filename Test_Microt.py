from paramiko import SSHClient
from paramiko import AutoAddPolicy
from time import sleep, ctime
from Check_All_Base import Check_From_Table, Set_Time
from DB_O2 import Exex_2, Trafic_Down
import asyncio
def Connection():
	mip2 = 'vpnbus.test.net.ua'
	ml2 = 'wifibus'
	mp2 = 'BusWifi'
	#try:
	global ssh2 # Объявим переменную подключения глобальной для того чтобы обратится извне
	ssh2 = SSHClient() # Создаем клиент подключения
	ssh2.set_missing_host_key_policy(AutoAddPolicy())# Создаем стек ключей подлкючения для доступа 
	ssh2.connect(mip2, port=22, username=ml2, password=mp2) # Проводим подключение к микротику
	#except: 
		#print ("Что-то пошло не так с подключением к Германии \n Засыпаю на 3 минуты и переподключусь")
		#print ("Время ", ctime())
		#Connection()

def Connection_O2(bus, Adress, Login, Password):
		Ad = Adress
		Log = Login
		Pass = Password
		ssh_O2 = SSHClient() # Создаем клиент подключения
		ssh_O2.set_missing_host_key_policy(AutoAddPolicy())# Создаем стек ключей подлкючения для доступа 
		ssh_O2.connect(Ad, port=22, username=Log, password=Pass)# Подключаемся
		
		exe_Upload = "put [interface get [find name=O2] rx-byte]"
		exe_Download = "put [interface get [find name=O2] tx-byte]"
		
		Upload = ssh_O2.exec_command(exe_Upload)[1].read()
		Download = ssh_O2.exec_command(exe_Download)[1].read()
		Summa = Trafic(Upload, Download)
		
		Trafic_Down(Summa, bus)

def Trafic(Upload, Download):
	print (Upload, ' ', Download)
	Upload = int(Upload)/1000000
	Download = int(Download)/1000000
	Sum_Trafic = round((Upload + Download),2)
	print (str(Sum_Trafic) + " Mb")
	return Sum_Trafic
	#print("Upload: ",Upload, type(Upload))
	#print("Download: ",Download, type(Download))
	#print (Trafic)

def Active():
	exe2 = "/ppp active print" # Создаем запрос для проверки активности комплектов
	excmd3 = ssh2.exec_command(exe2)[1].read()# Считываем информацию из полученных Байтов
	excmd4 = excmd3.decode("utf-8")# Переводим байты в строку
	Status_excmd4 = excmd4[103:len(excmd4)].split("  ")# Разбиваем строку по розделителю пробелов

	i = 0;# Цикл который поможет убрать лишние пробелы
	for i in range(Status_excmd4.count('')):
		Status_excmd4.remove('')

	global Active_comp
	Active_comp = []
	k = 0 # Цикл который дробит полученную строку на участки информации и записывает их в многомерный массив
	for k in range(int(len(Status_excmd4)/6)):
		Active_comp.append(Status_excmd4[0:6])
		del Status_excmd4[0:6]
		#print(Active_comp[k])
	return Active_comp

def Close_Connection():
	ssh2.close() # Закрываем соединение с микротиком

async def Active_Complekt(Komplect):
		Online = False
		Connection();
		Active(); 
		for i in range(len(Active_comp)):
			#print ( "Комплект: ", Active_comp[i][0], "В сети: ", Active_comp[i][4])
			Komplect_Online = Active_comp[i][0].lstrip().rstrip()
			Set_Time(Komplect_Online)
			if str(Komplect) == str(Komplect_Online):
				Online = True
		#Check_Base(Komplect)
		Close_Connection()
		if Online == True:
			await asyncio.sleep(1)
			#Uptime = Active_comp[i][4]
			return True
		else:
			#Uptime = 0
			return False 

if __name__ =='__main__':
	Connection();
	Active();
	Active_Complekt('bus0045');
	Close_Connection();