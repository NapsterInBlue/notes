---
title: "Strip Whitespace"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to strip whitespace to clean unstructured text data for machine learning in Python."
type: technical_note
draft: false
---
## Create Text


```python
# Create text
text_data = ['   Interrobang. By Aishwarya Henriette     ',
             'Parking And Going. By Karl Gautier',
             '    Today Is The night. By Jarek Prakash   ']
```

## Remove Whitespace


```python
# Strip whitespaces
strip_whitespace = [string.strip() for string in text_data]

# Show text
strip_whitespace
```




    ['Interrobang. By Aishwarya Henriette',
     'Parking And Going. By Karl Gautier',
     'Today Is The night. By Jarek Prakash']


