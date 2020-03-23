"""
@author: Sammar Abbas
"""

import numpy as np ### defining alias of it


""" HOW TO CHECK Data Type and CHANGING Data Type OF Ndarray """
""" HOW TO change from an array to list """

a = np.array([1,2,3]) # 1 dimension array
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype) # shows int32 means it takes 32bits (4bytes) to store int
a = a.astype('float32') # changing data type
print(a.dtype)
print(a) 
print()
print("-----------")
print()

b = np.array([ [1,2,3] , [4,5,6] ]) # 2 dimensions array
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)
lst = b.tolist() # convert from array to list
print(lst)
print()
print("-----------")
print()

c = np.array([ [ [1,2,3],[4,5,6] ] , [ [11,12,13],[14,15,16] ] ]) # 3 dimension array
print(c)
print(c.ndim)
print(c.shape)
print(c.dtype)
print()
print("-----------")
print()

print("++++++++++++++++++++++")

