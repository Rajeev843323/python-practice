#How to remove characters from the first String which are present in the second String?
__doc__='''
"Write an efficient Python function that takes two strings as arguments and removes the
characters from the first string, which are present in the second string also. For
example, if the first String ""India is great"" and second String is ""in"" then the
output should be ""da s great
Read more: https://www.java67.com/2018/04/21-string-programming-and-coding-interview-
questions-answers.html#ixzz6UujIiUDN'''

#method 1
str1="india is great"
str2="in"
temp=""
for i in str1:
    if i in str2:
        pass
    else:
        temp=temp+i    
print(temp)    


#Method 2 : by function
def remvdupl2string(str1,str2):
    temp=""
    for char in str1:
        if char in str2:
            pass
        else:
            temp=temp+char
    return temp



if __name__=="main":
    print(remvdupl2string('india is great','in'))          