import numpy as np
import scipy.sparse as sps
from matrix_Gilbert import generate_hilbert_matrix

ITERATION_LIMIT = 150000000000

# A = np.array([[10., -1., 2., 0.],
#               [-1., 11., -1., 3.],
#               [2., -1., 10., -1.],
#               [0.0, 3., -1., 8.]])
# b = np.array([6., 25., -11., 15.])
#
# A = np.array([[5., 3., 10., 0.],
#               [-1., 10., -1., 3.],
#               [2., -1., 10., 6.],
#               [0., 3., 2., 8.]])
# b = np.array([6., 20., 4., 12.])

A = np.array([[10., -1., 1., 0.],
              [1., 10., 1., -1.],
              [1., -1., 10., 0.],
              [0., 1., -1., 10.]])
b = np.array([11., 10., 11., 10.])

# k = 4
# A = generate_hilbert_matrix(k)
# A = A.toarray()
# b = np.array([1.0, 1.0, 1.0, 1.0])

# A = np.array([[10., 1., -1.],
#               [1., 10., -1.],
#               [-1., 1., 10.]])
#
# b = np.array([11., 10., 10.])

iter = 0
x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        iter += 1
        # print("Iteration {0}: {1}".format(it_count, x))

    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break

    x = x_new

print("Iterations:", iter)
print("Jacobi:")
print(x)

