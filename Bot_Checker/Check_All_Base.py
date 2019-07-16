import sqlite3
import time
import datetime

dt = datetime.datetime.now()
print(dt)
time_for_Lifcell = datetime.timedelta(days = 28)
print(time_for_Lifcell + dt)