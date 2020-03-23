"""
@author: Sammar Abbas
"""
import numpy as np ### defining alias of it


""" NAN - Not A Number; special value """

a = np.array([ [1,2,3], [4,5,6], [7,8,9] ], dtype=float)
a[1,1] = np.nan
print(a)

print()
print("+++++++++++++++++++++")
print()

""" full with ZEROS, ONES and FULL """

a = np.zeros(5)  # create array size 5 values all 0 in float
a = np.ones(5)  # create array size 5 values all 1 in float
a = np.ones((5,2)) # 2 dimension row 5 and column 2 values 1 in float

#we don't have such function for 2s 3s 4s..... but we use full
a = np.full(5, 2)  #create array of size 5 value all 2 in INT not float
print (a)
print(a.dtype)

print()
print("++++++++++++++++++++++++")

