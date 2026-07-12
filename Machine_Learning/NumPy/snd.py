import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9,0])
# print(arr,type(arr),arr.dtype)

# arr1 = np.array([1,2,3,4,5,"prime"])
# print(arr1,type(arr1),arr1.dtype)

# print(arr.shape,arr1.shape)

twoD = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(twoD)
print(arr2,type(arr2),arr2.dtype,arr2.shape)

### create

# arr3 = np.zeros((2,3),dtype = "int32")  #prefil
# print(arr3,arr3.shape)

# arr3 = np.ones((2,3),dtype = "int32")  #
# print(arr3,arr3.shape)

# arr3 = np.full((2,3),100)  
# print(arr3,arr3.shape)

# arr3 = np.eye(3)  
# print(arr3,arr3.shape)

# arr3 = np.arange(1,10,2)  
# print(arr3,arr3.shape)

arr3 = np.linspace(0,10,4)  
print(arr3,arr3.shape)

