'''s="1234"
print(type(s))
a=(int(s))
print(type(a))'''

'''def romanval(strrom):
    if strrom=="I":
        return 1
    if strrom=="V":
        return 5
    if strrom=="X":
        return 10
    if strrom=="L":
        return 50
    if strrom == "C":
        return 100
    if strrom=="D":
        return 500
    if strrom=="M":
        return 1000    
    return -1

def romanchange(string):
    i=0
    result=0
    while i < len(string):
        temp1=romanval(string[i])
        
        if i+1 < len(string):
            temp2=romanval(string[i+1])
            
            if temp1>=temp2:
                result = result + temp1
                i = i + 1
            else:
                result = result + temp2 - temp1
                i = i + 2
        else:
            result = result + temp1
            i = i +1
    return result'''


#Find permutation of given string



    

#if __name__=="__main__":
    #print(romanval("M"))
 #   print(romanchange("MDMDXCIX"))
    
