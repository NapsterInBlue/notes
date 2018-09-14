import pandas as pd
import numpy as np

from sklearn.metrics import confusion_matrix
import matplotlib.pylab as plt



def print_cm(result):
    print('Actual'.rjust(27))
    print('False'.rjust(23), 'True'.rjust(6))
    print('Predicted  False  ',
          str(result[0][0]).rjust(4), ' ',
          str(result[0][1]).rjust(4))
    print('True'.rjust(16),
          str(result[1][0]).rjust(6), ' ',
          str(result[1][1]).rjust(4))
    
def downsample_class(X, y, classToDownsample=1, downsampleToPct=.1):
    df = pd.DataFrame(np.c_[X, y])
    
    true_rows = df[df[df.columns[-1]] == classToDownsample].index
    num_desired_true = int(downsampleToPct * len(true_rows))
    
    survivors = np.random.choice(true_rows, num_desired_true)
    chopping_block = set(true_rows) - set(survivors)
    df = df.drop(chopping_block)
    
    X = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values

    assert(len(X) == len(y))
    return X, y





def false_positive_ratio(tp, tn, fn, fp):
    return fp / (fp + tn)

def precision(tp, tn, fn, fp):
    return tp / (tp + fp)

def recall(tp, tn, fn, fp):
    return tp / (tp + fn)

def f1_score(tp, tn, fn, fp):
    return 2 / ((1 / precision(tp, tn, fn, fp))
                + (1 / recall(tp, tn, fn, fp)))


def plot_multiple_thresholds(y, y_pred_probs):
    fpr = []
    tpr = []
    pre = []
    rec = []
    f1 = []

    for threshold in np.linspace(0.01, .99):
        preds = (y_pred_probs >= threshold).astype(int)

        (tn, fn), (fp, tp) = confusion_matrix(y, preds)

        fpr.append(false_positive_ratio(tp, tn, fn, fp))
        pre.append(precision(tp, tn, fn, fp))
        rec.append(recall(tp, tn, fn, fp))
        f1.append(f1_score(tp, tn, fn, fp))

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(fpr, label="FPR")
    ax.plot(pre, label="Precision")
    ax.plot(rec, label="Recall")
    ax.plot(f1, label="F1 Score")

    ax.legend()