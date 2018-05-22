---
title: "Partial Function Applications"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Partial function applications in Python."
type: technical_note
draft: false
---
Partial function application allows us to create "functions" from other functions with pre-filled arguments. This can be very useful when we want to pipe the output of one function into a function requiring two functions.

## Preliminaries


```python
from functools import partial
```

## Create A Function


```python
def multiply(x, y):
    return x * y
```

## Create A Function With Y Pre-Filled


```python
double = partial(multiply, y=2)
```

## Run The Partial Function


```python
double(3)
```




    6


