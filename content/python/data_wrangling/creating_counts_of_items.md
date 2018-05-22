---
title: "Create Counts Of Items"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Create Counts Of Items in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
from collections import Counter
```

## Create A Counter


```python
# Create a counter of the fruits eaten today
fruit_eaten = Counter(['Apple', 'Apple', 'Apple', 'Banana', 'Pear', 'Pineapple'])

# View counter
fruit_eaten
```




    Counter({'Apple': 3, 'Banana': 1, 'Pear': 1, 'Pineapple': 1})



## Update The Count For An Element


```python
# Update the count for 'Pineapple' (because you just ate an pineapple)
fruit_eaten.update(['Pineapple'])

# View the counter
fruit_eaten
```




    Counter({'Apple': 3, 'Banana': 1, 'Pear': 1, 'Pineapple': 2})



## View The Items With The Highest Counts


```python
# View the items with the top 3 counts
fruit_eaten.most_common(3)
```




    [('Apple', 3), ('Pineapple', 2), ('Banana', 1)]


