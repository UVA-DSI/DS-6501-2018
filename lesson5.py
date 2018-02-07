#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:57:46 2018

@author: lpa2a
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

from numpy import nan as NA


### Descriptive statistics
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
                index=['a', 'b', 'c', 'd'],
                columns=['one', 'two'])
df

df.sum()
df.sum(axis=1) # NB for this one NaNs are treated at 0

df.cumsum()

df.mean(axis=1, skipna=False)

df.describe() # also works on other objects

df.idxmax()  # returns the id of the index of the max


### Handling Missing Data
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data
string_data.isnull()
string_data[0]=None
string_data.isnull()

data = Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()] # another way to do it

data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()  #  row wise
data
cleaned

data.dropna(how='all') # only if whole row is NA

data[4] = NA
data
data.dropna(axis=1, how='all') # for columns



df = DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA; df.iloc[:2, 2] = NA   # nb book uses ix
df
df.dropna(thresh=3)
df.dropna(thresh=2)
df.dropna(thresh=1)

df.fillna(0)
df.fillna({1: 0.5, 3: -1})
df.fillna({1: 0.5, 2: -1})

df.fillna(0, inplace=True)
df


df = DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA; df.iloc[4:, 2] = NA
df
df.fillna(method='ffill') 
df.fillna(method='ffill', limit=2)

data = Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())



### Hierarchical Indexing -- adding higher dimensionality -- no examples




### read_csv et al
df = pd.read_csv('ex1.csv')
df
pd.read_table('ex1.csv', sep=',')

pd.read_csv('ex2.csv', header=None)
pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('ex2.csv', names=names, index_col='message')

result = pd.read_table('ex3.txt', sep='\s+')
result

pd.read_csv('ex4.csv', skiprows=[])
pd.read_csv('ex4.csv', skiprows=[0, 2, 3])

result = pd.read_csv('ex5.csv')
result

### NB the value NA became NaN -- this is called a sentinel
### NB the empty value is also coded as NaN

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('ex5.csv', na_values=sentinels)


### reading text files in pieces

result = pd.read_csv('ex6.csv')
result

pd.read_csv('ex6.csv', nrows=5)

chunker = pd.read_csv('ex6.csv', chunksize=10)
chunker

tot = Series([])
for chunk in chunker:
    tot = tot.add(chunk['key'].value_counts(), fill_value=0)

tot




### Writing out data -- just like read in no examples
### stop for today




### JSON
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
              {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

import json

result = json.loads(obj) # To convert a JSON string to Python form, use json.loads
result
type(result)

#json.dumps on the other hand converts a Python object back to JSON:
asjson = json.dumps(result)


# JSON --> Python use json.loads
# Python --> JSON use json.dumps

# for more see example in chapter 7 about USDA






### Web APIs
import requests
url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp = requests.get(url)
resp

# status cat - https://http.cat/

data = resp.json()  # new way of handling JSON built in to requests
data[:5]

issue_labels = DataFrame(data)
issue_labels


### Database Operations
## Throw out everything you know about databases

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
    
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
    
df1
df2

pd.merge(df1,df2) # nb we use pd.merge not df1.merge

### nb no key specified it defaulted to similiar key

pd.merge(df1,df2,on='key')


df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
    
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})

pd.merge(df3, df4, left_on='lkey', right_on='rkey')


### NB: By default merge does an 'inner' join

pd.merge(df1, df2, how='outer',on='key')


df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
    
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
    
df1
df2

pd.merge(df1, df2, on='key', how='left')

# many-to-many merge give use cartesian product
# eg: a gets 4 entries because 2 in each df

# multi key merge
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
pd.merge(left, right, on=['key1', 'key2'], how='outer')


pd.merge(left, right, on='key1')
# pandas added _x and _y because the key was repeated
# you can set the suffixes with the argument
pd.merge(left, right, on='key1', suffixes=('_left', '_right'))



### Now let's use Index for merging
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

left1
right1

pd.merge(left1, right1, left_on='key', right_index=True)

# hierarchical indexing is complicated best for the privacy of your own office

# now really forget everything you knew about databases

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])

right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])

left2
right2

left2.join(right2, how='outer')  # yep, now we use join and its a member of the dataframe

# It also supports joining the index of the passed DataFrame on one of the columns of the calling DataFrame:
left1.join(right1, on='key')
# uses 'key' from left1 and index from right1



### concatenate

### combining data with overlap

### pivoting

### removing duplicates

### transforming data using a function or mapping

### 