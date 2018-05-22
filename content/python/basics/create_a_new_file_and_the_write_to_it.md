---
title: "Create A New File Then Write To It"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Create A New File Then Write To It Using Python."
type: technical_note
draft: false
---
## Create A New File And Write To It


```python
# Create a file if it doesn't already exist
with open('file.txt', 'xt') as f:
    # Write to the file
    f.write('This file now exsits!')
    # Close the connection to the file
    f.close()
```

## Open The File And Read It


```python
# Open the file
with open('file.txt', 'rt') as f:
    # Read the data in the file
    data = f.read()
    # Close the connection to the file
    f.close()
```

## View The Contents Of The File


```python
# View the data in the file
data
```




    'This file now exsits!'



## Delete The File


```python
# Import the os package
import os

# Delete the file
os.remove('file.txt')
```
