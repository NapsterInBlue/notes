---
title: "If Else On Any Or All Elements"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "If else on any or all elements in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# import pandas as pd
import pandas as pd
```

## Create a simulated dataset


```python
# Create an example dataframe
data = {'score': [1,2,3,4,5]}
df = pd.DataFrame(data)
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



## Does any cell equal 3?


```python
# If any element in df.score equals three,
if (df.score == 3).any():
    # Print this
    print('Does any cells equal 3? Yes!')
# Otherwise,
else:
    # Print this
    print('Does any cells equal 3? No!')
```

    Does any cells equal 3? Yes!


## Do all cells equal 3?


```python
# If all elements in df.score equal three,
if (df.score == 3).all():
    # Print this
    print('Do all cells equal 3? Yes!')
# Otherwise
else:
    # Print this
    print('Do all cells equal 3? No!')
```

    Do all cells equal 3? No!

