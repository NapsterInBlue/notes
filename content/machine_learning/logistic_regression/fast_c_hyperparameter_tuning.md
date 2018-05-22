---
title: "Fast C Hyperparameter Tuning"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to fast C hyperparameter tuning for logistic regression in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
Sometimes the characteristics of a learning algorithm allows us to search for the best hyperparameters significantly faster than either brute force or randomized model search methods.

scikit-learn's `LogisticRegressionCV` method includes a parameter `Cs`. If supplied a list, `Cs` is the candidate hyperparameter values to select from. If supplied a integer, `Cs` a list of that many candidate values will is drawn from a logarithmic scale between 0.0001 and and 10000 (a range of reasonable values for C).

## Preliminaries


```python
# Load libraries
from sklearn import linear_model, datasets
```

## Load Iris Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Use Cross-Validation To Find The Best Value Of C


```python
# Create cross-validated logistic regression
clf = linear_model.LogisticRegressionCV(Cs=100)

# Train model
clf.fit(X, y)
```




    LogisticRegressionCV(Cs=100, class_weight=None, cv=None, dual=False,
               fit_intercept=True, intercept_scaling=1.0, max_iter=100,
               multi_class='ovr', n_jobs=1, penalty='l2', random_state=None,
               refit=True, scoring=None, solver='lbfgs', tol=0.0001, verbose=0)


