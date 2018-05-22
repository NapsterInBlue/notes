---
title: "Random Forest Regression"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Training a random forest regressor in scikit-learn."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
```

## Load Boston Housing Data


```python
# Load data with only two features
boston = datasets.load_boston()
X = boston.data[:,0:2]
y = boston.target
```

## Create Random Forest Regressor


```python
# Create decision tree classifer object
regr = RandomForestRegressor(random_state=0, n_jobs=-1)
```

## Train Random Forest Regressor


```python
# Train model
model = regr.fit(X, y)
```
