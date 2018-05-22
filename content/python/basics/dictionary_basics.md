---
title: "Dictionary Basics"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Dictionary basics in Python."
type: technical_note
draft: false
---
### Basics

- Not sequences, but mappings. That is, stored by key, not relative position.
- Dictionaries are mutable.

### Build a dictionary via brackets


```python
unef_org = {'name' : 'UNEF',
            'staff' : 32,
            'url' : 'http://unef.org'}
```

### View the variable


```python
unef_org
```




    {'name': 'UNEF', 'staff': 32, 'url': 'http://unef.org'}



# Build a dict via keys


```python
who_org = {}
who_org['name'] = 'WHO'
who_org['staff'] = '10'
who_org['url'] = 'http://who.org'
```

### View the variable


```python
who_org
```




    {'name': 'WHO', 'staff': '10', 'url': 'http://who.org'}



## Nesting in dictionaries

### Build a dictionary via brackets


```python
unitas_org = {'name' : 'UNITAS',
              'staff' : 32,
              'url' : ['http://unitas.org', 'http://unitas.int']}
```

### View the variable


```python
unitas_org
```




    {'name': 'UNITAS',
     'staff': 32,
     'url': ['http://unitas.org', 'http://unitas.int']}



## Index the nested list

### Index the second item of the list nested in the url key.


```python
unitas_org['url'][1]
```




    'http://unitas.int'


