"""python have two loops one is while and other is for loop. while loop: we can execute
a set of statements as long as condition is true. in while loop we are seting the initial
value first the loop body its increment or decrement value"""
#print 1 to 10 numbers

i=1
while(i<=10):
  print(i)
  i=i+1

#print even and odd number from 6 to 20

i=6
while i<=20:
  if i%2==0:
    print(i)
  i=i+1  


i=6
while i<=20:
  if i%2!=0:
    print(i)
  i=i+1   

#break statement can stop the loop even if the while condition is true

i=1
while i<=10:
  print(i)
  if i==5:
    break
  i=i+1

#continue statement stop for the current position and continue for the next
i=0
while i<10:
  i=i+1
  if i==4:
    continue
  print(i)
 
#for loop for a list
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)

#looping through a string
a='banana'
for i in a:
  print(i)
#Or
for i in 'banana':
  print(i)

#break statement with for loop
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)
  if i=='banana':
    break
#continue statement with for loop
for i in fruits:
  if i=='banana':
    continue
  print(i)

#range function in loop
for i in range(10):
  print(i)

for i in range(4,10):
  print(i)

for i in range(2,20,2):
  print(i)

#Nested for loop
fruits=['apple','banana','papaya']
colr=['red','yellow','green']
for i in fruits:
  for j in colr:
   print(i,j)     




