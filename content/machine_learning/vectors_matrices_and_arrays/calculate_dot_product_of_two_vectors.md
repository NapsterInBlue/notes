---
title: "Calculate Dot Product Of Two Vectors"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to calculate the dot product of two vectors in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import numpy as np
```

## Create Two Vectors


```python
# Create two vectors
vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])
```

## Calculate Dot Product (Method 1)


```python
# Calculate dot product
np.dot(vector_a, vector_b)
```




    32



## Calculate Dot Product (Method 2)


```python
# Calculate dot product
vector_a @ vector_b
```




    32


