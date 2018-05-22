---
title: "Iterating Over Dictionary Keys"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Iterating over dictionary keys using Python."
type: technical_note
draft: false
---
## Create A Dictionary


```python
Officers = {'Michael Mulligan': 'Red Army',
            'Steven Johnson': 'Blue Army',
            'Jessica Billars': 'Green Army',
            'Sodoni Dogla': 'Purple Army',
            'Chris Jefferson': 'Orange Army'}
```


```python
Officers
```




    {'Chris Jefferson': 'Orange Army',
     'Jessica Billars': 'Green Army',
     'Michael Mulligan': 'Red Army',
     'Sodoni Dogla': 'Purple Army',
     'Steven Johnson': 'Blue Army'}



## Use Dictionary Comprehension


```python
# Display all dictionary entries where the key doesn't start with 'Chris'
{keys : Officers[keys] for keys in Officers if not keys.startswith('Chris')}
```




    {'Jessica Billars': 'Green Army',
     'Michael Mulligan': 'Red Army',
     'Sodoni Dogla': 'Purple Army',
     'Steven Johnson': 'Blue Army'}



Notice that the entry for 'Chris Jefferson' is not returned.
