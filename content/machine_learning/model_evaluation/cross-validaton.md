---
title: "Cross-Validation"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to cross-validate models for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
```

## Load Digits Dataset


```python
# Load the digits dataset
digits = datasets.load_digits()

# Create the features matrix
X = digits.data

# Create the target vector
y = digits.target
```

## Create Pipeline


```python
# Create standardizer
standardizer = StandardScaler()

# Create logistic regression
logit = LogisticRegression()

# Create a pipeline that standardizes, then runs logistic regression
pipeline = make_pipeline(standardizer, logit)
```

## Create k-Fold Cross-Validation


```python
# Create k-Fold cross-validation
kf = KFold(n_splits=10, shuffle=True, random_state=1)
```

## Conduct k-Fold Cross-Validation


```python
# Do k-fold cross-validation
cv_results = cross_val_score(pipeline, # Pipeline
                             X, # Feature matrix
                             y, # Target vector
                             cv=kf, # Cross-validation technique
                             scoring="accuracy", # Loss function
                             n_jobs=-1) # Use all CPU scores
```

## Calculate Mean Performance Score


```python
# Calculate mean
cv_results.mean()
```




    0.96493171942892597


