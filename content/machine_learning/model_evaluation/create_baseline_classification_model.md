---
title: "Create Baseline Classification Model"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to create a baseline classification model in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
```

## Load Iris Flower Dataset


```python
# Load data
iris = load_iris()

# Create target vector and feature matrix
X, y = iris.data, iris.target
```

## Split Data Into Training And Test Set


```python
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

## Create Dummy Regression Always Predicts The Mean Value Of Target


```python
# Create dummy classifer
dummy = DummyClassifier(strategy='uniform', random_state=1)

# "Train" model
dummy.fit(X_train, y_train)
```




    DummyClassifier(constant=None, random_state=1, strategy='uniform')



## Evaluate Performance Metric


```python
# Get accuracy score
dummy.score(X_test, y_test)  
```




    0.42105263157894735


