---
title: "Sort A List Of Strings By Length"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Sort a list of strings by length."
type: technical_note
draft: false
---
## Create a list of names


```python
commander_names = ["Alan Brooke", "George Marshall", "Frank Jack Fletcher", "Conrad Helfrich", "Albert Kesselring"] 
```

## Sort Alphabetically By Length

To complete the sort, we will combine two operations:

- `lambda x: len(x)`, which returns the length of each string.
- `sorted()`, which sorts a list.


```python
# Sort a variable called 'commander_names' by the length of each string
sorted(commander_names, key=lambda x: len(x))
```




    ['Alan Brooke',
     'George Marshall',
     'Conrad Helfrich',
     'Albert Kesselring',
     'Frank Jack Fletcher']


