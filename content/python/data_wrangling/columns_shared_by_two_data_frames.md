---
title: "Columns Shared By Two Data Frames"
author: "Chris Albon"
date: 2018-03-12T11:53:49-07:00
description: "Find the columns shared by two data frames in Pandas."
type: technical_note
draft: false
---
## Preliminaries


```python
# Import library
import pandas as pd
```

## Create Data Frames


```python
# Create a data frame
dataframe_one = pd.DataFrame()
dataframe_one['1'] = ['1', '1', '1']
dataframe_one['B'] = ['b', 'b', 'b']

# Create a second data frame
dataframe_two = pd.DataFrame()
dataframe_two['2'] = ['2', '2', '2']
dataframe_two['B'] = ['b', 'b', 'b']
```

## Find Shared Columns


```python
# Convert each data frame's columns into sets, then find
# the intersection of those two sets. This will be the
# set of columns shared by both data frames.
set.intersection(set(dataframe_one), set(dataframe_two))
```




    {'B'}


