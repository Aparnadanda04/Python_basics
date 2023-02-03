import datetime

x = datetime.date.today()
print(x)
# using now() to get the current time 
current_time = datetime.datetime.now()

print("Time is now in UTC and local time: ", current_time)

from datetime import datetime
now = datetime.now()
print(now)

# get the current day 
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print("The current day, month, year & hour, minute, second is: ", day, month, year, hour, minute, second, timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# difference between two points in Time using timedelta function in Py

from datetime import timedelta 

t1 = timedelta(weeks=20, days=10, hours=6, seconds=25)
t2 = timedelta(days=8, hours=4, minutes=3, seconds=30)
t3 = t1 - t2 
print("t3 as time delta: ", t3)

# for timezone 

import datetime
import pytz
