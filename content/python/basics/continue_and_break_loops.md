---
title: "Continue And Break Loops"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Continue and break loops in Python."
type: technical_note
draft: false
---
### Import the random module


```python
import random
```

### Create a while loop


```python
# set running to true
running = True
```


```python
# while running is true
while running:
    # Create a random integer between 0 and 5
    s = random.randint(0,5)
    # If the integer is less than 3
    if s < 3:
        # Print this
        print('It is too small, starting over.')
        # Reset the next interation of the loop
        # (i.e skip everything below and restart from the top)
        continue
    # If the integer is 4
    if s == 4:
        running = False
        # Print this
        print('It is 4! Changing running to false')
    # If the integer is 5,
    if s == 5:
        # Print this
        print('It is 5! Breaking Loop!')
        # then stop the loop
        break
```

    It is too small, starting over.
    It is too small, starting over.
    It is too small, starting over.
    It is 5! Breaking Loop!

