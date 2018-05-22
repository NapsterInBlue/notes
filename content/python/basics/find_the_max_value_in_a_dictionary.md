---
title: "Find The Max Value In A Dictionary"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Find the max value in a dictionary using Python."
type: technical_note
draft: false
---
## Create A Dictionary


```python
ages = {'John': 21,
        'Mike': 52,
        'Sarah': 12,
        'Bob': 43
       }
```

## Find The Maximum Value Of The Values


```python
max(zip(ages.values(), ages.keys()))
```




    (52, 'Mike')


