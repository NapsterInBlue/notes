import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from keras import backend as K


import numpy as np
import matplotlib.pyplot as plt

def deprocess_image(x):
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1

    x += 0.5
    x = np.clip(x, 0, 1)

    x *= 255.
    x = np.clip(x, 0, 255).astype('uint8')
    return x


def generate_pattern(model, layer_name, filter_index, size=150):
    layer_output = model.get_layer(layer_name).output
    loss = K.mean(layer_output[:, :, :, filter_index])

    grads = K.gradients(loss, model.input)[0]
    grads /= (K.sqrt(K.mean(K.square(grads))) + 1e-5)

    iterate = K.function([model.input], [loss, grads])

    input_img_data = np.random.random((1, size, size, 3)) * 20 + 128.

    step = 0.1
    for i in range(5000):
        loss_value, grads_value = iterate([input_img_data])
        input_img_data += grads_value * step

    img = input_img_data[0]
    deprocessed = deprocess_image(img)

    return deprocessed


def generate_layer(model, layer_name, size=64, margin=5):
    results = np.zeros((8 * size + 7 * margin,
                        8 * size + 7 * margin,
                        3), dtype='uint8')

    for i in range(8):
        for j in range(8):
            filter_img = generate_pattern(model, layer_name, 
                                          filter_index=i + (j*8),
                                          size=size)

            horizontal_start = i * size + i * margin
            horizontal_end = horizontal_start + size

            vertical_start = j * size + j * margin
            vertical_end = vertical_start + size

            results[horizontal_start:horizontal_end,
                    vertical_start:vertical_end, :] = filter_img

    plt.figure(figsize=(20, 20))
    plt.imshow(results)