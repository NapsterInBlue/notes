---
title: "Detect Edges"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to detect edges images using OpenCV in Python."
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

## Load image


```python
# Load image as greyscale
image_gray = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
```

## Detect Edges


```python
# Calculate median intensity
median_intensity = np.median(image_gray)

# Set thresholds to be one standard deviation above and below median intensity
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))

# Apply canny edge detector
image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)
```

## View Edges


```python
# Show image
plt.imshow(image_canny, cmap='gray'), plt.axis("off")
plt.show()
```


![png](detect_edges_8_0.png)

