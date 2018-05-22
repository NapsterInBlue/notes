---
title: "Convert Strings To Dates"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to convert stings to dates for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
import numpy as np
import pandas as pd
```

## Create Strings


```python
# Create strings
date_strings = np.array(['03-04-2005 11:35 PM',
                         '23-05-2010 12:01 AM',
                         '04-09-2009 09:09 PM'])
```

## Convert Strings To Timestamps

If `errors="coerce"` then any problem will not raise an error (the default behavior) but instead will set the value causing the error to `NaT` (i.e. a missing value).

<table>
  <tr>
    <th>Code</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
      <td><pre>%Y</pre></td>
    <td>Full year</td>
    <td>`2001`</td>
  </tr>
   <tr>
    <td><pre>%m</pre></td>
    <td>Month w/ zero padding</td>
    <td>`04`</td>
  </tr>
   <tr>
    <td><pre>%d</pre></td>
    <td>Day of the month w/ zero padding</td>
    <td>`09`</td>
  </tr>
  <tr>
    <td><pre>%I</pre></td>
    <td>Hour (12hr clock) w/ zero padding</td>
    <td>`02`</td>
  </tr>
  <tr>
    <td><pre>%p</pre></td>
    <td>AM or PM</td>
    <td>`AM`</td>
  </tr>
  <tr>
    <td><pre>%M</pre></td>
    <td>Minute w/ zero padding</td>
    <td>`05`</td>
  </tr>
  <tr>
    <td><pre>%S</pre></td>
    <td>Second w/ zero padding</td>
    <td>`09`</td>
  </tr>
</table>


```python
# Convert to datetimes
[pd.to_datetime(date, format="%d-%m-%Y %I:%M %p", errors="coerce") for date in date_strings]
```




    [Timestamp('2005-04-03 23:35:00'),
     Timestamp('2010-05-23 00:01:00'),
     Timestamp('2009-09-04 21:09:00')]


