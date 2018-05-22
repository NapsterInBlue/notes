---
title: "Create A Temporary File"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "reate A Temporary File Using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
from tempfile import NamedTemporaryFile
```

## Create A Temporary File


```python
f = NamedTemporaryFile('w+t')
```

## Write To The Temp File


```python
# Write to the file, the output is the number of characters
f.write('Nobody lived on Deadweather but us and the pirates. It wasn’t hard to understand why.')
```




    85



## View The Tmp File's Name


```python
f.name
```




    '/var/folders/0b/pj3wsd750fjf8xzfb0n127w80000gn/T/tmphv1dkovx'



## Read The File


```python
# Go to the top of the file
f.seek(0)

# Read the file
f.read()
```




    'Nobody lived on Deadweather but us and the pirates. It wasn’t hard to understand why.'



## Close (And Thus Delete) The File


```python
f.close()
```
