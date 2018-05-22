---
title: "Flatten Lists Of Lists"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Flatten lists of lists using Python."
type: technical_note
draft: false
---

```python
# Create a list containing three lists of names
list_of_lists = [['Amy','Betty','Cathryn','Dana'], 
                 ['Elizabeth','Fay','Gora'], 
                  ['Heidi','Jane','Kayley']]
```


```python
# For each element in list_of_lists, take each element in the list
flattened_list = [i for row in list_of_lists for i in row]
```


```python
# View the flattened list
flattened_list
```




    ['Amy',
     'Betty',
     'Cathryn',
     'Dana',
     'Elizabeth',
     'Fay',
     'Gora',
     'Heidi',
     'Jane',
     'Kayley']


