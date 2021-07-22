"""Sets are used to store multiple items in a single variable this is one of 4 built in
data type in python other three are list, tuple and dictionary sets are collection on 
records unorded and unindexed this is written with curly brackets {}. unordered means
we are not sure that in which order items will appear. Set items are unordered, 
unchangable and do not allow duplicate values. we can not define its item by index
because everytime orders of sets items has been changed. once the set is created we can
not changed its item but we can add new item in sets. ex"""

thisset={'apple', 'banana', 'cherry'}
print(thisset)
print(len(thisset))

set1={'apple', 'banana', 2,4,5,True,False}
print(type(set1))

thisset=set(('apple','banana','cherry'))
print(thisset)

"""Access set items: We can not access items of set using an index or a key, but we use 
loop or specified value with 'in' keyword for accessing the items. ex"""

thisset={'apple', 'banana', 'cherry'}
for i in thisset:
    print(i)

#check banana in set
thisset={'apple', 'banana', 'cherry'}
if 'banana' in thisset:
    print('banana is in thisset')

#Add items in set using add() function
thisset={'apple', 'banana', 'cherry'}
thisset.add('mango')
print(thisset)    

#add items from another set using update(), we can also add list, tuple, dictionary
set1={'apple','banana', 'cherry'}
set2={'mango','guava', 'papaya'}
list1=['A','B','C','D']
tuple1=(2,4,6,8)
set1.update(set2)
set1.update(list1)
set1.update(tuple1)
print(set1)


#Remove set items
set1={'apple','banana', 'cherry'}
set1.remove('banana')
print(set1)

set1={'apple','banana', 'cherry'}
set1.discard('banana')
print(set1)


set1={'apple','banana', 'cherry'}
set1.pop()
print(set1)


set1={'apple','banana', 'cherry'}
set1.clear()
print(set1)


set1={'apple','banana', 'cherry'}
del(set1)
print(set1)

#Join sets or add sets: several way we can add or join 2 sets
#Union or update print all item from both sets excluding duplicate value
set1={"a","b", "c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

set1={"a","b", "c"}
set2={1,2,3}
set1.update(set2)
print(set1)

#intersection_update() or intersection () method print only common item from both sets
set1={"a","b", "c"}
set2={'a','d','e','c'}
set1.intersection_update(set2)
print(set1)

set1={"a","b", "c"}
set2={'a','d','e','c'}
set3=set1.intersection(set2)
print(set3)

#print all elements from both set excluding common or duplicate items
set1={"a","b", "c"}
set2={'a','d','e','c'}
set1.symmetric_difference_update(set2)
print(set1)

set1={"a","b", "c"}
set2={'a','d','e','c'}
set3=set1.symmetric_difference(set2)
print(set3)