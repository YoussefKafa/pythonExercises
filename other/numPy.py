import numpy as np
"""
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
"""
arr = np.array([1,2,3,4,5]) #ndarray
"""
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
"""
arr1=np.array((1,2,3,4,5))

#2D-array
arr2=np.array([[1,2],[3,4]])
#print(arr2.ndim) #prints 2
#3D-array
arr3=np.array([   [[1,2],[3,4]] ,   [[5,6],[7,8]]   ])
#print(arr3.ndim) #prints 3

#n-D array
arr4=np.array([1,2,3,4,5], ndmin=6)
#print(arr4.ndim) #prints 6

# array indexing
#print(arr1[1]) #prints 2
#print(arr2[1,0]) #prints 3
#print(arr3[0,0,0]) #prints 1

# slicing arrays
"""
We pass a slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
"""
arr1=[1,2,3,4,5]
#print(arr1[0:2]) #prints 1 2
#print(arr1[0:4:1]) #prints 1 2 3 4
#print(arr1[0:4:2])  #prints 1 3
#print(arr1[0:5:2]) #prints [1,3,5]
#print(arr1[0:10]) #prints [1,2,3,4,5]
#print(arr1[:3]) #prints [1,2,3]
#print(arr1[-3:-1]) #prints [4,3]
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#print(arr[0:2, 1:4]) #[[2 3 4][7 8 9]] #arrays from 0 to 2 and slice from 1 to 4 from each



# Data types in numpy
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
arr = np.array([1, 2, 3, 4], dtype='S')
#print(arr) #prints [b'1' b'2' b'3' b'4']
#print(arr.dtype) #prints |S1
arr = np.array([1, 2, 3, 4], dtype='i4') #4 is the size
#print(arr) #prints [1 2 3 4]
#print(arr.dtype) #prints int32
#arr = np.array(['a', 2, 3, 4], dtype='i')
#the last array raise an error ( ValueError: invalid literal for int() with base 10: 'a' )
#converting
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('S')
#print(newarr) #prints [b'1.1' b'2.1' b'3.1']
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
#print(newarr) # [True False True]

# Copy VS. View
"""
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
"""
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
#print(arr) #[42  2  3  4  5]
#print(x) # [1 2 3 4 5]

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
#print(arr) # [42  2  3  4  5]
#print(x) # [42  2  3  4  5]

