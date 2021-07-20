__doc__='''Problem 1: I want to print all items with hello in prifix but do not want to
 print hello with kiwi. kiwi should be only kiwi 
 examp input: ["apple", "banana", "cherry", "kiwi", "mango"]
  output: ["hello apple", "hello banana", "hello cherry", "kiwi", "hello mango"] '''

#set all value of list with hello except kiwi
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist=['hello'+ " "+x for x in fruits if x!='kiwi']
#print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
myDict = {
    "anil",
    "rajeev"
}
fruits.append(myDict)

print(fruits)
newlist=[]
for i in fruits:
    if i != 'kiwi':
        i = 'hello ' + i
    newlist.append(i)

newlist.append(myDict)
print(newlist)