#Find first non reapeating character in a string: Method 1
"""str="isthisnotmyname"
tempdup=[]
tempuniq=[]
for i in str:
    if str.count(i)>1:
        if i not in tempdup:
            tempdup.append(i)
    elif str.count(i)==1:
        if i not in tempuniq:
            tempuniq.append(i)
print("First non repeating character is: "+tempuniq[0])
    
#Method 2 first non repeating
strinput="firstfnonrepeatinglettercheck"
tempdict={}
templist=[]
for char in strinput:
    if char in tempdict:
        tempdict[char]+=1
    else:
        tempdict[char]=1    
for key, val in tempdict.items():
    if val==1:
        templist.append(key)
print("First non repeating character in string is :" + templist[0])      

#method 3
def firstnonrepeatchar(str):
    temp1={}
    temp2=[]
    for ch in str:
        if ch in temp1:
            temp1[ch]+=1
        else:
            temp1[ch]=1
    for key, val in temp1.items():
        if val==1:
            temp2.append(key)
    return temp2[0]"""

#reverse of words in sentence : method 1
'''sentence="My name is Rajeev Kumar"
temp=list(sentence.split(" "))
for i in range(len(temp)-1,-1,-1):
    print(temp[i])'''

#reverse of words using function : method
def reverse(sentence):
    answer = ''
    temp = ''
    for char in sentence:
        if char != ' ':
            temp+=char
        else:
            answer = temp + ' ' + answer
            temp = ''
    answer = temp + ' ' + answer
    return answer


'''a=""
t=""
s="This is python class"
for i in s:
    if i != " ":
        t=t+i
    else:
        a=  t + " " + a
        t=""
a = t + " " + a
print(a)
#if want to remove one extra space after class then print like this
print(a[0:-1])'''




if __name__=="__main__":
  #  print(reversewords("my name is Rajeev Kumar Gupta"))
#print("Non repeat char>>>>: " + firstnonrepeatchar("aabbcdde") 
   #sentence = 'This is a string to try'
   print(reverse("my name is Rajeev Kumar Gupta"))
