---
title: "Enhance Contrast Of Color Image"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to enhance the contrast of images using OpenCV in Python."
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

## Load Image


```python
# Load image
image_bgr = cv2.imread('images/plane.jpg')
```

## Convert Image To YUV Color Format


```python
# Convert to YUV
image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
```

## Enhance Image


```python
# Apply histogram equalization
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
```

## Convert To RGB


```python
# Convert to RGB
image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)
```

## View Image


```python
# Show image
plt.imshow(image_rgb), plt.axis("off")
plt.show()
```


![png](enhance_contrast_of_color_image_12_0.png)

