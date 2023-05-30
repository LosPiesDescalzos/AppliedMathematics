""" lam,x = jacobi(a,tol = 1.0e-9).
    Solution of std. eigenvalue problem [a]{x} = lam{x}
    by Jacobi's method. Returns eigenvalues in vector {lam}
    and the eigenvectors as columns of matrix [x].
"""
import numpy as np
from math import sqrt


def jacobi(a, tol=1.0e-9):  # Jacobi method
    def max_elem(a):  # Find largest off-diag. element a[k,l]
        n = len(a)
        a_max = 0.0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(a[i, j]) >= a_max:
                    a_max = abs(a[i, j])
                    k = i
                    l = j

        return a_max, k, l

    def rotate(a, p, k, l):  # Rotate to make a[k,l] = 0
        n = len(a)
        a_diff = a[l, l] - a[k, k]
        if abs(a[k, l]) < abs(a_diff) * 1.0e-36:
            t = a[k, l] / a_diff
        else:
            phi = a_diff / (2.0 * a[k, l])
            t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
            if phi < 0.0:
                t = -t

        c = 1.0 / sqrt(t ** 2 + 1.0)
        s = t * c
        tau = s / (1.0 + c)
        temp = a[k, l]
        a[k, l] = 0.0
        a[k, k] = a[k, k] - t * temp
        a[l, l] = a[l, l] + t * temp
        for i in range(k):  # Case of i < k
            temp = a[i, k]
            a[i, k] = temp - s * (a[i, l] + tau * temp)
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(k + 1, l):  # Case of k < i < l
            temp = a[k, i]
            a[k, i] = temp - s * (a[i, l] + tau * a[k, i])
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(l + 1, n):  # Case of i > l
            temp = a[k, i]
            a[k, i] = temp - s * (a[l, i] + tau * temp)
            a[l, i] = a[l, i] + s * (temp - tau * a[l, i])
        for i in range(n):  # Update transformation matrix
            temp = p[i, k]
            p[i, k] = temp - s * (p[i, l] + tau * p[i, k])
            p[i, l] = p[i, l] + s * (temp - tau * p[i, l])

    n = len(a)
    max_rot = 5 * (n ** 2)  # Set limit on number of rotations
    p = np.identity(n) * 1.0  # Initialize transformation matrix
    for i in range(max_rot):  # Jacobi rotation loop
        aMax, k, l = max_elem(a)
        if aMax < tol:
            return np.diagonal(a)  # , p
        rotate(a, p, k, l)

    print('Jacobi method did not converge')
