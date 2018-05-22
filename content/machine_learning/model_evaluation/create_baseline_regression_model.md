---
title: "Create Baseline Regression Model"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to create a baseline regression model in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.datasets import load_boston
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

## Load Boston Housing Dataset


```python
# Load data
boston = load_boston()

# Create features
X, y = boston.data, boston.target
```

## Split Data Into Training And Test Set


```python
# Make test and training split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

## Create Dummy Regression Always Predicts The Mean Value Of Target


```python
# Create a dummy regressor
dummy_mean = DummyRegressor(strategy='mean')

# "Train" dummy regressor
dummy_mean.fit(X_train, y_train)
```




    DummyRegressor(constant=None, quantile=None, strategy='mean')



## Create Dummy Regression Always Predicts A Constant Value


```python
# Create a dummy regressor
dummy_constant = DummyRegressor(strategy='constant', constant=20)

# "Train" dummy regressor
dummy_constant.fit(X_train, y_train)
```




    DummyRegressor(constant=array(20), quantile=None, strategy='constant')



## Evaluate Performance Metric


```python
# Get R-squared score
dummy_constant.score(X_test, y_test)  
```




    -0.065105020293257265


