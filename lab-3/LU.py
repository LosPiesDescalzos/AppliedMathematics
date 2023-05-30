import scipy.sparse as sps


def LU(A):
    n, m = A.shape

    U = sps.csr_matrix(sps.rand(n, m, density=0.0))
    L = sps.csr_matrix(sps.rand(n, m, density=0.0))

    for i in range(n):
        for j in range(m):
            U[0, i] = A[0, i]
            L[i, 0] = A[i, 0] / U[0, 0]

            s = 0.0

            for k in range(i):
                s += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - s

            if i > j:
                L[j, i] = 0
            else:
                s = 0.0
                for k in range(i):
                    s += L[j, k] * U[k, i]
                L[j, i] = (A[j, i] - s) / U[i, i]

    return [L, U]