from paramiko import SSHClient
from paramiko import AutoAddPolicy
import time

mip = '192.168.1.31'
ml = 'O2_Check'
mp = 'admin2'



ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(mip, port=22, username=ml, password=mp)


i = 0
while i<10:
	exe = "put [/queue simple get queue-O2 byte]"
	excmd2 = ssh.exec_command(exe)[1].read()
	print(excmd3)
	str(excmd2)
	sp = []
	sp = str(excmd2).split('/')
	l1 = int(sp[0][2:])
	l2 = int(sp[1][0:-5])
	MBite = (l1+l2)/1000000
	print ('Vodafone_Test: ', MBite, "Mb", '\n')
	i +=1
	time.sleep(15)

ssh.close()