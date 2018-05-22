---
title: "Save Images"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to save images using OpenCV in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
import cv2
import numpy as np
from matplotlib import pyplot as plt
```

## Load Image As Greyscale


```python
# Load image as grayscale
image = cv2.imread('images/plane.jpg', cv2.IMREAD_GRAYSCALE)

# Show image
plt.imshow(image, cmap='gray'), plt.axis("off")
plt.show()
```


![png](save_images_4_0.png)


## Save Image


```python
# Save image
cv2.imwrite('images/plane_new.jpg', image)
```




    True


