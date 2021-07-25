#Simple if statement
a=33
b=200
if b>a:
    print('b is greater')

#elif statement
a=33
b=33
if b>a:
    print('b is greater than a')
elif b==a:
    print('b =a')
else:
    print('b >a')    


#if with And and or statement
a=200
b=33
c=300
if a>b and a<c:
    print('a have middle value')
if a>b or b>c:
    print('one condition true with or statement')    

#Nested if statement
x=18
if x>10:
    print('x is greater than 10')
    if x>20:
        print('x is also greater than 20')
    if x<20:
        print('but x is less than 20') 
else:
    print('x is less than 10')     


"""The pass statement: if statements cannot be empty, but if you for some reason have an
if statement with no content, put in the pass statement to avoid getting an error."""

a=33
b=200
if b>a:
    pass

       