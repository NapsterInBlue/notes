---
title: "Calculate Difference Between Dates And Times"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to calculate differences between dates and times for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import pandas as pd
```

## Create Date And Time Data


```python
# Create data frame
df = pd.DataFrame()

# Create two datetime features
df['Arrived'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-04-2017')]
df['Left'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-06-2017')]
```

## Calculate Difference (Method 1)


```python
# Calculate duration between features
df['Left'] - df['Arrived']
```




    0   0 days
    1   2 days
    dtype: timedelta64[ns]



## Calculate Difference (Method 2)


```python
# Calculate duration between features
pd.Series(delta.days for delta in (df['Left'] - df['Arrived']))
```




    0    0
    1    2
    dtype: int64


