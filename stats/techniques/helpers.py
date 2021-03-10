import matplotlib.pylab as plt
import numpy as np


def make_dataset():
    np.random.seed(0)
    y = np.random.normal(.5, .08, (100,))
    X = range(len(y))
    
    return X, y

def make_fig(X, y):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.scatter(X, y)
    ax.set_ylim(0, 1)
    return ax
