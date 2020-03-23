"""
@author: Sammar Abbas
"""
import numpy as np ### defining alias of it

""" ACCESSING OF DATA and MANIPULATION """

b = np.array([ [1,2,3] , [4,5,6] ]) # 2 dimensions array
print(b)

print(b[0][2])
print(b[1][1])

# above can be written in this way also

print(b[0,2])
print(b[1,1])
print()

b[0,2] = 5 # will change value of that index only
b[0] = 11,12,13  # will change value of entire column
print(b)
print("----+++----")
print()
b[0] = [21,25,29]  #this will row index 0, not concatenate it
print(b)

print(b[::,0]) # means give me all rows and only Column index "0"
print(b[1::,:2])

print()
print("-----------")
print()

print("++++++++++++++++++++")

