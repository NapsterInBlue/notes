---
title: "Concurrent Processing"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Concurrent processing in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
from concurrent import futures
```

## Create Data


```python
data = range(100)
```

## Create Function


```python
# Create some function that takes a value
def some_function(value):
    # And outputs it raised to its own power
    return value**value
```

## Run The Function On The Data Concurrently


```python
# With a pool of workers
with futures.ProcessPoolExecutor() as executor:
    # Map the function to the data
    result = executor.map(some_function, data)
```

## View Results


```python
# List the first 5 outputs
list(result)[0:5]
```




    [1, 1, 4, 27, 256]


