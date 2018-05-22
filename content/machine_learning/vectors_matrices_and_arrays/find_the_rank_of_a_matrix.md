---
title: "Find The Rank Of A Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to find the rank of a matrix in Python."
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

## Find Rank Of Matrix


```python
# Return matrix rank
np.linalg.matrix_rank(matrix)
```




    2


