"""
@author: Sammar Abbas
"""
import numpy as np ### defining alias of it

""" RANDOM VALUES ARRAY """

a = np.random.randint(8, size = (3,4)) #ending value 7 less than 8
a = np.random.randint(2,8, size = (3,4)) #between 2 to 7
a = np.random.rand(3)  # randomly producing number but less than zero but in array[3]
a = np.random.randint(3) #this won't create array but just a value between 0 to 2 not 3
print(a)
print()
print("+++++++++++++++++++++++")
