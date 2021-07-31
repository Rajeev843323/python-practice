"""Python datetime is not its own data type but this can be used by importing its module
name is datetime to work with dates as date object.  """

import numpy
import datetime as dt
import math as mt
x=dt.datetime.now()
print(x)
print(x.day)
print(x.year)
print(x.month)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%d"))
print(x.strftime("%Z"))
print(x.strftime("%x"))

x=min(10,5,20,30)
y=max(10,30,15,12)
print('min value is: '+str(x))
print('max value is: '+str(y))

list1=[10,20,5,13,20,17]
print(max(list1))
print(min(list1))

#Print absolute value of a number
print(abs(-7.5))

#print power of a number 4
print(pow(5,4))
print(mt.sqrt(625))

#round the number upward and downward
print(mt.ceil(4.3))
print(mt.floor(17.5))

#value of pi
print(mt.pi)
