import New_Checker_Bot
import time
New = New_Checker_Bot.Checker()
print(New.insert_comment('bus0001'))
#print(New.database()) 
while New.check_time() == False:
    print(New.check_time())
    time.sleep(30)
