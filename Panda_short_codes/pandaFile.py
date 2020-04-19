"""
Panda Library
"""
import pandas as pd 
import numpy as np
"""
################# SERIES ###########################
data = ['Karachi', 'Lahore', 'Toronto', 'Delhi']
index = ['k', 'l', 't', 't']
a = pd.Series(data, index)

print (a)

###################
data = {'a': 'Karachi', 'b': 'Lahore', 'c': 'Toronto', 'd': 'Delhi'}
index = ['k', 'l', 't', 't']
a = pd.Series(data)  # for dict no index require it will use keys as index

print (a)

###################


################# DATA FRAMES ####################

d1 = {'a': 'Karachi', 'b': 'Lahore', 'c': 'Toronto'} #keys available a, b, c
d2 = {'a': 'Sammar', 'b': 'Ali', 'd': 'Zainab'} #keys available a, b, d
data = {'first': d1, 'second': d2}
a = pd.Series(data)  # for dict no index require it will use keys as index
print (f"Series: \n{a}")

a = pd.DataFrame(data)  # for dict no index require it will use keys as index
print (f"Data: \n{a}")  #the keys not present in another dict, NaN value will be shown

#### how to display 2d array in DATAFRAME
n1 = np.array([[10, 20, 30], [11, 22, 33]])
a = pd.DataFrame(n1)
print()
print(a)
print()


##################
#### change field name ####
s1 = pd.Series([1,2,3,5,8])
s2 = pd.Series([9,8,5,6,3])
s3 = pd.Series([8,4,5,2,6])
data = {'s1' : s1, 's2' : s2, "s3" : s3}
a = pd.DataFrame(data)
print()
print(a)
print()
"""

##################
#### change field rows names ####
s1 = pd.Series([1,2,3,5,8])
s2 = pd.Series([9,8,5,6,3])
s3 = pd.Series([8,4,5,2,6])
data = {'s1' : s1, 's2' : s2, "s3" : s3}
a = pd.DataFrame(data)
a.index = ['a','b','c','d','e']

print()
print(a)
print()
"""
##################
#### read csv files ####
names = pd.read_csv('data23.csv')
print(names)
"""