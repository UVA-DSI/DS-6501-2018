#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:53:44 2018

@author: lpa2a
"""

# Convention
import numpy as np

# Set up an array
data1 = [0,1,2,3,4,5]
arr1 = np.array(data1)

# Inspect member variables -- OOP alert
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)

# What if mixed with floats
data2 = [0,1,2,3,4.5,5]
arr2 = np.array(data2)
print(arr2.dtype)

# What if mixed with string
data3 = [0,1,2,3,'pizza',5]
arr3 = np.array(data3)
print(arr3.dtype)

# What if mixed with string differently
data3 = ['pizza',1,2,3,4,5]
arr3 = np.array(data3)
print(arr3.dtype)

# mismatched list of lists --> 1dim
data4 = [[0,1,2],[3,4]]
arr4 = np.array(data4)
print(arr4)
print(arr4.shape)

# matched list of lists
data5 = [[0,1,2],[3,4,5]]
arr5 = np.array(data5)
print(arr5)
print(arr5.shape)


# other array generators
arr6 = np.zeros(10)
print(arr6)
arr7 = np.empty(10)
print(arr7)
arr8 = np.arange(10)
print(arr8)    

# and there are others -- see the text book
# Let's look up the docs for np.zeros
# good search numpy documentation zeros

# Type conversion or casting
print(arr8.dtype)
arr9 = arr8.astype(np.float)
print(arr9.dtype)

### NB: astype(...) creates a new array, it does not change initial array

# You can do array math
arr10 = np.arange(5)
print(arr10+arr10)


##### Indexing and Slicing works like python

arr11 = np.arange(10)
print(arr11)
print(arr11[4])
print(arr11[4:8])
arr11[4:8] = -1
print(arr11)

# Terminology: broadcasting -- line 79 - a value is pushed to many places
# slices are views: modifying a view modifies the source

arr12 = arr11[4:8]
arr12 = -5
print(arr11)
print(arr12)

# To make a copy use .copy(...)
arr13 = arr11[4:8].copy()
print(arr13)
arr13[:]=22
print(arr13)
print(arr11)


# we're not going to get into 2D stuff in class
# but feel free to come to office hours to talk about them



### Booblean Indexing -- cool and useful

# example straight from book - minor differences

names = np.array(['Bob', 'Joe', 'Will', 'Bob'])
data = np.random.randn(4, 4)

print(names)
print(data)

print(names == 'Bob')
print(data[names == 'Bob'])

mask = (names == 'Bob') | (names == 'Will')

print(data[mask])

data[data < 0] = 0


# Fancy Indexing - our first slight of hand
arr14 = np.arange(10)
print(arr14)
print(arr14[[5,2,8,6]])



# Reshaping

arr = np.arange(15).reshape((3, 5))
print(arr.T)
print(arr)
print(arr.swapaxes(0,1))  # can go to higher dimensions



# universal functions
print(np.sqrt(arr14))
# other usual suspects: abs,exp,floor, etc - nice table in book



# Who got the Expressing Conditional Logic as Array Operations
# it shows two ways to do something.
#   1) base python
#   2) using numpy
#   you need to have the magic function np.where
#   as we go through the class pay attention to the functions
# before you see them/are introduced to them you won't think to use them

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(cond, xarr, yarr)

print(result)



# statistical methods.
# nice table in the book

# another special function
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))

# again theres a table in the book



