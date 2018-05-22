---
title: "Calculate The Average, Variance, And Standard Deviation"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to calculate the average, variance, and standard deviation of an array in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import numpy as np
```

## Create Matrix


```python
# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
```

## Calculate Mean


```python
# Return mean
np.mean(matrix)
```




    5.0



## Calculate Variance


```python
# Return variance
np.var(matrix)
```




    6.666666666666667



## Calculate Standard Deviation


```python
# Return standard deviation
np.std(matrix)
```




    2.5819888974716112


