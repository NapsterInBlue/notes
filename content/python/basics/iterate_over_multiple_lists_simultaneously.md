---
title: "Iterate Over Multiple Lists Simultaneously"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Iterate over multiple lists simultaneously using Python."
type: technical_note
draft: false
---
## Create Two Lists


```python
names = ['James', 'Bob', 'Sarah', 'Marco', 'Nancy', 'Sally']
ages = [42, 13, 14, 25, 63, 23]
```

## Iterate Over Both Lists At Once


```python
for name, age in zip(names, ages):
     print(name, age)
```

    James 42
    Bob 13
    Sarah 14
    Marco 25
    Nancy 63
    Sally 23

