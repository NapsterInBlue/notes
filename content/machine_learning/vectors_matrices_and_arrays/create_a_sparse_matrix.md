---
title: "Create A Sparse Matrix"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to create a sparse matrix in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
import numpy as np
from scipy import sparse
```

## Create Dense Matrix


```python
# Create a matrix
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
```

## Convert To Sparse Matrix


```python
# Create compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)
```

Note: There are many types of sparse matrices. In the example above we use CSR but the type we use should reflect our use case.
