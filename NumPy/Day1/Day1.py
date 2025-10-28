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

