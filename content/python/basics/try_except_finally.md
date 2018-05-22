---
title: "Try, Except, and Finally"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Try, except, and finally using Python."
type: technical_note
draft: false
---
## Create data


```python
# Create some data
scores = [23,453,54,235,74,234]
```

## Try something that doesn't work


```python
# Try to:
try:
    # Add a list of integers and a string
    scores + 'A string of characters.'
# If you get an error, set the error as 'e',
except Exception as e:
    # print the error, e
    print('Error:', e)
# Then,
finally:
    # print end program
    print('End Program')
```

    Error: can only concatenate list (not "str") to list
    End Program


## Try something that works


```python
# Try to:
try:
    # Print scores
    print('Worked!', scores)
# If you get an error, set the error as 'e',
except Exception as e:
    # print the error, e
    print('Error:', e)
# Then,
finally:
    # print end program
    print('End program')
```

    Worked! [23, 453, 54, 235, 74, 234]
    End program

