---
title: "Test Code Speed"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Test code speed using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
import cProfile
```

## Create A Slow Function


```python
def slow_function():
    total = 0.0
    
    for i, _ in enumerate(range(10000)):
        
        for j, _ in enumerate(range(1, 10000)):
            total += (i * j)

    return total
```

## Test The Speed Of The Function


```python
cProfile.run('slow_function()', sort='time')
```

             4 function calls in 13.291 seconds
    
       Ordered by: internal time
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1   13.291   13.291   13.291   13.291 <ipython-input-2-64fc1cd43878>:1(slow_function)
            1    0.000    0.000   13.291   13.291 {built-in method builtins.exec}
            1    0.000    0.000   13.291   13.291 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    


## How To Read cProfile's Output

- **ncalls:** Number of calls to the function.
- **tottime:** Total time.
- **percall:** Time per call.
- **cumtime:** Total time in function and sub-functions.
- **percall:** Time to call.
- **:lineno(function):** Name of the operation.

## Alternative In Jupyter Notebook:


```python
%%timeit

slow_function()
```

    1 loop, best of 3: 12.9 s per loop

