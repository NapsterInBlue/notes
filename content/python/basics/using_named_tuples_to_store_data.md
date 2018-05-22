---
title: "Using Named Tuples To Store Data"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Using named tuples to store data using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
from collections import namedtuple
```

## Create A Named Tuple


```python
Vehicle = namedtuple('Vehicle', 'make model wheels manual')
```

## Create An Entry


```python
forrester = Vehicle('Forrester', 'Subaru', 4, True)
```

## View The Data In Entry


```python
forrester.model
```




    'Subaru'




```python
forrester.wheels
```




    4


