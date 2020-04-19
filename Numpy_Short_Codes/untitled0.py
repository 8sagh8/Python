# -*- coding: utf-8 -*-
"""
NUMPY few small functions and caluclations
NUMPY read data from file
"""

import numpy as sam

a = sam.array([1,2,3])
print(a)
print(f"Dimension of an array: {a.ndim}")   # check dimension of an array

a = sam.array([[1,2,3], [2, 3, 7]])
print(a)
print(f"Dimension of an array: {a.ndim}")   # check dimension of an array

a = sam.array([[1,2,3], [2, "a", 7]])
print(a)
print(f"Dimension of an array: {a.ndim}")   # check dimension of an array

a = sam.array([[1,2,3], [2, 3.5, 7]])
print(a)
print(f"Dimension of an array: {a.ndim}")   # check dimension of an array

a = sam.array([[1,2,3], [2, "sam"]])
print(a)
print(f"Dimension of an array: {a.ndim}")   # check dimension of an array

a = sam.array([[1,2,3], [2, 3]])
print(a)
print(f"Dimension of an array: {a.ndim}")   # check dimension of an array



import numpy as sam

a = sam.array([[1,2,3], [2, 3, 7], [4,8,6]])

print(f"shape: {a.shape}")
print(f"dimension: {a.ndim}")
print(f"size: {a.size}")
print(f"{a}")
print(f"mean: \n{a.mean()}") # finding mean of the value
print(f"principal diagonal: \n{a.diagonal()}") # finding principal diagonal of the value
print(f"max value: \n{a.max()}") # finding max value
print(f"another way of max value: \n{sam.max(a)}") # use likewise for others min, add and etc
print(f"min value: \n{a.min()}") # finding min of the value
print(f"multiply all values: \n{a.prod()}") # finding factorial means multiply all the values available in numpy
print(f"changing shape: \n{a.reshape(1,9)}") # reshaping numpy, changing shape but not converted from 2d to 1d
print(f"adding up all the values in matrix: \n{a.sum()}") # add all
print(f"make rows into column and columns into rows: \n{a.transpose()}") # make rows into column and column into rows
print(f"adding all pricipal diagonal values: \n{a.trace()}") # will add values of principal diagonal
print(a)
a.resize(4,3) #this will resize and add additional columns and rows accordingg to need
print(f"changed resize \n{a}")
print(f"adding 2 in matrix's each value: {a+2}") # adding two in each value of a matrix



### make sure data in file to be in correct order because it will be creating a matrix

a = sam.genfromtxt('data.txt', delimiter= " ")
print(a)    #by default data type is float

a = a.astype('int32') #casting into int
print(a)

