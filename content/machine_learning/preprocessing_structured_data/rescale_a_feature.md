---
title: "Rescale A Feature"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to rescale a feature for machine learning in Python."
type: technical_note
draft: false
---
<a alt="MinMax Scaling" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/MinMax_Scaling_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn import preprocessing
import numpy as np
```

## Create Feature


```python
# Create feature
x = np.array([[-500.5], 
              [-100.1], 
              [0], 
              [100.1], 
              [900.9]])
```

## Rescale Feature Using Min-Max


```python
# Create scaler
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

# Scale feature
x_scale = minmax_scale.fit_transform(x)

# Show feature
x_scale
```




    array([[ 0.        ],
           [ 0.28571429],
           [ 0.35714286],
           [ 0.42857143],
           [ 1.        ]])


