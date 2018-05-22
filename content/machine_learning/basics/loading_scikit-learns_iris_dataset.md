---
title: "Loading scikit-learn's Iris Dataset"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Loading the built-in Iris datasets of scikit-learn."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from sklearn import datasets
import matplotlib.pyplot as plt 
```

## Load Iris Dataset

The [Iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) is one of the most famous databases for classification. It contains three classes (i.e. three species of flowers) with 50 observations per class.


```python
# Load digits dataset
iris = datasets.load_iris()

# Create feature matrix
X = iris.data

# Create target vector
y = iris.target

# View the first observation's feature values
X[0]
```




    array([ 5.1,  3.5,  1.4,  0.2])


