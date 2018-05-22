---
title: "Sharpen Images"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to sharpen images using OpenCV in Python."
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

## Sharpen Image


```python
# Create kernel
kernel = np.array([[0, -1, 0], 
                   [-1, 5,-1], 
                   [0, -1, 0]])

# Sharpen image
image_sharp = cv2.filter2D(image, -1, kernel)
```

## View Image


```python
# Show image
plt.imshow(image_sharp, cmap='gray'), plt.axis("off")
plt.show()
```


![png](sharpen_images_8_0.png)

