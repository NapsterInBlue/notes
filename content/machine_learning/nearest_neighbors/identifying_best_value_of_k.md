---
title: "Identifying Best Value Of k"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Identifying best value of k in k-nearest neighbors classifier in scikit-learn."
type: technical_note
draft: false
---
<a alt="Identifying The Best Neighborhood Size" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/K-NN_Neighborhood_Size_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
```

## Load Iris Flower Data


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Standardize Data


```python
# Create standardizer
standardizer = StandardScaler()

# Standardize features
X_std = standardizer.fit_transform(X)
```

## Fit A k-Nearest Neighbor Classifier


```python
# Fit a KNN classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean', n_jobs=-1).fit(X_std, y)
```

## Create Search Space Of Possible Values Of k


```python
# Create a pipeline
pipe = Pipeline([('standardizer', standardizer), ('knn', knn)])

# Create space of candidate values
search_space = [{'knn__n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}]
```

## Search Over Possible Values of k


```python
# Create grid search 
clf = GridSearchCV(pipe, search_space, cv=5, verbose=0).fit(X_std, y)
```

## View k For Best Performing Model


```python
# Best neighborhood size (k)
clf.best_estimator_.get_params()['knn__n_neighbors']
```




    6


