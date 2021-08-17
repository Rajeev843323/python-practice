"""Joining numpy arrays: Joining means putting contents of 2 or more arrays in a single
array. In sql two table joining is based on a key, whereas numpy array is joining based
on axis. we are joining arrays using concatenate() function along with its axis, by
default axis taken as zero."""

import numpy as np
arr1=np.array([2,4,6,8])
arr2=np.array([10,20,30,40])
arr3=np.concatenate((arr1,arr2))
print(arr3)

#join 2D array with axis 1
arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6=np.concatenate((arr4,arr5),axis=1)
print(arr6)

#Join 3D array
arr7=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
arr8=np.array([[[17,18,19,20],[21,22,23,24]],[[25,26,27,28],[29,30,31,32]]])
arr9=np.concatenate((arr7,arr8),axis=2)
print(arr9)

#We can also join array using stack() function

import numpy as np
x=np.random.randint(100)
print(x)


