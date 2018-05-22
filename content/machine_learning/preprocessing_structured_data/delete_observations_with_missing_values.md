---
title: "Delete Observations With Missing Values"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to delete observations with missing values."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
import numpy as np
import pandas as pd
```

## Create Feature Matrix


```python
# Create feature matrix
X = np.array([[1.1, 11.1], 
              [2.2, 22.2], 
              [3.3, 33.3], 
              [4.4, 44.4], 
              [np.nan, 55]])
```

## Delete Observations With Missing Values


```python
# Remove observations with missing values
X[~np.isnan(X).any(axis=1)]
```




    array([[  1.1,  11.1],
           [  2.2,  22.2],
           [  3.3,  33.3],
           [  4.4,  44.4]])


