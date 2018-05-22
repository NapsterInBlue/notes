---
title: "Enumerate A List"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Enumerate a list in Python"
type: technical_note
draft: false
---

```python
# Create a list of strings
data = ['One','Two','Three','Four','Five']
```


```python
# For each item in the enumerated variable, data
for item in enumerate(data):
    # Print the whole enumerated element
    print(item)
    # Print only the value (not the index number)
    print(item[1])
```

    (0, 'One')
    One
    (1, 'Two')
    Two
    (2, 'Three')
    Three
    (3, 'Four')
    Four
    (4, 'Five')
    Five

