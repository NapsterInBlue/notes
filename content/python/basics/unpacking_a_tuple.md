---
title: "Unpacking A Tuple"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Unpacking a tuple using Python."
type: technical_note
draft: false
---
## Create List Of Tuples


```python
# Create a list of tuples where the first and second element of each 
# super is the first last names, respectively
soldiers = [('Steve', 'Miller'), ('Stacy', 'Markov'), ('Sonya', 'Matthews'), ('Sally', 'Mako')]
```

## Unpack Tuples


```python
# For the second element for each tuple in soldiers,
for _, last_name in soldiers:
    # print the second element
    print(last_name)
```

    Miller
    Markov
    Matthews
    Mako

