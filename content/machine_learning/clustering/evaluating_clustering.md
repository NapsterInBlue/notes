---
title: "Evaluating Clustering"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to evaluate clustering models for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
```

## Create Feature Data


```python
# Generate feature matrix
X, _ = make_blobs(n_samples = 1000,
                  n_features = 10,
                  centers = 2,
                  cluster_std = 0.5,
                  shuffle = True,
                  random_state = 1)
```

## Cluster Observations


```python
# Cluster data using k-means to predict classes
model = KMeans(n_clusters=2, random_state=1).fit(X)

# Get predicted classes
y_hat = model.labels_
```

## Calculate Silhouette Coefficient

Formally, the $i$th observation's silhouette coefficient is:

$$s\_{i} = \frac{b\_{i} - a\_{i}}{\text{max}(a\_{i}, b\_{i})}$$

where $s\_{i}$ is the silhouette coefficient for observation $i$, a\_{i} is the mean distance between $i$ and all observations of the same class and b\_{i} is the mean distance between $i$ and all observations from the closest cluster of a different class. The value returned by `silhouette_score` is the mean silhouette coefficient for all observations. Silhouette coefficients range between -1 and 1, with 1 indicating dense, well separated clusters.


```python
# Evaluate model
silhouette_score(X, y_hat)
```




    0.89162655640721422


