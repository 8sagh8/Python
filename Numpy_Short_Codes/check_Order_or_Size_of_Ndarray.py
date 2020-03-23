"""
@author: Sammar Abbas
"""

import numpy as np ### defining alias of it


""" HOW TO CHECK ORDER AND SIZE OF Ndarray """

a = np.array([1,2,3]) # 1 dimension array
print(a)
print(a.ndim)
print(a.shape)
print()
print("-----------")
print()

b = np.array([ [1,2,3] , [4,5,6] ]) # 2 dimensions array
print(b)
print(b.ndim)
print(b.shape)
print()
print("-----------")
print()

c = np.array([ [ [1,2,3],[4,5,6] ] , [ [11,12,13],[14,15,16] ] ]) # 3 dimension array
print(c)
print(c.ndim)
print(c.shape)
print()
print("-----------")
print()

print("++++++++++++++++++++++")

