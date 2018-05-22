---
title: "Remove Punctuation"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to remove punctuation from unstructured text data for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
import string
import numpy as np
```

## Create Text Data


```python
# Create text
text_data = ['Hi!!!! I. Love. This. Song....', 
             '10000% Agree!!!! #LoveIT', 
             'Right?!?!']
```

## Remove Punctuation


```python
# Create function using string.punctuation to remove all punctuation
def remove_punctuation(sentence: str) -> str:
    return sentence.translate(str.maketrans('', '', string.punctuation))

# Apply function
[remove_punctuation(sentence) for sentence in text_data]
```




    ['Hi I Love This Song', '10000 Agree LoveIT', 'Right']


