from paramiko import SSHClient
from paramiko import AutoAddPolicy

def Connection_Routs():
	mip = '172.31.1.194'
	ml = 'admin'
	mp = 'Myxa194'
	#ssh # Объявим переменную подключения глобальной для того чтобы обратится извне
	ssh = SSHClient() # Создаем клиент подключения
	ssh.set_missing_host_key_policy(AutoAddPolicy())# Создаем стек ключей подлкючения для доступа 
	ssh.connect(mip, port=22, username=ml, password=mp) # Проводим подключение к микротику
	command = "/ip route print"
	ssh_command = ssh.exec_command(command)[1].read()
	ssh_command = ssh_command.decode("utf-8")
	print(ssh_command)

Connection_Routs()