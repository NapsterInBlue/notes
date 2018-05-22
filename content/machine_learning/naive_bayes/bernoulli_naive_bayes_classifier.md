---
title: "Bernoulli Naive Bayes Classifier"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to train a Bernoulli naive bayes classifer in Scikit-Learn"
type: technical_note
draft: false
---
The Bernoulli naive Bayes classifier assumes that all our features are binary such that they take only two values (e.g. a nominal categorical feature that has been one-hot encoded).

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn.naive_bayes import BernoulliNB
```

## Create Binary Feature And Target Data


```python
# Create three binary features
X = np.random.randint(2, size=(100, 3))

# Create a binary target vector
y = np.random.randint(2, size=(100, 1)).ravel()
```

## View Feature Data


```python
# View first ten observations
X[0:10]
```




    array([[1, 1, 1],
           [0, 1, 0],
           [1, 1, 1],
           [0, 0, 0],
           [1, 0, 1],
           [1, 1, 1],
           [0, 1, 1],
           [1, 1, 1],
           [1, 1, 1],
           [1, 1, 0]])



## Train Bernoulli Naive Bayes Classifier


```python
# Create Bernoulli Naive Bayes object with prior probabilities of each class
clf = BernoulliNB(class_prior=[0.25, 0.5])

# Train model
model = clf.fit(X, y)
```
