---
title: "Nested For Loops Using List Comprehension"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Nested for loops using list comprehension."
type: technical_note
draft: false
---

```python
# Create two lists
squads = ["1st Squad", '2nd Squad', '3rd Squad']
regiments = ["51st Regiment", '15th Regiment', '12th Regiment']
```


```python
# Create a tuple for each regiment in regiments, for each squad in sqauds
[(regiment, squad) for regiment in regiments for squad in squads ]
```




    [('51st Regiment', '1st Squad'),
     ('51st Regiment', '2nd Squad'),
     ('51st Regiment', '3rd Squad'),
     ('15th Regiment', '1st Squad'),
     ('15th Regiment', '2nd Squad'),
     ('15th Regiment', '3rd Squad'),
     ('12th Regiment', '1st Squad'),
     ('12th Regiment', '2nd Squad'),
     ('12th Regiment', '3rd Squad')]


