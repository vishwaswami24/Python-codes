
import datetime
'''
print('Minimum year:',datetime.MINYEAR)
print('Maximum year:',datetime.MAXYEAR)

dt=datetime.datetime(2023,5,24,14,34,40)
print(dt)
print(type(dt))
'''
dt=datetime.datetime.today()
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.time())
