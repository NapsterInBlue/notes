---
title: "Discretize Features"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to discretize features for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import Binarizer
import numpy as np
```

## Create Data


```python
# Create feature
age = np.array([[6], 
                [12], 
                [20], 
                [36], 
                [65]])
```

## Option 1: Binarize Feature


```python
# Create binarizer
binarizer = Binarizer(18)

# Transform feature
binarizer.fit_transform(age)
```




    array([[0],
           [0],
           [1],
           [1],
           [1]])



## Option 2: Break Up Feature Into Bins


```python
# Bin feature
np.digitize(age, bins=[20,30,64])
```




    array([[0],
           [0],
           [1],
           [2],
           [3]])


