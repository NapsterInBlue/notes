---
title: "Visualize Neural Network Architecutre"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to visualize neural network architecture in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load libraries
from keras import models
from keras import layers
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
```

    Using TensorFlow backend.


## Construct Neural Network Architecture


```python
# Start neural network
network = models.Sequential()

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=16, activation='relu', input_shape=(10,)))

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=16, activation='relu'))

# Add fully connected layer with a sigmoid activation function
network.add(layers.Dense(units=1, activation='sigmoid'))
```

## Visualize Network Architecture


```python
# Visualize network architecture
SVG(model_to_dot(network, show_shapes=True).create(prog='dot', format='svg'))
```




![svg](visualize_neural_network_architecture_6_0.svg)



## Save To File


```python
# Save the visualization as a file
plot_model(network, show_shapes=True, to_file='network.png')
```
