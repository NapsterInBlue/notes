---
title: "Function Annotation Examples"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Function annotation examples in Python.."
type: technical_note
draft: false
---
## Create A Function With Annotations


```python
''' 
Create a function. 

The argument 'text' is the string to print with the default value 'default string'
and the argument 

The argument 'n' is an integer of times to print with the default value of 1. 

The function should return a string.
'''
def print_text(text:'string to print'='default string', n:'integer, times to print'=1) -> str:
    return text * n
```

## Run The Function


```python
# Run the function with arguments
print_text('string', 4)
```




    'stringstringstringstring'




```python
# Run the function with default arguments
print_text()
```




    'default string'


