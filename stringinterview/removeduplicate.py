#Remove duplicate method 1

str="ttthhiiiisssjkuuuuooooy"
temp={}
newstr=[]
s=""
for char in str:
    if char in temp:
        temp[char]+=1
    else:
        temp[char]=1
print(temp)    

for key, value in temp.items():
    if value==1:
        newstr.append(key)
    elif value>1:
        newstr.append(key[0])

for i in newstr:
    s=s+i
print(s)    

#Remove duplicate using unordered set 2nd method
str="tttthhhhiiiissss"
b=set(str)
newstr="".join(b)
print(newstr)

#Remove duplicate following the same order of string 3rd method
str="hhhhiiiisssstttt"
b=set(str)
newstr=""
__doc__=''' in below loop if character already found in newstr variable (blank) then pass to next
step of loop without doing anything else part is saying if character not found then
append to next character in newstr'''


for i in str:
    if i in newstr:
        pass
    else:
        newstr=newstr+i
print(newstr)        


#Remove duplicate by make a function

def delduplicate(strng):  
    newstr=""
    for char in strng:
        if char in newstr:
            pass
        else:
            newstr=newstr+char
    print(newstr)


if __name__== "__main__":
    strng="thththiiiishshclass" 
    delduplicate(strng)

from removeduptwostring import remvdupl2string
print(remvdupl2string('india is great','in'))          







