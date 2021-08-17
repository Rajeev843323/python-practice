"""copy is a new array which is a copy of original array and view is just a view of
original array. if any changes done in copy will not effect the original array, if
changes done in view will effect the original array. """

#make a copy change the original array and display both array
import numpy as np
from numpy.core.fromnumeric import ndim
arr1=np.array([1,2,3,4,5])
x=arr1.copy()
arr1[0]=10
print(arr1)
print(x)

#Make a view, change the original array and display both array.
arr2=np.array([2,4,6,8,10])
y=arr2.view()
arr2[1]=50
print(arr2)
print(y)

#Make a view, change the view and display both array
arr3=np.array([10,20,30,40])
z=arr3.view()
z[2]=100
print(arr3)
print(z)

#check array have own array using base method if array owns the data will return none
a=arr3.copy()
b=arr3.view()
print(a.base)
print(b.base)


"""Shape of an array: Shape of an array provides no. of elements in each dimension. it 
returns a tuple with no. of its index having no. of corresponding elements. """
arr = np.array([[1, 2, 3, 4], [5, 6, 7,8]])
print(arr.shape)

"""Reshape of array: Reshaping means change the shape of an array. we know shape of an
array means no. of elements in each dimension. so through reshaping we can change it 
means add or remove dimensions or change no. of elements in each dimension. """
#convert 1-D array into 2-D array with its 4 dimension having 3 elements each.
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr5=arr4.reshape(4,3)
print(arr5)

#convert 1-D into 3-D array will have 2 arrays that contains 3 array, each with 2 elements
arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr7=np.array([[[1,2],[2,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
arr8=np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
arr9=arr6.reshape(2,3,2)
arr10=arr6.reshape(3,2,2)
print(arr9)
print(arr10)

#convert multidimensional array into 1-D array we are using reshape(-1) methos
arr8=np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
arr11=arr8.reshape(-1)
print(arr11)

#convert 3-d into 2-d array
arr12=arr8.reshape(3,4)
print(arr12)

"""Numpy Array: Iterating: Iterating means going through elements one by one """ 
#Iterate on the elements of the following 1-D array
import numpy as np
arr13=np.array([2,4,6,8])
for x in arr13:
    print(x)

#Iterate the elements of 2-D array
arr14=np.array([[2,4,6,8],[10,12,14,16]])
for x in arr14:
    print(x)
    for y in x:
        print(y)

#Iterate elements of 3-D array
arr15=np.array([[[1,2,3,4,5],[6,7,8,9,10]],
[[11,12,13,14,15],[16,17,18,19,20]]]) 
print(arr15)
for x in arr15:
    print(x)       

for a in arr15:
    for b in a:
        for c in b:
            print(c)

"""Iterating array using nditer(): this nditer() function can be used from basic to 
advance iteration. in basic we are using for loop for n time and this is difficult to
write so we can use nditer() this will print each element of array"""

for x in np.nditer(arr15):
    print(x)

"""Enumerated Iteration using ndenumerate(): Enumerate means mentioning sequence number
of elements one by one. Sometime we have required corresponding index of elements while
itering. for this purpose we are using ndnumerate() function."""    

#enumerate the following 1-D array
import numpy as np
arr16=np.array([2,4,6,8,10])
for indx, x in np.ndenumerate(arr16):
    print(indx,x)

#enumerate the 2-D array
arr17=np.array([[1,2,3,4,5],[2,4,6,8,10],[10,20,30,40,50]])
for indx,x in np.ndenumerate(arr17):
    print(indx,x)

