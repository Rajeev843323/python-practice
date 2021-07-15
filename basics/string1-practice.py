"String in python is either surrounded by single quote '' or by a double quote "" marks"
#Assigning string to a variable
a='Hello python'
b="Rajeev kumar"
print(a+'\n'+b)

#Multiline string: Multiline string can assign by three quotes, if we do not assign it behaves like multiline comments
a="""Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string."""
print(a)

#String are arrays: Strings in python are arrays of bytes. elements of the string accessing by square bracket []
a="Hello World"
print(a[3])

#Looping through a string
for x in 'banana':
    print(x)

#len() function: len() function is use to provide the lenth of a string
a='Hello World'
print(len(a))

#check string: to check certain character or phrase in a string we are using 'in' keyword
a = "The best things in life are free!"
print('free' in a)

txt='India is a great country'
if 'great' in txt:
    print('yes')
else:
    print("No")

txt='India is a great country'
if 'person' not in txt:
    print('person not available')
else:
    print("person is  available")
    print('ok')

#Get the character from position 2 to position 5
a="Hello World"
print(a[2:5])

#Get the character from start to position 5
a="Hello world"
print(a[:4])

#Get the character from position 2 to end
a="Hello world"
print(a[2:])

#Negative indexing use to start position from end of the string
a="Hello world"
print(a[-5:-2])

#Change in upper care & lower case
a="Hello world"
print(a.upper())
print(a.lower())

#Remove whitespace: strip() method using to be remove extra blank spaces from either starting or end of the string
a="  Hello world.  "
print(a.strip())

#Replace string
a='Hello world how are you'
print(a.replace('o','a'))

#if we want to replace only 2 number of 'o' from starting of the string and rest not changed
a='Hello world how are you'
print(a.replace('o','a',2))

#Split string
a='my,name,is,rajeev,kumar'
print(a.split(','))
print(a.replace(',',' '))

#concatenate the string: in python concatenate two string using + symbol
a='Rajeev'
b='kumar'
c=a+" "+b
print(c)

#format() method: we can combine string and number by two way one using format() and other by change integer into string
a="My name is John and I am"
age=32
b="year old"
print(a+" "+str(age)+" "+b)

a='my name is john I am {} year old'
age=32
print(a.format(age))

a="My name is John and I am {}"
age=32
b="year old"
print(a.format(age)+" "+b)


age=30
sal=30000
pin=121010
dt=15
yr=2021
str="Today is {} Jul of year {} I am {} year old, my salary is {}, my pin no. is {}"
print(str.format(dt,yr,age,sal,pin))
str="Today is {3} Jul of year {4} I am {0} year old, my salary is {1}, my pin no. is {2}"
print(str.format(age,sal,pin,dt,yr))


txt = "Hello World"
x =txt[2:5]
print(x)