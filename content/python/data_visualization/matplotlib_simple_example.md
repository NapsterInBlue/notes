---
title: "Matplotlib, A Simple Example"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Matplotlib, a simple example."
type: technical_note
draft: false
---
### Tell Jupyter to load matplotlib and display all visuals created inline (that is, on this page)


```python
%matplotlib inline
```

### Import matplotlib's pyplot module


```python
import matplotlib.pyplot as pyplot
```

### Create a simple plot


```python
pyplot.plot([1.6, 2.7])
```




    [<matplotlib.lines.Line2D at 0x10c4e7978>]




![png](matplotlib_simple_example_6_1.png)

