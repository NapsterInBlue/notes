---
title: "Construct A Dictionary From Multiple Lists"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Construct a dictionary from multiple lists in Python."
type: technical_note
draft: false
aliases:
    - /python/construct_a_dictionary_from_multiple_lists_python.html
---
## Create Two Lists


```python
# Create a list of theofficer's name
officer_names = ['Sodoni Dogla', 'Chris Jefferson', 'Jessica Billars', 'Michael Mulligan', 'Steven Johnson']

# Create a list of the officer's army
officer_armies = ['Purple Army', 'Orange Army', 'Green Army', 'Red Army', 'Blue Army']
```

## Construct A Dictionary From The Two Lists


```python
# Create a dictionary that is the zip of the two lists
dict(zip(officer_names, officer_armies))
```




    {'Chris Jefferson': 'Orange Army',
     'Jessica Billars': 'Green Army',
     'Michael Mulligan': 'Red Army',
     'Sodoni Dogla': 'Purple Army',
     'Steven Johnson': 'Blue Army'}


