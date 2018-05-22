---
title: "Getting The Diagonal Of A Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to get the diagonal of a matrix in Python."
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

## Get The Diagonal


```python
# Return diagonal elements
matrix.diagonal()
```




    array([1, 5, 9])



## Calculate The Trace


```python
# Calculate the tracre of the matrix
matrix.diagonal().sum()
```




    15


