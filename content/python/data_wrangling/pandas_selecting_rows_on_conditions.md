---
title: "Selecting pandas DataFrame Rows Based On Conditions"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Selecting pandas dataFrame rows based on conditions."
type: technical_note
draft: false
aliases:
    - /python/pandas_selecting_rows_on_conditions.html
---
## Preliminaries


```python
# Import modules
import pandas as pd
import numpy as np
```


```python
# Create a dataframe
raw_data = {'first_name': ['Jason', 'Molly', np.nan, np.nan, np.nan], 
        'nationality': ['USA', 'USA', 'France', 'UK', 'UK'], 
        'age': [42, 52, 36, 24, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'nationality', 'age'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>nationality</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>USA</td>
      <td>42</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>USA</td>
      <td>52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>France</td>
      <td>36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>UK</td>
      <td>24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>UK</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



## Method 1: Using Boolean Variables


```python
# Create variable with TRUE if nationality is USA
american = df['nationality'] == "USA"

# Create variable with TRUE if age is greater than 50
elderly = df['age'] > 50

# Select all cases where nationality is USA and age is greater than 50
df[american & elderly]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>nationality</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>USA</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>



## Method 2: Using variable attributes 


```python
# Select all cases where the first name is not missing and nationality is USA 
df[df['first_name'].notnull() & (df['nationality'] == "USA")]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>nationality</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>USA</td>
      <td>42</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>USA</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>


