---
title: "How To Use Default Dicts"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to use default dicts in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
import collections
```

## Create A DefaultDict

Default Dicts work just like regular dictionaries, except a key is called that doesn't have a value, a default value (note: value, not key) is supplied.


```python
# Create a defaultdict with the default value of 0 (int's default value is 0)
arrests = collections.defaultdict(int) 
```

## Add A New Key With A Value


```python
# Add an entry of a person with 10 arrests
arrests['Sarah Miller'] = 10
```


```python
# View dictionary
arrests
```




    defaultdict(int, {'Sarah Miller': 10})



## Add A New Key Without A Value


```python
# Add an entry of a person with no value for arrests,
# thus the default value is used
arrests['Bill James']
```




    0




```python
# View dictionary
arrests
```




    defaultdict(int, {'Bill James': 0, 'Sarah Miller': 10})


