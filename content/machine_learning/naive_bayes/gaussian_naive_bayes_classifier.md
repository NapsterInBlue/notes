---
title: "Gaussian Naive Bayes Classifier"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to train a Gaussian naive bayes classifer in Scikit-Learn"
type: technical_note
draft: false
---
<a alt="Gaussian Naive Bayes Classifier" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/Gaussian_Naive_Bayes_Classifier_print.png" class="flashcard center-block">
</a>

Because of the assumption of the normal distribution, Gaussian Naive Bayes is best used in cases when all our features are continuous.

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
```

## Load Iris Flower Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Train Gaussian Naive Bayes Classifier


```python
# Create Gaussian Naive Bayes object with prior probabilities of each class
clf = GaussianNB(priors=[0.25, 0.25, 0.5])

# Train model
model = clf.fit(X, y)
```

## Create Previously Unseen Observation


```python
# Create new observation
new_observation = [[ 4,  4,  4,  0.4]]
```

## Predict Class


```python
# Predict class
model.predict(new_observation)
```




    array([1])



Note: the raw predicted probabilities from Gaussian naive Bayes (outputted using `predict_proba`) are not calibrated. That is, they should not be believed. If we want to create useful predicted probabilities we will need to calibrate them using an isotonic regression or a related method.
