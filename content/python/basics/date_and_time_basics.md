---
title: "Date And Time Basics"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Date and time basics in Python."
type: technical_note
draft: false
---

```python
# Import modules
from datetime import datetime
from datetime import timedelta
```


```python
# Create a variable with the current time
now = datetime.now()
now
```




    datetime.datetime(2014, 5, 11, 20, 5, 11, 688051)




```python
# The current year
now.year
```




    2014




```python
# The current month
now.month
```




    5




```python
# The current day
now.day
```




    11




```python
# The current hour
now.hour
```




    20




```python
# The current minute
now.minute
```




    5




```python
# The difference between two dates
delta = datetime(2011, 1, 7) - datetime(2011, 1, 6)
delta
```




    datetime.timedelta(1)




```python
# The difference days
delta.days
```




    1




```python
# The difference seconds
delta.seconds
```




    0




```python
# Create a time
start = datetime(2011, 1, 7)
```


```python
# Add twelve days to the time
start + timedelta(12)
```




    datetime.datetime(2011, 1, 19, 0, 0)


