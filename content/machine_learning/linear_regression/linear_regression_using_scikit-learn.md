---
title: "Linear Regression Using Scikit-Learn"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to conduct linear regression in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import warnings

# Suppress Warning
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
```

## Load Boston Housing Dataset


```python
# Load data
boston = load_boston()
X = boston.data
y = boston.target
```

## Fit A Linear Regression


```python
# Create linear regression
regr = LinearRegression()

# Fit the linear regression
model = regr.fit(X, y)
```

## View Intercept Term


```python
# View the intercept
model.intercept_
```




    36.491103280361038



## View Coefficients


```python
# View the feature coefficients
model.coef_
```




    array([ -1.07170557e-01,   4.63952195e-02,   2.08602395e-02,
             2.68856140e+00,  -1.77957587e+01,   3.80475246e+00,
             7.51061703e-04,  -1.47575880e+00,   3.05655038e-01,
            -1.23293463e-02,  -9.53463555e-01,   9.39251272e-03,
            -5.25466633e-01])


