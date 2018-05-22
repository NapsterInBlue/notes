---
title: "Swapping Variable Values"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Swapping variable values using Python."
type: technical_note
draft: false
---
### Setup the originally variables and their values


```python
one = 1
two = 2
```

### View the original variables


```python
'one =', one, 'two =', two
```




    ('one =', 1, 'two =', 2)



### Swap the values


```python
one, two = two, one
```

### View the swapped values, notice how the values for each variable have changed


```python
'one =', one, 'two =', two
```




    ('one =', 2, 'two =', 1)


