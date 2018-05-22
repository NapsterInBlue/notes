---
title: "Flatten A Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to flatten a matrix in Python."
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

## Flatten Matrix


```python
# Flatten matrix
matrix.flatten()
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])


