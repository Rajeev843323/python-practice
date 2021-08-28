"""Dictionary are used to store collection of data with their key:value pairs.
Dictionary is ordered, changable and not allow duplicates. Dictionaries are written with
curly brackets {} and have its keys and values. we can print item value by using key ex"""

dict1={'id':101,'name':'Rajeev Kumar','salary':40000}
print(dict1)

dict1={'id':101,'name':'Rajeev Kumar','salary':40000}
print(dict1['name'])
print(len(dict1))

#get the value of dictionary using key and using get() function
dict1={'id':101,'name':'Rajeev Kumar','salary':40000}
x=dict1['name']
print(x)
y=dict1.get('id')
print(y)

#keys() method returns all the keys of a dictionary
print(dict1.keys())

#Adding items into dictionary
dict1={'id':101,'name':'Rajeev Kumar','salary':40000}
dict1['address']='Delhi'
print(dict1)

#update dictionary
dict1.update({'name':'Rakesh','pin':843323})
print(dict1)

#remove items from dictionary
dict1.pop('pin')
del(dict1['id'])
print(dict1)
dict1.clear()
print(dict1)

#Loop in dictionary

#This will show all key name of a dictionary
dict1={'id':101,'name':'Rajeev Kumar','salary':40000}
for x in dict1:
    print(x)
#OR
for x in dict1.keys():
    print(x)

#print all value of a dictionary
for x in dict1:
    print(dict1[x]) 
#OR
for x in dict1.values():
    print(x)       

#Print all keys and values of a dictionary using items() method
for x,y in dict1.items():
    print(x,y)

#Copy a dictionary: this can be done using copy() and dict() function
dict1={'id':101,'name':'Rajeev Kumar','salary':40000}
dict2=dict1.copy()
dict3={}
print(dict2)
dict3=dict2.copy()
print(dict3)
dict4=dict(dict3)
print(dict4)

#Nested Dictionary
employee={
    'employee1':{
        'eid': 101, 'name':'Rajeev Kumar','age':32
    },
    'employee2':{
        'eid':102, 'name': 'Prakash Kumar','age':35
    },
    'employe3':{
        'eid':103,'name':'Vyom Sharma','age':45
     }
}

print(employee)

#OR we can create 3 dictionary separately and create another one dictionary which hold 3
employee1={
        'eid': 101, 'name':'Rajeev Kumar','age':32
        }
employee2={
        'eid':102, 'name': 'Prakash Kumar','age':35
        }
employe3={
        'eid':103,'name':'Vyom Sharma','age':45
        }
employee={'employee1':employee1,'employee2':employee2,'employee3':employe3}
print(employee)
