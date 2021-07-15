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

#Negative index: -1 index indicating the last item in the list
