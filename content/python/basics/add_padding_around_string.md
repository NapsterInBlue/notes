---
title: "Add Padding Around String"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Add Padding Around String Using Python."
type: technical_note
draft: false
---
## Create Some Text 


```python
text = 'Chapter 1'
```

## Add Padding Around Text 


```python
# Add Spaces Of Padding To The Left
format(text, '>20')
```




    '           Chapter 1'




```python
# Add Spaces Of Padding To The Right
format(text, '<20')
```




    'Chapter 1           '




```python
# Add Spaces Of Padding On Each Side
format(text, '^20')
```




    '     Chapter 1      '




```python
# Add * Of Padding On Each Side
format(text, '*^20')
```




    '*****Chapter 1******'


