---
title: "Imputing Missing Class Labels Using k-Nearest Neighbors"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to impute missing class labels using k-nearest neighbors for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
```

## Create Feature Matrix


```python
# Create feature matrix with categorical feature
X = np.array([[0, 2.10, 1.45], 
              [1, 1.18, 1.33], 
              [0, 1.22, 1.27],
              [1, -0.21, -1.19]])


```

## Create Feature Matrix With Missing Values


```python
# Create feature matrix with missing values in the categorical feature
X_with_nan = np.array([[np.nan, 0.87, 1.31], 
                       [np.nan, -0.67, -0.22]])
```

## Train k-Nearest Neighbor Classifier


```python
# Train KNN learner
clf = KNeighborsClassifier(3, weights='distance')
trained_model = clf.fit(X[:,1:], X[:,0])
```

## Predict Missing Values' Class


```python
# Predict missing values' class
imputed_values = trained_model.predict(X_with_nan[:,1:])

# Join column of predicted class with their other features
X_with_imputed = np.hstack((imputed_values.reshape(-1,1), X_with_nan[:,1:]))

# Join two feature matrices
np.vstack((X_with_imputed, X))
```




    array([[ 0.  ,  0.87,  1.31],
           [ 1.  , -0.67, -0.22],
           [ 0.  ,  2.1 ,  1.45],
           [ 1.  ,  1.18,  1.33],
           [ 0.  ,  1.22,  1.27],
           [ 1.  , -0.21, -1.19]])


