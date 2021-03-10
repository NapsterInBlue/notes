import numpy as np

def substring(a, b):
    mat = np.zeros((len(a), len(b)), dtype=int)
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if a[i] == b[j]:
                mat[i][j] = 1 + mat[i-1][j-1]
    
    longest = mat.max()
    max_i, max_j = np.unravel_index(mat.argmax(), mat.shape)

    print a, b, '\b:', longest
    print a[max_i-longest+1:max_i+1], '\n'


if __name__ == '__main__':
    substring('test', 'best')
    substring('forgive', 'shiv')
    substring('ridiculous', 'fictitious')