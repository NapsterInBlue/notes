---
title: "Selecting Elements In An Array"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to select elements in a NumPy array."
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
# Create row vector
vector = np.array([1, 2, 3, 4, 5, 6])
```

## Select Element


```python
# Select second element
vector[1]
```




    2



## Create Matrix


```python
# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
```

## Select Element


```python
# Select second row, second column
matrix[1,1]
```




    5



## Create Tensor


```python
# Create matrix
tensor = np.array([
                    [[[1, 1], [1, 1]], [[2, 2], [2, 2]]],
                    [[[3, 3], [3, 3]], [[4, 4], [4, 4]]]
                  ])
```

## Select Element


```python
# Select second element of each of the three dimensions
tensor[1,1,1]
```




    array([4, 4])


