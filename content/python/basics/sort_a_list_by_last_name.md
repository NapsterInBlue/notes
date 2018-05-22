---
title: "Sort A List Of Names By Last Name"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Sort a list of names by last name."
type: technical_note
draft: false
---
## Create a list of names


```python
commander_names = ["Alan Brooke", "George Marshall", "Frank Jack Fletcher", "Conrad Helfrich", "Albert Kesselring"] 
```

## Sort Alphabetically By Last Name

To complete the sort, we will combine three operations:

- `lambda x: x.split(" ")`, which is a function that takes a string `x` and breaks it up along each blank space. This outputs a list.
- `[-1]`, which takes the last element of a list.
- `sorted()`, which sorts a list.


```python
# Sort a variable called 'commander_names' by the last elements of each name.
sorted(commander_names, key=lambda x: x.split(" ")[-1])
```




    ['Alan Brooke',
     'Frank Jack Fletcher',
     'Conrad Helfrich',
     'Albert Kesselring',
     'George Marshall']


