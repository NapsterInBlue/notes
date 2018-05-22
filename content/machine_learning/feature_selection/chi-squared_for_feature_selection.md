---
title: "Chi-Squared For Feature Selection"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to remove irrelevant features using chi-squared for machine learning in Python."
type: technical_note
draft: false
---
<a alt="chi-squared_for_feature_selection" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/Chi-Squared_For_Feature_Selection_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
```

## Load Data


```python
# Load iris data
iris = load_iris()

# Create features and target
X = iris.data
y = iris.target

# Convert to categorical data by converting data to integers
X = X.astype(int)
```

## Compare Chi-Squared Statistics


```python
# Select two features with highest chi-squared statistics
chi2_selector = SelectKBest(chi2, k=2)
X_kbest = chi2_selector.fit_transform(X, y)
```

## View Results


```python
# Show results
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_kbest.shape[1])
```

    Original number of features: 4
    Reduced number of features: 2

