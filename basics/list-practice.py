"""Lists are used to store multiple items in a single variable. Lists are one of 4 built in data types
in python, the other 3 are Touple, Set and Dictionary these all 3 are also storing multiple data items in a
single variable but all have its own qualities and uses. Lists are created by using [] square bracket. ex
list items are ordered, changable and allow duplicate values. list items are indexed the first item has index
[0], second item have index[1] and so on."""

list1=['Apple', 'Banana', 'Cherry']
print(list1)

"""Ordered: if we are saying lists are ordered it means that items have a defined order and that order will
not change. if you add new item in a list then new item will be placed at end of the list. There are some
list methods will change the order, but in general the order of the items are not changed."""

"""Changable: List is changable it means that the items in the list can be change, add and remove after it 
has been created, it also allow the duplicate value"""

list1=['apple', 'banana', 'cherry', 'apple']
print(list1)

#determine how many items in a list using len() function with list
list1=['apple', 'banana', 'cherry']
print(len(list1))

#List can be of any type
list1=['apple','banana','cherry']
list2=[2,4,6,8]
list3=[True, False, False, True]
list4=['apple, banana',2,4,6,True, False]
print(list1,list2,list3,list4)
print(type(list4))

"""There are four collection data type or collection arrays in python programming. they are
List: is a collection which is ordered, mutable(changable), allow duplicate members creatdd using []
Tuple: is a collection which is ordered, imutable(unchangable), no duplicate members using ()
set: unordered, unindexed, no duplicate
Dictionary: ordered, changable, no duplicate"""


#access the list items
#access 2nd item from the list the first item has index 0
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative index: -1 index indicating the last item and -2 means second last item in the list
#print last item from the list
thislist=['apple','banana','cherry','mango']
print(thislist[-1])
print(thislist[-2])

#Range of indexes
#Print 3rd, 4th, 5th item from list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Here output start with index 2 (included) and end at index 5 (not included)

#Print begining to index 4 (not included kiwi)
print(thislist[:4])

#Print index 2 to end
print(thislist[2:])

#Range of negative indexs
#Print -4 (orange) to -1 (mango not included)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check item in the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if 'orange' in thislist:
    print('yes orange available in list')
else:
    print('not available')    

#count items in list
thislist = ["apple", "banana", "cherry", 'banana',"orange", "kiwi", 'mango',"melon", "mango",'guava', 'xyz']
print(thislist.count('banana'))
print(len(thislist))

#Change item value in a list
#change the second item
thislist=['apple','banana','cherry']
thislist[1]='mango'
print(thislist)

#change range of items
thislist=['apple','banana','cherry','mango']
thislist[1:3]=['guava','papaya']
print(thislist)

#When we insert more or less item than the replaced items, remaining item will autometically move accordingly
thislist=['apple','banana','cherry','mango']
thislist[1:3]=['guava','papaya','blackberry']
print(thislist)

thislist=['apple','banana','cherry','mango']
thislist[1:3]=['guava']
print(thislist)

#Insert new item in the list without replacing old value we are using insert() method with the list with index
#insert watermelon as third item
thislist=['apple','banana','cherry','mango']
thislist.insert(2,'watermelon')
print(thislist)

list1=['apple','banana','cherry']
list2=['mango','guava','papaya']
list1.append('mango')
print(list1.append(list2))

#To append list items from onle list to another list use extend() method
list1=['apple','banana','cherry']
list2=['mango','guava','papaya']
list1.extend(list2)
print(list1)

#Append items in a list from other type like tuple, dictionary etc
list1=['apple','banana','cherry']
tuple1=('mango','guava','papaya')
dict1={'Rajeev','Sanjeev','Rajesh'}
list1.extend(tuple1)
print(list1)


#Remove list items
#remove specified items from the list
thislist=['apple','banana','cherry','mango']
thislist.remove('banana')
print(thislist)

#remove specified index: specified index will delete by del or pop command
thislist=['apple','banana','cherry','mango']
del thislist[2]
print(thislist)

thislist=['apple','banana','cherry','mango']
thislist.pop(1)
print(thislist)

thislist=['apple','banana','cherry','mango']
del thislist[1:3]
print(thislist)

#if we do not specified any index in pop this will remove last item
thislist=['apple','banana','cherry','mango']
thislist.pop()
print(thislist)

#if not specifying any index in del this will delete complete list
thislist=['apple','banana','cherry','mango']
del thislist
print(thislist)

#clear only items from the list
thislist=['apple','banana','cherry','mango']
thislist.clear()
print(thislist)


#Loop for a list
#print all item of a list
thislist=['apple','banana','cherry','mango']
for x in thislist:
    print(x)

#we can write loop with range() and len() function white printing items of list by its index
thislist=['apple','banana','cherry','mango']
for i in range(len(thislist)):
    print(thislist[i])


"""Whilw loop inside a list: use len() function to determine the length of the list then start loop variable
with zero, and loop this through list item, and index variable increase by 1"""

thislist=['apple','banana','cherry','mango']
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1


#Find fruit name which contains 'a' letter
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list1=[]
for i in fruits:
    if 'a' in i:
        list1.append(i)
print(list1)
        

#Same program can be write using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if 'a' in x]
print(newlist)


#Print all item except apple
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if x!='apple']
print(newlist)


#print all item using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits]
print(newlist)
#OR
print([x for x in fruits])

#Print 0 to 9 numbers
for x in range(10):
    print(x)

#OR
newlist=[x for x in range(10)]
print(newlist)


#Print only numbers lower than 5
newlist=[x for x in range(10) if x<5]
print(newlist)

#change all list items in upper case
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x.upper() for x in fruits]
print(newlist)

#set all value of list with hello
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=['hello'+ ' '+x for x in fruits]
print(newlist)

#set all value of list with hello except kiwi
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=['hello'+ " "+x for x in fruits if x!='kiwi']
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for i in fruits:
    if i!='kiwi':
        print('hello'+' '+i)
    else:
        print(i)    







































