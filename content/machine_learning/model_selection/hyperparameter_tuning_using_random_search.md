---
title: "Hyperparameter Tuning Using Random Search"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to conduct random search for hyperparameter tuning in scikit-learn for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from scipy.stats import uniform
from sklearn import linear_model, datasets
from sklearn.model_selection import RandomizedSearchCV
```

## Load Iris Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create Logistic Regression


```python
# Create logistic regression
logistic = linear_model.LogisticRegression()
```

## Create Hyperparameter Search Space


```python
# Create regularization penalty space
penalty = ['l1', 'l2']

# Create regularization hyperparameter distribution using uniform distribution
C = uniform(loc=0, scale=4)

# Create hyperparameter options
hyperparameters = dict(C=C, penalty=penalty)
```

## Create Random Search


```python
# Create randomized search 5-fold cross validation and 100 iterations
clf = RandomizedSearchCV(logistic, hyperparameters, random_state=1, n_iter=100, cv=5, verbose=0, n_jobs=-1)
```

## Conduct Random Search


```python
# Fit randomized search
best_model = clf.fit(X, y)
```

## View Hyperparameter Values Of Best Model


```python
# View best hyperparameters
print('Best Penalty:', best_model.best_estimator_.get_params()['penalty'])
print('Best C:', best_model.best_estimator_.get_params()['C'])
```

    Best Penalty: l1
    Best C: 1.66808801881


## Predict Using Best Model


```python
# Predict target vector
best_model.predict(X)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])


