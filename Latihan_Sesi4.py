# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 13:13:51 2022

@author: chris
"""
import numpy as np



a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) #aray=kumpulan data
print(a[0])

[[0.1, 0.2, 0.3],
 [1., 1., 1.]]
print(a[0,1])

import numpy as np
a = np.array([1, 2, 3])


np.zeros(6)

print(np.arange(4))
print(np.arange(0,10,2)) # (start, stop, step)

# batasannya 10,kenaikan 2

print(np.arange(4))
print(np.arange(0,50,10)) # (start, stop, step)

np.arange(2,29,5)

# np.append()
# np.delete()
# np.sort()

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.append(arr,[6,7,8,9])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.delete(arr, 1)
# yg terhapus dihitung dr nol

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.delete(arr, 2)
# yg terhapus dihitung dr nol


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.delete(arr, 6)


arr = np.array([7, 8, 9, 10])
np.delete(arr, 6)


arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
-np.sort(-arr)


# ndarray.ndim()
# ndarray.size()
# ndarray.shape()

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example)
array_example.size
#size = jumlah karakter = 8x3


array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example)
array_example.shape



arr = np.array([2, 1, 5, 3, 7, 4, 6, 8, 11, 12])
a = np.arange(6)
print(a)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
b = arr.reshape(2,4)
print(b)

#2=kolom 4=baris


arr = np.array([1, 2, 3, 4, 5, 6])
arr.shape
arr2 = arr[np.newaxis]
print(arr2.shape)
print(arr2)


arr = np.array([1, 2, 3, 4, 5, 6]) #6 angka
arr.shape
arr2 = arr[np.newaxis]
print(arr2.shape)
print(arr2)

row_vector = a[np.newaxis, :] #titikdua output akan kesamping
print(row_vector.shape)
print(row_vector)



arr = np.array([1, 2, 3, 4, 5, 6]) #6 angka
arr.shape
arr2 = arr[np.newaxis]
print(arr2.shape)
print(arr2)

col_vector = a[:, np.newaxis]
print(col_vector.shape)
print(col_vector)

a = np.array([1, 2, 3, 4, 5, 6])
a.shape


a = np.array([1, 2, 3, 4, 5, 6])
b = np.expand_dims(a, axis=1)
b.shape


data = np.array([1,2,3])

print(data)
print(data[0])
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])


data = np.array([1,2,3, 4, 5, 6])

print(data)
print(data[0])
print(data[1])
print(data[0:4])#seprti subtring
print(data[4:])
print(data[-4:])

data = np.array([1,2,3, 4, 5, 6])
b=sorted(data,reverse=True)
print(b)
print(b[1:])



data = np.array([1,2,3, 4, 5, 6])
b=sorted(data,reverse=True)
print(b)
print(b[-3:])


arr = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
arr
print(arr)
print(arr[arr>=3])



divisible_by_2 = arr[arr%4==1]
print(divisible_by_2)


c = arr[(arr > 2) & (arr < 11)]
print(c)

# slicing indexing
# np.vstack()
# np.hstack()
# np.hsplit()
# .view()
# .copy()

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr1 = arr[3:8]
arr1

arr = np.array
arr([[1, 1, 1],
     [2, 2, 2]])
arr([[3, 3, 3],
     [4, 4, 4]])
a_1=arr([[1, 1, 1],
     [2, 2, 2]])
a_2=arr([[3, 3, 3],
     [4, 4, 4]])
np.vstack((a_1, a_2))


import numpy as np

arrsplit = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
print(arrsplit)
np.hsplit(arrsplit,3)

arrsplit = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
print(arrsplit)
np.hsplit(arrsplit,2)


arrsplit = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
print(arrsplit)
np.hsplit(arrsplit,4)

arrsplit = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
print(arrsplit)
np.hsplit(arrsplit,6)



import numpy as np
a=np.arr([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
b=arr.view
print(arr)


a = np.array([1, 2, 3, 4])
a.sum()

import numpy as np
a=np.array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
a.sum(axis=1)
print(a.sum(axis=1))

import numpy as np
a=np.array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
a.sum(axis=0)
print(a.sum(axis=0))

import numpy as np
np.array([[1,2],[3,4]])
print(np.array([[1,2],[3,4]]))
print(np.ones((3,2)))
print(np.zeros((3,2)))
print(np.random.random((3,2)))


data_col = np.array([[1, 2, 3, 4, 5, 6]]).T
print(data_col)

import numpy as np
np.array([[1, 2, 3],
       [4, 5, 6]])
data_col.reshape(3, 2)













import numpy as np
arrflat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arrflat)
arrflat.flatten()



















