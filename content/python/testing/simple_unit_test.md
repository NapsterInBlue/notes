---
title: "Simple Unit Test"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "A simple unit test in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
import unittest
import sys
```

## Create Function To Be Tested


```python
def multiply(x, y):
    return x * y
```

## Create Test

Note: It is standard practice to name a unit test `test_` + `<function being tested>`. This naming standard allows for automated test using some libraries.


```python
# Create a test case
class TestMultiply(unittest.TestCase):
    # Create the unit test
    def test_multiply_two_integers_together(self):
        # Test if 4 equals the output of multiply(2,2)
        self.assertEqual(4, multiply(2,2))
```

## Run Test


```python
# Run the unit test (and don't shut down the Jupyter Notebook)
unittest.main(argv=['ignored', '-v'], exit=False)
```

    test_multiply_two_integers_together (__main__.TestMultiply) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    OK





    <unittest.main.TestProgram at 0x104919128>


