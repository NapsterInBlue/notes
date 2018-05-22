---
title: "Dimensionality Reduction With PCA"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to reduce the dimensions of the feature matrix for machine learning in Python."
type: technical_note
draft: false
---
<a alt="Dimensionality Reduction With PCA" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/Principal_Component_Analysis_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
```

## Load Data


```python
# Load the data
digits = datasets.load_digits()
```

## Standardize Feature Values


```python
# Standardize the feature matrix
X = StandardScaler().fit_transform(digits.data)
```

## Conduct Principal Component Analysis


```python
# Create a PCA that will retain 99% of the variance
pca = PCA(n_components=0.99, whiten=True)

# Conduct PCA
X_pca = pca.fit_transform(X)
```

## View Results


```python
# Show results
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_pca.shape[1])
```

    Original number of features: 64
    Reduced number of features: 54

