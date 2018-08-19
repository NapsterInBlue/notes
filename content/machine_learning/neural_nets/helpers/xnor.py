import numpy as np
import matplotlib.pylab as plt


def make_xnor_dataset(points):
    xs_x1 = np.ones(points) * .1 + np.random.rand(points) * .2
    xs_y1 = np.ones(points) * .75 + np.random.rand(points) * .2

    xs_x2 = np.ones(points) * .75 + np.random.rand(points) * .2
    xs_y2 = np.ones(points) * .1 + np.random.rand(points) * .2

    xs_x = np.append(xs_x1, xs_x2)
    xs_y = np.append(xs_y1, xs_y2)

    ys_x1 = np.ones(points) * .1 + np.random.rand(points) * .2
    ys_y1 = np.ones(points) * .1 + np.random.rand(points) * .2

    ys_x2 = np.ones(points) * .75 + np.random.rand(points) * .2
    ys_y2 = np.ones(points) * .75 + np.random.rand(points) * .2

    ys_x = np.append(ys_x1, ys_x2)
    ys_y = np.append(ys_y1, ys_y2)

    x_s = np.c_[xs_x, xs_y]
    y_s = np.c_[ys_x, ys_y]

    X = np.append(x_s, y_s, axis=0)
    y = np.append(np.zeros(len(x_s)), np.ones(len(y_s)))

    return X, y


def plot_xnor_dataset(X, y):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='prism')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    return ax
