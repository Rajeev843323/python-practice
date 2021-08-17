#Find maximum occuring character in given string: 1st method

#from typing_extensions import ParamSpecArgs


test_str = "GeeksforGeeks"
dict1={}
for i in test_str:
    if i in dict1:
       dict1[i]+=1
    else:
       dict1[i]=1
a=max(dict1,key=dict1.get)
print(str(a)+":====="+str(dict1[a])) 


#Find maximum occuring character in given string: 2nd method - using function
#Function 1
def maxoccur(text):
    __doc__ = '''
        text = 'abcaad'
        temp = {
            'a': 3,
            'b': 1,
            'c': 1,
            'd': 1
        }
        result = a
    '''
    temp = {}
    for char in text:
        if not char in temp:
            temp[char] = 1
            continue
        temp[char] += 1
    result = max(temp, key=temp.get)
    return result             

 
#function 2
def charoccurance(strinput):
    splitstr={}
    for char in strinput:
        if char in splitstr:
            splitstr[char]+=1
        else:
            splitstr[char]=1
    result=max(splitstr,key=splitstr.get) 
    return result    



#Print duplicate character in given string : 1st method
str="Mynameisrajeevkumar"
list1=[]
list2=[]
for i in str:
    if str.count(i)>1:
        if i not in list1:
            list1.append(i)
print(list1)        

   
#Print duplicate character in given string : 2nd method     
str="Thisismyfavourate"
temp={}
temp2=[]
for char in str:
    if char in temp:
        temp[char]+=1
    else:
        temp[char]=1
for x,y in temp.items():
    if y>1:
        temp2.append(x)
print("Duplicate values are:")
print(temp2)    


#Print duplicate character in given string : 3rd method using function 
def duplicatefind(str):
    tempdict={}
    templist=[]
    for char in str:
        if char in tempdict:
            tempdict[char]+=1
        else:
            tempdict[char]=1

    for key, value in tempdict.items():
        if value>1:
            templist.append(key)
    return templist

#print duplicate character 4th method
str5="ttttthhhhhisppukky"
newstr=""
for char in str5:
    if char not in newstr:
        
    else:
        print("only duplicate: "+newstr[char])
    



if __name__=="__main__":
    stringoriginal="Thisisstringcheckkkkkks"
    print('max occurance character in string is',charoccurance(stringoriginal))
 
    test_str = "GeeksforGeeks"
    print("TEST 1:", maxoccur(test_str))

    test_str = "Hello World"
    print("TEST 2:", maxoccur(test_str))  

    str=input("Enter string in whcich will find duplicate: ")
    print("Duplicate string are :",duplicatefind(str))





