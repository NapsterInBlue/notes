---
title: "Unpacking Function Arguments"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Unpacking function arguments using Python."
type: technical_note
draft: false
---
## Create Argument Objects


```python
# Create a dictionary of arguments
argument_dict = {'a':'Alpha', 'b':'Bravo'}

# Create a list of arguments
argument_list = ['Alpha', 'Bravo']
```

## Create A Simple Function


```python
# Create a function that takes two inputs
def simple_function(a, b):
    # and prints them combined
    return a + b
```

## Run the Function With Unpacked Arguments


```python
# Run the function with the unpacked argument dictionary
simple_function(**argument_dict)
```




    'AlphaBravo'




```python
# Run the function with the unpacked argument list
simple_function(*argument_list)
```




    'AlphaBravo'


