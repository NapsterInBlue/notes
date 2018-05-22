---
title: "Variance Thresholding Binary Features"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to select the best binary features for machine learning using variance thresholding in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
from sklearn.feature_selection import VarianceThreshold
```

## Load Data


```python
# Create feature matrix with: 
# Feature 0: 80% class 0
# Feature 1: 80% class 1
# Feature 2: 60% class 0, 40% class 1
X = [[0, 1, 0],
     [0, 1, 1],
     [0, 1, 0],
     [0, 1, 1],
     [1, 0, 0]]
```

## Conduct Variance Thresholding

In binary features (i.e. Bernoulli random variables), variance is calculated as:

$$\operatorname {Var} (x)= p(1-p)$$

where $p$ is the proportion of observations of class `1`. Therefore, by setting $p$, we can remove features where the vast majority of observations are one class.


```python
# Run threshold by variance
thresholder = VarianceThreshold(threshold=(.75 * (1 - .75)))
thresholder.fit_transform(X)
```




    array([[0],
           [1],
           [0],
           [1],
           [0]])


