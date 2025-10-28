# Day 1 - NumPy Basics
import numpy as np
import sys
import time

# --------------------------
# 1. Continuous Memory (Compact Storage)
# --------------------------
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

print("Python list element addresses:")
for x in py_list:
    print(id(x))

print("\nNumPy array element addresses:")
print(np_array.__array_interface__['data'])


# --------------------------
# 2. Vectorization
# --------------------------
list_data = [1, 2, 3, 4, 5]
list_result = [x * 2 for x in list_data]
np_data = np.array([1, 2, 3, 4, 5])
np_result = np_data * 2

print("\nList result:", list_result)
print("NumPy result:", np_result)

# --------------------------
# 3. Same Data Type
# --------------------------
py_list = [1, '2', 3.5, 4, True]
np_array = np.array([1, 2, 3, 4])

types_list = [type(x) for x in py_list]
print("\nPython list types:", types_list)
print("NumPy array type:", np_array.dtype)

# Mixed Data Types Examples
arr = np.array([1, 2, "hello", 3])
print("\nMixed int+str:", arr, "dtype:", arr.dtype)

arr = np.array([1, 2, 3.5, 4])
print("Mixed int+float:", arr, "dtype:", arr.dtype)

arr = np.array([1, 0, True, False])
print("Mixed int+bool:", arr, "dtype:", arr.dtype)

