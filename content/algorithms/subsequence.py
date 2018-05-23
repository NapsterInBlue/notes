import numpy as np

def build_grid(a, b):
    mat = np.zeros((len(a), len(b)), dtype=int)
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if a[i] == b[j]:
                if j == 0:
                    mat[i][j] = mat[i-1][j] + 1
                else:
                    mat[i][j] = mat[i-1][j-1] + 1
            else: 
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    return mat


def get_letters(a, b, mat, longest):
    max_i, max_j = np.unravel_index(mat.argmax(), mat.shape)

    output = ['']
    i, j = max_i, max_j
    val = mat[max_i][max_j]

    while longest:
        if mat[i][j] == max(mat[i-1][j], mat[i][j-1]):
            if val == mat[i-1][j]:
                i = i - 1
            if val == mat[i][j-1]:
                j = j - 1
        else:
            val = mat[i-1][j-1]
            output.append(a[i])
            longest -= 1
            i -= 1
            j -= 1
        if i == 0 or j == 0:
            output.append(a[j])
            break

    return ''.join(output[::-1])


def subsequence(a, b):
    mat = build_grid(a, b)
    longest = mat.max()    
    letters = get_letters(a, b, mat, longest)

    print a, b, longest, '\n', letters, '\n'


if __name__ == '__main__':
    subsequence('mooser', 'mousez') == 4
    subsequence('firetruck', 'fuck')
    subsequence('color', 'colour')
    subsequence('convoluted', 'complicated')
    subsequence('ashes', 'scythes')