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


# --------------------------
# 4. Creating Arrays
# --------------------------
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros((2, 3))
arr4 = np.ones((3, 4))
arr5 = np.identity(5)
arr6 = np.arange(10)
arr7 = np.arange(10, 25, 2)
arr8 = np.linspace(0, 20, 10)
arr9 = arr8.copy()

# --------------------------
# 5. Array Properties
# --------------------------
arr10 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr10.shape, arr10.ndim, arr10.size, arr10.itemsize, arr10.dtype)
print(arr10.astype('float'))

# --------------------------
# 6. List vs NumPy
# --------------------------
py_list = list(range(1000))
np_array = np.arange(1000)
print("Python list size:", sys.getsizeof(py_list), "bytes")
print("NumPy array size:", np_array.nbytes, "bytes")

# Speed Test
py_list = list(range(1_000_000))
start = time.time()
py_result = [x * 2 for x in py_list]
print("Python list time:", time.time() - start)

np_array = np.arange(1_000_000)
start = time.time()
np_result = np_array * 2
print("NumPy array time:", time.time() - start)

# --------------------------
# 7. Indexing & Slicing
# --------------------------
arr12 = np.arange(24)
print(arr12[7], arr12[-1], arr12[7:14], arr12[-6:-1])

arr13 = np.arange(24).reshape(6, 4)
print(arr13[2])
print(arr13[:, 2])
print(arr13[4:6, 2:4])

# --------------------------
# 8. Iteration
# --------------------------
for i in np.nditer(arr13):
    print(i, end=" ")

# --------------------------
# 9. Operations
# --------------------------
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([4, 5, 6, 7, 8, 9])
print(arr1 + arr2, arr1 * arr2, arr1 / arr2)
print(arr1 > 3, arr1 == arr2)

# --------------------------
# 10. Reshaping
# --------------------------
arr10 = np.arange(8).reshape(2, 2, 2)
print(arr10.ravel())

arr5 = np.arange(24)
print(arr5.reshape(2, 12).transpose())

# --------------------------
# 11. Stack and Split
# --------------------------
arr3 = np.arange(6).reshape(2, 3)
arr6 = np.arange(12, 18).reshape(2, 3)
arr7 = np.arange(19, 25).reshape(2, 3)

print(np.hstack((arr3, arr6, arr7)))
print(np.vstack((arr3, arr6, arr7)))

print(np.hsplit(arr3, 3))
print(np.vsplit(arr3, 2))

# --------------------------
# 12. Boolean Indexing
# --------------------------
arr = np.random.randint(1, 100, 24).reshape(6, 4)
print(arr[arr > 50])
arr[(arr > 50) & (arr % 2 != 0)] = 0
print(arr)

# --------------------------
# 13. Broadcasting
# --------------------------
arr1 = np.arange(9).reshape(3, 3)
arr2 = np.arange(3).reshape(1, 3)
print(arr1 + arr2)

# --------------------------
# 14. Missing Values
# --------------------------
a = np.array([1, 2, 3, 4, np.nan, 5, 6, np.nan])
print(a)
