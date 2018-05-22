---
title: "Make Simulated Data For Clustering"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Make a simulated dataset for clustering."
type: technical_note
draft: false
---
## Preliminaries


```python
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
```

## Make Data


```python
# Make the features (X) and output (y) with 200 samples,
X, y = make_blobs(n_samples = 200,
                  # two feature variables,
                  n_features = 2,
                  # three clusters,
                  centers = 3,
                  # with .5 cluster standard deviation,
                  cluster_std = 0.5,
                  # shuffled,
                  shuffle = True)
```

## View Data


```python
# Create a scatterplot of the first and second features
plt.scatter(X[:,0],
            X[:,1])

# Show the scatterplot
plt.show()
```


![png](make_simulated_data_for_clustering_6_0.png)

