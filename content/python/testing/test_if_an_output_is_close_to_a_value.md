---
title: "Test If Output Is Close To A Value"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Test if output is close to a value using Python."
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
def add(x, y):
    return x + y
```

## Create Test


```python
# Create a test case
class TestAdd(unittest.TestCase):
    # Create the unit test
    def test_add_two_floats_roughly_equals_11(self):
        # Test if add(4.48293848, 6.5023845) return roughly (to 1 place) 11 (actual product: 10.98532298)
        self.assertAlmostEqual(11, add(4.48293848, 6.5023845), places=1)
```

## Run Test


```python
# Run the unit test (and don't shut down the Jupyter Notebook)
unittest.main(argv=['ignored', '-v'], exit=False)
```

    test_add_two_floats_roughly_equals_11 (__main__.TestAdd) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    OK





    <unittest.main.TestProgram at 0x1049191d0>


