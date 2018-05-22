---
title: "Compare Two Dictionaries"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Compare two dictionaries using Python."
type: technical_note
draft: false
---
## Make Two Dictionaries


```python
importers = {'El Salvador' : 1234,
             'Nicaragua' : 152,
             'Spain' : 252
            }

exporters = {'Spain' : 252,
             'Germany' : 251,
             'Italy' : 1563
             }
```

## Find Duplicate Keys


```python
# Find the intersection of importers and exporters
importers.keys() & exporters.keys()
```




    {'Spain'}



## Find Difference In Keys


```python
# Find the difference between importers and exporters
importers.keys() - exporters.keys()
```




    {'El Salvador', 'Nicaragua'}



## Find Key, Values Pairs In Common


```python
# Find countries where the amount of exports matches the amount of imports
importers.items() & exporters.items()
```




    {('Spain', 252)}


