---
title: "Create Interaction Features"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to create interaction features for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
```

## Create Feature Matrix


```python
# Create feature matrix
X = np.array([[2, 3], 
              [2, 3], 
              [2, 3]])
```

## Add Interaction Features


```python
# Create PolynomialFeatures object with interaction_only set to True
interaction = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

# Transform feature matrix
interaction.fit_transform(X)
```




    array([[ 2.,  3.,  6.],
           [ 2.,  3.,  6.],
           [ 2.,  3.,  6.]])


