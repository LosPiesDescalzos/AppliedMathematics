import numpy as np
from scipy.linalg import lu


def get_condition_number(array):
    x = max_matrix_norm(array)
    invert_matrix = plu_inverse(array)
    y = max_matrix_norm(invert_matrix)
    return x * y


def max_matrix_norm(array):
    norm = np.array([])
    for arr in array:
        sum = 0
        for i in arr:
            sum += i
        norm = np.append(norm, sum)

    max = norm[0]
    for i in range(len(norm)):
        if max < norm[i]:
            max = norm[i]

    return max


def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y


def back_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i:], x[i:])) / U[i, i]
    return x


def plu_inverse(A):
    n = A.shape[0]
    b = np.eye(n)
    Ainv = np.zeros((n, n))
    P, L, U = lu(A)
    for i in range(n):
        y = forward_substitution(L, np.dot(P, b[i, :]))
        Ainv[i, :] = back_substitution(U, y)
    return Ainv
