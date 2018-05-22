---
title: "Select Random Element From A List"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Select random Element from a list."
type: technical_note
draft: false
---
## Preliminaries


```python
from random import choice
```

## Create List


```python
# Make a list of crew members
crew_members = ['Steve', 'Stacy', 'Miller', 'Chris', 'Bill', 'Jack']
```

## Select Random Item From List


```python
# Choose a random crew member
choice(crew_members)
```




    'Stacy'


