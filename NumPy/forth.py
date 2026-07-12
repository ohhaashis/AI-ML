# Multi-Dimensional Array
import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr2d)
print(np.sum(arr2d))

no_of_columns = np.sum(arr2d,axis = 0)

print(f"sum of columns : {no_of_columns}")

no_of_rows = np.sum(arr2d,axis = 1)

print(f"sum of rows : {no_of_rows}")

print(arr2d[0:3,1])