---
title: "Adding And Subtracting Matrices"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to add and subtract matrices in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import numpy as np
```

## Create Matrices


```python
# Create matrix
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

# Create matrix
matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])
```

## Add Matrices


```python
# Add two matrices
np.add(matrix_a, matrix_b)
```




    array([[ 2,  4,  2],
           [ 2,  4,  2],
           [ 2,  4, 10]])



## Subtract Matrices


```python
# Subtract two matrices
np.subtract(matrix_a, matrix_b)
```




    array([[ 0, -2,  0],
           [ 0, -2,  0],
           [ 0, -2, -6]])


