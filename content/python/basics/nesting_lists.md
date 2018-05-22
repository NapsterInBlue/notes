---
title: "Nesting Lists"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Nesting lists."
type: technical_note
draft: false
---

```python
# Create a list of three nested lists, each with three items
state_regions = [['California', 'Oregon', 'Washington'],
        ['Texas','Georgia','Alabama'],
        ['Maine','Vermont','New York']]
```


```python
# View the list
state_regions
```




    [['California', 'Oregon', 'Washington'],
     ['Texas', 'Georgia', 'Alabama'],
     ['Maine', 'Vermont', 'New York']]




```python
# Print the second list's third item
state_regions[1][2]
```




    'Alabama'


