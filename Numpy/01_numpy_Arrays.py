import numpy as np
# lst1 = [1, 2, 3, 4, 5]
# arr1 = np.array(lst1)
# print(arr1)
# print(type(arr1))
# print(arr1.shape)

# lst2 = [6,7,8,9,10]
# lst3 = [11,12,13,14,15]
# arr2 = np.array([lst1, lst2, lst3])
# print(arr2)
# print(arr2.shape)

# arr3 = np.array([1,2,3,4,5,7,8,9,9,0,87,6])
# print(arr3)

# print(arr3[1:])
# print(arr3[:-2])
# print(arr3[2::3])


# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]],ndmin=5)
# print(arr)

# print(arr.ndim)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

newarr = arr.reshape(-1)

print(newarr)