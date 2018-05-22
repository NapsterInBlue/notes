---
title: "Testable Documentation"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Testable documentation using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
import doctest
```

## Create A Function To Test

Note that our test cases are inside the function's documentation. Each test case is marked by a `>>>` and the expect output is the line below.


```python
def summation(a, b):
    """
    Takes two inputs and outputs their sum.
    
    Tests:
    
    >>> summation(5, 4)
    9
    
    >>> summation(4, 3)
    7
    
    >>> summation('foo','bar')
    'foobar'
    
    >>> summation(3,'d')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b
```

Notice that in the last test, we are making sure the function outputs the correct error.

## Test Function


```python
doctest.testmod(verbose=True)
```

    Trying:
        summation(5, 4)
    Expecting:
        9
    ok
    Trying:
        summation(4, 3)
    Expecting:
        7
    ok
    Trying:
        summation('foo','bar')
    Expecting:
        'foobar'
    ok
    Trying:
        summation(3,'d')
    Expecting:
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
       4 tests in __main__.summation
    4 tests in 2 items.
    4 passed and 0 failed.
    Test passed.





    TestResults(failed=0, attempted=4)


