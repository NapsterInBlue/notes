---
title: "Installing OpenCV"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to install OpenCV in Python."
type: technical_note
draft: false
---
While there are a number of good libraries out there, OpenCV is the most popular and documented library for handling images. One of the biggest hurdles to using OpenCV is installing it. However, fortunately we can use Anaconda's package manager tool conda to install OpenCV in a single line of code in our terminal: 

`conda install --channel https://conda.anaconda.org/menpo opencv3`

Afterwards, we can check the installation by opening a notebook, importing OpenCV, and checking the version number (3.1.0):


```python
# Load library
import cv2

# View version number
cv2.__version__
```




    '3.2.0'


