'''There are built in by default data types in python
1)Numeric (Integer, Float, complex)
2)String
3)Sequence type : List, Tuple, Range
4)Mapping type : Dictionary
5)Set type : Set, Frozenset
6)Boolean type : bool
7)Binary types : bytes, bytearray, memoryview

Number, String and Tuples are imutable it means its value can not be changed
however List, Set and Dictionary are mutable it means its value can be change
for example'''

#We can get the data type of any object or variable using type() function. for example
x=5
print(type(x))
y="Rajeev"
print(type(y))

#Example of Integer data Type, no need to be write integer or int while defining integer type
a=10
b=20
c=a+b
print(c)

#Example of float data type
a=10.5
b=20.1
print(a+b)

#Example of String data type
a='Rajeev'
b='Kumar'
print(a+' '+b)

#In python the data type is set while we assigning a value to a variable. for example
#String type
x="Hello world"
print(x)

#Numeric type
x=10
y=20.7

#tuple type
x=("Apple","Banana","Cherry")
print(type(x))
print(x)


#list example
x=['apple','banana','cherry']
print(x)
x.append('Mango')
print(x)

#range type: mostly range is using in loop for example
x=range(10)
print(x)
print(type(x))

for i in range(5):
    print(i)

#Type Dictionary    
a={'name':'Rajeev','age':32}
print(a)
print(type(a))

#Type Set
a={"apple","Banana","Cherry"}
print(a)
print(type(a))

'''frozenset: as we know set is mutable type it means we chan change its value 
if we want to make it imutable it means we do not want to change its value then we are using frozenset fox ex'''

a=({'apple','mango','cherry'})
print(a)
print(type(a))
a.add({'papaya'})
print(a)





