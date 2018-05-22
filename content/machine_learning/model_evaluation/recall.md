---
title: "Recall"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to evaluate a Python machine learning using recall."
type: technical_note
draft: false
---
<a alt="Recall" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/Recall_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
```

## Generate Features And Target Data


```python
# Generate features matrix and target vector
X, y = make_classification(n_samples = 10000,
                           n_features = 3,
                           n_informative = 3,
                           n_redundant = 0,
                           n_classes = 2,
                           random_state = 1)
```

## Create Logistic Regression


```python
# Create logistic regression
logit = LogisticRegression()
```

## Cross-Validate Model Using Recall


```python
# Cross-validate model using precision
cross_val_score(logit, X, y, scoring="recall")
```




    array([ 0.95080984,  0.94961008,  0.95558223])


