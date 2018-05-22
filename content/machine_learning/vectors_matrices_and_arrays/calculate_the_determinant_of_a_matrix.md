---
title: "Calculate The Determinant Of A Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to calculate the determinant of a matrix in Python."
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

## Calculate Determinant


```python
# Return determinant of matrix
np.linalg.det(matrix)
```




    -9.5161973539299405e-16


