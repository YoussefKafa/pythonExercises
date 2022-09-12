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

