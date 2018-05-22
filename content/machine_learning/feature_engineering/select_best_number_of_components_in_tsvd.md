---
title: "Selecting The Best Number Of Components For TSVD"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to select the best number of component in truncated singular value composition for dimensionality reduction using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
from sklearn import datasets
import numpy as np
```

## Load Digits Data And Make Sparse


```python
# Load the data
digits = datasets.load_digits()

# Standardize the feature matrix
X = StandardScaler().fit_transform(digits.data)

# Make sparse matrix
X_sparse = csr_matrix(X)
```

## Run Truncated Singular Value Decomposition


```python
# Create and run an TSVD with one less than number of features
tsvd = TruncatedSVD(n_components=X_sparse.shape[1]-1)
X_tsvd = tsvd.fit(X)
```

## Create List Of Explained Variances


```python
# List of explained variances
tsvd_var_ratios = tsvd.explained_variance_ratio_
```

## Create Function Calculating Number Of Components Required To Pass Threshold


```python
# Create a function
def select_n_components(var_ratio, goal_var: float) -> int:
    # Set initial variance explained so far
    total_variance = 0.0
    
    # Set initial number of features
    n_components = 0
    
    # For the explained variance of each feature:
    for explained_variance in var_ratio:
        
        # Add the explained variance to the total
        total_variance += explained_variance
        
        # Add one to the number of components
        n_components += 1
        
        # If we reach our goal level of explained variance
        if total_variance >= goal_var:
            # End the loop
            break
            
    # Return the number of components
    return n_components
```

## Run Function


```python
# Run function
select_n_components(tsvd_var_ratios, 0.95)
```




    40


