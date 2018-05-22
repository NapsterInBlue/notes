---
title: "Selecting The Best Alpha Value In Ridge Regression"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to select the best alpha value when conduct in ridge regression in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.linear_model import RidgeCV
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

Note: Because in linear regression the value of the coefficients is partially determined by the scale of the feature, and in regularized models all coefficients are summed together, we must make sure to standardize the feature prior to training.


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Create Ridge Regression With Candidate Alpha Values


```python
# Create ridge regression with three possible alpha values
regr_cv = RidgeCV(alphas=[0.1, 1.0, 10.0])
```

## Fit Ridge Regression

scikit-learn includes a `RidgeCV` method that allows us select the ideal value for $\alpha$:


```python
# Fit the linear regression
model_cv = regr_cv.fit(X_std, y)
```

## View Best Model's Alpha Value


```python
# View alpha
model_cv.alpha_
```




    1.0


