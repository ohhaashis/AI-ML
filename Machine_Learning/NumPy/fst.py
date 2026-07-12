import numpy as np
import time

arr = np.array([1,2,3,4,5,6,7,8,9,0,])
a = [1,2,3,4,5,6,7,8,9,0,]

# print(type(arr)) # <class 'numpy.ndarray'>
# print(type(a)) # <class 'list'>

## execution performance

size = 1_000_000
py_list = list(range(size))

# start = time.time()

# sq_list = [x**2 for x in py_list]

# end = time.time()

# print(f"Python list time = {end-start} seconds")

np_arr = np.array(py_list)

# st = time.time()

# # vectorization
# sq_arr = np_arr**2

# ed = time.time()

# print(f"Numpy Array time is = {ed-st} seconds")

### memory 

import sys 

print(f"python list size = {sys.getsizeof(py_list)*len(py_list)} bytes")
print(f"numpy array size = {np_arr.nbytes} bytes")