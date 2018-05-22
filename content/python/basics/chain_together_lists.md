---
title: "Chain Together Lists"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Chain together lists using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
from itertools import chain
```

## Create Two Lists


```python
# Create a list of allies
allies = ['Spain', 'Germany', 'Namibia', 'Austria']

# Create a list of enemies
enemies = ['Mexico', 'United Kingdom', 'France']
```

## Iterate Over Both Lists As A Single Sequence


```python
# For each country in allies and enemies
for country in chain(allies, enemies):
    # print the country
    print(country)
```

    Spain
    Germany
    Namibia
    Austria
    Mexico
    United Kingdom
    France

