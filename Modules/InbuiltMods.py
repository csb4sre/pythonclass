import math #Importing a full method


from math import pi as p # importing one functionality or function
from math import pi,sqrt # importing multiple functions

print(dir(math))
print(2*math.pi*5)
print(p)
print(sqrt(9))

import time
print(time.time()) # gives the current linux timestamp so far since 1970
#print(dir(time))
print(time.asctime()) # gives the current date and time


import calendar
print(calendar.month(2018,5))
print(calendar.calendar(2018))

import random
print(dir(random))
print(random.randint(0,100))

print(random.choice(['choice', 'is', 'yours', 1, 2, 'or', 3]))



