---
title: "Creating Lists From Dictionary Keys And Values"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Creating Lists From Dictionary Keys And Values Using Python."
type: technical_note
draft: false
---
### Create a dictionary


```python
dict = {'county': ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'fireReports': [4, 24, 31, 2, 3]}
```

### Create a list from the dictionary keys


```python
# Create a list of keys
list(dict.keys())
```




    ['fireReports', 'year', 'county']



### Create a list from the  dictionary values


```python
# Create a list of values
list(dict.values())
```




    [[4, 24, 31, 2, 3],
     [2012, 2012, 2013, 2014, 2014],
     ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma']]


