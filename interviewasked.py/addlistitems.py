'''Q. How to do sum of two list items correnpondingly'''
#Method 1 using range in loop
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
list3=[]
for i in range(len(list1)):
    list3=list1[i]+list2[i]
    print(list3)

#Method 2 using zip function. zip itrate the two list items correspondingly
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
for i, j in zip(list1, list2):
    temp=i+j
    print(temp)
    

    