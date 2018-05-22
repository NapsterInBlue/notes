---
title: "Blurring Images"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to blurring images using OpenCV in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt
```

## Load Image As Greyscale


```python
# Load image as grayscale
image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
```

## Blur Image


```python
# Blur image
image_blurry = cv2.blur(image, (5,5))
```

## View Image


```python
# Show image
plt.imshow(image_blurry, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()
```


![png](blurring_images_8_0.png)

