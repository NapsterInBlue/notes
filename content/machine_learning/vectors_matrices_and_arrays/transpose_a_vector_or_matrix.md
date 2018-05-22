---
title: "Transpose A Vector Or Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to transpose a vector or matrix in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import numpy as np
```

## Create Vector


```python
# Create vector
vector = np.array([1, 2, 3, 4, 5, 6])
```

## Create Matrix


```python
# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
```

## Transpose Vector


```python
# Tranpose vector
vector.T
```




    array([1, 2, 3, 4, 5, 6])



## Transpose Matrix


```python
# Transpose matrix
matrix.T
```




    array([[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]])


