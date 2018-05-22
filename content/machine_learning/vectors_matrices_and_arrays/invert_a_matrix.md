---
title: "Invert A Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to invert a matrix in Python."
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
matrix = np.array([[1, 4],
                   [2, 5]])
```

## Invert Matrix


```python
# Calculate inverse of matrix
np.linalg.inv(matrix)
```




    array([[-1.66666667,  1.33333333],
           [ 0.66666667, -0.33333333]])


