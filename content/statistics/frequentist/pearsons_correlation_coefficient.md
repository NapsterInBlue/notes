---
title: "Pearsons Correlation Coefficient"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Pearson's Correlation Coefficient in Python."
type: technical_note
draft: false
---
Based on [this](http://stackoverflow.com/a/17389980/2935984) StackOverflow answer by [cbare](http://stackoverflow.com/users/199166/cbare).

## Preliminaries


```python
import statistics as stats
```

## Create Data


```python
x = [1,2,3,4,5,6,7,8,9]
y = [2,1,2,4.5,7,6.5,6,9,9.5]
```

## Calculate Pearson's Correlation Coefficient

There are a number of equivalent expression ways to calculate Pearson's correlation coefficient (also called Pearson's r). Here is one.

$$r={\frac {1}{n-1}}\sum\_{i=1}^{n}\left({\frac {x\_{i}-{\bar {x}}}{s\_{x}}}\right)\left({\frac {y\_{i}-{\bar {y}}}{s\_{y}}}\right)$$

where $s\_{x}$ and $s\_{y}$ are the sample standard deviation for $x$ and $y$, and $\left({\frac {x\_{i}-{\bar {x}}}{s\_{x}}}\right)$ is the [standard score](https://en.wikipedia.org/wiki/Standard_score) for $x$ and $y$.


```python
# Create a function
def pearson(x,y):
    
    # Create n, the number of observations in the data
    n = len(x)
    
    # Create lists to store the standard scores
    standard_score_x = []
    standard_score_y = []
    
    # Calculate the mean of x
    mean_x = stats.mean(x)
    
    # Calculate the standard deviation of x
    standard_deviation_x = stats.stdev(x)
    
    # Calculate the mean of y
    mean_y = stats.mean(y)
    
    # Calculate the standard deviation of y
    standard_deviation_y = stats.stdev(y)

    # For each observation in x
    for observation in x: 
        
        # Calculate the standard score of x
        standard_score_x.append((observation - mean_x)/standard_deviation_x) 

    # For each observation in y
    for observation in y:
        
        # Calculate the standard score of y
        standard_score_y.append((observation - mean_y)/standard_deviation_y)

    # Multiple the standard scores together, sum them, then divide by n-1, return that value
    return (sum([i*j for i,j in zip(standard_score_x, standard_score_y)]))/(n-1)
```


```python
# Show Pearson's Correlation Coefficient
pearson(x,y)
```




    0.9412443251336238


