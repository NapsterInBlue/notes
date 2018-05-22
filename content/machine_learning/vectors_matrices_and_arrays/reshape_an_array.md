---
title: "Reshape An Array"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to reshape a NumPy array."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import numpy as np
```

## Create Array


```python
# Create a 4x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
```

## Reshape Array


```python
# Reshape matrix into 2x6 matrix
matrix.reshape(2, 6)
```




    array([[ 1,  2,  3,  4,  5,  6],
           [ 7,  8,  9, 10, 11, 12]])


