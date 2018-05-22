---
title: "Handling Imbalanced Classes With Downsampling"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to handle imbalanced classes with downsampling during machine learning in Python."
type: technical_note
draft: false
---
<a alt="Downsampling" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/Downsampling_print.png" class="flashcard center-block">
</a>

In downsampling, we randomly sample without replacement from the majority class (i.e. the class with more observations) to create a new subset of observation equal in size to the minority class.

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn.datasets import load_iris
```

## Load Iris Dataset


```python
# Load iris data
iris = load_iris()

# Create feature matrix
X = iris.data

# Create target vector
y = iris.target
```

## Make Iris Dataset Imbalanced


```python
# Remove first 40 observations
X = X[40:,:]
y = y[40:]

# Create binary target vector indicating if class 0
y = np.where((y == 0), 0, 1)

# Look at the imbalanced target vector
y
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])



## Downsample Majority Class To Match Minority Class


```python
# Indicies of each class' observations
i_class0 = np.where(y == 0)[0]
i_class1 = np.where(y == 1)[0]

# Number of observations in each class
n_class0 = len(i_class0)
n_class1 = len(i_class1)

# For every observation of class 0, randomly sample from class 1 without replacement
i_class1_downsampled = np.random.choice(i_class1, size=n_class0, replace=False)

# Join together class 0's target vector with the downsampled class 1's target vector
np.hstack((y[i_class0], y[i_class1_downsampled]))
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


