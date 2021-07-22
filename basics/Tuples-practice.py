"""Like list Tuples are also used to store multiple items in a single variable. tuple is 
one of 4 built in data type in python whin store collection of data other 3 are list,
set and dictionary all have different qualities and uses. 
touple is a collection which is ordered and unmutable (unchangable) touple is written
with small bracket () tuple allow ducplicate value its item also be accessed by index
[0],[1] etc. when we are saying tuples are ordered it means its order will not changed."""


#Create a tuple
from typing import Tuple


tuple1=('cat', 'dog','horse','cow')
print(tuple1)

#tuple with duplicate value
tuple1=('a','b','c','b','d','c')
print(tuple1)

#Tuple with only one item. we should have to must add comma "," at the end after the item
thistuple=('apple',)
print(thistuple)

#A Tuple can also contains multiple data type
tuple1=('c','d','apple',10,5,20,True, False)
print(tuple1)

#We can also create tuple by using tuple() method. plz note double small bracket
tup1 = tuple(('apple','banana','cherry'))
print(tup1)

#access item of tuple by its index value
tuple1=('cat', 'dog','horse','cow')
print(tuple1[1])
print(tuple1[2])
print(tuple1[-1])
print(tuple1[:3])
print(tuple1[2:])
print(tuple1[2:4])
print(tuple1[2:3])
print(tuple1[-4:-1])

#check if item is available in the tuple
tuple1=('cat', 'dog','horse','cow')
if 'dog' in tuple1:
    print('yes item is available')

""" Update tuples: As we know tuple's items are unchangable so we can not change, add or 
remove items once tuple is created. but there is a way through which tuple can be change
that way is convert the tuple into the list then after change the list value and again
convert list into the tuple"""

y=('apple','banana','cherry')
x=list(y)
print(x)
x[1]='kiwi'
print(x)
y=tuple(x)
print(y)
x.append('mango')
print(x)
y=tuple(x)
print(y)


#Add one tuple into another tuple
tuple1=('apple','banana','cherry')
tuple2=('kiwi','mango')
tuple1=tuple1+tuple2
print(tuple1)

#delete item from a tuple
tuple1=('apple', 'banana', 'cherry', 'kiwi', 'mango')
list1=list(tuple1)
list1.remove('cherry')
tuple1=tuple(list1)
print(tuple1)
del(list1[2])
tuple1=tuple(list1)
print(tuple1)

"""Unpacking of tuple: Normally when we creating a tuple and assigning some values inside
a tupble is called packing a tuple but in python we are also allowed to extract value
back into the variable is called unpacking of tuple."""

tuple1=('apple', 'banana', 'cherry')
(a,b,c)=tuple1
print(a)
print(b)
print(c)
print(a,b,c)                                                                                           

tuple1=('apple', 'banana', 'cherry', 'kiwi', 'mango')
(a,b,*c)=tuple1
print(a)
print(b)
print(c)

tuple1=('apple', 'banana', 'cherry', 'kiwi', 'mango')
(a,*b,c)=tuple1
print(a)
print(b)
print(c)

#Loop inside a tuple
tuple1=('apple', 'banana', 'cherry', 'kiwi', 'mango')
for i in tuple1:
    print(i)

for i in range(len(tuple1)):
    #print(i)
    print(tuple1[i])    

tuple1=('apple', 'banana', 'cherry', 'kiwi', 'mango')
i=0
while i<len(tuple1):
    print(tuple1[i])
    i=i+1

#Join two tuples 
tuple1=('apple','banana','cherry')
tuple2=('mango','guava','papaya')
tuple3=(2,4,6,)
tuple4=tuple1+tuple2
tuple5=tuple1+tuple3
print(tuple4)
print(tuple5)

#multiply the tuple
tuple1=('apple','banana','cherry')
tuple2=(2,4,6,)
tuple3=tuple1*2
tuple4=tuple2*2
print(tuple3)
print(tuple4)
