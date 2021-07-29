"""A function is a block of code which run when it is called. we can pass data which is 
called parameter into a function. a function can return data as a result. in python
function is creating using 'def' keyword. to call the function we are using function name
followed by paranthesis: information can be passed into function as arguments. we can
pass argument in function as many as we want, just separate by comma. parameter and
argument both can be used as same things in function. 
Parameter is the variable listed inside the paranthesis () while funtion defining and
argument is the value that is sent to function when it is called.
bydefault function must be called with the correct number of arguments not more not less
it means if function expecting 2 arguments we have to call the function with 2  arguments
not more not less."""

def myfunction():
    print('this is my first function in python')
myfunction()  

#create a function which pass first name as argument
def firstname(fname):
    print(fname + " "+"kumar")
firstname('Rajeev')
firstname('Rajesh')
firstname('Deepak')

#Create a function with two parameters first name and last name
def funcname(fname,lname):
    print(fname+" "+lname)
funcname('Rajeev','Kumar')
funcname('Rajesh','Kumar')
funcname('Deepak','Gupta')
funcname('Mukesh', 'Sahni') 

"""Arbitrary arguments: if we do not know how many arguments will passed in a function
use * before parameter name while defining the function. here functin will receive a 
tuple of arguments and can access items accordingly"""
def funcarb(*city):
    print('city of employee is '+city[2])
funcarb('Noida','Delhi','Gurgaon','Ghaziabad')

#We can also send the arguments with key=value syntax
def cityfunc(a,b,c,d):
    print('city of employees is: '+c)
cityfunc(a='Delhi',b='Patna',c='Noida',d='Lucknow')    

"""Arbitrary Keyword arguments: if we do not know how many keys has passed as arguments
use ** before parameter while defining a function"""

def arbkeyfunc(**name):
    print('Name is '+name['b'])
arbkeyfunc(a='Rajeev',b='Rajesh',c='Deepak',d='Pankaj')

#Default Parameter: if we do not passing any argument function considering default value
def functiondefault(country='India'):
    print('I am from :'+country)
functiondefault('USA')
functiondefault()
functiondefault('UK')
functiondefault()
functiondefault('Austrellia')    


#Passing a list as an argument
list1=['apple','banana','cherry']
def func(list1):
    for i in list1:
        print(i)
func(list1)        

#Return statement: by using return keyword function returning a value
def retrnfunction(x):
    return 5*x
print(retrnfunction(10))
print(retrnfunction(7))
print(retrnfunction(15))
print(retrnfunction(32))

"""Pass statement in function: generally function body can not be blank while defining
function. but due to some reason have a need of function definition with no content
we are using pass statement to avoid error"""

def funcpass():
    pass
