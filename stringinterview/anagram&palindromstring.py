'''two string are called anagram of each other when length and characters both are same
in both string but its order is different of each other ex army and mary'''
'''str1="ArmY"
str2="MaRy"
temp1=set()
temp2=set()
for i in str1:
    temp1.add(i.lower())
for i in str2:
    temp2.add(i.lower())    
    
if temp1==temp2:
    print("both are anagram")
else:
    print("both are not anagram")    '''

#2nd method to check anagram using function and avoid case of string also
'''def isanagram(str1, str2):
    tempset1=set()
    tempset2=set()
    for char in str1:
        tempset1.add(char.lower())
    for char in str2:
        tempset2.add(char.lower())
    if tempset1==tempset2:
        print("Yes " + str1 + ": is anagram of " + str2)
    else:
        print("No " + str1 + ": is not anagram of " + str2)   '''

#Method 3 anagram sollution using sort
'''def checkanagram(str1, str2):
    a=str1.lower()
    b=str2.lower()
    if len(str1)==len(str2):
        if sorted(a)==sorted(b):
            print(str1 + " is anagram of :" + str2)
        else:
            print("both are not anagram")
    else:
        print("length of both string is not equal so not an anagram")   '''        


'''Check string is palindrome: String is said to be palindrome if its reverse of the 
string is same as string. for example radar, malyalam etc'''
def palindrome(str):
    temp1=""
    temp2=""
    for i in str:
        temp1+=i

    for j in range(len(str)-1,-1,-1):
        temp2=temp2+str[j]

    if temp1.lower()==temp2.lower():
        print("String "+ str + " is palindrome")
    else:
        print("String "+ str + " is not palindrome")  


if __name__=="__main__":

    #isanagram("Dalda", "ladla")
    #checkanagram(input("input string first: "), input("\n input string 2nd :"))
    palindrome("malayaLAm")
