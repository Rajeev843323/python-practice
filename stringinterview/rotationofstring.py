'''Write an efficient program to test if two given String is a rotation of each other
or not, e.g. if given String is "XYZ" and "ZXY" then your function should return true,
but if the input is "XYZ" and "YXZ" then return false.'''
'''str1="XYZ"
str2="ZYx"
temp1=str1[::-1].lower()
temp2=str2.lower()
if temp1==temp2:
   print(True)
else:
   print(False)'''   

def isstrrotational(str1, str2):
    if len(str1)!=len(str2):
        output1="leangth of both string is not matched so both are different"
    else:
        temp1=str1[::-1].lower()
        temp2=str2.lower()
        if temp1==temp2:
            output1="Yes both string are reverse of each other where case of string not considered"
        else:
            output1="both are different string"    
           
    return output1


#reverse the string without recursion
def reversestringwithloop(str):
    temp=""
    for i in range(len(str)-1,-1,-1):
        a=str[i]
        temp=temp+a
    return temp




if __name__=="__main__":
    print("reverse string using loop output is : " + reversestringwithloop("abcedg"))
    print(isstrrotational("Rajeev","veijar"))
    