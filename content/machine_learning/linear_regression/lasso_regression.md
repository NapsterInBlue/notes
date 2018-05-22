---
title: "Lasso Regression"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to conduct lasso regression in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
```

## Load Boston Housing Dataset


```python
# Load data
boston = load_boston()
X = boston.data
y = boston.target
```

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Fit Ridge Regression

The hyperparameter, $\alpha$, lets us control how much we penalize the coefficients, with higher values of $\alpha$ creating simpler modelers. The ideal value of $\alpha$ should be tuned like any other hyperparameter. In scikit-learn, $\alpha$ is set using the `alpha` parameter.


```python
# Create lasso regression with alpha value
regr = Lasso(alpha=0.5)

# Fit the linear regression
model = regr.fit(X_std, y)
```
