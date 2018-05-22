---
title: "Handle Imbalanced Classes In Random Forest"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Handle imbalanced classes in random forests in scikit-learn."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import datasets
```

## Load Iris Flower Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Adjust Iris Dataset To Make Classes Imbalanced


```python
# Make class highly imbalanced by removing first 40 observations
X = X[40:,:]
y = y[40:]

# Create target vector indicating if class 0, otherwise 1
y = np.where((y == 0), 0, 1)
```

## Train Random Forest While Balancing Classes

When using `RandomForestClassifier` a useful setting is `class_weight=balanced` wherein classes are automatically weighted inversely proportional to how frequently they appear in the data. Specifically:

$$w\_j = \frac{n}{kn\_{j}}$$

where $w\_j$ is the weight to class $j$, $n$ is the number of observations, $n\_j$ is the number of observations in class $j$, and $k$ is the total number of classes.


```python
# Create decision tree classifer object
clf = RandomForestClassifier(random_state=0, n_jobs=-1, class_weight="balanced")

# Train model
model = clf.fit(X, y)
```
