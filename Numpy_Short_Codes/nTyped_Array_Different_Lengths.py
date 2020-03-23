"""
@author: Sammar Abbas
"""

import numpy as np ### defining alias of it


""" for n type of array with different length of values
    print function will show as two lists instead of MATRIX 
"""
"""
c = np.array([[4,5,6],[7,8], ['a','b','c']]) 

print(c)
print(type(c))

print("++++++++++++++++++")
"""

""" for n type of array with different length of values
    print function will show as two lists instead of MATRIX 
"""
"""
d = np.array([[4,5,6], "SAM"]) 

print(d)
print(type(d))

print("++++++++++++++++++")
"""

"""WHY Ndarray store same type of data
    if we enter on string and rest int it will cast them into string
    or if one float rest int then it will cast into float
"""
"""
a = np.array([[1,2,3],[5,6,7.5]])
print(a)

print("++++++++++++++++++")
"""

""" HOW TO CHECK DIMENSIONS OF ARRAY """
"""
a = np.array([[1,2,3],[5,6,7.5]])
print(a.ndim)  #.ndim to see dimensions  # will show 2

b = np.array([[1,2,3],[5,6]])
print(b.ndim)  #.ndim to see dimensions  # will show 1

print("++++++++++++++++++")
"""


""" HOW TO CHECK ORDER AND SIZE OF Ndarray """

"""
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
"""

""" HOW TO CHECK Data Type and CHANGING Data Type OF Ndarray """
""" HOW TO change from an array to list """

"""
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

"""

""" ACCESSING OF DATA and MANIPULATION """
"""
b = np.array([ [1,2,3] , [4,5,6] ]) # 2 dimensions array
print(b)

print(b[0][2])
print(b[1][1])

# above can be written in this way also

print(b[0,2])
print(b[1,1])

b[0,2] = 5 # will change value of that index only
b[0] = 11,12,13  # will change value of entire column
print(b)
print("----+++----")
b[0] = [21,25,29]  #this will row index 0, not concatenate it
print(b)

print(b[::,0]) # means give me all rows and only Column index "0"
print(b[1::,:2])

print()
print("-----------")
print()

print("++++++++++++++++++++")
"""

""" NAN - Not A Number; special value """
"""
a = np.array([ [1,2,3], [4,5,6], [7,8,9] ], dtype=float)
a[1,1] = np.nan
print(a)

print("+++++++++++++++++++++")
"""

""" full with ZEROS, ONES and FULL """
"""
a = np.zeros(5)  # create array size 5 values all 0 in float
a = np.ones(5)  # create array size 5 values all 1 in float
a = np.ones((5,2)) # 2 dimension row 5 and column 2 values 1 in float

#we don't have such function for 2s 3s 4s..... but we use full
a = np.full(5, 2)  #create array of size 5 value all 2 in INT not float
print (a)
print(a.dtype)

print("++++++++++++++++++++++++")
"""

""" IDENTITY MATRIX - it is always of same rows and column and
 left top to right bottom contains 1
 rest of all are in 0 """
""" 
a = np.identity(3, dtype="float32")
print(a)

print("++++++++++++++++")
"""

""" RANDOM VALUES ARRAY """
"""
a = np.random.randint(8, size = (3,4)) #ending value 7 less than 8
a = np.random.randint(2,8, size = (3,4)) #between 2 to 7
a = np.random.rand(3)  # randomly producing number but less than zero but in array[3]
a = np.random.randint(3) #this won't create array but just a value between 0 to 2 not 3
print(a)
print("+++++++++++++++++++++++")
"""

