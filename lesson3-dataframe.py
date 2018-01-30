#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:48:03 2018

@author: lpa2a
"""

# import convention
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

### creating a data frame

# dict of equal-length lists or NumPy arrays
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame(data)
print(df)

# specify columns by name to pick order
print(DataFrame(data, columns=['year', 's', 'p']))

# retrieving a column
print(df.year)
# or
print(df['year'])

###
#### The column returned when indexing a DataFrame is a view on the underlying data, not a copy. 
###

# notice that a column of a dataframe is a series
print(type(df.year))

# retrieving a row
print(df.loc[0])  # label based
print(df.ix[0])   # depricated
print(df.iloc[0]) # poistional based

# create a new column - act like it exists - like a python dictionary
print(df)
df['votes']=2
print(df)



# another way to make a data frame
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
df3 = DataFrame(pop)
print(df3)