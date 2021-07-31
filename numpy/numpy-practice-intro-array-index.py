"""Numpy means Numerical Python. Numpy is a python library. numpy is used for working
with arrays. Numpy have functions for working in many domain like linear algebra,
fourier transform (frequencies, sound waves related function where function depend on
time and space etc), and matrices. it is open source and can use anyone.

      Numpy provides the array objects which is 50 time more faster than traditional 
python list. ndarray is the object of numpy which support many functions. arrays are very
frequently used in data science. data science is a branch of computer science where we 
study how store, use and analyze data for deriving the output or information. 

      Numpy arrays are stored at one continuous place in memory so processor can access
      and manipulate very quickly. this behaviour is called locality of reference in
      computer science. Numpy is partially written in python language and mostly written
      in C or C++ """
#we can create numpy alias as np and use this in program

import numpy as np
arr=np.array([2,4,6,8,10])
print(arr)      

#check numpy version
print(np.__version__)

#we can create ndarray object using array() function
arr1=np.array([3,4,5,6])
print(arr1) 

#We can pass anything like list, tuple or array and will converted in array while using array() function
arr2=np.array((5,6,8,9))
print(arr2)

"""Dimension in arrays: dimension is one level of array depth(Nested array). Nested array
is the array that have arrays of their elements. """

#0-D (zero dimensional) array with value 42:

arr3=np.array(42)
print(arr3)

#1-D (one dimensional) array is an array which contains its element with 0-D value
arr4=np.array([4,5,6,3,2,0])
print(arr4)

#2-D (2 Dimentional) array is an array containing 1-D array as its elements.
arr5=np.array([[2,4,6,6],[3,5,7,8]])
print(arr5)

#3-D (3 Dimentional) array is an array containing 2-D array as its elements.
arr6=np.array([[[3,4,5,6],[2,4,6,8]],[[7,8,9,0],[0,9,8,7]]])
arr7=np.array([[[3,4,5,6],[2,4,6,8]],[[7,8,9,0],[0,9,8,7]],[[10,20,30,40],[20,40,60,90]]])
print(arr6)
print(arr7)

#check dimensions of given array: ndim is an attribute of arry returning dimenstion
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
print(arr6.ndim)

#Array can have n no. of dimensions. we can define demention using ndmin argument
arr8=np.array([4,6,8,2],ndmin=5)
print(arr8)
print('dimention of array arr8 is :',arr8.ndim)

#Array indexing : is used to access the items of an array
#Access element from 1-D array
import numpy as np
arr9=np.array([2,4,6,8])
print(arr9[2])

#Access items from 2-D array: will take 2 index one is for dimention and other for index
#get 2nd element of 1st dim or 1st dimension
arr10=np.array([[2,4,6,8],[8,10,12,14]])
print(arr10[0,1])

#3rd element of 2nd dim
print(arr10[1,2])

#5th element on 2nd dim
arr11 = np.array([[1,2,3,4,5], [6,7,8,9,20]])
print(arr11[1,4])

#access from 3-D array: take 3 indexes 1st for index 2nd for index of index 3rd for item
#Access the third element of the second array of the first array:
arr12 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr12[0,1,2])

#Negative index in array also accessing array from last
#last element of 2nd dim
arr13 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr13[1,-1])

print(arr13[0:2,2])


"""Slicing the array: syntax is [start:end], if we want to step while definning slicing
syntax is [start:end:step]"""
#Slice elements from index 1 to index 5
arr14=np.array([1,2,3,4,5,6,7,8])
print(arr14[1:5])

#slice from index 4 to end
print(arr14[4:])

#slice from begining to index 4
print(arr14[:4])

#slice from index 3 to end start from end
print(arr14[-3:-1])

#return every other element (alternate) from index 1 to index 5 using step
print(arr14[1:6:2])

#return every other item from entire array
print(arr14[::2])

#Slicing 2-D array
#from the second element of 2-D array, slice elements from index 1 to index 4
arr15 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr15[1,1:4])

#From both elements of 2-D array return index number 2
print(arr15[0:2,2])

#From both elements of 2-D array slice index 1 to index 4
print(arr15[0:2,1:4])

