#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:18:05 2018

@author: lpa2a
"""

# import convention
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# series
ser = Series([4, 7, -5, 3])
print(ser)

ser = Series([4,'pizza',-5,3])
print(ser)

type(ser)

# index on the left and values on the right

# to recover values
ser.values
type(ser.values) # numpy.ndarray

# to recover indecies
ser.index


# setting indecies
ser2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])


# two ways to index
print(ser2[0])
print(ser2['d'])

# the return of fancy indexing
print(ser2[['a','b','c']])


# our usual tricks still work
print(ser2[ser2>0])
print(ser2*2)
print(np.exp(ser2))
# and many more


# before we've generated from lists, here's for dicts
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
ser3 = Series(sdata)
print(ser3)

# what if we have a different format to the dict
sdata2 = {'Ohio': {'baseball':35000}, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
ser3b = Series(sdata2)
print(ser3b)

# now lets set the indecies by hand
states = ['California', 'Ohio', 'Oregon', 'Texas']
ser4 = Series(sdata, index=states)
print(ser4)




### NaN (not a number) which is considered in pandas to mark missing or NA values.


# use these guys to detect NaN
print(pd.isnull(ser4))
print(pd.notnull(ser4))




### major point: indecies are aligned for operations

print(ser3)
print(ser4)
print(ser3+ser4)


# you can edit a series index in place
ser4.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(ser4)
ser4
