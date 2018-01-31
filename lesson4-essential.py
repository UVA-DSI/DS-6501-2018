#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:25:56 2018

@author: lpa2a
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# reindexing for series
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj

obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)


obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
obj3.reindex(range(6), method='ffill')


# reindexing for dataframes
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])
frame

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2

states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

### NB: to reindex the columns you use the columns argument

# dropping with series
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj

obj.drop(['d', 'c'])

# dropping with dataframe
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data.drop(['Colorado', 'Ohio'])

data.drop('two', axis=1)

data.drop(['two', 'four'], axis=1)

# inclusive slicing
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj['b':'c']

# dataframe indexing
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data

data[:2]  # first two rows

data[data['three'] > 5] # NB: reference data in index of data

data < 5

data[data < 5] = 0
data

data.ix['Colorado', ['two', 'three']]   # 1st edition of text
data.loc['Colorado', ['two', 'three']]  # current syntax

data.ix[['Colorado', 'Utah'], [3, 0, 1]]
data.loc[['Colorado', 'Utah'], [3, 0, 1]]
data.iloc[['Colorado', 'Utah'], [3, 0, 1]]

# arithmetic operations
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

df1 + df2
#vs
df1.add(df2, fill_value=0)


# cute side trick
df1.reindex(columns=df2.columns, fill_value=0)




# motivation with arrays -- broadcasting
arr = np.arange(12.).reshape((3, 4))
arr

arr[0]

arr - arr[0]

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.ix[0]

frame
series

frame - series

series2 = Series(range(3), index=['b', 'e', 'f'])

frame + series2

series3 = frame['d']

frame
series3

frame.sub(series3, axis=0)


# function application and mapping

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])

frame
np.abs(frame)

f = lambda x: x.max() - x.min()
frame.apply(f) 
frame.apply(f, axis=1)

### NB: a bunch are built in: eg: sum and mean

def f(x):return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)

# for elementwise use applymap
format = lambda x: '%.2f' % x
frame.applymap(format)
frame['e'].map(format)



# sorting
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()

# this works just like you would expect with dataframe
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])

frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=False)


# now shift gears and sort by values
obj = Series([4, 7, -3, 2])
obj.order()  # error
obj.sort_values()

obj = Series([4, np.nan, 7, np.nan, -3, 2])
obj.sort_values()

frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_index(by='b') # from old version of book
frame.sort_values(by='b')  # you can make this a list if you like



# ranking
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()

obj.rank(method='first')

obj.rank(ascending=False, method='max')

frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
frame
frame.rank(axis=1)


# duplicate indecies
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
obj.index.is_unique

obj['a']
obj['c']

# same deal for dataframes
### progress point



